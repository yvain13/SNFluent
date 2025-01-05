import requests
import json
import gradio as gr

API_URL = "https://8000-01jgshszpvsr6py22g2kywvje5.cloudspaces.litng.ai/generate"

def generate_response(message, history):
    """Function to handle chat interactions"""
    print("\n=== Debug Information ===")
    print("Input Message:", message)
    print("Current History:", history)
    
    # Initialize history if None
    history = history or []
    
    # Prepare API request
    messages = []
    for user_msg, _ in history:
        messages.append({"role": "user", "content": user_msg})
    messages.append({"role": "user", "content": message})
    
    payload = {
        "messages": messages
    }
    
    print("\nAPI Payload:", json.dumps(payload, indent=2))
    
    try:
        response = requests.post(API_URL, json=payload)
        print("\nAPI Response Status:", response.status_code)
        print("Raw API Response:", response.text)
        
        if response.status_code == 200:
            response_json = response.json()
            print("\nParsed Response:", json.dumps(response_json, indent=2))
            
            response_text = response_json.get("response", "No response received")
            print("\nExtracted Response Text:", response_text)
            
            # Return in the format Gradio expects
            return [{"role": "user", "content": message},
                   {"role": "assistant", "content": response_text}]
        else:
            error_msg = f"Error: API returned status code {response.status_code}"
            print("\nError:", error_msg)
            return [{"role": "user", "content": message},
                   {"role": "assistant", "content": error_msg}]
    except Exception as e:
        error_msg = f"Error calling API: {str(e)}"
        print("\nException:", error_msg)
        return [{"role": "user", "content": message},
                {"role": "assistant", "content": error_msg}]

# Create the Gradio interface
def create_demo():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # ServiceNow Fluent Assistant
        Welcome to the ServiceNow Fluent Assistant! You can ask me to:
        - Create tables with specific columns
        - Generate client scripts
        - Create business rules
        - Add records to tables
        """)
        
        chatbot = gr.Chatbot(
            value=[],
            height=400,
            show_copy_button=True,
            show_share_button=False,
            type="messages"  # Explicitly set to use message format
        )
        
        with gr.Row():
            msg = gr.Textbox(
                label="Type your message here",
                placeholder="e.g., create a TABLE with 3 columns and a record for incident table",
                lines=2,
                scale=9
            )
            submit_btn = gr.Button("Send", scale=1)
            clear_btn = gr.Button("Clear", scale=1)
        
        # Example prompts
        gr.Examples(
            examples=[
                "create a TABLE with 3 columns and a record for incident table",
                "create a client script to validate priority field",
                "create a business rule to auto-assign incidents",
            ],
            inputs=msg,
            label="Example prompts"
        )

        # Set up event handlers
        msg_submit = msg.submit(
            generate_response,
            inputs=[msg, chatbot],
            outputs=chatbot
        )
        msg_submit.then(lambda: "", None, msg)  # Clear input after submission

        submit_btn.click(
            generate_response,
            inputs=[msg, chatbot],
            outputs=chatbot
        ).then(lambda: "", None, msg)  # Clear input after submission

        clear_btn.click(
            lambda: [],  # Return empty list for chat history
            None,
            [chatbot],
            queue=False
        ).then(
            lambda: "",  # Clear input
            None,
            [msg],
            queue=False
        )

    return demo

if __name__ == "__main__":
    # Launch the Gradio interface
    demo = create_demo()
    demo.launch(
        share=False,
        server_name="0.0.0.0",
        server_port=7860,
        show_api=False
    )

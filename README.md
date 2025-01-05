# ServiceNow Fluent Assistant

A conversational AI interface for ServiceNow development assistance, powered by a custom language model and presented through a user-friendly Gradio interface.

## Overview

This project provides a chat interface for interacting with a specialized ServiceNow development assistant. It can help with:
- Creating tables with specific columns
- Generating client scripts
- Creating business rules
- Adding records to tables
- Other ServiceNow development tasks

## Components

The project consists of two main components:

1. **API Interface** (`agent.py`)
   - Handles communication with the SNFluent language model
   - Processes natural language requests into ServiceNow-specific implementations
   - Manages conversation context and history
   - Provides structured responses for table creation, client scripts, and business rules

2. **Chat Interface** (`gradio.py`)
   - Provides a web-based chat interface using Gradio
   - Maintains conversation history
   - Offers example prompts for common tasks
   - Displays code snippets with proper formatting
   - Includes copy-to-clipboard functionality

## Installation

1. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the chat interface:
```bash
python gradio.py
```

2. Access the interface:
   - Local URL: http://localhost:7860
   - The interface will be available on your local machine

3. Using the chat:
   - Type your request in natural language
   - Use example prompts for common tasks
   - Copy generated code using the copy button
   - Clear the chat history as needed

## Example Prompts

Here are some example prompts you can try:

```
create a TABLE with 3 columns and a record for incident table
```
```
create a client script to validate priority field
```
```
create a business rule to auto-assign incidents
```

## API Reference

The backend API endpoint is available at:
```
https://8000-01jgshszpvsr6py22g2kywvje5.cloudspaces.litng.ai/generate
```

API expects requests in the following format:
```json
{
    "messages": [
        {"role": "user", "content": "your request here"}
    ]
}
```

## Dependencies

- gradio>=4.8.0
- requests>=2.31.0

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

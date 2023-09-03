# Chat.openAi wrapper

A simple chat library wrapper for OpenAI. OpenAiChatLib makes it easier to integrate OpenAI chat models into your applications, providing session management and optional system prompts.

## Table of Contents

- [Installation](#installation)
- * [From .whl File](#from-whl-file)
  * [Directly From Source](#directly-from-source)
- [Usage](#usage)
  * [Starting a New Session](#starting-a-new-session)
  * [Asking Questions](#asking-questions)
- [Licensing](#licensing)

## Installation



1. Clone this repository:


    git clone https://github.com/Dhanasrepo/openai.chat.wrapper.git


### From .whl File

1. Navigate to the root directory and copy the `openaichatlib.whl`file to your required destination
2. Install using pip:


    pip install /path_to_whl_file/openaichatlib.whl


### Directly From Source (alternative to .whl)


1. Navigate to the root directory and install:


    pip install .


## Usage

### Starting a New Session

First, initialize the chat session:


    from openaichatlib.chat import Chat

    chatbot = Chat("YOUR_OPENAI_API_KEY")


To start a new chat session:


    session_data = chatbot.start_new_session()


You can also specify a system prompt:


    session_data = chatbot.start_new_session("You are a bot specialized in creating a python code")


### Asking Questions

With the session initiated, you can now ask the model questions:


    data = {
    'session_id': session_data['session_id'],
    'history': session_data['history'],
    'question': "Create a wrapper class for openAi chatbot"
    }

    response = chatbot.ask(**data)
    print(response['response'])


## Licensing

The code in this project is licensed under the MIT license. See the LICENSE file for more information.

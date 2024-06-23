from gen_prompts import get_prompt, gen_summary_prompt, gen_email_prompt
from utils import set_history
from parse_docx import marker

import streamlit as st  #all streamlit commands will be available through the "st" alias
import chatbot_lib as glib  #reference to local lib script

st.set_page_config(page_title="Chatbot")  #HTML title
st.title("Chatbot")  #page title

if 'memory' not in st.session_state:  #see if the memory hasn't been created yet
    st.session_state.memory = glib.get_memory()  #initialize the memory

if 'chat_history' not in st.session_state:  #see if the chat history hasn't been created yet
    st.session_state.chat_history = []  #initialize the chat history

# Re-render the chat history (Streamlit re-runs this script, so need this to preserve previous chat messages)
for message in st.session_state.chat_history:  #loop through the chat history
    with st.chat_message(message["role"]):  #renders a chat line for the given role, containing everything in the with block
        st.markdown(message["text"])  #display the chat content

input_text = st.chat_input("Chat with your bot here")  # display a chat input box

# 1) Get document, with marked changes
input_doc_list = marker("NDA 1.docx") # get_blank_doc()

summaries = []
for i, doc in enumerate(input_doc_list):
    print(i)
    # 2) Get initial prompt for model
    doc_prompt = get_prompt(doc.page_content)
    set_history(st, doc_prompt, "user")

    # 3) Get chat analysis of diffs
    chat_response = glib.get_chat_response(input_text=doc_prompt, memory=st.session_state.memory)  # call the model through the supporting library
    set_history(st, chat_response, "assistant")  # add the chat response to the chat history

    st.session_state.chat_history = []  # clear the chat history

    summaries.append(chat_response)


# 4) Summarise changes
print("Summarising changes")
all_summaries = "\n\n".join(summaries)
summary_prompt = gen_summary_prompt(all_summaries)
set_history(st, summary_prompt, "user")  # add the chat response to the chat history
chat_summary = glib.get_chat_response(input_text=summary_prompt, memory=st.session_state.memory)  # call the model through the supporting library

set_history(st, chat_summary, "assistant")  # add the chat response to the chat history
st.session_state.chat_history = []  # clear the chat history

# 5) Generate email
st.session_state.chat_history = []  # clear the chat history
email_prompt = gen_email_prompt(chat_summary)
chat_email = glib.get_chat_response(input_text=email_prompt, memory=st.session_state.memory)  # call the model through the supporting library
set_history(st, chat_summary, "assistant")  # add the chat response to the chat history


def get_blank_doc():
    msg = """The "Parties" will cooperate on joint projects within the scope of their respective normal activities, and will exchange technical and commercial information. (the “Purpose”).
The term "Confidential Information" includes, by way of non-limitative examples, databases, know-how, formulas, processes, drawings, sketches, photographs, plans, drafts, specifications, samples, reports, customer and supplier lists, pricing information, studies, results, inventions and ideas [START], personally identifiable information and [END] any other information which is of a nature that the "Parties" shall reasonable deem "Confidential Information" transmitted by one of the "Parties" to the other whether before, on or after the effective date hereof in connection with such projects. """

    return msg


def set_history(st, msg, mode):
    st.session_state.chat_history.append({"role": mode, "text": msg})  # append the user's latest message to the chat history

    if mode == "user":
        with st.chat_message("user"):  # display a user chat message
            st.markdown(msg)  # renders the user's latest message
    elif mode == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg)

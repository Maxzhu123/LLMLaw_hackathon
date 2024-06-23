def get_prompt(doc):

    init = """This is a legal document that has been revised. Insertions marked with [start_insert] and [end_insert]. Deletions are marked with [start_del] and [end_del]. Explain the impact of the changes made. The response will be clear and concise. If there are no meaningful changes, respond with N/A."""

    return f'{init} \n\n {doc}'


def gen_summary_prompt(summaries):
    prompt = """The following is a summary of changes made to a legal document, each sepeareted by a newline. Summarise the changes, focusing on the important points. The response should be clear and concise"""

    return f'{prompt} \n\n {summaries}'

def gen_email_prompt(summary):
    prompt = """You have been asked to send an email to the other party in the legal document. Write an email that summarises the changes made to the document. The response should be clear and concise"""

    return f'{prompt} \n\n {summary}'

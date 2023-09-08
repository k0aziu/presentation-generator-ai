from gpt4free import you
import codecs

def ask_ai(question, conversation):

    response = you.Completion.create(prompt=str(question), chat=conversation)

    while response.text == "Unable to fetch the response, Please try again.":
        response = you.Completion.create(prompt=str(question), chat=conversation)
    conversation.append({"question": str(question), "answer": response.text})
    text = codecs.decode("\n" + response.text + "\n", 'unicode_escape')

    return(text)
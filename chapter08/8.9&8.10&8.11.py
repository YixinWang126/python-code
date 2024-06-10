def show_messages(messages):  
    for message in messages:  
        print(message)  

def send_messages(messages, sent_messages):
    ms = messages[:]
    for message in ms:  
        print(f"Sending: {message}")  
        sent_messages.append(message)  
        messages.remove(message)
   
messages = ["Hello, World!", "This is a test message.", "How are you?"]  
sent_messages = []
  
show_messages(messages)
send_messages(messages[:], [])
print(messages, sent_messages)
send_messages(messages, sent_messages)
print(messages, sent_messages)



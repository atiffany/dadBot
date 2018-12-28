import time

def findWordAfter(word, input):
    sentence = input.split()
    flag = False
    for word in sentence:
        if flag == True:
            return word
        if word == "i'm" or word == "im":
            flag = True

def response(input):
    input = input.lower()
    if "hello" in input or "hi" in input:
        return "hello there!"
    elif "i'm" in input or "im" in input:
        name = findWordAfter("i'm", input)
        return "hiya " + name + " I'm Dad"
    elif "goodbye" in input:
        return "smell ya later"
    else:
        return "Say whaaat?"

print("Hello. I am the DadBot.")
attempts = 0
while(attempts < 5):
    input = raw_input("What can I do ya for?\n>>")
    print(response(input))
    attempts += 1
print("\nBuh-Bye!")

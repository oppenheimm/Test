dict = {}
words = {}

with open(r"C:\Users\Tommi\Forritun Visual stud\messages1.txt") as f:
    for line in f:
        line = line.strip()
        (tag, nr, msg) = line.split(" ")
        msg = msg.replace("_", " ")
        dict[(tag, nr)] = msg

        if tag not in words:
            words[tag] = {}

        words[tag][
            nr
        ] = msg  # Add the message to the dictionary associated with the tag

for tag, msg_dict in words.items():
    sorted_msgs = sorted(msg_dict.items(), key=lambda x: int(x[0]))
    words[tag] = "".join(
        msg for nr, msg in sorted_msgs
    )  # Remove the space between messages

# Print the combined messages
for tag, msg in sorted(words.items()):
    print(f"{tag}: {msg}")

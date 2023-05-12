    new_letter = file.replace("[name]", name)
        with open(f"ReadyToSend/{name}.txt", mode="w") as file:
            file.write(new_letter)
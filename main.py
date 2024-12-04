#27 yaml -> json wed, fr

def convert(file):
    yaml = file.readlines()
    output = "{"

    last_padding = -1

    for line in yaml:

        line = line.strip("\n")

        if line.strip():

            new_padding = 0
            while line[new_padding] == " ":
                new_padding+=1

            new_padding//=2

            if new_padding<last_padding:
                output+="}"*(last_padding-new_padding) +", "
            elif new_padding==last_padding:
                output+=", "

            last_padding = new_padding

            parts = line.split(":", 1)
            output+= f'"{parts[0].strip()}"'
            if parts[1]:
                output+= f': {parts[1].strip()}'
            else:
                output+=': {'


    return output+"}"*(last_padding+1)

if __name__ == "__main__":
    file = open("schedule.yaml", encoding="utf-8")

    json = convert(file)

    with open("output.json", "w", encoding = "utf-8") as file:
        file.write(json)

        





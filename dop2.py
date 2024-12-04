import re

def convert(file):
    yaml = file.readlines()
    output = "{"

    last_padding = -1

    for line in yaml:
        line = line.strip("\n")

        if line.strip():
            match = re.match(r"^( *)([^:]+):(.*)", line)
            if match:
                spaces, key, value = match.groups()

                new_padding = len(spaces) // 2

                if new_padding < last_padding:
                    output += "}" * (last_padding - new_padding) + ", "
                elif new_padding == last_padding:
                    output += ", "

                last_padding = new_padding

                output += f'"{key.strip()}"'
                if value.strip():
                    output += f': {value.strip()}'
                else:
                    output += ': {'

    return output + "}" * (last_padding + 1)

if __name__ == "__main__":
    file = open("schedule.yaml", encoding="utf-8")
    json = convert(file)
    with open("output2.json", "w", encoding="utf-8") as file:
        file.write(json)

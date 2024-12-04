import json

def parse_line(line):
    stripped_line = line.strip()
    indent = len(line) - len(line.lstrip())

    if stripped_line.startswith("- "):
        return indent, "list_item", parse_line(stripped_line[2:].strip())
    elif ": " in stripped_line:
        key, value = map(str.strip, stripped_line.split(": ", 1))
        return indent, "pair", (key, value.strip('"'))
    elif stripped_line.endswith(":"):
        key = stripped_line[:-1].strip()
        return indent, "empty_pair", (key, None)
    elif stripped_line.startswith("---"):
        return indent, "start", None
    elif stripped_line.startswith("..."):
        return indent, "end", None
    else:
        raise ValueError("Unexpected line encountered")

def convert_line(indent, element_type, content, current_obj, stack):
    if element_type == "pair":
        key, value = content
        current_obj[key] = value
    elif element_type == "empty_pair":
        key, _ = content
        current_obj[key] = {}
        stack.append((current_obj[key], indent))
    elif element_type == "list_item":
        if not isinstance(current_obj, list):
            stack.pop()
            last_obj = stack[-1][0]
            for key, value in last_obj.items():
                if value == current_obj:
                    break
            last_obj[key] = []
            current_obj = last_obj[key]
            stack.append((current_obj, indent-1))
        current_obj.append({})
        stack.append((current_obj[-1], indent))
        convert_line(content[0] + 2, content[1], content[2], current_obj[-1], stack)



def convert(file):
    lines = file.readlines()
    root = {}
    stack = [(root, -1)]

    for line in lines:
        if not line.strip() or line.strip().startswith("#"):
            continue

        indent, element_type, content = parse_line(line)

        while stack and stack[-1][1] >= indent:
            stack.pop()

        current_obj, _ = stack[-1]

        convert_line(indent, element_type, content, current_obj, stack)

    return root


if __name__ == "__main__":
    file = open("for_grammatics.yaml", encoding="utf-8")
    json_data = convert(file)
    with open("output3.json", "w", encoding="utf-8") as file:
        json.dump(json_data, file, ensure_ascii=False, indent=4)
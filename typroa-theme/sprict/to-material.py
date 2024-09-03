import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(output_file, "w") as f:
    alert_sign = False
    for line in lines:
        if line.startswith("> [!"):
            alert_sign = True
            type = line.split("!")[1].strip()[:-1]
            f.write(f"!!! {type}\n")
            continue
        if line.startswith(">") and alert_sign:
            f.write("    " + line[2:])
        else:
            alert_sign = False
            f.write(line)

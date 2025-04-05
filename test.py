def read_log_file():
    with open("D:\\MCP\\applog.txt", "r") as f:
        log_contents = f.read()
    return log_contents

text = read_log_file()
print(text)
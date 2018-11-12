

def is_heading(line, level=1):
    return line[:level] == '#' * level
    
def is_code(line):
    return line[:3] == "```"

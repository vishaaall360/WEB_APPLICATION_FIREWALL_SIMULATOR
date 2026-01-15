from rules import SQL_INJECTION, XSS, PATH_TRAVERSAL, COMMAND_INJECTION

def inspect_request(user_input):
    text = user_input.lower()

    for rule in SQL_INJECTION:
        if rule in text:
            return "SQL Injection Detected"

    for rule in XSS:
        if rule in text:
            return "XSS Attack Detected"

    for rule in PATH_TRAVERSAL:
        if rule in text:
            return "Path Traversal Detected"

    for rule in COMMAND_INJECTION:
        if rule in text:
            return "Command Injection Detected"

    return "Safe Request"

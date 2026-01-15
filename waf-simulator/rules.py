SQL_INJECTION = [
    "select", "union", "drop", "insert", "update", "--", "' or '1'='1"
]

XSS = [
    "<script>", "</script>", "javascript:", "onerror", "onload"
]

PATH_TRAVERSAL = [
    "../", "..\\", "/etc/passwd", "boot.ini"
]

COMMAND_INJECTION = [
    ";", "&&", "|", "`", "$("
]

# Test Report – WAF Simulator

## Test Cases

| Input | Expected Output |
|------|----------------|
| hello | Safe Request |
| <script>alert(1)</script> | XSS Detected |
| ' OR '1'='1 | SQL Injection Detected |
| ../etc/passwd | Path Traversal Detected |

## Result
All test cases passed successfully.

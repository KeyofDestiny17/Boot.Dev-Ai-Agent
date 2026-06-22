from functions.get_file_content import get_file_content

test_files = ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

for file in test_files:
    result = get_file_content("calculator", file)
    print(f"{file} length: {len(result)}")
    print(f"{file} truncated: {'truncated' in result}")

    if result.startswith("Error:"):
        print(f"  {result}")
    else:
        for line in result.splitlines():
            print(f"  {line}")
    print("")
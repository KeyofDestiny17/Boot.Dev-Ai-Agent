from functions.get_files_info import get_files_info

test_path = [".", "pkg", "/bin", "../"]

for path in test_path:
    if path == ".":
        description = "current directory"
    else:
        description = f"'{path}' directory"
    
    print(f"Result for {description}:")
    result = get_files_info("calculator", path)

    if result.startswith("Error:"):
        print(f"  {result}")
    else:
        for line in result.splitlines():
            print(f"  {line}")
    print("")
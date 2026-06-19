from functions.get_files_info import get_files_info

print(get_files_info("calculator", "."))
print(get_files_info("calculator", "pkg"))

print("Result for 'bin' directory:")
print(f"  {get_files_info('calculator', '/bin')}")

print("Result for '../' directory:")
print(f"  {get_files_info('calculator', '../')}")

from functions.get_files_info import get_files_info

def test_get_files_info():
    current_directory = get_files_info("calculator", ".")
    print(f"Result for current directory:")
    print(current_directory)

    pkg_dir = get_files_info("calculator", "pkg")
    print(f"Result for 'pkg' directory:")
    print(pkg_dir)

    bin_dir = get_files_info("calculator", "/bin")
    print(f"Result for '/bin' directory:")
    print(bin_dir)

    root_directory = get_files_info("calculator", "../")
    print(f"Result for '../' directory:")
    print(root_directory)

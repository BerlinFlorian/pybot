from functions.get_file_content import get_file_content

def test_get_file_content():
    result = get_file_content("calculator", "lorem.txt")

    print(result)

    result2 = get_file_content("calculator", "pkg/calculator.py")
    print(result2)

    result3 = get_file_content("calculator", "/bin/cat")
    print(result3)

    result4 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result4)

def main(*args, **kwargs):
    test_get_file_content()


if __name__ == "__main__":
    main()

from functions.get_files_info import get_files_info

def test():
    ret = get_files_info("calculator", ".")
    print(ret)

    ret2 = get_files_info("calculator", "pkg")
    print(ret2)

    ret3 = get_files_info("calculator", "/bin")
    print(ret3)

    ret4 = get_files_info("calculator", "../")
    print(ret4)

if __name__ == "__main__":
    test()
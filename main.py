from utils.requester import get_status


def main():
    status = get_status("https://ya.ru")
    print(f"Status code: {status}")


if __name__ == "__main__":
    main()

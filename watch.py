import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    find = re.search('.+src="https?://(?:www.)?youtube.com/embed/(.+?)"', s)
    if find:
        url = "https://youtu.be/" + find.group(1)
        return url
    else:
        return None


if __name__ == "__main__":
    main()

import re


def read_input_file():
    content = open("input.txt").read()
    return content


def filter_combined_number(text):
    res = re.findall("^[^\\d]*(\\d).*?(\\d?)[^\\d]*$", text)
    secondDigit = res[0][1] if res[0][1] != "" else res[0][0]
    return int(f'{res[0][0]}{secondDigit}')


if __name__ == '__main__':
    print("+++ Dec 01 - T1 +++")
    fileContent = read_input_file()
    lines = fileContent.split("\n")
    nmbrs = []
    for line in lines:
        nmbrs.append(filter_combined_number(line))
    print(nmbrs)
    print(sum(nmbrs))

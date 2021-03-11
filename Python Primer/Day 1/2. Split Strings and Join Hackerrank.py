# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
def split_and_join(line):
    split_str = line.split(" ")
    joined_str = "-".join(split_str)
    return joined_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
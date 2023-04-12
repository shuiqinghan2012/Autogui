import os

# def readLine(testfilename):
#     if (".txt") not in testfilename:
#         print("只支持txt文件，请使用txt作为输入！")
#     with open(testfilename, 'r',encoding='utf-8') as f:
#         for line in f:
#             if line.strip():  # 如果不是空行
#                 return line.strip()
#                 # print(line.strip())
#                 # print('输出一行')
#
# filename = "testfilename.txt"
# lineTxt=readLine(filename)
# print(lineTxt)

# def read_next_line(filename):
#     with open(filename, 'r',encoding='utf-8') as f:
#         for line in f:
#             if line.strip():
#                 return line.strip()
#     return None
#
# filename = "testfilename.txt"
#
# next_line = read_next_line(filename)
# while next_line:
#     # 进行处理，比如打印该行
#     print(next_line)
#     # 读取下一行
#     next_line = read_next_line(filename)


# def read_next_line(file):
#     line = file.readline()
#     while line:
#         if line.strip():
#             return line.strip()
#         line = file.readline()
#     return None
#
# # with open("testfilename.txt", 'r',encoding='utf-8') as f:
# #     line = read_next_line(f)
# #     while line:
# #         print(line)
# #         line = read_next_line(f)
# # 要重复输出文件内容20次，您可以使用一个循环来多次调用 read_next_line() 函数并打印每行。具体来说，您可以将 read_next_line() 函数放入一个循环中，并在循环中调用该函数和 print() 函数20次。以下是一个示例代码：
# with open("testfilename.txt", 'r',encoding='utf-8') as f:
#     for i in range(20):
#         line = read_next_line(f)
#         while line:
#             print(line)
#             line = read_next_line(f)
#         f.seek(0)  # 将文件指针回到文件开头，以便下一轮循环重新读取文件内容


def readline(filename):
    with open(filename, 'r',encoding='utf-8') as f:
        if not hasattr(readline, 'lines'):
            readline.lines = f.readlines()
            readline.current = 0
        while True:
            if readline.current == len(readline.lines):
                readline.current = 0
            line = readline.lines[readline.current].strip()
            readline.current += 1
            if line:
                return line


filename = "testfilename.txt"
for i in range(20):
    print(readline(filename))

#题目
# 键盘输入正整数n，按要求把n输出到屏幕，格式要求:宽度为20个字符，减号字符-填充，右对齐，带千位分隔符。
# 如果输入正整数超过20位，则按照真实长度输出。
# 例如:键盘输入正整数n为1234，屏幕输出---------------1,234
# 原文档
# n = eval(input("请输入正整数："))
# print("{______}".format(n))

# 要求实现
n = eval(input("请输入正整数："))
print("{:->20,}".format(n))
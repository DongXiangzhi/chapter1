import io  # 导入io模块

f = io.StringIO()  # 定义文本流
f.write('好好学习，')  # 写入流
f.write('天天向上！ ')  # 写入流
print(f.getvalue())
f = io.StringIO('胡马大宛名，\n锋棱瘦骨成。')  # 定义文本流
while True:
    s = f.readline()  # 读取流
    if s == '':
        break
    print(s.strip())

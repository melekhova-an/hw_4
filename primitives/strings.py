"""
Это примеры работы со строками
"""
# Учимся писать строки!

s = "Hello, " \
    "'world'!"
print(s)

s = 'Hello, "world"!'
s = 'Hello, \'world\'!'
s = """Hello', "world!"""
s = '''Hello, 
world!'''
print(s)

s = "Hello, \nWorld!"
print(s)
# Сырые строки

s = r"Hello, \nWorld!"
s = "Hello, \\nWorld!"
print(s)

# Индексы и слайсы

s = "abcdefg"
print(s[0])
print(s[-1])

print(s[0:3])
print(s[0:len(s)])
print(s[0:len(s):2])

print("проверка")
print(s[len(s)::-1])

print(s[::-1])

# Оперируем

s.startswith("https://")
s = "1234"
n = 1234
s.isdigit()

# Форматируем

hello = "Hello"
world = "world"

print(hello + ", " + world + "!")
print(f"{hello}, {world.upper()}!")
print("{}, {}!".format(hello, world))
print("{h}, {w}{w}{w}{w}{w}{w}{w}!".format(h=hello, w=world))

print("%s %s" % (hello, world))

url_template = "https://google.com/{}"

url_template.format("/api/user")
url_template.format("/api/group")


# Строку в число, и наоборот

s = "1234"
n = 1234

assert int(s) == n
assert s == str(n)
s = "abc123"
int(s)


# ss = "abc"
# ss[0] = "d"

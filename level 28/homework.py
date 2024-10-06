# შექმნათ სია 10 სხვადასხვა მონაცემთა ტიპის მნიშვნელობით
data_list = [42, 3.14, "Hello", True, None, [1, 2, 3], (4, 5), { "key": "value" }, {1, 2, 3}, bytearray(b'hello')]

# ცვლილებები 5 მონაცემზე
data_list[0] = 100  # Int
data_list[1] = 2.71  # Float
data_list[2] = "World"  # String
data_list[3] = False  # Boolean
data_list[5] = [4, 5, 6]  # List

# საბოლოო შედეგის პრინტვა
print(data_list)

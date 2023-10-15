class CreateList:
    def __init__(self):  # private value 2
        self.__val = 2

    # 3->[2,3,4]  #10->[2,3,4,5,6,7,8,9,10,11]
    def creat_success_list(self, value):
        a = []
        for x in range(value):
            a.append(x+self.__val)
        print(a)


class CreateTwoList(CreateList):  # inherit
    def creat_2_void_list(self):
        a = []
        b = []
        return a, b

    def creat_2_void_list(self, value):
        return self.creat_success_list(value), self.creat_success_list(value)


createTwoList = CreateTwoList()
ans1 = createTwoList.creat_success_list(3)
ans2 = createTwoList.creat_2_void_list()
print(ans1)
print(ans2)

"""
createList = CreateList()
# createList.__val = 8  # 因為私有化，數值不會被改動
a = createList.creat_success_list(10)
print(a)
"""

# a = []
# for x in range(8):
#     # a.append(x)
#     a.append(x+2)
# print(a)


aa=3
bb=4
cc=aa+bb
print(cc)
print("call second py")

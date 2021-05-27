# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 '나도코딩' 입니다")

# print('저는 \"나도코딩\" 입니다.')
# print("저는 \'나도코딩\' 입니다.")

# print("C:\\Users\\dltjd\\Desktop\\PythonWorkspace>")

# print("Red Apple\rPine")
# print("Redd\bApple")
# print("Red\tApple")

class address:
    def __init__(self, url):
        self.url = url

    def creat_password(self):
        if "http://" or "www." or ".com" in self.url:
            self.url = self.url.replace("http://", "")
            self.url = self.url.replace("www.", "")
            self.url = self.url.replace(".com", "")
            print(self.url + "의 비밀번호는 " +
                  self.url[:3] + str(len(self.url)) + str(self.url.count("e")) + "!" + "입니다.")

        else:
            print(self.url + "의 비밀번호는 " +
                  self.url[:3] + str(len(self.url)) + str(self.url.count("e")) + "!" + "입니다.")


myAddress = address("www.baidoandweibo.com")
myAddress.creat_password()


# url = "http://naver.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# print(my_str)

# address = "leeshop"
# print(address + str(len(address)) + str(address.count("e")) + "!")

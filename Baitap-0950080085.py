# bài tập 1
def xuat():
  t = int(input("Nhập: "))
  if 0 < t <= 100:
    for i in range (1,t+1):
        c=input()
        print(f"Test{i}:\n{c.title()}")
xuat()

# bài tập 2
def xuat():
    t = int(input("Nhập: "))
    if 0 < t <= 100:
        for i in range(1, t + 1):
            str1 = input()
            nguyenam = 0
            phuam = 0
            str1.lower()
            for n in str1:
                if (n == 'a' or n == 'e' or n == 'i' or i == 'o' or n == 'u'):
                    nguyenam = nguyenam + 1
            else:
                phuam = phuam + 1
                print(f"Test{i}:\n{nguyenam} \n{phuam}")


xuat()


##bài tập 3

def xuat():
    t = int(input("Nhập: "))
    if 0 < t <= 100:
        for i in range(1, t + 1):
            str = input()
            print(f"Test{i}:", str.count(" "))


xuat()


# bài tập 4

def xuat():
    t = int(input("Nhập số lượng các dòng: "))
    if t > 0 and t <= 100:
        for i in range(1, t + 1):
            str_word = input("Nhập chữ: ")
            print(str_word.replace("\t", " "))


xuat()


# bài tập 5

def xuat(s1, s2):
    if s2 in s1:
        print(s1.count(s2))
    else:
        print('Chuỗi "{}" không xuất hiện trong chuỗi "{}"'.format(s2, s1))


t = int(input("Nhập: "))
if 0 < t <= 100:
    for i in range(t):
        s1 = input("nhập 1: ")
        s2 = input("nhập 2: ")
        print(f"test {i + 1}:", end="\n")
        xuat(s1, s2)


# bài tập 6

def xuat(s1, s2, s3):
    print(s1.replace(s2, s3))


t = int(input("Nhập: "))
if 0 < t <= 100:
    for i in range(t):
        s1 = input("Nhập chuỗi: ")
        s2 = input("nhập từ cũ: ")
        s3 = input("Nhập từ mới: ")
        print(f"test {i + 1}:", end="\n")
        xuat(s1, s2, s3)


# bài tập 7

def xuat():
    t = int(input("Nhập: "))
    if 0 < t <= 100:
        for i in range(1, t + 1):
            nhap = input()
            tucu = nhap.split()
            tumoi = []
            j = 0

            for ii in range(len(tucu)):
                if tucu[ii] not in tumoi:
                    tumoi.insert(j, tucu[ii])
                    j = j + 1

            n = ""
            for ii in range(len(tumoi)):
                n = n + tumoi[ii] + " "

            print(f"Test{i}: {n}")


xuat()
#Bài Tập 8:

def dem_tu(s1):
     str = s1.split(" ")
     count = {}
     for i in str:
         if i in count:
             count[i] += 1
         else:
             count[i] = 1
     for i in sorted(count, key=count.get, reverse=False):
         print(f"{i}-{count[i]}")

 r = int(input("nhập vào số lần: "))
 if 0 < r <= 100:
     for i in range(r):
         s1 = input("nhập chuỗi: ")
         print(f"test {i + 1}:", end="\n")
         dem_tu(s1)


# bài 10

def xuat():
    t = int(input("Nhập: "))
    if 0 < t <= 100:
        for i in range(1, t + 1):
            c = input()
            print(f"Test{i}:\n",
                  c.strip().title().replace("\t", " ").replace(".", ". ").replace(" .", ".").replace("!", ".").replace(
                      "?", "."))


xuat()
#

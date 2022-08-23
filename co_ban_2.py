#............./////xử lý file \\\\\\\.............
    # mở file
#hàm open: open(file,mode='r')
file_ob=open('FILE.txt')#mode mặc định là r
# các mode
'''
1) r: mở để đọc(mặc định)
2) r+: mở để đọc và ghi
3) w: mở để ghi. trước tiên nó sẽ xóa hết nội dung của file hiện có, nếu ko tồn tại file thì nó sẽ tự tạo ra file
4) w+: mở để đọc và ghi. trước đó xóa hết nội dung của file hiện có, nếu ko tồn tại thì tự tạo file
5) a: mở để ghi. nếu file ko tồn tại thì sẽ tạo 1 file
6) a+: mở để đọc và ghi. nếu file ko tồn tại thì sẽ tạo file'''
    
    #đóng file
file_ob.close()
    
    #đọc file
file_ob=open('FILE.txt')
#phương thức read <file>.read(size): size âm hoặc bỏ trống thì sẽ đọc hết nội dung file, còn lại thì sẽ đọc số ký tự bằng size
print(file_ob.read(2))
data=file_ob.read()
print(data)
file_ob.close()
#phương thức readline đọc từng dòng 1
file_ob=open('FILE.txt')
data=file_ob.readline()
print(data)
#phương thức readlines : đọc toàn bộ file sau đó cho chúng vào 1 list với mỗi phần tử là 1 dòng của file
file_ob=open('FILE.txt')
data=file_ob.readlines()
print(data)
#đọc file bằng constructor nhận iterable
file_ob=open('FILE.txt')
""" list_data=list(file_ob)
print(list_data) """
tup_data=tuple(file_ob)
print(tup_data)
file_ob.close()


    #ghi trong file
#phương thức write <file>.write(text) : trả về số ký tự được thêm vào
file=open('FILE.txt','w+')
file.write('update txt\n hihi')
file.close()
file=open('FILE.txt')
print(file.read())
    #kiểm soát con trỏ file
#phương thức seek: <file>.seek(offset,whence=0) text file thì whence=0, còn binary file thì bằng 1 or 2
#giúp di chuyển con trỏ về vị trí cần 
file.seek(0)
print(file.read())
# câu lệnh with
""" with expression [as variable]:
    with-block     """
with open('FILE.txt') as fle:
    data=fle.read()#kết thúc with block thì file đóng luôn
print(data)
#có thể kết hợp with với :=
with (fl:=open('FILE.txt','r')):
    data2=fl.read()

#////////////////////iteration\\\\\\\\\\\\\\\\\\\\\\\\
#là khái niệm chung cho việc lấy từng phần tử của 1 đối tượng 
# https://howkteam.vn/course/lap-trinh-python-co-ban/iteration-va-mot-so-ham-ho-tro-cho-iteration-object-trong-python-1571


#////////////////////hàm xuất\\\\\\\\\\\\\\\\\\\
#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
    #*objects : packing argument
    #sep : chia ra, phân ra(mặc định là khoảng trắng)
    #end : kết thúc bằng (mặc định \n)
    #file: mặc định là xuất ra màn hình, ngoài ra còn vào file

#///////////////////hàm nhập\\\\\\\\\\\\\\
#input nhập vào chuỗi nên nhập vào là gì đi nữa thì vẫn là kiểu str
a=input('string: ')
print(a)

#////////////////\\\\\\\\\boolean\\\\\\\\\\\\\\\\
#là kiểu dữ liệu trả về true hoặc false
# sử dụng trong việc so sánh giữa 2 iterable
print('abv'>'abc')
# sd trong toán tử is
# not- and - or
# các giá trị khác 0, rỗng, none khi chuyển về boolean thì là true
# mặc định 1 true, 0 false
a=5
print(1<a<6<8)

#/////////////////////////cấu trúc rẽ nhánh\\\\\\\\\\\\\\\\\\\\\\
        #//////////if đơn
'''if expression:

     #If-block'''
a=2
b=5
if a<b:
    print('a nhỏ hơn b')

        #////////////if - else if
'''if expression:

    # If-block

elif 2-expression:

    # 2-if-block

elif 3-expression:

    # 3-if-block

…

elif n-expression:

    # n-if-block'''
a=3
if a<0:
    print('a nhỏ hơn 0')
elif a<5:
    print('a nhỏ hơn 5')

         # /////////if-else
'''if expression:

    # If-block

else:

    # else-block'''
if a<0: print('a âm')
else: print('a dương')

        # ///shorthand if-else
#<Giá trị 1> if <Điều kiện> else <Giá trị 2> điều kiện đúng thì gt 1 còn sai thì gt2
a=5
b=9 if a>0 else 10
print('a bằng 5' if a == 5 else 'a khác 5')
        #////if-elif-else (ez)
        #/////match-case
a=5
match a:# chỉ chọn 1 case
    case 1: print('a=1')
    case 7: print('a=7')
    case _: print('a=5')
# case mở rộng
t = 5
match t:
    case 1 | 3 | 5 | 7 | 9:
        print("t là số lẻ bé hơn 10")
    case 2 | 4 | 6 | 8:
        print("t là số chẵn bé hơn 10")
    case _:
        print("t bằng 0")

x = 0
t = 4
match t:
    case 4 if x == 1:
        print("t = 4 và x = 1")
    case 4 if x == 0:
        print("t = 0 và x = 0")

# /////////////////////////////vòng lặp while\\\\\\\\\\\\\\\\\\
'''
while expression:

     # while-block
'''
k=5
while k>0:
    print('k=',k)
    k-=1

#//// break: kết thúc vòng lặp 
k=2
while True:
    if(k>0): print('k>0')
    else:break
    k-=1

#///// continue : chạy tiếp vòng lặp
'''
while expression:

    #while-block-1

    continue

    #while-block-2
'''
# vòng lặp sẽ thứ tự là chạy while-block-1 -> continue -> bỏ qua while block 2
k=0
while k<10:
    if k%2==0:
        k+=1
        continue
    print(k,'là số lẻ')
    k+=1

#///////// pass : giúp tránh lỗi nếu như vòng lặp ko có lệnh nào
'''
while expression:
    pass
'''
a=5
while a>0:
    pass

###//////// while-else : khi vòng while kết thúc thì lệnh else được thực hiện
'''
while expression:

    # while-block

else:

    # else-block
'''
k=5
while k>3:
    print('k lớn hơn 3')
    k-=1
else:
    print('k nhỏ hơn 3')
####nếu trong vòng while có break thì phần else cũng ko được thực hiện 

#///////////////////vòng lặp for\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'''
for variable_1, variable_2, .. variable_n in sequence:
    # for-block
'''
iter_=(x for x in range(3))
for value in iter_:
    print('->',value)

#...for-else : hoạt động tương tự while-else
'''
for variable_1, variable_2, .. variable_n in sequence:

    # for-block

else:

    # else-block
'''


# .... kiểu dữ liệu dãy số range
#cách 1: range(stop)
for value in range(3):
    print(value)
#cách 2: range(start,stop,[step])
for value in range(3,8):
    print(value)
for value in range(3,8,2):
    print(value)

# sử dụng range để duyệt list, tuple, chuỗi
lst=['s',(1,2,3),{'abc','cde'}]
for i in range(len(lst)):
    print(lst[i])

# comprehension: [ output-expression for-statement optional-predicate ]
a=['--'.join((a.capitalize(), b.upper() + c.lower())) for a, b, c in [('how', 'kteam', 'EDUCATION'), ('chia', 'sẻ', 'FREE')]] # bỏ trống optional-predicate
print(a)

# enumerate : enumerate(iterable[, start]) 
# start mặc định là 0
# tạo ra cấu trúc (start+0,seq[0]),(start+1,seq[1]),...
student=['lan','ngọc','thảo']
gen=enumerate(student)
for value in gen:
    print(value)

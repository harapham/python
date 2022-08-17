#comment....
#in ra màn hình
print("#Harapham")

#khai báo biến
a=1
b=2
s=a+b
print(s)
ten="Hara"
print(ten)
x,y,z=4,5,6
print(x,y,z)
# kiểm tra loại dữ liệu
print(type(ten))

#...........kiểu dữ liệu:.............
#       int, float,str,....,số thực, phân số,....

#lấy toàn bộ nội dung của thư viện (decimal)
from decimal import* # từ thư viện decimal import mọi thứ(*)
    #lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec=30
print(Decimal(10)/Decimal(3))

# hàm phân số Fraction()
from fractions import*
frac=Fraction(6,9)
print(frac)

# hàm số phức 
# <phần thực>+<phần ảo>
c=complex(2,5)
print(c)
print(c.real)
print(c.imag)

# toán tử 
    # chia dư %, chia nguyên //, chia thường /,lũy thừa **

# toán tử := (Assignment expression)
    #thực hiện phép gán khi đang thực hiện lệnh khác
a=3
b=(a:=a+3)+3
print(a)
print(b)
print(t:=5)
#thư viện math
    #để sử dụng 1 thư viện thì 
import math
    #trả về phần nguyên của x
math.trunc(2.3)
    #trả về số làm tròn của x và luôn nhỏ hơn hoặc bằng x
math.floor(2.9)
    #trả về số làm tròn của x và luôn lớn hơn hoặc bằng x
math.ceil(2.9)
    #trả về số thực là trị tuyệt đối của x
math.fabs(-2.9)
    #trả về căn bậc 2 của x
math.sqrt(4)
    #trả về UCLN của x,y
math.gcd(5,9)



#............. chuỗi trong python..............



s='Harapham'
print(s)
print(type(s))
    #chuỗi nhiều dòng
s = '''dong 1
… dong 2
… dong 3'''
print(s)
s='dong1\ndong2\ndong3'
print(s)

#docstring (một dạng chú thích)
'''đây là comment cho nhiều dòng'''

''' escape sequence 
- phát ra 1 tiếng bip \a
- lùi con trỏ về và xóa ký tự trước đó \b
- newline \n
- tab \t
- in ra ký tự ' \'
- in ra ký tự " \"
- in ra ký tự \ \\
'''
print('python\\ngắn gọn')

#chuỗi trần (ko dùng đến escape sequence) : r'nội dung chuỗi'
a=r'\n dấu \n đã bị bỏ qua'
print(a)
# lặp lại chuỗi
a='hara<3'
a*=3
print(a)
# tìm chuỗi trong chuỗi(nếu có trả về true ko thì về false)
print('hara'in'harapham')
#các toán tử so sánh chuỗi <,>,==,!=,<=,>=
print('hahaha'>'hahoho')
#để xem vị trí ký tự trong bảng mã unicode 
print(ord('t'))

# indexing của chuỗi
s='0123'
print(s[3],s[2])
print(s[-1],s[-2])
# cắt chuỗi
s='harapham'
print(s[0:3],s[4:len(s)-1])
print(s[0:4],s[4:len(s)])
print(s[2:None]) # hoặc là
print(s[2:])
print(s[:-2])
print(s[:])

# cắt chuỗi theo bước
a='0123456789'
print(a[2:8:2])
print(a[8:1:-2])
print(a[::-1])#lật ngược chuỗi

# ép kiểu dữ liệu: cú pháp <kiểu dữ liệu>(<giá trị>)
a='123'
b=int(a)
print(a,type(a),b,type(b))

#thay đổi nội dung chuỗi
s='chuỗi ban đầu đây nhé'
print(s)
s=s[0:6]+'đã thay đổi'+s[13:]
print(s)

# định dạng bằng toán tử %
print('hello %d hehe %s' %(1,'haha'))
# định dạng bằng chuỗi f (f-string)
variable='string'
print(f'this is a {variable}')
print(f'1:{{one}}, 2:{{two}}, 3:{variable}')
print(f'biến là {variable=}')
# định dạng bằng format
print('a: {},b: {},c: {}'.format(1,2,3))
print('a: {2},b: {1},c: {0}'.format(1,2,3))
print('a: {one},b: {two},c: {three}'.format(one=1,two=2,three=3))
    # căn lề trong format 
print('{:-^20}'.format('căn giữa nè'))
print('{:*<20}'.format('căn trái nè'))
print('{:+>20}'.format('căn phải nè'))


            ##biến đổi chuỗi
# capitalize: trả về chuỗi viết hoa ký tự đầu, viết thường các ký tự còn lại
print('haraPham'.capitalize())
# upper: trả về chuỗi viết hoa
print('hAraPham'.upper())
# lower : trả về chuỗi viết thường
print('HARapham'.lower())
# swapcase: trả về chuỗi có các ký tự thường thành hoa và ngược lại
print('HaRaPhAm'.swapcase())
# title: trả về chuỗi dạng tiêu đề(ký tự đầu của từ viết hoa)
print('hAra pHAM'.title())

            ##định dạng chuỗi
#phương thức center : <chuỗi>.center(width, [fillchar]) trả về chuỗi căn giữa có chiều rộng width
print('hara'.center(23))
print('hara'.center(23,'*'))
#phương thức rjust: căn lề phải
print('hara'.rjust(23))
print('hara'.rjust(23,'-'))
#phương thức ljust : căn lề trái
print('hara'.ljust(23))
print('hara'.ljust(23,'+'))
            # mã hóa
#phương thức encode: mã hóa chuỗi theo 1 chuẩn nào đó
a='hara hoho hihi hêhê hôhô'
b=a.encode(encoding='utf-8',errors='strict')
print(b)
b=a.encode()
print(b)
#phương thức decode : giải mã chuỗi đã được encode
c=b.decode()
print(c)
#phương thức join : trả về chuỗi nối xen kẽ
print(a.join(['1','2','3']))
#phương thức replace : thay thế các ký tự trong chuỗi
print(a.replace('a','AA'))
print(a.replace('h','HH',5))
#phương thức strip : trả về chuỗi với đầu đuôi được bỏ đi các ký tự char (nếu ko có char thì bỏ khoảng trắng và các escape sequence trừ \a)
print('   hara   '.strip())
print('???/?hara//?/???'.strip('?'))
print('abcbcacbHaraphamaccc'.strip('abc'))
#phương thức rstrip 
print('abcbcacbHaraphamaccc'.rstrip('abc'))
#phương thức lstrip
print('abcbcacbHaraphamaccc'.lstrip('abc'))
#phương thức removeprefix : xóa 1 ký tự đầu tiên đã biết
print('aacbHaraphamaccc'.removeprefix('a'))
#phương thức removesuffix
print('bHaraphamaccc'.removesuffix('c'))

            # các phương thức tách chuỗi
#phương thức split
a='harapham hee hee hoho'
b=a.split(' ')
print(b)
c=a.split(' ',2)
print(c)
#phương thức rsplit
d=a.rsplit(' ',2)
print(d)
#phương thức spitlines
a='mot\nhai\nba\nbon\n'
print(a.splitlines())
#phương thức partition
a='harapham hee hee hoho'
print(a.partition('he'))
#phương thức rpartition
print(a.rpartition('he'))
            #các phương thức tiện ích
#phương thức count
print(a.count('he'))
print(a.count('h',5,7))
#phương thức startswith : tìm xem chuỗi có bắt đầu bằng các ký tự cho sẵn ko
print(a.startswith('ha'))
print(a.startswith('h',4,9))
#phương thức endswith 
print(a.endswith('ha'))
print(a.endswith('h',4,9))
#phương thức find
print(a.find('p'))
print(a.find('p',5,9))
#phương thức rfind
print(a.rfind('p'))
print(a.rfind('p',5,15))
#phương thức index (giống find nhưng nếu ko tìm được thì sẽ lỗi)
print(a.index('a'))
#phương thức rindex
print(a.rindex('e'))
            #các phương thức xác thực
#phương thức islower: trả về true nếu tất cả các ký tự là viết thường
print(a.islower())
#phương thức isupper
print(a.isupper())
#phương thức istitle
print(a.istitle())
#phương thức isidentifier
'''Phương thức isidentifier trả về True khi cả ba điều kiện sau được thỏa mãn:

Chuỗi phải được bắt đầu bằng dấu gạch dưới (_) hoặc các kí tự chữ cái
Chuỗi không được chứa bất kì khoảng trắng nào
Không được chứa các kí tự đặc biệt (_, %, $, _...) ngoại trừ việc kí tự đầu tiên có thể là dấu gạch dưới.'''
print('_hara'.isidentifier())
#phương thức isdigit: trả về true nếu chuỗi đều là số
print('1234'.isdigit())
#phương thức isspace
print('   '.isspace())
print('  d '.isspace())
#phương thức iskeyword
import keyword
print(keyword.iskeyword('def'))





#.....................//// kiểu dữ liệu list////..................
[1,2,3,4]# đây là 1 list số nguyên
['a','b','c'] #đây là 1 list chuỗi
[[1,2],[3,4]] #đây là 1 list chứa list
[1,[2,'ba'],'bon'] #đây là 1 list chứa nhiều thứ :>

            #khởi tạo list
lst=[1,3,4,'nam']
empty_list=[]



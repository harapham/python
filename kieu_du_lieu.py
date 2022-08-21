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


# toán tử 
n = 69
n +1
n.__add__(1) # tương tự khi bạn n + 1
n.__sub__(9) # tương tự n - 9
n.__mul__(2) # tương tự n * 2
n.__radd__(1) # tương tự 1 + n
n.__rsub__(9) # tương tự 9 - n
n.__neg__() # tương tự -n


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
li=list([1,2,3])
str_lst=list('hara')
            #toán tử trong list
lst+=[5,6]
lst=li*2
print(5 in lst)
#toán tử so sánh nếu so sánh hết 2 list mà ko có giá trị khác thì chọn list dài hơn là lớn hơn
print(lst>li)
#indexing và cắt list giống chuỗi\
# thay đổi nội dung trong list
li[2]=5
            #ma trận
lis=[[1,2,3],[4,5,6]]
#gọi ra giống như c++
#######lưu ý không được gán list này với list kia nếu ko có chủ đích
# vì nếu đổi 1 trong 2 thì cả 2 đều bị thay đổi
# toán tử is trả về true nếu 1 trong 2 biến được trỏ đến biến còn lại (là được chỉ cùng 1 địa chỉ với được gán với nhau ý )
a=[1,2,3]
b=[1,2,3]
print(a is b)
a=b
print(a is b)
# cách copy (do chỉ là copy ko phải trỏ nên toán tử is trả về false)
#copy chỉ sao chép các phần tử của list chứ ko hề sao chép các phần tử con của list
#do đó nếu thay đổi con của list thì cả 2 lại thay đổi theo
a_copy1=list(a)
a_copy2=a[:]
a_copy3=a.copy()
                #....các tiện ích trong list
#phương thức count
ha=[1,2,3,4,1,5]
print(ha.count(1))
#phương thức index
print(ha.index(2))
#phương thức copy
ra=ha.copy()
#phương thức clear
ra.clear()
        #các phương thức cập nhật
# append thêm phần tử vào cuối list
ha.append(3)
#extend thêm nhiều phần tử vào cuối list
ha.extend([4,5])
#insert thêm phần tử vào vị trí i
ha.insert(1,0)
#pop bỏ đi phần tử thứ i 
ha.pop(1)
#remove bỏ đi phần tử có giá trị x đầu tiên
ha.remove(1)
        #các phương thức xử lí
#reverse đảo ngược
ha.reverse()
#sort sắp xếp theo 1 thức tự nào đó (mặc định là từ bé đến lớp)
ha.sort() #xếp tử bé đến lớn
ha.sort(reverse=True) #xếp từ lớn đến nhỏ
a='thank you very much'
b=a.split(' ')
b.sort(key=len) #sắp xếp theo chiều dài
print(b)


##,,,,,,,,,,,....... kiểu dữ liệu tuple
#vd
(1,2,3,4,5)
('r','t','k','haha',3,4)
([1,2],[3,4,5],6,(1,2))
#khởi tạo
tup=(1,2,3,4)# nếu khởi tạo 1 giá trị thì là tup=(1,)
empty_tub=()
#contructor (tạo ra 1 tuple)
tup=tuple([1,3,4])
new=(value for value in range(10) if value %2==0)
n_tup=tuple(new)
        # toán tử
#tuple giống hệt chuỗi, còn list chỉ hơi giống thôi
#indexing và cắt tuple
print(len(tup))
#gọi ra được từng index như list và chuỗi
# không thể thay đổi nội dung như chuỗi
        #ma trận
#giống như list
        #....;;;;các phương thức
#count
# index (trả về vị trí)


#//////////\\\\\\ kiểu dưc liệu set
# ko thể chứa 1 set trong set, ko chứa list
# các giá trị trùng sẽ tự bị loại
set_1={55,22}
set_2={'hehe'}
set_3 = {(69, 'Free'), (1, 2, 3)}
#comprehension
set_1={value for value in range(3)}
#contructor 
set_1=set((1,2,3))
print(set_1)
# set ko quan tâm đến vị trí của các phần tử
set_2=set('harapham')
print(set_2)

# ///////toán tử\
#in
print(1 in set_1)
#toán tử - trả về set gồm phần tử thuộc s1 và ko thuộc s2 (s1-s2)
print({1,2,3,4}-{1,2})
# toán tử & trả về set gồm phần tử thuộc cả 1 set
print({1,2,3}&{2,3,4,5})
#toán tử | trả về tất cả các phần tử thuộc s1 và s2
print({1,2,3}|{1,4,5,6})
#toán tử ^ trả về toán tử chỉ thuộc 1 set nghĩa là bỏ hết các cái chung ấy
print({1,2,3}^{3,4,5})
    #indexing và cắt ko hỗ trợ
    #...//// các phương thức
#clear
#copy
    # các phương thức đối sánh(giống các toán tử nhưng cho phép hoạt động với các iterable(đối tượng))
# phương thức union (toán tử |)
a={1,2,3,4,5}
b={2,4,6,7}
print(a.union(b))
# intersection (&)
a.intersection(b)
#difference (-)
a.difference(b)
#symmetric_difference (^) (chỉ được phép có 1 iterable trong ngoặc)
a.symmetric_difference(b)
    #....phương thức cập nhật
#pop trả về giá trị được lấy ra đồng thời xóa nó trong set
#remove 
a={1,2,3,4}
a.remove(1)
#discard loại bỏ giá trị trong set nếu ko có thì bỏ qua nghĩa là sẽ ko bị báo lỗi như remove
a.discard(2)
#add
a.add(5)
#update thêm lần lượt các phần tử của iterable vào trong set
a.update('abc',(1,2,3),[5,7,8])
    # phương thức xác thực
#issubset trả về true nếu set là tập con của other set
a.issubset(b)
#issuperset trả về true nếu set là tập hợp mẹ của otherset
a.issuperset(b)


#///////\\\\\\\\kiểu dữ liệu dict
# các phần tử là cặp key-value
dic={'name':'hara','member':23}
#comprehension
dic={key:value for key,value in [('name','hara'),('member',23)]}
#   contructor
# tạo dict rỗng
dic=dict()
#khởi tạo dict từ mapping object (khó)
class Map_Class:
          def keys(self):
                return [1, 2, 3]
          def __getitem__(self, key):
               return key * 2
map_obj = Map_Class()
dic = dict(map_obj)
# iterable
iter=[('name','hara'),('member',23)]
dic=dict(iter)
f = [('ab'), ('cd')]
dic_f=dict(f)
# khởi tạo bằng keyword arguments
dic_k = dict(name='Kteam', member=69)
#phương thức fromkeys : cho phép tạo 1 dict với các keys nằm trong 1 iterable. các giá trị này đều mặc định none
iter_=('name','number')
dic_none=dict.fromkeys(iter_)
print(dic_none)
dic=dict.fromkeys(iter_,'tự đặt đây')
print(dic)
#lấy value trong dict bằng key
print(dic['name'])
#thay đổi nội dung trong dict
dic['name']='hara'
#thêm thủ công 1 phần tử vào dict
dic['new key']='new value'
print(dic)
    # các phương thức tiện ích
#<dict>.copy()
#<dict>.clear()
    #các phương thức xử lý
#get: trả về giá trị của key. nếu ko có key trả về default
print(dic.get('name'))
#items: trả về 1 giá trị thuộc dict_items.
#các giá trị của dict_items sẽ là 1 tuple với giá trị thứ 1 là key thứ 2 là value
print(dic.items())
#key: trả về giá trị thuộc lớp dict_keys
#các giá trị của dict_keys sẽ là các key trong dict (dict_keys là 1 iterable)
print(dic.keys())
#values : trả về giá trị thuộc lớp dict_values
#các giá trị của dict_values sẽ là các value trong dict
print(dic.values())
#pop: bỏ đi phần tử có key và trả về value của key đó
#<dict>.pop(key,[default]) -> nếu ko có key thì báo lỗi nếu ko khai default(default=none) còn nếu có thêm default thì trả về default
dic.pop('new key')
dic.pop('non-exist','default_value')
#popitem : trả về 1 tuple với key và value tương ứng bất kỳ và loại bỏ cặp key-value ấy ra khỏi dict
print(dic.popitem())
print(dic)
#setdefault: trả về giá trị của key trong dict. ko có key thì trả về giá trị default và 1 cặp key-value mới sẽ đc thêm vào dict với key =key và value =default
#<dict>.setdefault(key,[default])
print(dic.setdefault('name'))
dic.setdefault('no1')
dic.setdefault('no2','tự đặt 2')
print(dic)
#update: cập nhật nội dung cho dict <dict>.update([E],**F)
 #kiểu packing arguments
dic.update(no3=3,no4=4)
print(dic)
 #kiểu truyền E
E={'no5':5,'no6':6}
dic.update(E)
E2=[('no7',7),('no8',8)]
dic.update(E2)
E3=(['no9',9],['no0',0])
dic.update(E3)
#toán tử | với 2 dict: trả về 1 dict mới với các cặp key-value có ở trong 2 dict
{'1':1,'2':2}|{'3':3,'4':4}

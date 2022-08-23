#//////////////////////function\\\\\\\\\\\\\\

# khai báo function
'''
def <function_name>(parameter_1 [: <kiểu dữ liệu gợi ý của parameter_1>], parameter_2 [: <kiểu dữ liệu gợi ý của parameter_2>], .., parameter_n [: <kiểu dữ liệu gợi ý của parameter_n>]) [-> <kiểu dữ liệu trả về được gợi ý> ]

    function-block
'''
def p(something : str)-> None:
    print(something)
    print('printed by print-function')

p('hara')

# gọi hàm (call function) <function>() hoặc  <tên biến> = <function> 
def call():
    print('hello')

call()

#Parameter và Argument
# parameter chính là tham số của hàm – là tên các biến sẽ được sử dụng trong hàm. Còn argument là đối số, tức là giá trị mà ta truyền cho parameter.
def Print(sthing): # sthing là parameter (tham số)
    print(sthing)
Print("hehe") # “hehe” là argument (đối số)

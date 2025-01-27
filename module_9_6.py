def all_variants(text):
    for j in range(1, len(text)+1):
        for i in range(0, len(text)):
            if i+j > len(text):
                break
            yield text[i:i+j]

a = all_variants("abc")
for i in a:
    print(i)

"""
Вывод на консоль:
a           
b           
c           
ab          
bc                
abc         
"""
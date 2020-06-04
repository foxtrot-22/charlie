#var=input("Type an expression:")
#print(var)
#myoperators=['*','-','+','/']
#mylist=['12'3,4,5,6,7,8,9,'*']
#separated = [x for x in mylist]
# new = [x for x in mylist if x in myoperators]
# old = [x for x in mylist if x not in myoperators]
# print(new)
# print(old)
# for i in new:
#     print(i)
# import re
# import ast
# test_str = "2*5-134+66"
# output = ast.literal_eval(test_str)
# print(output)
# # res = re.split(r'(\D)', test_str)
# # print(res)
# #var = input("Type an expression:")
# #print (eval(var))
# import ast
# sample_string = '"5*5"'
# output_value = ast.literal_eval(sample_string)
# print(output_value)
# print(eval(output_value))
sample = "6*5"
y=sample.split("*")
for i in y:
    print(i)
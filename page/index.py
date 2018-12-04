import ast
data = dict()
f = open('./../data/users.txt', 'r')

f_users = f.read()
users = ast.literal_eval(f_users)
f.close()
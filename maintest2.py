import subprocess

# cmd1 = ['dir']
# cmd2 = ['dir', r'C:\Users\Piyush\Desktop']


#p1 = subprocess.run(cmd1, shell=True,)
# print(p1)
# p1 = subprocess.run(cmd2, shell=True)
# print(p1)

a = input()
print('got it')

username = input('Enter username: ')
email = input('Enter email: ')

print('got it')

# cmd1 = ['git' 'config' '--global' 'user.name' 'f"{username}"']
# cmd2 = ['git' 'config' '--global' 'user.email' 'f"{email}"']
#
# cmd3 = ['git' 'init']
#
# cmd4 = ['git' 'add' '.']
#
# cmd5 = ['git' 'commit' '-m' '"my first commit"']
#
# cmd6 = ['get' 'status']


cmd1 = ['git' 'config' '--global' 'user.name' 'f"{username}"']
p1 = subprocess.run(cmd1, capture_output=True, shell=True, text=True)
print(p1.stdout)

a = input('-------: ')


cmd2 = ['git' 'config' '--global' 'user.email' 'f"{email}"']
p1 = subprocess.run(cmd2, capture_output=True, shell=True, text=True)
print(p1.stdout)

a = input('-------: ')

cmd3 = ['git' 'init']
p1 = subprocess.run(cmd3, capture_output=True, shell=True, text=True)
print(p1.stdout)

a = input('-------: ')

cmd4 = ['git' 'add' '.']
p1 = subprocess.run(cmd4, capture_output=True, shell=True, text=True)
print(p1.stdout)

a = input('-------: ')

cmd5 = ['git' 'commit' '-m' '"my first commit"']
p1 = subprocess.run(cmd5, capture_output=True, shell=True, text=True)
print(p1.stdout)

a = input('-------: ')


cmd6 = ['get' 'status']
p1 = subprocess.run(cmd6, capture_output=True, shell=True, text=True)
print(p1.stdout)

a = input('-------: ')

cmd7 = input(
    "Copy and past here your git remote of your existing repository \n  Your existing Repo git Remote : ")
cmd7 = cmd7.split()
p1 = subprocess.run(cmd7, capture_output=True, shell=True, text=True)
print(p1.stdout)

a = input('-------: ')

cmd8 = ['git' 'push' '-u' 'origin' 'master']
p1 = subprocess.run(cmd8, capture_output=True, shell=True, text=True)
print(p1.stdout)


import subprocess

# cmd1 = ['dir']
# cmd2 = ['dir', r'C:\Users\Piyush\Desktop']


#p1 = subprocess.run(cmd1, shell=True,)
# print(p1)

p1 = subprocess.run('dir', shell=True)
print(p1)

a = input('----')
print('got it')

username = input('Enter username: ')
email = input('Enter email: ')

print('got it')
#
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


cmd1 = ['git', 'config', '--global', 'user.name', f"{username}"]
p1 = subprocess.run(cmd1, capture_output=True, shell=True, text=True)
print(p1.stdout, p1.returncode)

a = input('username   done: ')


cmd2 = ['git', 'config', '--global', 'user.email', f"{email}"]
p2 = subprocess.run(cmd2, capture_output=True, shell=True, text=True)
print(p2.stdout, p2.returncode)

a = input('email   done: ')



cmd3 = ['git', 'init']
p3 = subprocess.run(cmd3, capture_output=True, shell=True, text=True)
print(p3.stdout, p3.returncode)

a = input('git init   done: ')


cmd4 = ['git', 'add', '.']
p4 = subprocess.run(cmd4, capture_output=True, shell=True, text=True)
print(p4.stdout, p4.returncode)

a = input('git add .    done: ')


cmd5 = ['git', 'commit', '-m', "my first commit"]
p5 = subprocess.run(cmd5, capture_output=True, shell=True, text=True)
print(p5.stdout, p5.returncode)

a = input('my first commint   done: ')

cmd6 = ['get', 'status']
p6 = subprocess.run(cmd6, capture_output=True, shell=True, text=True)
print(p6.stdout, p6.returncode)

a = input('get status   done: ')


cmd7 = input(
    "Copy and past here your git remote of your existing repository \n  Your existing Repo git Remote : ")
cmd7 = cmd7.split()
p7 = subprocess.run(cmd7, capture_output=True, shell=True, text=True)
print(p7.stdout, p7.returncode)

a = input('push link1   done: ')



cmd8 = ['git', 'push', '-u', 'origin', 'master']
p8 = subprocess.run(cmd8, capture_output=True, shell=True, text=True)
print(p8.stdout, p8.returncode)

a = input('push link2   done: ')
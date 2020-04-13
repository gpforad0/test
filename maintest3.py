import subprocess

a = input('start:')


p2 = subprocess.run('cd yul', shell=True)
print(p2, p2.returncode)
a = input('go ahead')

p1 = subprocess.run('mkdir yul', shell=True)
print(p1, p1.returncode)


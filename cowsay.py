import os

stream = os.popen('cowsay -l')
output = stream.read().split('  ')

with open('cowsay.txt', 'w') as file:
    for txt in output:
        st = os.popen(f'cowsay -f {txt} {txt}')
        out = st.read()
        file.write(out + '\n')

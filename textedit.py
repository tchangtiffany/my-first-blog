def hi():
    print('Hi there!')
    print('How are you?')

#hi()

# def hi(name):
#     if name == 'Ola':
#         print('Hi Ola!')
#     elif name == 'Sonja':
#         print('Hi Sonja!')
#     else:
#         print('Hi Tiff!')
#
# hi("TT")
def hi(name):
    print("hi "+name)

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')
for i in range(1, 6):
    print(i)

def identify():
    return __name__

print(globals())

# print(f'Running directly.  Module __name__: {identify()}')
# print('This will not be seen when the module is imported')

if __name__ == '__main__':
    print(f'Running directly.  Module __name__: {identify()}')
    print('This will not be seen when the module is imported')

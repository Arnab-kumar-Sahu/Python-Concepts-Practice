file=open("python.txt","w") # write method always delete the existing data if present and add new one
file.write('hello again\n')
file.writelines(['hello ','who ','are ','you ','again '])#it can accept sequence but sequence only with string values
file.close()
fout= open("mynewfile.txt", "w")
for i in range(2, 17):
    fout.write(str(i)+ "\n")
fout.close()

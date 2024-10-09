def merge_file(file1,file2,output_file):
    with open(file1,'r') as f1,open(file2,'r') as f2, open(output_file,'w') as outfile:
        outfile.write(f1.read())
        outfile.write('\n')
        outfile.write(f2.read())

merge_file('./test/test.txt', './test/test2.txt' , './test/out.txt')
    
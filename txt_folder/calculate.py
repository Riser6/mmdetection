file = "txt_folder/coatl_yolox.txt"
file1 = 'txt_folder/coatl_yolox/s1.txt'
file2 = 'txt_folder/coatl_yolox/s2.txt'
file3 = 'txt_folder/coatl_yolox/s3.txt'
file4 = 'txt_folder/coatl_yolox/s4.txt'
with open(file, 'r') as f:
    data = f.readlines()
    total = len(data)
    my_sum = 0
    for number in data[1:]:
        my_sum += float(number)
    ave = my_sum/total
    print(ave)

with open(file1, 'r') as f:
    data = f.readlines()
    total = len(data)
    my_sum = 0
    for number in data[1:]:
        my_sum += float(number)
    ave = my_sum/total
    print(ave)

with open(file2, 'r') as f:
    data = f.readlines()
    total = len(data)
    my_sum = 0
    for number in data[1:]:
        my_sum += float(number)
    ave = my_sum/total
    print(ave)

with open(file3, 'r') as f:
    data = f.readlines()
    total = len(data)
    my_sum = 0
    for number in data[1:]:
        my_sum += float(number)
    ave = my_sum/total
    print(ave)

with open(file4, 'r') as f:
    data = f.readlines()
    total = len(data)
    my_sum = 0
    for number in data[1:]:
        my_sum += float(number)
    ave = my_sum/total
    print(ave)

with open(file5, 'r') as f:
    data = f.readlines()
    total = len(data)
    my_sum = 0
    for number in data[1:]:
        my_sum += float(number)
    ave = my_sum/total
    print(ave)
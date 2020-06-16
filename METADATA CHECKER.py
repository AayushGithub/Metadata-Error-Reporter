





Path = 'enter path of md files'






import os
import csv
import sys 
stdoutOrigin=sys.stdout 
sys.stdout = open("RESULTS.txt", "w")
filelist = os.listdir(Path)
list_of_pass=[]
list_of_fail=[]
num_files=0
for i in filelist:
    if i.endswith(".md"):
        num_files+=1
        print('--------------------------------------------------------------')
        print('Current File :',i)
        print('--------------------------------------------------------------')
        with open(Path + i, 'r',encoding='utf-8') as myfile:
            data = myfile.read().splitlines()
        try:
            saved_list=data[0:9]
            len_s=len(saved_list)

            all_tests_pass=0

            first=saved_list[0]
            if(first=='---'):
                all_tests_pass+=1
                print("First Line Test Passed")
            else:
                print("First Line Test FAILED")

            second=saved_list[1]
            title=second[0:7]
            edited=second[7:]
            if title == 'TITLE: ':
                all_tests_pass+=1
                print("Title Prefix Test Passed")
            else:
                print("Title Prefix Test FAILED")
                

            third=saved_list[2]
            desc=third[0:13]
            length_desc=len(third[13:])
            if desc == 'DESCRIPTION: ':
                all_tests_pass+=1
                print("Description Prefix Test Passed")
            else:
                print("Description Prefix Test FAILED")
                
            if 120<=length_desc<=158:
                all_tests_pass+=1
                print('Description Length Test Passed')
            else:
                print("Description Length Test FAILED")

            fourth=saved_list[3]
            author=fourth[0:8]
            if author == 'AUTHOR: ':
                all_tests_pass+=1
                print("Author Prefix Test Passed")
            else:
                print("Author Prefix Test FAILED")

            fifth=saved_list[4]
            date=fifth[0:6]
            if date == 'DATE: ':
                all_tests_pass+=1
                print("Date Prefix Test Passed")
            else:
                print("Date Prefix Test FAILED")

            format_check=0

            year=int(fifth[6:10])
            h1=fifth[10]
            month=(fifth[11:13])
            h2=fifth[13]
            day=fifth[14:]
            if 1800<=year<=2200:
                format_check+=1
            if(h1=='-'):
                format_check+=1
            if (month == '01' or month=='02' or month == '03' or month=='04'
                or month == '05' or month=='06' or month == '07' or month=='08'
                or month == '09' or month=='10' or month == '11' or month=='12'):
                format_check+=1
            if(h2=='-'):
                format_check+=1
            if (day == '01' or day=='02' or day == '03' or day=='04'
                or day == '05' or day=='06' or day == '07' or day=='08'
                or day == '09' or day=='10' or day == '11' or day=='12'
                or day == '13' or day=='14' or day == '15' or day=='16'
                or day == '17' or day=='18' or day == '19' or day=='20'
                or day == '21' or day=='22' or day == '23' or day=='24'
                or day == '25' or day=='26' or day == '27' or day=='28'
                or day == '29' or day=='30' or day == '31'):
                format_check+=1
                
            if (format_check==5):
                all_tests_pass+=1
                print('Date Format Check Passed')
            else:
                print("Date Format Check FAILED")

            sixth=saved_list[5]
            image=sixth[0:7]
            if image == 'IMAGE: ':
                all_tests_pass+=1
                print("Image Prefix Test Passed")
            else:
                print("Image Prefix Test FAILED")

            seventh=saved_list[6]
            if(seventh=='---'):
                all_tests_pass+=1
                print("Last Line Test Passed")
            else:
                print("Last Line Test FAILED")

            eight=saved_list[7]
            if(eight==''):
                all_tests_pass+=1
                print('Blank Line Test Passed')
            else:
                print("Blank Line Test FAILED")

            ninth=saved_list[8]
            heading=ninth[2:]
            if (heading==edited):
                all_tests_pass+=1
                print('Heading and Title Match Test Passed')
            else:
                print("Heading and Title Match Test FAILED")    
                

            if(all_tests_pass == 11):
                print('ALL TESTS Passed')
                list_of_pass.append(i)
            else:
                list_of_fail.append(i)
                print('--------------------------------------------------------------')
                print("Atleast 1 Test FAILED")
        except:
            print('--------------------------------------------------------------')
            print("SOME ERROR WAS FOUND PLEASE CHECK FILE :",i)
            list_of_fail.append(i)
if(num_files!=1):
    pass_file='Files that passed all tests.csv'
    fail_file='Files that failed tests.csv'
    with open(pass_file,"w") as fo:
        wr = csv.writer(fo,delimiter="\n")
        wr.writerow(list_of_pass)
    with open(fail_file,"w") as fo:
        wr = csv.writer(fo,delimiter="\n")
        wr.writerow(list_of_fail)
sys.stdout.close()
sys.stdout=stdoutOrigin

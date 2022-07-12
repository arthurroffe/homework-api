# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 17:07:39 2022

@author: 88698
"""

'''
處理資料的數字(總樓數)
'''



import csv
import os

#把資料放在新資料夾所以判斷是否有一樣的名稱
new_forder = "chaged_csv"
if os.path.exists(new_forder):
    pass
else:
    os.makedirs(new_forder)
    
all_csv = []
#找所有csv檔案
for file in os.listdir("./"):
    if file.endswith(".csv"):
        all_csv.append(file)

#將中文數字轉換成阿拉伯數字    
for csv_name in all_csv:
    file_path = csv_name
    file_to_w_path = f"{new_forder}/{file_path}"
    
    csv_file = open(file_path,encoding="utf-8-sig")
    reader = csv.reader(csv_file)
    wf = open(file_to_w_path,'w',encoding="utf-8-sig",newline="")
    writer = csv.writer(wf)
            
    
    first_dis = {"零":0,"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}
    second_dis = {"一":1,"二":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":0}
    for index,i in enumerate(reader):
		#將標題重寫進去
        if index == 0:
            print(i)
            writer.writerow(i)
		#不是標題往這裡走
        elif index >= 2:
			#把層刪掉
            temp_list = i[10].split("層")
			#將多餘的空白元素刪掉
            if "" in temp_list: 
                temp_list.remove("")
			#如果只剩一個給他數值零
            if len(temp_list) == 0:
                temp_list.append("零")
			#如果已經是數值就給他原本有的值
            if temp_list[0].isdigit():
                i[10] = int(temp_list[0])
                writer.writerow(i)
			#如果不是數值
            else:
				#將文字分開
                temp_list = list(temp_list[0])
				#如果是一個就是單數
                if len(temp_list) == 1 :
                    i[10] = first_dis[temp_list[0]]
                    writer.writerow(i)
				#如果是兩個就是十幾或是幾十
                elif len(temp_list) == 2:
                    first_num = first_dis[temp_list[0]]
                    second_num = second_dis[temp_list[1]]
                    if first_num == 10 :
                        first_num = 1
                    i[10] = str(first_num) + str(second_num)
                    writer.writerow(i)
				#如果是三個就是幾十幾
                elif len(temp_list)  == 3:
                    first_num = first_dis[temp_list[0]]
                    second_num = second_dis[temp_list[2]]
                    i[10] = str(first_num) + str(second_num)
                    writer.writerow(i)
	#關閉文件避免錯誤
    wf.close()
    csv_file.close()
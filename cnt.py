import os
import xlsxwriter

cl = [
'',
'Nguyễn Hoàng Minh Anh',
'Trần Chương Anh',
'Phạm Dương Gia Bảo',
'Phan Phát Duy Bình',
'Trương Trí Dũng',
'Hà Minh Dũng',
'Nguyễn Minh Duy',
'Lê Thị Mỹ Duyên',
'Trương Tiến Đạt',
'Tô Thị Ngọc Hiền',
'Hà Minh Hiếu',
'Đặng Ngọc Hoàng',
'Nguyễn Huỳnh Tấn Khải',
'Vương Khang',
'Nguyễn Đăng Khoa',
'Bùi Đức Mạnh',
'Nguyễn Hà Hùng Minh',
'Huỳnh Giáng My',
'Phạm Hoàng Gia Nghi',
'Nguyễn Duy Ngọc',
'Phan Hồng Ngọc',
'Nguyễn Cao Đức Nguyên',
'Hà Quyền Nhân',
'Nguyễn Huỳnh Thảo Như',
'Nguyễn Thạch Thiên Phúc',
'Nguyễn Minh Quang',
'Đặng Ngọc Quyên',
'Hồ Trần Nhật Quyền',
'Đặng Minh Thiện',
'Nguyễn Quang Thông',
'Nguyễn Minh Tiến',
'Nguyễn Thanh Tuấn',
'Nguyễn Minh Triết'
]

print(len(cl))
workbook = xlsxwriter.Workbook('pic.xlsx')
worksheet = workbook.add_worksheet()

for i in range(1,34) :
    worksheet.write(i,0,cl[i])
    worksheet.write(i,1,len(os.listdir("./train"+"/"+str(i))))

workbook.close()
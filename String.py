message = 'Hello World'

result = len(message)

# ตรวจสอบว่า มีข้อความย่อย ใน ข้อความใหญ่ หรือไม่
print('World' in message)

# ตรวจสอบว่า ข้างในข้อความมีแต่ตัวเลขหรือไม่
print(message.isdigit())

# แปรงเป็นตัวใหญ่
print(message.upper())

# แทนคำที่ระบุด้วยคำอื่น
print(message.replace('World', '!!!'))

# ทำการแยกข้อความอออกจากกันตาม keyword ที่ระบุ
print(message.split(' '))

# แปรง list มาเป็น string โดยจะนำมาต่อกันด้วยข้อความที่ระบุ
print(' '.join(message.split(' ')))
quests = ['ปลูกต้นมะม่วง', 'ล้วงปลาไหล', 'ไล่ศัตรูพืช']

# เพิ่มข้อมูลไปที่ตำแหน่งสุดท้าย
# quests.append('ขูดมะพร้าว')

# เพิ่มข้อมูลไปที่ตำแหน่งที่เราระบุ
# quests.insert(1, 'ขูดมะพร้าว')

# ลบข้อมูลออกจาก list
# quests.remove('ล้วงปลาไหล')

# ตรวจสอบว่ามีข้อมูลนี้อยู่ใน list หรือไม่
if 'ไล่ศัตรูพืช' in quests:
    print('เข้าเมืองได้')

# นับจำนวนสมาชิก
max_quests = 5
if len(quests) <= max_quests:
    quests.append('จับปลาดุก')

for quest in quests:
    print(quest)
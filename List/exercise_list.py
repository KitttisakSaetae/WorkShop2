# จงแสดง "banana"
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# จงแก้ไขข้อมูลจาก "apple" เป็น "kiwi"
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

# จงเพิ่ม "kiwi" ไปยัง fruits list
fruits = ["apple", "banana", "cherry"]
fruits.append("kiwi")

# จงเพิ่ม "lemon" ไประหว่าง "apple" กับ "ิิbananna"
fruits = ["apple", "banana", "cherry"]
fruits.insert(0, "lemon")
print(fruits)

# จงลบ "cherry" จาก list
fruits = ["apple", "banana", "cherry"]
fruits.remove("cherry")
print(fruits)

# จงแสดงตัวสุดท้ายของ fruits
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

# จงแสดงจำนวนของ fruits
fruits = ["apple", "banana", "cherry"]
x = 0
for num in fruits:
    x = x + 1
print(x)
# หรืออีกวิธี
print(len(fruits))

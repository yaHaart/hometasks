videocards = [3070, 2060, 4000, 3090, 3070, 3090, 4000]
new_video_list = []
biggest = 0
print('Старый список видеокарт: ', videocards)
for i in videocards:
    if i > biggest:
        biggest = i

for i in videocards:
    if i != biggest:
        new_video_list.append(i)

print('Новый список видеокарт: ', new_video_list)

# зачёт! 🚀

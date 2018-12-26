import random

full_list = "Lily, Angela, Morayo, Peter, Adi, Alex, Andrew, Max, Tommy, Josh, Ellery"

cut_list_1 = [x.replace(" ", "") for x in full_list.split(",")]
cut_list_2 = [x.replace(" ", "") for x in full_list.split(",")]

assignments = {}

while len(cut_list_1) > 0:
    giver = cut_list_1[random.randint(0, len(cut_list_1)-1)]
    receiver = cut_list_2[random.randint(0, len(cut_list_2) - 1)]
    if giver != receiver:
        cut_list_1.remove(giver)
        cut_list_2.remove(receiver)
        assignments[giver] = receiver


for key in assignments:
    # print(key + " -> " + assignments[key])
    with open("SantaResults/" + key + ".txt", "w+") as file:
        file.write(assignments[key])

# print(assignments)






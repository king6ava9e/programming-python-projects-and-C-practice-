#OPENINING THE FILE
with open("hr_system.txt") as file_opened:
    for file in file_opened:
        #sripping the whitespace
        file_srip = file.strip()

        #splittiong into files
        file_split = file_srip.split(" ")
        name = file_split[0]
       # print(name)
        salary = float(file_split[3])
        ID_number = file_split[1]

        job_title = file_srip[2]
        print(f" {name} (ID : {ID_number}), Tile : {job_title} - ${salary:.2f}")

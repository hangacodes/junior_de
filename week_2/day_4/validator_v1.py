r1 = "Mina,29,DE,active"
r2 = "Bo,200,DE,active"
r3 = "Rui,40,JP,inactive"

#R1: r1 = "Mina,29,DE,active"
parts1 = r1.split(",")
name1 = parts1[0].strip()
age1 = int(parts1[1])
country1 = parts1[2].strip()
status1 = parts1[3].strip()

if len(parts1) != 4:
    print("ERROR_FIELDS")
else:
    if age1 < 0 or age1 > 120:
        print("ERROR_AGE")
    elif status1 != "active":
        print("SKIP_INACTIVE")
    else:
        if country1 == "DE":
            print("PROCESS_DE")
        else:
            print("PROCESS_OTHER")



#R2 : r2 = "Bo,200,DE,active"
parts2 = r2.split(",")
name2 = parts2[0].strip()
age2 = int(parts2[1])
country2 = parts2[2].strip()
status2 = parts2[3].strip()

if len(parts2) != 4:
    print("ERROR_FIELDS")
else:
    if age2 < 0 or age2 > 120:
        print("ERROR_AGE")
    elif status2 != "active":
        print("SKIP_INACTIVE")
    else:
        if country2 == "DE":
            print("PROCESS_DE")
        else:
            print("PROCESS_OTHER")



#R3 : r3 = "Rui,40,JP,inactive"
parts3 = r3.split(",")
name3 = parts3[0].strip()
age3 = int(parts3[1])
country3 = parts3[2].strip()
status3 = parts3[3].strip()

if len(parts3) != 4:
    print("ERROR_FIELDS")
else:
    if age3 < 0 or age3 > 120:
        print("ERROR_AGE")
    elif status3 != "active":
        print("SKIP_INACTIVE")
    else:
        if country3 == "DE":
            print("PROCESS_DE")
        else:
            print("PROCESS_OTHER")

#NOW THIS ONE WAS A STRUGGLE! First deliverable that made me actually think and fail
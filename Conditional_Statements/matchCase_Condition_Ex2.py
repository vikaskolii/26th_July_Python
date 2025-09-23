inp="CW"

match inp:
    case "CD":
        print("running CD code")
    case "CW":
        print("running CW code")
    case "BI":
        print("running BI code")
    case "MT":
        print("running MT code")
    case "MS":
        print("running MS code")
    case _:
        print("provide valid input")

## You are building a ticket info system  for a railway app
## Based on seat type, show its features


## Task : 
#Input  : "sleeper", "ac", " general", " luxury"
# Match using  match - case
# unknown -> show : "Invalid Seat type"

ticket_type = input("Enter your seat type (sleeper/AC/general/luxury) : " ).lower()

match ticket_type:
    case "sleeper":
        print(f"Your seat type is sleeper , Only sleep Berth available")
    case "ac":
        print(f"Your seat type is ac , Bedsheet, berth, blanket availbale")
    case "general":
        print(f"No berth available")
    case "luxury":
        print(f"premium seats with meals include")
    case _:
        print("invalid seat type")



"""You're building a ticket info system ofr a railway app .
based on seat tyep, show its feateures.
task :
Input:"sleeper","AC","general","luxury"
match using match-case 
Unknwon ---> show :"Invalid seat type"""


input_seat_type=input("Enter seat type(sleeper, AC,general,luxury)").lower()
match input_seat_type:
    case "sleeper":
        print("sleeper class:NO AC , beds available ")
    case "ac":
        print("AC class: AC available, bed available comfortable ride")
    case "general":
        print("general class:Cheapest options , no reservation")
    case "luxury":
        print("luxury class:Ac available , bed available, meal available , comfortable ride")
    case _:
        print("Invalid seat type")

    
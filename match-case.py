
# Switch statement / match-case statement in Python 3.10+

# http =int(input("Enter HTTP status code: "))
def http_status(http):
    match http:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal server error"
        case 600:
            return "custom error"
        case 403 | 401:
            return "forbidden"
        case _:
            return "unknown status"
    
# print(http_status(http))    

# days = input("Enter day (e.g., Monday): ")

def day_type(days):
     match days:
         case "satuday" | "sunday":
                return "weekend"
         case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
                return "weekday"
         case _:
                return "invalid day"

# print(day_type(days))

grades = int(input("enter Your grades : "))

def grade_category(grades):
     match grades:
          case 90 | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100:
                return "A"
          case 80 | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89:
                return "B"
          case 70 | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79:
                return "C"
          case 60 | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69:
                return "D"
          case _ :
               return "Fail"
          
print(grade_category(grades))
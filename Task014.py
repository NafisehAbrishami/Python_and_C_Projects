def daramad (hour , per_hour):
    if per_hour < 200:
        print (hour * per_hour)
        return "alaki kar nakon"
    else :
        print (hour * per_hour)
        return  "movavaq bashi"
hour = 8
per_hour = 150


print (daramad(hour , per_hour))

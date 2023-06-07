def hoquq (hour, per_hour):
    if hour > 8:
        return'Too much work!'
    else:
        daramad = hour * per_hour
        return daramad

hour = 8.1
per_hour = 2.5
daramad_kol = hoquq (hour, per_hour)

print (daramad_kol)


def office_outed(staff, boss):
    total_score = sum(staff.values()) + staff[boss]
    happiness_rating = total_score / len(staff)
    if happiness_rating > 5:
        return 'Nice Work Champ!'
    else:
        return 'Get Out Now!'

office_outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura')
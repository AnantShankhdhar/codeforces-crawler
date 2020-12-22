def rank_color(rating):
    if rating==0:
        rank='Unrated'
        color='Black'
    elif rating<=1199:
        rank='Newbie'
        color='Grey'
    elif rating<=1399:
        rank='Pupil'
        color='Green'
    elif rating<=1599:
        rank='Specialist'
        color='Cyan'
    elif rating<=1899:
        rank='Expert'
        color='Blue'
    elif rating<=2099:
        rank='Candidate Master'
        color='Purple'
    elif rating<=2299:
        rank='Master'
        color='Orange'
    elif rating<=2399:
        rank='International Master'
        color='Orange'
    elif rating<=2599:
        rank='Grandmaster'
        color='Red'
    elif rating<=2999:
        rank='International Grandmaster'
        color='Red'
    else:
        rank='Legendary Grandmaster'
        color='BRed'
    return rank,color
def getTotalBudget(people):
    r = 0
    for i in people:
        for k, v in i.items():
            if k == "budget":
                r = v+r
    return r

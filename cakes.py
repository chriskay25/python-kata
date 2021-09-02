def cakes(recipe, available):
    try:
        return min(int(available[i] / recipe[i]) for i in recipe)
    except:
        return 0

cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200})
cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"sugar": 1200, "eggs": 5, "milk": 200})
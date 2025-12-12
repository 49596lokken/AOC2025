database = open("5.txt").read().split("\n\n")


freshranges, ingredients = database

freshranges = freshranges.splitlines()

ingredients = ingredients.splitlines()
ans = 0
for ingredient in ingredients:
    for freshrange in freshranges:
        low, up = freshrange.split("-")
        low, up = int(low), int(up)+1

        if int(ingredient) in range(low, up):
            ans += 1
            break
print(ans)
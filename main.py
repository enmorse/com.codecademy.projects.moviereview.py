def movie_review(rating):
    return ["Avoid at all costs!" if rating < 5 else
            "This one was fun." if rating > 5 and rating < 9
            else "Outstanding!"]


print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."

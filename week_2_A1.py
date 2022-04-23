star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]
a = int(input('Enter Triology :- '))
b = int(input())
if a == 1:
    i = star_wars_movies[0]
    n = star_wars_movies[0][b-1]
elif a == 2:
    i = star_wars_movies[1]
    n = star_wars_movies[1][b-1]
else:
    i = star_wars_movies[2]
    n = star_wars_movies[2][b-1]
print(i)

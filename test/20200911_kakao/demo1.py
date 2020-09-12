def solution(v):
    answer = [
        v[0][0] ^ v[1][0] ^ v[2][0],
        v[0][1] ^ v[1][1] ^ v[2][1]
    ]

    return answer


v1 = [[1, 4], [3, 4], [3, 10]]
v2 = [[1, 1], [2, 2], [1, 2]]

#print(solution(v1))

data = "abc de f g".split(" ")
print(data)

class User:
    def __init__(self, name, height):
        self.name = name
        self.height = height

users = [User("roxy", 183), User("somi", 160)]
users.sort(key=lambda user : user .height)

for user in users:
    print(user.name)


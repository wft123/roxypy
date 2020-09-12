def solution(v):
    col_len = len(v[0])
    col_list = list(range(0, col_len))
    candidate_key = []

    for i in col_list:
        keys = comb(col_list, i)
        for key in keys:
            if is_minimality(candidate_key, key) and is_uniqueness(v, key):
                candidate_key.append(key)

    return len(candidate_key)


def comb(lst, n):
    ret = []
    if n > len(lst):
        return ret

    if n == 1:
        for i in lst:
            ret.append([i])
    elif n > 1:
        for i in range(len(lst) - n + 1):
            for temp in comb(lst[i + 1:], n - 1):
                ret.append([lst[i]] + temp)

    return ret


def is_uniqueness(matrix, keys):
    result = []
    for key in range(0, len(matrix)):
        data = ""
        for col in range(0, len(keys)):
            data += matrix[key][keys[col]]
        result.append(data)

    return len(v) == len(set(result))


def is_minimality(candidate_key, key):
    for candidate in candidate_key:
        if set(candidate) & set(key) == set(candidate):
            return False

    return True


v = [
    ["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
    ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]
]
print(solution(v))




'''
프렌즈대학교 컴퓨터공학과 조교인 제이지는 네오 학과장님의 지시로, 학생들의 인적사항을 정리하는 업무를 담당하게 되었다.

그의 학부 시절 프로그래밍 경험을 되살려, 모든 인적사항을 데이터베이스에 넣기로 하였고, 이를 위해 정리를 하던 중에 후보키(Candidate Key)에 대한 고민이 필요하게 되었다.

후보키에 대한 내용이 잘 기억나지 않던 제이지는, 정확한 내용을 파악하기 위해 데이터베이스 관련 서적을 확인하여 아래와 같은 내용을 확인하였다.

관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute) 또는 속성의 집합 중, 
다음 두 성질을 만족하는 것을 후보 키(Candidate Key)라고 한다.
유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다. 
즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.
제이지를 위해, 아래와 같은 학생들의 인적사항이 주어졌을 때, 후보 키의 최대 개수를 구하라.

위의 예를 설명하면, 학생의 인적사항 릴레이션에서 모든 학생은 각자 유일한 “학번”을 가지고 있다. 따라서 “학번”은 릴레이션의 후보 키가 될 수 있다. 
그다음 “이름”에 대해서는 같은 이름(“apeach”)을 사용하는 학생이 있기 때문에, “이름”은 후보 키가 될 수 없다. 
그러나, 만약 [“이름”, “전공”]을 함께 사용한다면 릴레이션의 모든 튜플을 유일하게 식별 가능하므로 후보 키가 될 수 있게 된다. 물론 [“이름”, “전공”, “학년”]을 
함께 사용해도 릴레이션의 모든 튜플을 유일하게 식별할 수 있지만, 최소성을 만족하지 못하기 때문에 후보 키가 될 수 없다. 따라서, 위의 학생 인적사항의 
후보키는 “학번”, [“이름”, “전공”] 두 개가 된다.

릴레이션을 나타내는 문자열 배열 relation이 매개변수로 주어질 때, 이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.

제한사항
relation은 2차원 문자열 배열이다.
relation의 컬럼(column)의 길이는 1 이상 8 이하이며, 각각의 컬럼은 릴레이션의 속성을 나타낸다.
relation의 로우(row)의 길이는 1 이상 20 이하이며, 각각의 로우는 릴레이션의 튜플을 나타낸다.
relation의 모든 문자열의 길이는 1 이상 8 이하이며, 알파벳 소문자와 숫자로만 이루어져 있다.
relation의 모든 튜플은 유일하게 식별 가능하다.(즉, 중복되는 튜플은 없다.)
입출력 예
relation	result
[[“100”,”ryan”,”music”,”2”],[“200”,”apeach”,”math”,”2”],[“300”,”tube”,”computer”,”3”],[“400”,”con”,”computer”,”4”],
[“500”,”muzi”,”music”,”3”],[“600”,”apeach”,”music”,”2”]]	
2

입출력 예 설명
입출력 예 #1 문제에 주어진 릴레이션과 같으며, 후보 키는 2개이다.

문제 풀이
가능한 모든 어트리뷰트의 조합을 만들고, 이 조합에서 조건을 만족시키는 조합만 추려야 하는 문제입니다.

dfs 또는 bit 를 이용한 집합 표현을 이용하여 어트리뷰트의 모든 부분 집합을 만들어냅니다.
만들어지는 각 부분 집합을 이용해서 중복 튜플이 있는지 검사합니다. 만약 중복 튜플이 없다면, 이 부분 집합을 슈퍼 키 집합(유일성을 만족하는 키들의 집합)에 포함시킵니다.

슈퍼 키 집합을 구한 후, 여기서 최소성을 만족하는 키들을 선택하여 후보 키 집합을 만들 수 있습니다.
만약 어떤 슈퍼 키 X에 대해 X의 부분집합인 슈퍼 키 Y가 없다면 (X ⊃ Y인 슈퍼 키 Y가 없다면) X는 후보 키로 선택될 수 있습니다.

예를 들어 어떤 릴레이션의 어트리뷰트가 ABCDE 이고, 슈퍼 키 집합이 {A, AB, BC, BCE, BDE, …} 라고 해봅시다.

A 는 후보 키로 선택될 수 있습니다.
AB 는 AB ⊃ A 이므로 후보 키가 될 수 없습니다.
BC 는 부분집합이 되는 다른 슈퍼 키가 없으므로 후보 키로 선택됩니다.
BCE 는 BCE ⊃ BC 이므로 후보 키가 될 수 없습니다.
BDE 는 부분집합이 되는 다른 슈퍼 키가 없으므로 후보 키로 선택됩니다.
…
따라서 이 경우 후보 키 집합은 {A, BC, BDE, …} 가 됩니다.

가능한 모든 조합을 만드는 부분 때문인지 앞쪽에 배치된 문제임에도 많은 지원자들이 어려움을 겪은 것으로 보입니다.
'''
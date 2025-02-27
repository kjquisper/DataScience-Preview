users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]   


friendship_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                    (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

friendship ={user["id"]: [] for user in users}

#print("lista de amigos",friendship)

for i,j in friendship_pairs:
    friendship[i].append(j)
    friendship[j].append(i)
    #print(i,j)
    #print(friendship)
    

#print("lista de amigos",friendship)    
    
#cual es el numero medio de conexiones

def number_of_friends(user):
    """cuantos amigos tiene el usuario"""
    user_id = user["id"]
    friend_id = friendship[user_id]
    return len(friend_id)


total_connections = sum(number_of_friends(user) for user in users)


num_users = len(users)

avg_connecction = total_connections / num_users

#print(avg_connecction)



def foaf_ids_users(user):
    return [foaf_id
            for friend_id in friendship[user["id"]]
            for foaf_id in friendship[friend_id]
            ]
    

#print(foaf_ids_users(users[0]))

#print(friendship[0])


#exluimos gente ya conocida por el usuario

from collections import Counter # no cargado inicialmente

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendship[user_id] # Para cada uno de mis amigos,
        for foaf_id in friendship[friend_id] # encuentra sus amigos
        if foaf_id != user_id # que no son yo
        and foaf_id not in
        friendship[user_id]# y no son mis amigos
    )
    
#print(friends_of_friends(users[3]))


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    """Find the ids of all users who like the target interest."""
    return [user_id
    for user_id, user_interest in interests
    if user_interest == target_interest]


#print(data_scientists_who_like(interests[0][1]))


#de intereses a usuarios
from collections import defaultdict
# Las claves son intereses, los valores son listas de user_ids con ese interés
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
    
#print(user_ids_by_interest)


# de usuarios a intereses

# Las claves son user_ids, los valores son listas de intereses para ese user_id
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    
    
print("\n")
#print(interests_by_user_id)
    
def most_common_interests_with(user):
    return Counter( 
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
)


#print(most_common_interests_with(users[0]))
#---------------------------------------------------------------------------------------------------------------------------

salaries_and_tenure = [(83000, 8.7), (88000, 8.1),
                       (48000, 0.7), (76000, 6),
                       (69000, 6.5), (76000, 7.5),
                       (60000, 2.5), (83000, 10),
                       (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenure:
    salary_by_tenure[tenure].append(salary)
    average_salary_by_tenure = {tenure: sum(salaries) / len(salaries) for tenure, salaries in salary_by_tenure.items() }
    
    
    
    
#print(salary_by_tenure,"\n",average_salary_by_tenure)
#no es util puesto que solo hay un salario por año de antiguedad

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

#salarios para bucket

#el defaultdict simplemente tiene la ventaja de asignar una lista vacia al valor si la clave no tiene contenido
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenure:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
""" print(salary_by_tenure_bucket)


print(salary_by_tenure_bucket.items()) """

#calculamos el salario medio por cada grupo
average_salary_by_bucket = {
tenure_bucket: sum(salaries) / len(salaries)
for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

#print(average_salary_by_bucket)

{'between two and five': 61500.0,
'less than two': 48000.0,
'more than five': 79166.66666666667}


#years_experience = [0.7, 1.9, 2.5, 4.2, 6.0, 6.5, 7.5, 8.1, 8.7, 10.0]

def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"

words_and_counts = Counter(word
                    for user, interest in interests
                    for word in interest.lower().split())



#print(words_and_counts)

#print(words_and_counts.most_common())


for word, count in words_and_counts.most_common():
    if count > 1:
        print(word,count)


    

    


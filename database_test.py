from firebase import firebase

# Starting database
firebase = firebase.FirebaseApplication('https://productivity-pen.firebaseio.com/'
, None)
result = firebase.get('/users', None)
result = firebase.get('/users/2', None, {'print': 'pretty'}, {'X_FANCY_HEADER': 'VERY FANCY'})
print(result)
# new_user = 'Amy Shan'
#
# result = firebase.get('/4', None)
#
# # result = firebase.post('/4', new_user, {'print': 'pretty'})
# print(result)

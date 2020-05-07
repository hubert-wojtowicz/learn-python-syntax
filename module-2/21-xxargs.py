def save_user(**user):
    print(user)
    print(user["id"])
    print(type(user))

save_user(id=1, name="admin")
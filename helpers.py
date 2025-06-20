import data


def modify_create_user_body(key, value):
    body_user = data.DataForUser.CREATE_USER_BODY.copy()
    body_user[key]=value
    return body_user

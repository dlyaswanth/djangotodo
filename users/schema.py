from drf_yasg import openapi

errorMessage = "Something went wrong !"

# create
response_schema_dict_create = {
    "200": openapi.Response(
        description="Success",
        examples={
            "application/json": {
                "status": True,
                "message": "User Created Successfully",
            }
        }
    ),
    "400": openapi.Response(
        description="Failure",
        examples={
            "application/json": {
                "status": False,
                "message": errorMessage,
            }
        }
    ),
}

# login 
response_schema_dict_login = {
    "200": openapi.Response(
        description="Success",
        examples={
            "application/json": {
                "status": True,
                "message": "Logged In Successfully",
                "data":{
                    "token":'',
                    "username":'',
                }
            }
        }
    ),
    "400": openapi.Response(
        description="Failure",
        examples={
            "application/json": {
                "status": False,
                "message": errorMessage,
            }
        }
    ),
}


# logout
response_schema_dict_logout = {
    "200": openapi.Response(
        description="Success",
        examples={
            "application/json": {
                "status": True,
                "message": "Logged out Successfully",
            }
        }
    ),
    "400": openapi.Response(
        description="Failure",
        examples={
            "application/json": {
                "status": False,
                "message": errorMessage,
            }
        }
    ),
}

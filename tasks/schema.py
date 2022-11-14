from drf_yasg import openapi

errorMessage = "Something went wrong !"

# list
response_schema_dict_list = {
    "200": openapi.Response(
        description="Success",
        examples={
            "application/json": {
                "status": True,
                "message": "Successfully Fetched",
                "data": []
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

# add
response_schema_dict_add = {
    "200": openapi.Response(
        description="Success",
        examples={
            "application/json": {
                "status": True,
                "message": "Created Successfully",
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

# edit
response_schema_dict_edit = {
    "200": openapi.Response(
        description="Success",
        examples={
            "application/json": {
                "status": True,
                "message": "Updated Successfully",
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


# delete
response_schema_dict_delete = {
    "200": openapi.Response(
        description="Success",
        examples={
            "application/json": {
                "status": True,
                "message": "Deleted Successfully",
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

from controllers import LoginUserControllers, RegisterUserControllers, LoginUserControllers2


user = {
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "login2_user": "/api/v01/user/login2", "login2_user_controllers": LoginUserControllers2.as_view("login2_api"),
    "register_user": "/api/v01/user/register", "register_user_controllers": RegisterUserControllers.as_view("register_api")
}


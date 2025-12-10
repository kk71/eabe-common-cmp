import getpass

from loguru import logger

from backend.models import *
from backend.services.auth import *


async def script():
    """修改已有用户的登录密码"""
    login_name = input("please enter the login name: ")
    u = await User.filter(login_name=login_name).first()
    if not u:
        raise ValueError(f"no user was found with {login_name=}")
    while True:
        raw_password = getpass.getpass("please enter password for the new account: ")
        raw_password2 = getpass.getpass("please re-enter password: ")
        if raw_password == raw_password2:
            break
        print("sorry the two passwords are not the same, please re-enter again.")
    s = UserAuthService(u)
    await s.set_new_password(raw_password)
    logger.success("done.")

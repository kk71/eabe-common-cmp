import getpass

from loguru import logger

from backend.models import *
from backend.services.auth import *


async def script():
    """创建一个管理员账户"""
    login_name = input("please enter the login name: ")
    while True:
        raw_password = getpass.getpass("please enter password for the new account: ")
        raw_password2 = getpass.getpass("please re-enter password: ")
        if raw_password == raw_password2:
            break
        print("sorry the two passwords are not the same, please re-enter again.")
    u = User(
        name="管理员",
        is_admin=True,
        login_name=login_name,
    )
    await u.save()
    s = UserAuthService(u)
    await s.set_new_password(raw_password)
    logger.success("done.")

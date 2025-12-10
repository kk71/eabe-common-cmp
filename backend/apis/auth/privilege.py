from typing import Optional
from collections import defaultdict

from pydantic import BaseModel, Field

from backend.apis import *
from backend.core.privilege import *
from backend.services.auth import *


@router.get(tags=[APITags.auth], summary="查询全部可用权限")
async def _() -> JsonResp[list[Privilege]]:
    return JsonResp(
        data=Privileges.all()
    )


class PrivilegeGroupGetter(BaseModel):
    root_group: PrivilegeGroup
    privilege_id_mapping: dict[str, list[str]]

    @classmethod
    def build(cls,
              entry_group: dict | None = None,
              group_privilege_name_mapping = None) -> Optional["PrivilegeGroupGetter"]:
        """
        两个参数都不传表示最外层
        :param entry_group:
        :param group_privilege_name_mapping:
        :return:
        """
        is_root = False
        if group_privilege_name_mapping is None:
            group_privilege_name_mapping = defaultdict(list)
            is_root = True
        if entry_group is None:
            entry_group = RootPrivilegeGroup.model_dump()
            is_root = True
        for i in entry_group["children"]:
            if "children" in i:
                cls.build(i, group_privilege_name_mapping)
            else:
                i["id"] = f"{entry_group["id"]}-{i["name"]}"
                group_privilege_name_mapping[i["name"]].append(i["id"])
        if is_root:
            return cls(
                root_group=entry_group,
                privilege_id_mapping=group_privilege_name_mapping
            )


@router.get("/group", tags=[APITags.auth], summary="查询全部可用权限分组")
async def _() -> JsonResp[PrivilegeGroupGetter]:
    return JsonResp(
        data=PrivilegeGroupGetter.build()
    )

__all__ = [
    "URL",
]

from urllib import parse

from pydantic import BaseModel, Field


class URL(BaseModel):
    """
    封装更易用的url
    部分字段意义参考 https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
    """
    scheme: str
    netloc: str
    path: str
    params: str
    query_dict: dict = Field(default_factory=dict, description="查询字典")
    fragment: str

    @classmethod
    def parse(cls, url: str) -> "URL":
        r = parse.urlparse(url)
        query_dict = {k: v[0] if len(v) == 1 else v for k, v in parse.parse_qs(r.query).items()}
        url_object = cls(
            scheme=r.scheme,
            netloc=r.netloc,
            path=r.path,
            params=r.params,
            query_dict=query_dict,
            fragment=r.fragment
        )
        return url_object

    def to_url(self) -> str:
        qd = parse.urlencode(self.query_dict)
        return parse.urlunparse((
            self.scheme, self.netloc, self.path, self.params, qd, self.fragment))

    def __str__(self):
        return self.to_url()

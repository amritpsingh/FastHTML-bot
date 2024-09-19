Title: fastapp – fasthtml

URL Source: https://docs.fastht.ml/api/fastapp.html

Markdown Content:
Usage can be summarized as:

```
from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get(): return Titled("A demo of fast_app()@")

serve()
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/fastapp.py#L38)

### fast\_app

> ```
>  fast_app (db_file:Optional[str]=None, render:Optional[<built-
>            infunctioncallable>]=None, hdrs:Optional[tuple]=None,
>            ftrs:Optional[tuple]=None, tbls:Optional[dict]=None,
>            before:Union[tuple,NoneType,fasthtml.core.Beforeware]=None,
>            middleware:Optional[tuple]=None, live:bool=False,
>            debug:bool=False, routes:Optional[tuple]=None,
>            exception_handlers:Optional[dict]=None,
>            on_startup:Optional[<built-infunctioncallable>]=None,
>            on_shutdown:Optional[<built-infunctioncallable>]=None,
>            lifespan:Optional[<built-infunctioncallable>]=None,
>            default_hdrs=True, pico:Optional[bool]=None,
>            surreal:Optional[bool]=True, htmx:Optional[bool]=True,
>            ws_hdr:bool=False, secret_key:Optional[str]=None,
>            key_fname:str='.sesskey', session_cookie:str='session_',
>            max_age:int=31536000, sess_path:str='/', same_site:str='lax',
>            sess_https_only:bool=False, sess_domain:Optional[str]=None,
>            htmlkw:Optional[dict]=None, bodykw:Optional[dict]=None,
>            reload_attempts:Optional[int]=1,
>            reload_interval:Optional[int]=1000, static_path:str='',
>            **kwargs)
> ```

_Create a FastHTML or FastHTMLWithLiveReload app._

   
|  | **Type** | **Default** | **Details** |
| --- | --- | --- | --- |
| db\_file | Optional\[str\] | None | Database file name, if needed |
| render | Optional\[callable\] | None | Function used to render default database class |
| hdrs | Optional\[tuple\] | None | Additional FT elements to add to |
| ftrs | Optional\[tuple\] | None | Additional FT elements to add to end of |
| tbls | Optional\[dict\] | None | Experimental mapping from DB table names to dict table definitions |
| before | Optional\[tuple\] | Beforeware | None | Functions to call prior to calling handler |
| middleware | Optional\[tuple\] | None | Standard Starlette middleware |
| live | bool | False | Enable live reloading |
| debug | bool | False | Passed to Starlette, indicating if debug tracebacks should be returned on errors |
| routes | Optional\[tuple\] | None | Passed to Starlette |
| exception\_handlers | Optional\[dict\] | None | Passed to Starlette |
| on\_startup | Optional\[callable\] | None | Passed to Starlette |
| on\_shutdown | Optional\[callable\] | None | Passed to Starlette |
| lifespan | Optional\[callable\] | None | Passed to Starlette |
| default\_hdrs | bool | True | Include default FastHTML headers such as HTMX script? |
| pico | Optional\[bool\] | None | Include PicoCSS header? |
| surreal | Optional\[bool\] | True | Include surreal.js/scope headers? |
| htmx | Optional\[bool\] | True | Include HTMX header? |
| ws\_hdr | bool | False | Include HTMX websocket extension header? |
| secret\_key | Optional\[str\] | None | Signing key for sessions |
| key\_fname | str | .sesskey | Session cookie signing key file name |
| session\_cookie | str | session\_ | Session cookie name |
| max\_age | int | 31536000 | Session cookie expiry time |
| sess\_path | str | / | Session cookie path |
| same\_site | str | lax | Session cookie same site policy |
| sess\_https\_only | bool | False | Session cookie HTTPS only? |
| sess\_domain | Optional\[str\] | None | Session cookie domain |
| htmlkw | Optional\[dict\] | None | Attrs to add to the HTML tag |
| bodykw | Optional\[dict\] | None | Attrs to add to the Body tag |
| reload\_attempts | Optional\[int\] | 1 | Number of reload attempts when live reloading |
| reload\_interval | Optional\[int\] | 1000 | Time between reload attempts in ms |
| static\_path | str |  | Where the static file route points to, defaults to root dir |
| kwargs |  |  |  |
| **Returns** | **Any** |  |  |

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/fastapp.py#L99)

### PageX

> ```
>  PageX (title, *con)
> ```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/fastapp.py#L98)

### ContainerX

> ```
>  ContainerX (*cs, **kwargs)
> ```

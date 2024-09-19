Title: Component extensions – fasthtml

URL Source: https://docs.fastht.ml/api/xtend.html

Markdown Content:
```
from pprint import pprint
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L25)

### A

> ```
>  A (*c, hx_get=None, target_id=None, hx_swap=None, href='#', hx_vals=None,
>     id=None, cls=None, title=None, style=None, accesskey=None,
>     contenteditable=None, dir=None, draggable=None, enterkeyhint=None,
>     hidden=None, inert=None, inputmode=None, lang=None, popover=None,
>     spellcheck=None, tabindex=None, translate=None, hx_post=None,
>     hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>     hx_target=None, hx_swap_oob=None, hx_include=None, hx_select=None,
>     hx_select_oob=None, hx_indicator=None, hx_push_url=None,
>     hx_confirm=None, hx_disable=None, hx_replace_url=None,
>     hx_disabled_elt=None, hx_ext=None, hx_headers=None, hx_history=None,
>     hx_history_elt=None, hx_inherit=None, hx_params=None,
>     hx_preserve=None, hx_prompt=None, hx_request=None, hx_sync=None,
>     hx_validate=None, **kwargs)
> ```

_An A tag; `href` defaults to ‘#’ for more concise use with HTMX_

```
A('text', ht_get='/get', target_id='id')
```

```
<a href="#" ht-get="/get" hx-target="#id">text</a>
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L31)

### Form

> ```
>  Form (*c, enctype='multipart/form-data', target_id=None, hx_vals=None,
>        id=None, cls=None, title=None, style=None, accesskey=None,
>        contenteditable=None, dir=None, draggable=None, enterkeyhint=None,
>        hidden=None, inert=None, inputmode=None, lang=None, popover=None,
>        spellcheck=None, tabindex=None, translate=None, hx_get=None,
>        hx_post=None, hx_put=None, hx_delete=None, hx_patch=None,
>        hx_trigger=None, hx_target=None, hx_swap=None, hx_swap_oob=None,
>        hx_include=None, hx_select=None, hx_select_oob=None,
>        hx_indicator=None, hx_push_url=None, hx_confirm=None,
>        hx_disable=None, hx_replace_url=None, hx_disabled_elt=None,
>        hx_ext=None, hx_headers=None, hx_history=None, hx_history_elt=None,
>        hx_inherit=None, hx_params=None, hx_preserve=None, hx_prompt=None,
>        hx_request=None, hx_sync=None, hx_validate=None, **kwargs)
> ```

_A Form tag; identical to plain [`ft_hx`](https://answerdotai.github.io/fasthtml/api/components.html#ft_hx) version except default `enctype='multipart/form-data'`_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L37)

### AX

> ```
>  AX (txt, hx_get=None, target_id=None, hx_swap=None, href='#',
>      hx_vals=None, id=None, cls=None, title=None, style=None,
>      accesskey=None, contenteditable=None, dir=None, draggable=None,
>      enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>      lang=None, popover=None, spellcheck=None, tabindex=None,
>      translate=None, hx_post=None, hx_put=None, hx_delete=None,
>      hx_patch=None, hx_trigger=None, hx_target=None, hx_swap_oob=None,
>      hx_include=None, hx_select=None, hx_select_oob=None,
>      hx_indicator=None, hx_push_url=None, hx_confirm=None,
>      hx_disable=None, hx_replace_url=None, hx_disabled_elt=None,
>      hx_ext=None, hx_headers=None, hx_history=None, hx_history_elt=None,
>      hx_inherit=None, hx_params=None, hx_preserve=None, hx_prompt=None,
>      hx_request=None, hx_sync=None, hx_validate=None, **kwargs)
> ```

_An A tag with just one text child, allowing hx\_get, target\_id, and hx\_swap to be positional params_

```
<a href="#" hx-get="/get" hx-target="#id">text</a>
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L43)

### Hidden

> ```
>  Hidden (value:Any='', id:Any=None, target_id=None, hx_vals=None,
>          cls=None, title=None, style=None, accesskey=None,
>          contenteditable=None, dir=None, draggable=None,
>          enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>          lang=None, popover=None, spellcheck=None, tabindex=None,
>          translate=None, hx_get=None, hx_post=None, hx_put=None,
>          hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None,
>          hx_swap=None, hx_swap_oob=None, hx_include=None, hx_select=None,
>          hx_select_oob=None, hx_indicator=None, hx_push_url=None,
>          hx_confirm=None, hx_disable=None, hx_replace_url=None,
>          hx_disabled_elt=None, hx_ext=None, hx_headers=None,
>          hx_history=None, hx_history_elt=None, hx_inherit=None,
>          hx_params=None, hx_preserve=None, hx_prompt=None,
>          hx_request=None, hx_sync=None, hx_validate=None, **kwargs)
> ```

_An Input of type ‘hidden’_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L49)

### CheckboxX

> ```
>  CheckboxX (checked:bool=False, label=None, value='1', id=None, name=None,
>             target_id=None, hx_vals=None, cls=None, title=None,
>             style=None, accesskey=None, contenteditable=None, dir=None,
>             draggable=None, enterkeyhint=None, hidden=None, inert=None,
>             inputmode=None, lang=None, popover=None, spellcheck=None,
>             tabindex=None, translate=None, hx_get=None, hx_post=None,
>             hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>             hx_target=None, hx_swap=None, hx_swap_oob=None,
>             hx_include=None, hx_select=None, hx_select_oob=None,
>             hx_indicator=None, hx_push_url=None, hx_confirm=None,
>             hx_disable=None, hx_replace_url=None, hx_disabled_elt=None,
>             hx_ext=None, hx_headers=None, hx_history=None,
>             hx_history_elt=None, hx_inherit=None, hx_params=None,
>             hx_preserve=None, hx_prompt=None, hx_request=None,
>             hx_sync=None, hx_validate=None, **kwargs)
> ```

_A Checkbox optionally inside a Label, preceded by a [`Hidden`](https://answerdotai.github.io/fasthtml/api/xtend.html#hidden) with matching name_

```
show(CheckboxX(True, 'Check me out!'))
```

Check me out!

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L59)

### Script

> ```
>  Script (code:str='', id=None, cls=None, title=None, style=None,
>          attrmap=None, valmap=None, **kwargs)
> ```

_A Script tag that doesn’t escape its code_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L65)

### Style

> ```
>  Style (*c, id=None, cls=None, title=None, style=None, attrmap=None,
>         valmap=None, **kwargs)
> ```

_A Style tag that doesn’t escape its code_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L70)

### double\_braces

> ```
>  double_braces (s)
> ```

_Convert single braces to double braces if next to special chars or newline_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L76)

### undouble\_braces

> ```
>  undouble_braces (s)
> ```

_Convert double braces to single braces if next to special chars or newline_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L82)

### loose\_format

> ```
>  loose_format (s, **kw)
> ```

_String format `s` using `kw`, without being strict about braces outside of template params_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L88)

### ScriptX

> ```
>  ScriptX (fname, src=None, nomodule=None, type=None, _async=None,
>           defer=None, charset=None, crossorigin=None, integrity=None,
>           **kw)
> ```

_A `script` element with contents read from `fname`_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L96)

### replace\_css\_vars

> ```
>  replace_css_vars (css, pre='tpl', **kwargs)
> ```

_Replace `var(--)` CSS variables with `kwargs` if name prefix matches `pre`_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L105)

### StyleX

> ```
>  StyleX (fname, **kw)
> ```

_A `style` element with contents read from `fname` and variables replaced from `kw`_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L113)

### On

> ```
>  On (code:str, event:str='click', sel:str='', me=True)
> ```

_An async surreal.js script block event handler for `event` on selector `sel`_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L120)

### Prev

> ```
>  Prev (code:str, event:str='click')
> ```

_An async surreal.js script block event handler for `event` on previous sibling_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L125)

### Now

> ```
>  Now (code:str, sel:str='')
> ```

_An async surreal.js script block on selector `me(sel)`_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L131)

### AnyNow

> ```
>  AnyNow (sel:str, code:str)
> ```

_An async surreal.js script block on selector `any(sel)`_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L136)

### run\_js

> ```
>  run_js (js, id=None, **kw)
> ```

_Run `js` script, auto-generating `id` based on name of caller if needed, and js-escaping any `kw` params_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L143)

### HtmxOn

> ```
>  HtmxOn (eventname:str, code:str)
> ```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L150)

### Titled

> ```
>  Titled (title:str='FastHTML app', *args, cls='container', target_id=None,
>          hx_vals=None, id=None, style=None, accesskey=None,
>          contenteditable=None, dir=None, draggable=None,
>          enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>          lang=None, popover=None, spellcheck=None, tabindex=None,
>          translate=None, hx_get=None, hx_post=None, hx_put=None,
>          hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None,
>          hx_swap=None, hx_swap_oob=None, hx_include=None, hx_select=None,
>          hx_select_oob=None, hx_indicator=None, hx_push_url=None,
>          hx_confirm=None, hx_disable=None, hx_replace_url=None,
>          hx_disabled_elt=None, hx_ext=None, hx_headers=None,
>          hx_history=None, hx_history_elt=None, hx_inherit=None,
>          hx_params=None, hx_preserve=None, hx_prompt=None,
>          hx_request=None, hx_sync=None, hx_validate=None, **kwargs)
> ```

_An HTML partial containing a `Title`, and `H1`, and any provided children_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L155)

### Favicon

> ```
>  Favicon (light_icon, dark_icon)
> ```

_Light and dark favicon headers_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L184)

### jsd

> ```
>  jsd (org, repo, root, path, prov='gh', typ='script', ver=None, esm=False,
>       **kwargs)
> ```

_jsdelivr [`Script`](https://answerdotai.github.io/fasthtml/api/xtend.html#script) or CSS `Link` tag, or URL_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/xtend.py#L192)

### clear

> ```
>  clear (id)
> ```

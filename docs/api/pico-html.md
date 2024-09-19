Title: Pico.css components – fasthtml

URL Source: https://docs.fastht.ml/api/pico.html

Markdown Content:
`picocondlink` is the class-conditional css `link` tag, and `picolink` is the regular tag.

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/pico.py#L30)

### set\_pico\_cls

> ```
>  set_pico_cls ()
> ```

Run this to make jupyter outputs styled with pico:

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/pico.py#L49)

### Card

> ```
>  Card (*c, header=None, footer=None, target_id=None, hx_vals=None,
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

_A PicoCSS Card, implemented as an Article with optional Header and Footer_

```
show(Card('body', header=P('head'), footer=P('foot')))
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/pico.py#L57)

### Group

> ```
>  Group (*c, target_id=None, hx_vals=None, id=None, cls=None, title=None,
>         style=None, accesskey=None, contenteditable=None, dir=None,
>         draggable=None, enterkeyhint=None, hidden=None, inert=None,
>         inputmode=None, lang=None, popover=None, spellcheck=None,
>         tabindex=None, translate=None, hx_get=None, hx_post=None,
>         hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>         hx_target=None, hx_swap=None, hx_swap_oob=None, hx_include=None,
>         hx_select=None, hx_select_oob=None, hx_indicator=None,
>         hx_push_url=None, hx_confirm=None, hx_disable=None,
>         hx_replace_url=None, hx_disabled_elt=None, hx_ext=None,
>         hx_headers=None, hx_history=None, hx_history_elt=None,
>         hx_inherit=None, hx_params=None, hx_preserve=None, hx_prompt=None,
>         hx_request=None, hx_sync=None, hx_validate=None, **kwargs)
> ```

_A PicoCSS Group, implemented as a Fieldset with role ‘group’_

```
show(Group(Input(), Button("Save")))
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/pico.py#L63)

### Search

> ```
>  Search (*c, target_id=None, hx_vals=None, id=None, cls=None, title=None,
>          style=None, accesskey=None, contenteditable=None, dir=None,
>          draggable=None, enterkeyhint=None, hidden=None, inert=None,
>          inputmode=None, lang=None, popover=None, spellcheck=None,
>          tabindex=None, translate=None, hx_get=None, hx_post=None,
>          hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>          hx_target=None, hx_swap=None, hx_swap_oob=None, hx_include=None,
>          hx_select=None, hx_select_oob=None, hx_indicator=None,
>          hx_push_url=None, hx_confirm=None, hx_disable=None,
>          hx_replace_url=None, hx_disabled_elt=None, hx_ext=None,
>          hx_headers=None, hx_history=None, hx_history_elt=None,
>          hx_inherit=None, hx_params=None, hx_preserve=None,
>          hx_prompt=None, hx_request=None, hx_sync=None, hx_validate=None,
>          **kwargs)
> ```

_A PicoCSS Search, implemented as a Form with role ‘search’_

```
show(Search(Input(type="search"), Button("Search")))
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/pico.py#L69)

### Grid

> ```
>  Grid (*c, cls='grid', target_id=None, hx_vals=None, id=None, title=None,
>        style=None, accesskey=None, contenteditable=None, dir=None,
>        draggable=None, enterkeyhint=None, hidden=None, inert=None,
>        inputmode=None, lang=None, popover=None, spellcheck=None,
>        tabindex=None, translate=None, hx_get=None, hx_post=None,
>        hx_put=None, hx_delete=None, hx_patch=None, hx_trigger=None,
>        hx_target=None, hx_swap=None, hx_swap_oob=None, hx_include=None,
>        hx_select=None, hx_select_oob=None, hx_indicator=None,
>        hx_push_url=None, hx_confirm=None, hx_disable=None,
>        hx_replace_url=None, hx_disabled_elt=None, hx_ext=None,
>        hx_headers=None, hx_history=None, hx_history_elt=None,
>        hx_inherit=None, hx_params=None, hx_preserve=None, hx_prompt=None,
>        hx_request=None, hx_sync=None, hx_validate=None, **kwargs)
> ```

_A PicoCSS Grid, implemented as child Divs in a Div with class ‘grid’_

```
colors = [Input(type="color", value=o) for o in ('#e66465', '#53d2c5', '#f6b73c')]
show(Grid(*colors))
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/pico.py#L76)

### DialogX

> ```
>  DialogX (*c, open=None, header=None, footer=None, id=None,
>           target_id=None, hx_vals=None, cls=None, title=None, style=None,
>           accesskey=None, contenteditable=None, dir=None, draggable=None,
>           enterkeyhint=None, hidden=None, inert=None, inputmode=None,
>           lang=None, popover=None, spellcheck=None, tabindex=None,
>           translate=None, hx_get=None, hx_post=None, hx_put=None,
>           hx_delete=None, hx_patch=None, hx_trigger=None, hx_target=None,
>           hx_swap=None, hx_swap_oob=None, hx_include=None, hx_select=None,
>           hx_select_oob=None, hx_indicator=None, hx_push_url=None,
>           hx_confirm=None, hx_disable=None, hx_replace_url=None,
>           hx_disabled_elt=None, hx_ext=None, hx_headers=None,
>           hx_history=None, hx_history_elt=None, hx_inherit=None,
>           hx_params=None, hx_preserve=None, hx_prompt=None,
>           hx_request=None, hx_sync=None, hx_validate=None, **kwargs)
> ```

_A PicoCSS Dialog, with children inside a Card_

```
hdr = Div(Button(aria_label="Close", rel="prev"), P('confirm'))
ftr = Div(Button('Cancel', cls="secondary"), Button('Confirm'))
d = DialogX('thank you!', header=hdr, footer=ftr, open=None, id='dlgtest')
# use js or htmx to display modal
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/pico.py#L83)

### Container

> ```
>  Container (*args, target_id=None, hx_vals=None, id=None, cls=None,
>             title=None, style=None, accesskey=None, contenteditable=None,
>             dir=None, draggable=None, enterkeyhint=None, hidden=None,
>             inert=None, inputmode=None, lang=None, popover=None,
>             spellcheck=None, tabindex=None, translate=None, hx_get=None,
>             hx_post=None, hx_put=None, hx_delete=None, hx_patch=None,
>             hx_trigger=None, hx_target=None, hx_swap=None,
>             hx_swap_oob=None, hx_include=None, hx_select=None,
>             hx_select_oob=None, hx_indicator=None, hx_push_url=None,
>             hx_confirm=None, hx_disable=None, hx_replace_url=None,
>             hx_disabled_elt=None, hx_ext=None, hx_headers=None,
>             hx_history=None, hx_history_elt=None, hx_inherit=None,
>             hx_params=None, hx_preserve=None, hx_prompt=None,
>             hx_request=None, hx_sync=None, hx_validate=None, **kwargs)
> ```

_A PicoCSS Container, implemented as a Main with class ‘container’_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/pico.py#L88)

### PicoBusy

> ```
>  PicoBusy ()
> ```

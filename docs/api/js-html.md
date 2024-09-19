Title: Javascript examples – fasthtml

URL Source: https://docs.fastht.ml/api/js.html

Markdown Content:
To expedite fast development, FastHTML comes with several built-in Javascript and formatting components. These are largely provided to demonstrate FastHTML JS patterns. There’s far too many JS libs for FastHTML to wrap them all, and as shown here the code to add FastHTML support is very simple anyway.

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/js.py#L15)

### light\_media

> ```
>  light_media (css:str)
> ```

_Render light media for day mode views_

|  | **Type** | **Details** |
| --- | --- | --- |
| css | str | CSS to be included in the light media query |

```
light_media('.body {color: green;}')
```

```
<style>@media (prefers-color-scheme: light) {.body {color: green;}}</style>
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/js.py#L22)

### dark\_media

> ```
>  dark_media (css:str)
> ```

_Render dark media for nught mode views_

|  | **Type** | **Details** |
| --- | --- | --- |
| css | str | CSS to be included in the dark media query |

```
dark_media('.body {color: white;}')
```

```
<style>@media (prefers-color-scheme:  dark) {.body {color: white;}}</style>
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/js.py#L35)

### MarkdownJS

> ```
>  MarkdownJS (sel='.marked')
> ```

_Implements browser-based markdown rendering._

|  | **Type** | **Default** | **Details** |
| --- | --- | --- | --- |
| sel | str | .marked | CSS selector for markdown elements |

Usage example [here](https://docs.fastht.ml/tutorials/quickstart_for_web_devs.html#rendering-markdown).

```
__file__ = '../../fasthtml/katex.js'
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/js.py#L43)

### KatexMarkdownJS

> ```
>  KatexMarkdownJS (sel='.marked', inline_delim='$', display_delim='$$',
>                   math_envs=None)
> ```

   
|  | **Type** | **Default** | **Details** |
| --- | --- | --- | --- |
| sel | str | .marked | CSS selector for markdown elements |
| inline\_delim | str | $ | Delimiter for inline math |
| display\_delim | str | $$ | Delimiter for long math |
| math\_envs | NoneType | None | List of environments to render as display math |

KatexMarkdown usage example:

```
longexample = r"""
Long example:

$$\begin{array}{c}

\nabla \times \vec{\mathbf{B}} -\, \frac1c\, \frac{\partial\vec{\mathbf{E}}}{\partial t} &
= \frac{4\pi}{c}\vec{\mathbf{j}}    \nabla \cdot \vec{\mathbf{E}} & = 4 \pi \rho \\

\nabla \times \vec{\mathbf{E}}\, +\, \frac1c\, \frac{\partial\vec{\mathbf{B}}}{\partial t} & = \vec{\mathbf{0}} \\

\nabla \cdot \vec{\mathbf{B}} & = 0

\end{array}$$
"""

app, rt = fast_app(hdrs=[KatexMarkdownJS()])

@rt('/')
def get():
    return Titled("Katex Examples", 
        # Assigning 'marked' class to components renders content as markdown
        P(cls='marked')("Inline example: $\sqrt{3x-1}+(1+x)^2$"),
        Div(cls='marked')(longexample)
    )
```

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/js.py#L58)

### HighlightJS

> ```
>  HighlightJS (sel='pre code', langs:str|list|tuple='python', light='atom-
>               one-light', dark='atom-one-dark')
> ```

_Implements browser-based syntax highlighting. Usage example [here](https://docs.fastht.ml/tutorials/quickstart_for_web_devs.html#code-highlighting)._

   
|  | **Type** | **Default** | **Details** |
| --- | --- | --- | --- |
| sel | str | pre code | CSS selector for code elements. Default is industry standard, be careful before adjusting it |
| langs | str | list | tuple | python | Language(s) to highlight |
| light | str | atom-one-light | Light theme |
| dark | str | atom-one-dark | Dark theme |

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/js.py#L82)

### SortableJS

> ```
>  SortableJS (sel='.sortable', ghost_class='blue-background-class')
> ```

   
|  | **Type** | **Default** | **Details** |
| --- | --- | --- | --- |
| sel | str | .sortable | CSS selector for sortable elements |
| ghost\_class | str | blue-background-class | When an element is being dragged, this is the class used to distinguish it from the rest |

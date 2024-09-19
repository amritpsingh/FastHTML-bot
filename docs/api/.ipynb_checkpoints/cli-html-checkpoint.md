Title: Command Line Tools – fasthtml

URL Source: https://docs.fastht.ml/api/cli.html

Markdown Content:
Command Line Tools – fasthtml
===============       

[![Image 1](https://docs.fastht.ml/logo.svg)](https://docs.fastht.ml/index.html)

*   [Home](https://fastht.ml/)
*   [Learn](https://about.fastht.ml/)

*   [](https://github.com/answerdotai/fasthtml)
*   [](https://x.com/answerdotai)

1.  [Source](https://docs.fastht.ml/api/core.html)
2.  [Command Line Tools](https://docs.fastht.ml/api/cli.html)

*   [Get Started](https://docs.fastht.ml/index.html)
    
*   [Tutorials](https://docs.fastht.ml/tutorials/index.html)
    
    *   [FastHTML By Example](https://docs.fastht.ml/tutorials/by_example.html)
        
    *   [Web Devs Quickstart](https://docs.fastht.ml/tutorials/quickstart_for_web_devs.html)
        
    *   [JS App Walkthrough](https://docs.fastht.ml/tutorials/e2e.html)
        
    *   [BYO Blog](https://docs.fastht.ml/tutorials/tutorial_for_web_devs.html)
        
*   Explanations
    
    *   [**ft** Components](https://docs.fastht.ml/explains/explaining_xt_components.html)
        
    *   [FAQ](https://docs.fastht.ml/explains/faq.html)
        
    *   [OAuth](https://docs.fastht.ml/explains/oauth.html)
        
    *   [Routes](https://docs.fastht.ml/explains/routes.html)
        
*   Reference
    
    *   [Custom Components](https://docs.fastht.ml/ref/defining_xt_component.html)
        
    *   [Live Reloading](https://docs.fastht.ml/ref/live_reload.html)
        
*   Source
    
    *   [Core](https://docs.fastht.ml/api/core.html)
        
    *   [Components](https://docs.fastht.ml/api/components.html)
        
    *   [Component extensions](https://docs.fastht.ml/api/xtend.html)
        
    *   [Javascript examples](https://docs.fastht.ml/api/js.html)
        
    *   [Pico.css components](https://docs.fastht.ml/api/pico.html)
        
    *   [OAuth](https://docs.fastht.ml/api/oauth.html)
        
    *   [Command Line Tools](https://docs.fastht.ml/api/cli.html)
        
    *   [fastapp](https://docs.fastht.ml/api/fastapp.html)
        

On this page
------------

*   [railway\_link](https://docs.fastht.ml/api/cli.html#railway_link)
*   [railway\_deploy](https://docs.fastht.ml/api/cli.html#railway_deploy)

*   [Report an issue](https://github.com/AnswerDotAI/fasthtml/issues/new)

Other Formats
-------------

*   [CommonMark](https://docs.fastht.ml/api/cli.html.md)

1.  [Source](https://docs.fastht.ml/api/core.html)
2.  [Command Line Tools](https://docs.fastht.ml/api/cli.html)

Command Line Tools
==================

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/cli.py#L15)

### railway\_link

> ```
>  railway_link ()
> ```

_Link the current directory to the current project’s Railway service_

* * *

[source](https://github.com/AnswerDotAI/fasthtml/blob/main/fasthtml/cli.py#L33)

### railway\_deploy

> ```
>  railway_deploy (name:str, mount:<function bool_arg>=True)
> ```

_Deploy a FastHTML app to Railway_

|  | **Type** | **Default** | **Details** |
| --- | --- | --- | --- |
| name | str |  | The project name to deploy |
| mount | bool\_arg | True | Create a mounted volume at /app/data? |

*   [Report an issue](https://github.com/AnswerDotAI/fasthtml/issues/new)

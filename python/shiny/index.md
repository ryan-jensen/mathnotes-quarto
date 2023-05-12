---
title: Shinylive applications embedded in Quarto documents
format: html
order: 3
filters:
  - shinylive
---




### Embedded Shiny application

To display a running Shiny app, use a code block with `{shinylive-python}`.

```{shinylive-python}
#| standalone: true
#| viewerHeight: 420

from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider("period", "Period", 0.5, 4, 1, step=0.5),
            ui.input_slider("amplitude", "Amplitude", 0, 2, 1, step=0.25),
            ui.input_slider("shift", "Phase shift", 0, 2, 0, step=0.1),
        ),
        ui.panel_main(
            ui.output_plot("plot"),
        ),
    ),
)


def server(input, output, session):
    @output
    @render.plot(alt="Sine wave")
    def plot():
        t = np.arange(0.0, 4.0, 0.01)
        s = input.amplitude() * np.sin(
            2 * np.pi / input.period() * (t - input.shift() / 2)
        )
        fig, ax = plt.subplots()
        ax.set_ylim([-2, 2])
        ax.plot(t, s)
        ax.grid()


app = App(app_ui, server)

```

Note that the code block currently must have `#| standalone: true`, which indicates that the code represents a complete Shiny application, as opposed to one which has parts spread throughout the document (which will be supported in the future).

The example above also uses `#| viewerHeight: 420` to set the height of the viewer to 420 pixels.


### Editor with app

If you want to display an editor panel with along with the running application, use `#| components: [editor, viewer]`. Users will be able to use the editor to modify the code and re-run the application.

:::{.column-page-inset-right}
```{shinylive-python}
#| standalone: true
#| components: [editor, viewer]

from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", 0, 100, 40),
    ui.output_text_verbatim("txt"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"The value of n*2 is {input.n() * 2}"

app = App(app_ui, server)

```
:::

The default width in a Quarto document is somewhat narrow for showing the editor and viewer next to each other. It can be made wider with [Quarto layout containers](https://quarto.org/docs/authoring/article-layout.html). In the example above it uses `column-page-inset-right`.


#### Vertically stacked components

To display the editor above the code, use `#| layout: vertical`.

```{shinylive-python}
#| standalone: true
#| components: [editor, viewer]
#| layout: vertical
#| viewerHeight: 300

from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.input_slider("n", "N", 0, 100, 40),
    ui.output_text_verbatim("txt"),
)

def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"The value of n*2 is {input.n() * 2}"

app = App(app_ui, server)

```


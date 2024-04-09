from taipy.gui import Gui, Markdown
import plotly.express as px

tips_df = px.data.tips()

main_chart_type_list = ["scatter", "density_contour"]
selected_main_chart_type = "density_contour"
margin_chart_type_list = ["histogram", "box", "violin"]
selected_margin_chart_type = "box"
show_marginal = True
show_smoker = True
show_size = True


def create_figure(main_chart_type, margin_chart_type, show_marginal, show_smoker, show_size):
    chart_args = {}
    if main_chart_type == "scatter":
        chart_fn = px.scatter
    else:
        chart_fn = px.density_contour

    if show_marginal:
        chart_args["marginal_x"] = margin_chart_type
        chart_args["marginal_y"] = margin_chart_type
    if show_smoker:
        chart_args["color"] = "smoker"
    if show_size and main_chart_type == "scatter":
        chart_args["size"] = "size"

    fig = chart_fn(tips_df, x="total_bill", y="tip", **chart_args)
    return fig


page = Markdown(
"""
<|toggle|theme|>

<|container|

<|card|

# Total Bill vs. Tips

<|layout|columns=1 1 1|

<|{selected_main_chart_type}|selector|lov={main_chart_type_list}|mode=radio|label=Main chart type|>

<|{selected_margin_chart_type}|selector|lov={margin_chart_type_list}|mode=radio|label=Margin chart type|>

<toggles|
Toggles

<|{show_marginal}|toggle|label=Show marginal|hover_text=Show marginal distribution|>

<|{show_smoker}|toggle|label=Show smoker|hover_text=Differentiate smokers by color|>

<|{show_size}|toggle|label=Show table size|hover_text=Display table size by marker size (only for scatter chart)|active={selected_main_chart_type == 'scatter'}|>
|toggles>

|>

<|chart|figure={create_figure(selected_main_chart_type, selected_margin_chart_type, show_marginal, show_smoker, show_size)}|>

|>

|>
""")  # fmt: skip

if __name__ == "__main__":
    Gui(page=page).run(dark_mode=False, run_browser=False, use_reloader=True)

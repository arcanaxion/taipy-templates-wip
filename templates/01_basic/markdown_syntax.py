from taipy.gui import Gui, Markdown
import plotly.express as px

tips_df = px.data.tips()

main_chart_type_list = ["scatter", "density_contour"]
selected_main_chart_type = "density_contour"
margin_chart_type_list = ["histogram", "box", "violin"]
selected_margin_chart_type = "box"


def create_figure(main_chart_type, margin_chart_type):
    if main_chart_type == "scatter":
        chart_fn = px.scatter
    else:
        chart_fn = px.density_contour
    fig = chart_fn(tips_df, x="total_bill", y="tip", marginal_x=margin_chart_type, marginal_y=margin_chart_type)
    return fig


page = Markdown(
"""
<|toggle|theme|>

<|container|

<|card|

# Total Bill vs. Tips

<|layout|columns=1 1|

<|{selected_main_chart_type}|selector|lov={main_chart_type_list}|mode=radio|label=Main chart type|>

<|{selected_margin_chart_type}|selector|lov={margin_chart_type_list}|mode=radio|label=Margin chart type|>

|>

<|chart|figure={create_figure(selected_main_chart_type, selected_margin_chart_type)}|>

|>

|>
""")  # fmt: skip

if __name__ == "__main__":
    Gui(page=page).run(dark_mode=False, run_browser=False, use_reloader=True)

# This entrypoint file to be used in development. Start by reading README.md
from unittest import main
import time_series_visualizer


# Test your function by calling it here
time_series_visualizer.draw_line_plot()
"""creating a line graph\n
Returns:
       this function does create a line graph every time we call it
       it makes a figure of the graph at the end of the function\n
       by the return fig\n
"""
time_series_visualizer.draw_bar_plot()
"""creating a bar graph\n
Returns:
       this function does create a bar graph every time we call it
       it makes a figure of the graph at the end of the function\n
       by the return fig\n
"""
time_series_visualizer.draw_box_plot()
"""creating a boxplot graph\n
Returns:
       this function does create a boxplot graph every time we call it
       it makes a figure of the graph at the end of the function\n
       by the return fig\n
"""

# Run unit tests automatically
main(module='test_module', exit=False)

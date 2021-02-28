from manim import *
import pandas as pd

class TimeSeries(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=8000,
            x_axis_config={"tick_frequency": 1000},
            #x_labeled_nums=np.arange(0, 15, 1),
            x_axis_label="Time",
            y_min=0,
            y_max=250,
            y_axis_config={"tick_frequency": 50},
            #y_labeled_nums=np.arange(0, 15, 1),
            y_axis_label="Value",
            include_tip=True,
            exclude_zero_label=False,
            **kwargs
            )
        abp_csv = pd.read_csv("./data/abp2.csv")[0:1000]
        self.times = abp_csv["time"]
        self.vals = abp_csv["val"]
        self.n=len(self.vals)

    def construct(self):
        self.setup_axes()
        function=VGroup()
        for i in range(0, self.n-1):
            start = self.coords_to_point(self.times[i], self.vals[i])
            end = self.coords_to_point(self.times[i+1], self.vals[i+1])
            startp = Dot(start, color=RED, radius=0.04)
            line=Line(start, end, color=BLUE)
            function.add(startp, line)
        endp = Dot(self.coords_to_point(self.times[self.n-1], self.vals[self.n-1]), color=RED, radius=0.04)
        function.add(endp)
        self.play(ShowCreation(function), run_time=5)
        self.wait(5)

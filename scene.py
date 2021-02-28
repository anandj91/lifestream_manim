from manim import *

class TimeSeries(GraphScene):
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=15,
            x_axis_config={"tick_frequency": 1},
            x_labeled_nums=np.arange(0, 15, 1),
            x_axis_label="Time",
            y_min=0,
            y_max=15,
            y_axis_config={"tick_frequency": 1},
            y_labeled_nums=np.arange(0, 15, 1),
            y_axis_label="Value",
            include_tip=True,
            **kwargs
            )
        self.vals = [0,1,5,3,2,5,6,1,3,10,4,7,13,2,2]
        self.n=len(self.vals)

    def construct(self):
        self.setup_axes()
        function=VGroup()
        for i in range(0, self.n-1):
            start = self.coords_to_point(i, self.vals[i])
            end = self.coords_to_point(i+1, self.vals[i+1])
            startp = Dot(start, color=RED)
            line=Line(start, end, color=BLUE)
            function.add(startp, line)
        endp = Dot(self.coords_to_point(self.n-1, self.vals[self.n-1]), color=RED)
        function.add(endp)
        self.play(ShowCreation(function), run_time=5)
        self.wait(5)

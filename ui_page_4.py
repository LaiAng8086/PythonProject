import csv_read
import seaborn as sns
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def get_ui(input):
    global ui
    ui = input


class Figure_Canvas(FigureCanvas):

    def __init__(self, title, projection_name=None):
        self.fig = Figure(layout='tight')
        FigureCanvas.__init__(self, self.fig)
        if(projection_name == None):
            self.axes = self.fig.add_subplot(111)
        else:
            self.axes = self.fig.add_subplot(111, projection=projection_name)
        self.axes.set_title(title)


def correlation(x, y):
    std_x = (x-x.mean())/x.std(ddof=0)
    std_y = (y-y.mean())/y.std(ddof=0)

    return (std_x * std_y).mean()


def setup():
    csv_read.read_data()
    fig = Figure_Canvas("Correlation Result")
    raised_hands = csv_read.csv_data['raisedhands']
    discussion = csv_read.csv_data['Discussion']
    v_resources = csv_read.csv_data['VisitedResources']
    v_announcements = csv_read.csv_data['AnnouncementsView']
    sns.heatmap(csv_read.csv_data.corr(), annot=True,ax=fig.axes)
    ui.page4_grid.addWidget(fig)
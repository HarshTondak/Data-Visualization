import justpy as jp
import pandas
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data['Day'] = data['Timestamp'].dt.date
day_average = data.groupby(['Day']).mean()

chart_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Day'
    },
    subtitle: {
        text: 'These graphs repesents average rating by review analysis'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Days'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Ratings'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 5'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} Day {point.y}*'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()

    h1 = jp.QDiv(a=wp, text="Analisys of Course Reviews", classes="text-h3 text-center q-pa-md")
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.title.text = "Average Rating by Day"
    hc.options.series[0].data = list(day_average['Rating'])
    hc.options.xAxis.categories = list(day_average.index)

    return wp

jp.justpy(app)
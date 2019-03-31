import plotly.plotly as py
# import plotly.tools as tls
import plotly.graph_objs as go
py.sign_in('Cliffy25', 'lrsnLBiTFOkdgH17aNIf')

# Create random data with numpy
import numpy as np


# NOTE: This is procedural code, and will need to be changed into OO format.

class Main:
	def main():
		N = 100
		random_x = np.linspace(0, 1, N)
		random_y0 = np.random.randn(N)+5
		random_y1 = np.random.randn(N)
		random_y2 = np.random.randn(N)-5

		# Create traces
		trace0 = go.Scatter(
			x = random_x,
			y = random_y0,
			mode = 'markers',
			name = 'markers'
		)

		trace1 = go.Scatter(
			x = random_x,
			y = random_y1,
			mode = 'lines',
			name = 'lines'
		)

		data = [trace0, trace1]
		py.plot(data, filename='scatter-mode-3')

Main.main()



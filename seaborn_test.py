import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

fmri = sns.load_dataset("fmri")
ax = sns.lineplot(x="timepoint", y="signal", hue="region", style="event", 
		markers=True, dashes=False, data=fmri)



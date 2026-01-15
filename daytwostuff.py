# %%
# python paths
Path = '@Prishab50 ➜ /workspaces/daytwostuff (main)'
New_Path = '(.venv) @Prishab50 ➜ /workspaces/daytwostuff (main)'
# The python path changed once the virtual environment was activated to (.venv) in the start
# which indicated it was active.

# Should you include the environment in your repo or not?
# You should not include the environment as it is specific to your machine,
# and as a requirements.txt file is included it is unnecessary.

# %%
import pandas as pd

#%%
df = pd.read_csv('Air_Quality.csv')
df.head()

# %%
# What do you notice about the extension menu?
# The extension menu shows the locally installed extensions as well as 
# the specific codespace extensions installed

# %%
# Data wrangler allows you to see and filter through a whole dataset in a table.
# It also allows you to write code and see how the dataset is being altered instantly.
# The third useful thing it can do is that you can make transformations visually instead of through code easily.

# %%
# Why do we use a requirements.txt file?
# A requirements.txt file allows one to easily convey what packages and versions are needed
# for a project to be extecuted. It makes it simple to install them as well. 



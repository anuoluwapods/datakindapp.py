import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image 


# App Header
col1, col2 = st.columns(2)
image = Image.open('image.png')

col1.markdown('''# **SNAP & BDT Program Web App**
''')
col2.write("A DATA KIND PROJECT")
col2.image(image)

col1.write("This Web application consists of only states with counties below federal poverty line")





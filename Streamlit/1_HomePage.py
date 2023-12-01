import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import json
import matplotlib.pyplot as plt
import plotly.express as px
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

import sys
sys.path.append("WebScraping")

from Soccer import *
from NHL import *
from NBA import *
from Styles import *

st.title("Sports Dashboard")

st.write("**Use this cool dashboard to check information about many sports**")
st.write("**Currently, we support soccer, basketball and Ice Hockey**")

st.header("Soccer")
st.text("This dashboard has information from many leagues around the world. Some of them are listed here.")
writeColumns('image', 'https://cdn.ssref.net/req/202311071/tlogo/fb/9.png', 'https://cdn.ssref.net/req/202311071/tlogo/fb/12.png',
            'https://cdn.ssref.net/req/202311071/tlogo/fb/20.png', 'https://cdn.ssref.net/req/202311071/tlogo/fb/11.png', 
             'https://cdn.ssref.net/req/202311071/tlogo/fb/13.png')

writeColumns('image', 'https://cdn.ssref.net/req/202311071/tlogo/fb/24.png', 'https://cdn.ssref.net/req/202311071/tlogo/fb/21.png',
            'https://cdn.ssref.net/req/202311071/tlogo/fb/45.png', 'https://cdn.ssref.net/req/202311071/tlogo/fb/31.png',
            'https://cdn.ssref.net/req/202311071/tlogo/fb/22.png')

st.header("Basketball")
st.text("Currently, this dashboard only has information about the NBA. More leagues will be available in the future.")
writeColumns('image', "https://cdn.ssref.net/req/202311071/tlogo/bbr/NBA-2024.png")

st.header("Hockey")
st.text("Currently, this dashboard only has information about the NHL.")
writeColumns('image', "https://cdn.ssref.net/req/202311071/tlogo/hr/NHL-2024.png")

st.text("This dashboard is an open source tool, so check out the code at our repository [here](https://github.com/vnasserb/SportsDashboard)")

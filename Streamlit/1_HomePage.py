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

st.text("**Use this cool dashboard to check information about many sports**")
st.text("**Currently, we support soccer, basketball and Ice Hockey**")

st.header("Soccer")
writeColumns('image', 'https://cdn.ssref.net/req/202311071/tlogo/fb/9.png', 'https://cdn.ssref.net/req/202311071/tlogo/fb/12.png',
            'https://cdn.ssref.net/req/202311071/tlogo/fb/20.png', 'https://cdn.ssref.net/req/202311071/tlogo/fb/24.png')

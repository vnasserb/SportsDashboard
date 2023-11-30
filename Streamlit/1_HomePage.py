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

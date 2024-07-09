# sqlalchemy-challenge

The purpose of this coding challenge is to perform basic climate analysis and data exploration of the provided climate database using SQLAlchemy ORM queries, Pandas, and Matplotlib.  

This analysis is in preparation for a proposed long holiday vacation in Honolulu, Hawaii in order to help with trip planning.

Depending on one's preference for rain, the jupyter notebook analysis provides a means of figuring out which time of year has the highest risk of heavier rainfall as shown in the following visualization:

![Most recent 12 months of precipitation measurements](https://github.com/acdlc4/sqlalchemy-challenge/blob/main/SurfsUp/image_output/Last_12_Mos_Precip_All.png)

Additionally, the jupyter notebook helps us figure out the location that is the most-active reporting location, which is USC00519281 - Waihee, HI.  The following histogram, based on this most-active location, shows us the high temperature measures and how often high temperatures reach the most favored temperatures above 70°F, at least by this coder's personal choice.

![Temperature histogram for USC00519281](https://github.com/acdlc4/sqlalchemy-challenge/blob/main/SurfsUp/image_output/Last_12_Mos_USC00519281.png)

The API provides a user a means of further analysis, with routes that output more explicit data based on:
- Precipitation measures by date
- A list of all stations providing data
- Final year of temperature observations of the most-active station
- Dynamic pages that provide lowest temperature, highest temperature, and average temperature provided with a start date or a start/end date range

Here's to hoping this helps in your (and also my) next trip to Hawaii!!

#### Flask-Python API Script location:
https://github.com/acdlc4/sqlalchemy-challenge/blob/main/SurfsUp/app.py

#### Jupyter Notebook location:
https://github.com/acdlc4/sqlalchemy-challenge/blob/main/SurfsUp/climate_starter.ipynb

Any questions?

Feel free to send a message to acdlc4@gmail.com with any questions / comments / concerns. Inspiration and credit for any code used is from work done during my attendance in the 2024 Northwestern University Data Analysis Bootcamp class sessions.

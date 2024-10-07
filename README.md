# US Presidential Poll Data Analysis: Can Kamala Win?

Link to the presentation: https://docs.google.com/presentation/d/1rA_lkLEZ0dGhIQs0ks-i8Zila951oxDI2tfB1v1qEe8/edit#slide=id.g307776ec05b_0_3

## Introduction

In the 2024 U.S. presidential race between Donald Trump and Kamala Harris, the polls suggest a tight race, similar to Trump's previous campaigns against Hillary Clinton (2016) and Joe Biden (2020). This project aims to compare polling data from these past elections with the current 2024 race, analyzing how well polls predicted the final outcomes. We focus on national versus state-level polling, with particular attention to large states like California and Texas, as well as decisive swing states like Pennsylvania, Michigan, and Georgia.


## Data Sources

We utilized multiple datasets from Kaggle to analyze U.S. poll and election data. These datasets provided comprehensive historical polling data up to mid-September 2024. The final election results for 2016 and 2020 were missing from these datasets, so we obtained them by webscraping Wikipedia’s election results pages. The biggest challenge was handling the sheer volume of data, which required careful selection, cleaning, and focusing on relevant data points.

**Strengths:**
Large and comprehensive datasets covering multiple elections.
Recent polling data up to mid-September 2024.
**Weaknesses:**
Final election results for 2016 and 2020 had to be scraped manually.
Cleaning and narrowing down data to focus on relevant states and candidates was necessary.


## Research Questions and Hypotheses

**Questions:**
What can be learned from past elections?
To what extent can polls predict actual election results?
Can Kamala Harris win the 2024 presidential election?

**Hypotheses:**
H1: The average deviation between September polls and the final election results is no more than 5%, both at the state and national levels.
H2: Poll trends are influenced by major events, potentially impacting election day results.

Presentation: https://docs.google.com/presentation/d/1rA_lkLEZ0dGhIQs0ks-i8Zila951oxDI2tfB1v1qEe8/edit#slide=id.p

## Methodology

**Data Selection:**
We sourced datasets from Kaggle, importing them into Jupyter Notebooks using Python (pandas) for analysis.

**Data Cleaning:**
Removed irrelevant rows/columns (e.g., third-party candidates not relevant to our analysis).
Focused on specific states (California, Texas, Pennsylvania, Michigan, Georgia).
Reformatted the date columns and calculated weekly polling averages for better comparison.
Validated pollsters' quality using ratings from FiveThirtyEight and excluded pollsters with low reliability (rating < 1.5 stars).

**Data Analysis:**
Created line and bar charts to track the polling data over time, comparing mid-September polling with the final election results from 2016, 2020, and projected for 2024.
Analyzed the gap between the candidates in the September polls vs. final vote percentages.

## Conclusions

H1: This hypothesis was falsified in key swing states, where the gap between mid-September polls and the final vote exceeded 5%. However, H1 held true at the national level.
H2: This hypothesis was supported, as polling trends showed correlations with significant events. However, while individual events influence polling data, their ultimate impact on the final election results is less predictable.

**Insights:**
Polls are generally reliable in predicting Democratic support, especially at the national level.
Trump outperformed polling predictions in both the 2016 and 2020 elections, particularly in swing states.
Harris' current lead in national polls suggests she could win in 2024.
Swing state polls remain less predictive, indicating that the 2024 race will likely be decided by these battlegrounds.
Kamala Harris is vulnerable in any state where her lead is less than 5%, making her victory uncertain.


## Further Questions
How might significant events in the coming weeks impact the 2024 election outcome?
What can we learn from comparing polls and election results from before the Trump era (pre-2016)?
Can Kamala Harris secure a decisive win given the unpredictable nature of swing states?


## Data Sources
Kaggle - U.S. Election Poll Data
Wikipedia - 2016 U.S. Presidential Election Results
Wikipedia - 2020 U.S. Presidential Election Results

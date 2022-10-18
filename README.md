# DeepCohort

Data slicing / Cohort creation is an important task in a lot of applications including ML systems, Business metric understanding and RCA operations. 

## Model Analysis
Cohort creation is important in ML systems, in understanding how model performs on different subset of data. With the subset space being exponential, DeepCohort helps in extracting meaningful and most impactful subsets to our target variable. Right now it builds a regression decision tree for this. 

## Root Cause Analysis Business Metric
This tool can also be used to identify most impactful cohorts to your metrics. For instance, it can identify which subgroup of your data is contributing most to the Revenue increase. Again Naive way is to look at all subsets of data, but as discussed, that space is exponential. 

### Note
This package outputs a Tree as an image. 


## Use
#### Installation
```python
pip install deepcohort
```
#### Code
```python
from deepcohort.src import tree_cohort
# df ->  Pandas data,  'Sales' -> target/ Metric column name
cohort = tree_cohort.Getcohort(df, 'Sales')

plot = cohort.plot_cohorts()  #for jupyter notebook
plot.save('plot.svg')
```


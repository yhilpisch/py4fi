# Python for Finance (O'Reilly)

This repository provides all Python codes and Jupyter Notebooks of the book _Python for Finance -- Analyze Big Financial Data_ by Yves Hilpisch.

<img src="http://hilpisch.com/python_for_finance.png" width="500">

Oder the book here http://shop.oreilly.com/product/0636920032441.do or under http://www.amazon.com/Python-Finance-Analyze-Financial-Data/dp/1491945281/.

There are two code versions available: for **Python 3.6** and **Python 2.7** (in the `legacy` folder; not maintained anymore).

## Python Packages

There is now a `yaml` file for the installation of required Python packages in the repository. This is to be used with the `conda` package manager (see https://conda.io/docs/user-guide/tasks/manage-environments.html). If you do not have Miniconda or Anaconda installed, we recommend to install **Miniconda 3.6** first (see https://conda.io/miniconda.html).

After you have cloned the repository, do on the **Linux/Mac** shell:

    cd py4fi
    conda env create -f py4fi_conda.yml
    source activate py4fi
    cd jupyter36
    jupyter notebook

On **Windows**, do:

    cd py4fi
    conda env create -f py4fi_conda.yml
    activate py4fi
    cd jupyter36
    jupyter notebook

Then you can navigate to the Jupyter Notebook files and get started.

## Yahoo! Finance & Google Finance Issues

Recently **Yahoo! Finance stopped their original financial data API service** that is used in the book in many different places (and been so by many others in the field for years) via the `pandas-datareader` package.

One way of fixing it in some places is to simply replace `data_source='yahoo'` by `data_source='google'` (and maybe working with an alternative symbol). However, Google Finance has also changed data availability via the their API such that this does only help partially.

Another way is to use this fix: https://github.com/ranaroussi/fix-yahoo-finance -- this is done for some code in chapter 11.

In the majority of cases where financial data is used, the `pandas-datareader` based code has been replaced by simple `pandas` code that accesses **data files** that are now part of the repository (`CSV` data files provided with data as provided either by the Thomson Reuters Eikon API or by data sources from FXCM Forex Capital Markets Ltd.). This makes sure that the code base is not subject to unforeseen API changes by third parties.

## Quant Platform

You can immediately use all codes and Jupyter Notebooks by registering on the Quant Platform under http://oreilly.quant-platform.com.

## Python for Algorithmic Trading Course & Certificate

<img src="http://hilpisch.com/images/finaince_visual_low.png" width="500">

Check out our **Python for Algorithmic Trading Course** under http://pyalgo.tpq.io.

Check out also our **Python for Algorithmic Trading Certificate Program** under http://certificate.tpq.io.

## Company Information

© Dr. Yves J. Hilpisch \| The Python Quants GmbH

The Quant Platform and all codes/Jupyter notebooks come with no representations or warranties, to the extent permitted by applicable law.

http://tpq.io \| pff@tpq.io \|
http://twitter.com/dyjh

**Quant Platform** \| http://oreilly.quant-platform.com

**Derivatives Analytics with Python (Wiley Finance)** \|
http://derivatives-analytics-with-python.com

**Python for Finance (O'Reilly)** \|
http://python-for-finance.com

**Python for Algorithmic Trading Course** \|
http://pyalgo.tpq.io

**Python for Finance Online Training** \|
http://training.tpq.io

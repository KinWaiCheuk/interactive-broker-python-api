# Setup
1. Clone this repository
1. `pip install -e .`
1. Check `/egg-info/SOURCES.txt` to see if the `ibw` package is installed correctly 
1. Download the [gateway](https://www.interactivebrokers.co.jp/jp/index.php?f=50761#collapseClientPortalAPI), and put it under the repository 
1. Install Java using [OpenJDK 8](https://developers.redhat.com/products/openjdk/download)
1. Go inside `clientportal.gw` and then run `.\bin\run.bat ".\root\conf.yaml"`

# WebAPI
## Manual authentication
1. `conda activate ibkr`
2. Go inside `clientportal.gw` and then run `.\bin\run.bat ".\root\conf.yaml"`
1. Go to https://localhost:5000 and login

## Auto authentication
run the script `web_api.ipynb`.

TODO: how to login to a paper account

# Using Jupyter notebook for data visualization (ib_insync version)
More detail can be found in this [tutorial](https://ibkrcampus.com/ibkr-quant-news/an-introduction-to-tws-api-with-jupyter-notebooks/)/

1. `pip install ib_insync`
1. Log in to TWS paper trading account (somehow this library only works in paper account)
1. Go to TWS and IBGW and check `File -> Global Configuration -> API -> Settings -> Enable ActiveX and Client Socket`
1. In the same meun, uncheck `read-only API`
1. Login using the jupyter notebook
TODO: make a IBGW version 

# Using Jupyter notebook for data visualization (ibapi version)
More detail can be found in this official [tutorial](https://interactivebrokers.github.io/tws-api/connection.html).

A third party [tutorial](https://algotrading101.com/learn/interactive-brokers-python-api-native-guide/) is also available.

1. `pip install ibapi`
1. Log in to TWS paper trading account (somehow this library only works in paper account)
1. Go to TWS and IBGW and check `File -> Global Configuration -> API -> Settings -> Enable ActiveX and Client Socket`
1. In the same meun, uncheck `read-only API`
1. Login using the jupyter notebook
TODO: make a IBGW version 

Tutorial
- https://ibkrcampus.com/trading-course/ibkrs-client-portal-api/
- [Getting Fundamentals](https://youtu.be/YbJYkYFiTII?si=q7zEtzH7O3bojAuv&t=982)

Reference
- https://www.interactivebrokers.com/api/doc.html
- 
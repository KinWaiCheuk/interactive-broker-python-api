from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.common import TickerId

class FundamentalDataApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def fundamentalData(self, reqId, data):
        print("Fundamental Data (ReqId {}): \n{}".format(reqId, data))
        self.disconnect()  # Disconnect after receiving the data

def reqFundamentalData(contract_symbol):
    app = FundamentalDataApp()
    app.connect("127.0.0.1", 7497, clientId=0)  # Change to your TWS or IB Gateway IP and port
    print("Connected to IB API")

    contract = Contract()
    contract.symbol = contract_symbol
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    
    print("Requesting fundamental data for symbol:", contract_symbol)
    app.reqFundamentalData(8001, contract, "ReportsFinSummary", [])
    app.run()

if __name__ == "__main__":
    reqFundamentalData("AAPL")  # Change to the symbol you want to get fundamental data for

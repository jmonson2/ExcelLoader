class Constants:
    INVALID_ARGUMENTS = "Invalid number of arguments. Enter api.py <Refresh Interval in Seconds> <File Path>"
    REQUEST_URI = "https://api.probit.com/api/exchange/v1/ticker"
    REQUEST_PARAMS = {"market_ids":"CNS-USDT"}
    GET = "GET"
    LAST = "last"
    DATA = "data"
    CONFIG_FILE = "config/config.cfg"
    INPUT_INTERVAL = 'Enter the interval in seconds to run the API call (3600/h) (86400/d): '
    INPUT_FILENAME = 'Enter the name of your excel file including file extension. Needs to be in the same folder as the program: '
    GETCONFIG_EXCEPTION = "Exception occured in getConfig: "
    WRITEVAL_EXCEPTION = "Exception occured in writeVal: "
    MAIN_EXCEPTION = "Exception occured in main: "
    CALLAPI_EXCEPTION = "Exception occured in callApi: "

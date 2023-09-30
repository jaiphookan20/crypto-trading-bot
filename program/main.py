from func_connections import connect_dydx
from constants import ABORT_ALL_POSITIONS

if __name__ == "__main__":
    
    # Connect to client
    try:
        print("Connecting to Client...")
        client = connect_dydx()
    except Exception as e:
        print(e)
        print("Error connecting to client: ", e)
        exit(1)


    # Abort all open positions
    if ABORT_ALL_POSITIONS:
        try:
            print("Closing all positions...")
        except Exception as e:

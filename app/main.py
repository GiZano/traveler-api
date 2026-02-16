import info_fetcher as info
import tools.saver as saver


welcome_message = r"""

***************************************************************
* __        __   _                            _               *     
* \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___         *
*  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \        *
*   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |       *
*  __\_/\_/ \___|_|\___\___/|_| |_| |_|\___| _\__\___/ ___ _  *
* |_   _| __ __ ___   _____| | ___ _ __     / \  |  _ \_ _| | *
*   | || '__/ _` \ \ / / _ \ |/ _ \ '__|   / _ \ | |_) | || | *
*   | || | | (_| |\ V /  __/ |  __/ |     / ___ \|  __/| ||_| *
*   |_||_|  \__,_| \_/ \___|_|\___|_|    /_/   \_\_|  |___(_) *
*                                                             * 
***************************************************************

"""

#TODO Save data into /saved/country_name.txt

if __name__ == '__main__':

    print(welcome_message)

    while True:
        # ask the user which country he would like to discover more about
        country = str(input("\nInsert a country name:"))
        try:
            # ask the user's available budget
            budget  = int(input("Insert the available budget (EUR):"))
            # retrieve and print data from info fetcher
            infos = info.fetchInfo(country, budget)
            print(infos[0])
            # ask if the user wants to save the data
            save = str(input("\nWould you like to save the sheet? (Y/N):")).upper()
            if save == 'Y':
                saver.save(infos[0], f'app/data/{infos[1]}.txt')
        except ValueError as ve:
            print(f"\n !Insert a numeric budget! {ve}\n")
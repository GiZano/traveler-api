import info_fetcher as info
import tools.saver as saver
import asyncio, aiohttp

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

async def main():

    print(welcome_message)

    async with aiohttp.ClientSession() as session:
        while True:
            # ask the user which country he would like to discover more about
            country = input("\nInsert a country name:")
            try:
                # ask the user's available budget
                budget  = int(input("Insert the available budget (EUR):"))
                # retrieve and print data from info fetcher
                infos = await info.fetchInfo(country, budget, session)
                print(infos[0])
                # ask if the user wants to save the data, only if data has been correctly retrieved
                if infos[0]:
                    save = str(input("\nWould you like to save the sheet? (Y/N):")).upper()
                    if save == 'Y':
                        # be sure to be in ./app for this saving dir to work
                        saver.save(infos[0], f'data/{infos[1]}.txt')
            except ValueError as ve:
                print(f"\n !Insert a numeric budget! \n")

if __name__ == '__main__':
    asyncio.run(main())
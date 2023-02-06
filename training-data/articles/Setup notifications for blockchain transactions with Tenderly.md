
## Setup notifications for blockchain transactions with Tenderly

In [the article where Yearn announced a partnership with Tenderly](https://medium.com/iearn/yearn-finance-partners-with-tenderly-to-supercharge-development-debugging-incident-analysis-6489260298a5) there was a section where we said:
>  “Tenderly has built-in customizable alerts that allow even novice users to create alerts on virtually any on-chain event.”

A Yearn contributor reached out to learn more about this, and I think it’s a great opportunity to showcase this feature! Let’s start by taking a look at which networks can we use with Tenderly besides Ethereum Mainnet:

![Networks supported by Tenderly](https://cdn-images-1.medium.com/max/NaN/0*Wl1GFyFM0A_rsKjO.png)

I’m gonna explore the **“Monitoring -> Alerting”** service located at [Tenderly’s dashboard](https://dashboard.tenderly.co/) sidebar after logging into any project:

![Sidebar on the left side after logged-in](https://cdn-images-1.medium.com/max/NaN/0*mG1NxKBKDjOy2OJ5.png)

There is a caveat to this service about free usage that will show up when you open the Alerting page:
>  *You’ll receive a batch of alerts that happened over 15 minutes. Upgrade your plan to Tenderly Pro/Dev to receive real-time alerts*

For testing, this isn’t a problem you so can proceed with the free version. For a more robust usage of alerts, you’ll have to upgrade your account.

Let’s start by checking everything can we do when trying to **create a new alert. **The article won’t explore all possibilities so take a look at them to understand the best usage for your needs:

![Create alert](https://cdn-images-1.medium.com/max/NaN/0*ivY6LieHeBRlNGvI.png)

* **Alert Type** will be the conditions we’ll set for a chain event to trigger a notification:

![all Alert Types](https://cdn-images-1.medium.com/max/NaN/0*4o1A4-U8GtdH3AAL.png)

* **Alert Target** will be the contract monitored for the above events and conditions:

![all Alert Targets](https://cdn-images-1.medium.com/max/NaN/0*NwaWo4VDNEmiOBU5.png)

* **Alert Destinations** will be the places that will receive notifications when the above contract meets the conditions for an alert:

![all Alert Destinations](https://cdn-images-1.medium.com/max/NaN/0*lVZTp3HG0637k3H1.png)

Before creating a new alert we must first:

* Decide which events of which contract we want to be notified about

* Add the contract we want to listen to in the “Contracts” tab, so we’ll be able to target it in step 2

* Connect with destinations that will receive the messages (we’ll use telegram in this guide) so we’ll be able to send notifications to it in step 3

Now let’s get started!

## Add Telegram as a destination

In the alerting tab, go to “Destinations” on the top menu and click on “Telegram”:

![Add Telegram as destination](https://cdn-images-1.medium.com/max/NaN/0*zssrqIaeZdmRlLq1.png)

Label it and follow the instructions to allow the bot to send you messages:

![Follow instructions to allow the bot to send messages to you](https://cdn-images-1.medium.com/max/NaN/0*Hc-GKGgdwnQKqsJK.png)

To complete the above process copy the “magic words” from instruction step 3. Paste it in the chat with Tenderly’s telegram bot that opens by clicking [@TenderlyRobot](https://t.me/TenderlyRobot)

![Confirmation message that the bot can now send messages in this chat!](https://cdn-images-1.medium.com/max/NaN/0*RB_mzUO1pFqbBii5.png)

## Monitoring Yearn Vault deposits/withdrawals

Let’s start by monitoring some events made on the SPELL yVault on the Fantom Network. We need to know the SPELL yVault contract address, we can find it by going to the [Yearn Vaults interface](https://yearn.finance/#/vaults) and clicking on the SPELL vault

![Yearn Vaults at Fantom](https://cdn-images-1.medium.com/max/NaN/0*iN0jkDc7V1kzSpDV.png)

After clicking on it we’ll see this page with all the vault details, click the “block explorer” button that will take you to the vault’s contract:

![SPELL yVault details](https://cdn-images-1.medium.com/max/NaN/0*Fcm0MguvUpCtEUTd.png)

This will open up the [SPELL yVault Contract on FTMScan](https://ftmscan.com/address/0xD3c19eB022CAC706c898D60d756bf1535d605e1d) (Fantom fork of [Etherscan](https://etherscan.io/)):

![[SPELL yVault Contract on FTMScan](https://ftmscan.com/address/0xD3c19eB022CAC706c898D60d756bf1535d605e1d)](https://cdn-images-1.medium.com/max/NaN/0*E-dHsAF2OMaWxVyj.png)

I highlighted the important information for our use-case in order:

* First the contract address

* Then the “Token Name” (helps when you have many contract tabs open)

* Lastly the history of methods (functions) that this contract executed

For our example, **we’ll add a notification for when anyone deposits tokens to the vault**. To do this copy the contract page URL:

[https://ftmscan.com/address/0xD3c19eB022CAC706c898D60d756bf1535d605e1d](https://ftmscan.com/address/0xD3c19eB022CAC706c898D60d756bf1535d605e1d)

Then go to Tenderly’s contract tab and click to import this contract in their dashboard, this will enable us to create alerts for it:

![Importing contract in Tenderly](https://cdn-images-1.medium.com/max/NaN/0*mWuwKsrD4vpA8H16.png)

Paste the address, select the “Vyper Contract” (name shows like this because Yearn Vaults use [Vyper programming language](https://vyper.readthedocs.io/en/stable/index.html)). When it shows up, click “Import”:

![Importing contract in Tenderly](https://cdn-images-1.medium.com/max/NaN/0*5rsE4SW66rahd21Q.png)

After importing the contract is ready for us to create an alert for it!

![Importing contract in Tenderly](https://cdn-images-1.medium.com/max/NaN/0*UbN5qpp-LIzwib_X.png)

Let’s go and create an alert then:

![Creating a new alert](https://cdn-images-1.medium.com/max/NaN/0*NxXHSz8Zvu-X4QVG.png)

We want to receive a notification every time someone deposits into the SPELL yVault. To do this we’ll check the “Deposit” method that exists in the yVault contract. “method” is an analogous name to “function call” so that’s the type of alert we’ll use in this case

![Select alert type](https://cdn-images-1.medium.com/max/NaN/0*9pHnL-7ky-zagKYn.png)

Target will be an address:

![Select alert target](https://cdn-images-1.medium.com/max/NaN/0*D_9J0c78CVK5v8co.png)

You’ll be able to select the contract we added previously and then pick any function that exists inside it. Note that many functions might have similar names, functions that start with “_” are often private internal functions and won’t be the ones we are looking for

In this case, we have **_deposit** (private: for internal usage) and **deposit** (public: for external users). We’ll pick the one that is public:

![Select alert target](https://cdn-images-1.medium.com/max/NaN/0*WkPeKfVy5gTagTDI.png)

Lastly, choose the telegram destination that was set up previously and save the alert:

![Select alert destination](https://cdn-images-1.medium.com/max/NaN/0*WYnR3XyDh7BNXJPM.png)

We are done! The alert is created and I’ll receive a message every time someone deposits SPELL in that yVault!

![Alert created successfully!](https://cdn-images-1.medium.com/max/NaN/0*ckXpYmgDqBsMqzCH.png)

Here is an example notification I got after setting up this example and depositing a bit of spell in the vault to trigger it, I got the notification instantly after transaction confirmation!

![Notification of new SPELL deposit at Fantom yVault sent to my Telegram!](https://cdn-images-1.medium.com/max/NaN/0*tjDWxmYEfHMAZKpn.png)

## Final Thoughts

This Yearn example showcases a simple way to monitor for a contract’s function call. If you explore all the options from the alerting system you’ll see this can be easily tweaked to many different usages, for example:

* NFT collections devs can monitor whenever their contract called the minting of a new token and announce it automatically on Discord

* People monitoring Tokenomics flows can use notifications to keep an eye on wallet balances and actions from contracts to see if devs are doing what is expected to be done

You can monitor any kind of on-chain activity and be notified by it, so experiment with all the different options!

Producers: [Worms](https://twitter.com/MarcoWorms), Reviewers: [Cryptouf](https://twitter.com/cryptouf), [Dark Ghosty](https://github.com/DarkGhost7)

## Made in [yearn.finance](https://yearn.finance/)

# Yearn Vault version release notes

## yVault v.0.1.0 - Goddard - Pre-release
- Oct 16,2020

## yVault v.0.1.1 - Tsiolkovsky - Pre-release
- Oct 20, 2022
- add ability to disable rate limiter
- fix withdraw queue failures
- add `addStrategyToQueue`
- add Harvested event to `BaseStrategy`
- remove withdrawal fee, add inflationary management fee

## yVault v.0.1.2 - Oberth - Pre-release
- Oct 27, 2020
- add recipient support to `deposit` and `withdraw` functions
- add "all assets" shortcut to `deposit` and `withdraw` functions
- remove `allowance == 0` check on approvals
- add `setName` and `setSymbol` governance methods

## yVault v.0.1.3 - von Braun - Pre-release
- Nov 3, 2020
- addvault natspec
- apply suggestions from code review

## yVault v.0.2.0 - Khomyakov - Pre-release
- Nov 19, 2020
- add sweep amount/ERC721 support
- use deposit limit remaining when depositing all
- separate strategist and reward roles in BaseStrategy
- update performance and management fee defaults
- add ability to report losses
- add available deposit limit as view-only function
- add guest list
- move from block-based calculations to time-based
- add Debt Payments to Vault.report()
- add Rate Limit Disable

## yVault v.0.2.1 - Laika - Pre-release
- Nov 28, 2020
- audit findings for Vault
- store vault activation timestamp
- audit findings for BaseStrategy
- improve exitPosition logic
- div by zero fix
  
## yVault v.0.2.2 - Belka - Pre-release
- Dec 3, 2020
- Upgrade Keeper Script
- Natspec upgrades for `BaseStrategy`
- Avoid transfer with `distributeRewards` if balance is 0
- Add Permit
  
## yVault v.0.3.0 - Strelka - Pre-release
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
  
## yVault v.0.3.0 - Strelka - release
- Jan 8, 2021
- add TVL calculation api
- standardize `permit`
- check for strategy vault and want address matches on add
- upgrade to Vyper 0.2.8
- add event logs for vault config updates
- set correct access control for `Vault.setEmergencyShutdown`
- incorporate `manager` entity in vault
- `migrateStrategy` shouldn't reset activation time
- consolidate `BaseStrategy.exitPosition` into `BaseStrategy.liquidatePosition`
- set vault deposit limit to zero on initialization
- use debt ratio vs. absolute debt limit
- remove `Vault.balanceSheetOfStrategy` and `Vault.totalBalanceSheet`
- protect against excessive losses on withdraw
- audit fixes

## yVault v.0.3.1 - Ham - release
- Jan 30, 2021
- Updates for Audit
- Only charge mgmt fee on invested funds
- Deploy script improvements
- Add Metadata URI to BaseStrategy
- Pull strategist rewards rather than push

## yVault v.0.3.2 - Bonny - release
- Feb 15, 2021
- Proxy Mode to BaseStrategy
- Support for non-compliant ERC20s (USDT)
- fix vault debtRatio update on _reportLoss
- management and Guardian should be able to harvest() a Strategy
- Profit lock up that increases share price steadily over time
- change "rate limit" feature to min/max harvest debt size params

## yVault v.0.3.3 - Malyshka - release
- Mar 15, 2021
- SECS_PER_YEAR to use Gregorian constant
- add `.clone(vault)` method to proxy-able BaseStrategy
- clone bug
- increase test suite coverage to 100%
- add deposit wrapper
- make pendingGovernance public
- don't endorse first release
- upgrade to vyper v0.2.11
- deploy proxy with prev release
- added state var default init to _initialize method
- cheapen wrapper withdrawals
- add ability to track endorsed vault tokens
- standardize terminology for vaults in registry

## yVault v.0.3.4 - Enos - release
- Mar 25, 2021
- delegated fees

## yVault v.0.3.5 - Sam - release
- Apr 5, 2021
- delegated assets bug
- deposit everything to AffiliateToken
- locked profit ratio
- mixbytes wrapper audit fixes
- increase precision for important calculations
- use `_reportLoss` function on losses to reduce impact

## yVault v.0.4.0 - Kusachka - release
- May 24, 2021
- style: update code style @zgfzgf
- perf: assessFees when gain==0 @zgfzgf
- fix: do not redeposit dust @steffenix
- fix: ytoken get name decimals from token @steffenix
- feat: add web UI and depositLimit mitigation steps @dudesahn
- chore: bump vyper version @steffenix
- perf: delete useless management_fee @zgfzgf
- feat: locked profit on deposit @Grandthrax
- fix: strategy performance fee @zgfzgf
- refactor: move condition shares calculation and save gas @t4sk
- chore: delete changelog @steffenix
- fix: performanceFee error @zgfzgf
- chore: bump API_VERSION @steffenix
- fix: job @steffenix
- feat: add release drafter @steffenix
- fix: inconsistent Liquidations in BaseStrategy Emergency Exit Mode @steffenix
- feat: develop without solidity 0.8 @steffenix
- docs: update github.com/iearn-finance to github.com/yearn @zgfzgf
- fix: correct spelling and usage of degradation @dudesahn
- fix: baseWrapper do not deposit dust @steffenix
- fix: comments in Vault.vy @antoncoding
- fix: compute credit error in report @zgfzgf
- docs: fixs prepareReturn want.balanceOf @zgfzgf
- feat: setEmergencyExit should allow to be called by vault guardian and vault management @steffenix
- fix: prevent clone of clone @steffenix
- chore: bump black version @steffenix
- feat: add emergency procedures @dougstorm
- fix: audit updates @steffenix
- chore: bump brownie version @steffenix
- fix: update code snippet @orbxball
- docs: update docs to match current procedure @fameal
- fix: missing param @steffenix
- feat: base wrapper add doc to public facing function @steffenix
- fix: baseStrategy doc @steffenix
- chore: check PR titles for conventional commits @fubuloubu
- test: hardhat compatibility @banteg
- feat: add management to initialize @steffenix
- fix: affiliate token withdraw calculation @dapp-whisperer
- feat: test for double accounting on withdrawal loss @Grandthrax
  
## yVault v.0.4.1 - Gordo - release
- May 27, 2021
- fix: revert changes on debt outstanding @steffenix
- perf: optimize code @zgfzgf
- feat: update release script for new vault versions @steffenix

## yVault v.0.4.2 - Tsygan - release
- May 28, 2021
- fix: example breaking doc generation @steffenix
- chore: update recommended releases @steffenix
- fix: keep initialize compatible with registry @steffenix
  
## yVault v.0.4.3 - Damka - release
- Jul 9, 2021
- fix: shares for amount calculation should use freeFunds @Stcrab

## yVault v.0.4.4 - release
- Oct 25, 2022
- docs: Add GitPOAP Badge to Display Number of Minted GitPOAPs for Contributors @burz
- chore: .gitattributes file no longer needed @fubuloubu
- fix: two imports @poolpitako
- fix: gov event @pandadefi
- fix: test CI typo @dudesahn
- fix: update token balance to share calculation @0xbok
- fix: assert shares amount before withdrawing @rareweasel
- chore: add Slither analyzer @fubuloubu)
- chore: bump ganache version @pandadefi
- docs: changes letter v in revent to c @parseb
- fix: implement modifiers @jmonteer
- docs: added import remapping instructions @mason
- feat: add event to sweep @pandadefi
- feat: add event to disable health check @pandadefi
- chore: doc moved @pandadefi
- feat: add event to setLockedProfitDegradation @pandadefi
- fix: move require isOriginal to main clone function @rareweasel
- feat: test small losses @poolpitako
- feat: add deposit and withdraw events @pandadefi
- chore: bump vyper version @pandadefi
- test: add function to increase pps with a strategy @pandadefi
- fix: add missing pr template @pandadefi
- chore: add pull request template @pandadefi
- feat: allow revoke permission from vault manager @0xparashar
- fix: base router transfering too many shares @pandadefi
- chore: refactor base strategy to reduce bytecode size @rareweasel
- fix: NatSpec typo in BaseWrapper.sol @Pet3ris
- chore: remove already imported interface @pandadefi
- fix: updated setRewards @jhb10c
- chore: bump brownie version @pandadefi
- fix: typo in SPECIFICATION.md @saguywalker
- chore: bump vault vyper version @pandadefi
- fix: comment typo @gzliudan
- feat: base router @pandadefi
- feat: add version to package.json @lbertenasco 
- chore: bump brownie version @pandadefi
- fix: update readme link @saltyfacu
- feat: call health check contract from vault @pandadefi

## yVault v.0.4.5 - release
- Nov 1, 2022
- fix: revert abi changes
- feat: update harvestTrigger
  
## yVault v.0.4.6 - release
- Feb 2, 2023
- fix: Increase characters allowed for `setSymbol()` and `setName()` @dudeshan
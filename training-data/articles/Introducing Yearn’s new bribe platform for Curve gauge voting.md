
## **Introducing Yearn’s new bribe platform for Curve gauge voting**

![](https://cdn-images-1.medium.com/max/3000/1*oI-zdUrG7g-2hxSw2lqvKQ.jpeg)

### [yBribe](https://ybribe.yearn.farm) is a platform where vote-escrowed Curve (veCRV) holders can receive compensation from buyers interested in increasing CRV emissions to their Curve pool’s gauge.

In DeFi, incentives for voting are commonly referred to as ‘bribes’. [yBribe](https://ybribe.yearn.farm) enables veCRV holders — be they protocols, DAOs, or individual users, to extract the value of their voting power. yBribe was launched in November of this year and we have observed early solid adoption with over $500k of bribes in the first round.

As a voter, there is no cost to use yBribe. Bribers pay a 1% maintenance fee — **the lowest of all platforms in the ecosystem** — which is applied when posting the bribe.

**This article details:
*** key functionalities 
* benefits of yBribe
* how to get started
* brief history 
* faq

## Overview

![](https://cdn-images-1.medium.com/max/2952/1*00CGDw5OiCJ3_kg_FQroJA.png)

### yBribe pairs users looking to buy votes, with those looking to sell them.

Curve conducts weekly gauge votes that determine the allocation of CRV rewards to various pools. By buying votes, DAOs, protocols, and users can influence the direction of these rewards and boost yields in pools beneficial to them. To do this, use the ‘Bribe a Gauge’ function on yBribe. Once the bribe is posted, voters will see the pending APR for the gauge increase.

![APRs are listed for the current and upcoming period](https://cdn-images-1.medium.com/max/4736/1*vJQwLb8RjIc0DQCj9OHNDA.png)

veCRV holders can sell their gauge votes to the highest bidder each week by voting on the bribed gauge with the highest APR. All the information users need to make profit-maximizing votes can be found on [yBribe](https://ybribe.yearn.farm).

### Bribers can more efficiently target the entire veCRV market

![Bribers can address larger segments of the market](https://cdn-images-1.medium.com/max/3200/1*nc8BnwpjUtZz60SfS-lkIQ.png)

veCRV ****holders can vote for their preferred incentivized pool through Curve’s gauge weight vote and receive rewards. There is a 10-day cooldown period for adjusting gauge weight on Curve. Your previous vote will remain valid until changed but will incur balance decay.

The new blacklist function partitions yBribe from gauge voters who already have dedicated bribe markets (e.g Convex/Votium). Now bribers can address the entire veCRV market by splitting bribes between platforms, and users earn more as double-dipping is blocked.

Unlike other platforms, there are no whitelists and you do not have to ask permission to add your token as a bribe. yBribe only charges a 1% fee in comparison to the 4% charged by others.

### Key benefits
> # yBribe is fully trustless, permissionless and non-custodial

* A new UI makes it clear for veCRV holders to identify the best opportunities.

* Convex votes are excluded from the system to make bribes more efficient.

* Fully trustless design and 100% on-chain design.

* Codebase is fully audited.

## How to get started

### Claiming a Bribe

Voters can sell their vote to the highest bidder by voting on the briber’s gauge. yBribe lists the gauge for the current and upcoming period.

![](https://cdn-images-1.medium.com/max/2890/1*4OznstN-KLCxWtsfiys3wg.png)

To pick the gauge to vote for you can review the APRs listed. The **current** **period** refers to the current period in which rewards are aggregated (i.e. this week). Pending period refer to the next week.

![](https://cdn-images-1.medium.com/max/2000/1*EuNYmuoHOAp6X-vn_dY96A.png)

Each gauge has an APR listed —

* **Current APR:** APR users can claim this week (if they haven’t already claimed)

* **Pending APR**: The APR they will be able to claim next week (week in this case starts on Thursday)

Once you identify the gauge you want to vote for, head over to Curve to vote by clicking “**Vote for Gauge**”.

![](https://cdn-images-1.medium.com/max/2890/1*UUrC-WjD_dO-5foExB3PyA.png)

After you vote, you’ll be able to claim any applicable rewards at the start of the next period.

**Example: **Bunny is a veCRV holder. Bunny goes to yBribe (which gets all data directly on-chain) to figure out which gauge is the best one to vote for.

![](https://cdn-images-1.medium.com/max/4028/1*FozaswfEe9orFyAB9AF84g.png)

As seen above, we can see MIM gauge is the best for the upcoming period. Bunny goes to vote for the MIM gauge on Curve and then at the start of the next period, they can claim their bribe.

The amount of the overall bribe they will collect is dynamically calculated based on how much vote weight Bunny provided relative to global vote weight on MIM gauge.

### Claim Period

Claim periods run from Thursday to Thursday, and the scrolling clock on the main page displays the time remaining in the current period.

Make sure you claim any claimable rewards before the current period ends, and/ or submit your votes for the next period. Be sure to claim any rewards before voting again on the same gauge or you’ll be locked out of rewards until the following week.

### Offering a Bribe

Bribers can offer a bribe to increase CRV emissions to your favorite Curve pool. Bribers can deposit any token as their bribe.

![](https://cdn-images-1.medium.com/max/3252/1*vAk5PISW_x9lM0xlZ6BDrA.png)
>  yBribe now lets users assign rewards to a different claiming address than the one used to vote. It also fixes a bug which under certain circumstances, allowed an initial bribe allocation to be drained before the start of a voting period.

## History and origins

### yBribe is an evolution of the BribeV2 contract

The original Curve gauge vote bribe contract, BribeV2, was released as a trustless mechanism for entities (usually protocols) to incentivize veCRV voters to cast votes for their desired gauge with the intent of increasing emissions to it. A briber would simply deposit tokens into BribeV2, and the contract reads from Curve’s Gauge Controller to calculate token allocations for each voter according to their global influence on the gauge weights.

After over a year of use, the Yearn team discovered an exploit in BribeV2. While Yearn did not write or deploy the original BribeV2 contract, we were heavy users of it, and therefore decided to act quickly to deploy a patched contract so that operations could resume.

Yearn’s yBribe retains all the best features of BribeV2 — including its fully permissionless and on-chain design. yBribe also fixes several bugs and has added several new features that make it more efficient and improve the UX.

## FAQs

* **What’s a bribe? **In DeFi, incentives for voting are commonly referred to as ‘bribes’.

* **How does yBribe work under the hood? **yBribe ‘holds’ bribe rewards and performs the calculations and distributions of those rewards. A user interacts with yBribe by claiming or offering a bribe. Voting occurs directly on Curve’s contracts.

* **Will I be able to convert my bribes into another token?** No

* **What is the countdown timer on the main page? **It is how long users have left to claim their rewards/bribes from the current period and get their vote in for the next period. It’s midnight Wednesday to Thursday (00:00 thursday) every week that the new round starts.

* **Can we claim on L2?** No

* **Wen vICVX?** Coming soon ;)

* **Will there be a bribe system for yCRV or veYFI?** yBribe is a generic system that anyone can use. We are not planning on making a bribe system just for yCRV or veYFI at this time.

* **What is the 1% fee used for?** To support continued development and new features.

* **What happens to the rewards I had in the old contract?** Users with bribes still claimable in the legacy contract can still claim them.

* **What is veCRV anyways?** Participating in Curve DAO governance requires that an account have a balance of vote-escrowed CRV (veCRV). veCRV is a non-standard ERC20 implementation and cannot be transferred. The only way to obtain veCRV is by locking CRV. The maximum lock time is four years. One CRV locked for four years provides an initial balance of one veCRV. These rewards are generated by the 0.04% swap fee that Curve charges on each trade. 50% of these fees go to users who add to the liquidity pools and 50% goes to users who hold veCRV.

## Learn More
[**yBribe**
*Sell your vote to the highest bidder, or offer a bribe to increase CRV emissions to your favorite Curve pool. Just like…*ybribe.yearn.farm](https://ybribe.yearn.farm/offer-bribe)

* [Gauge Weights](https://dao.curve.fi/gaugeweight)

* [Liquidity Gauges and Minting CRV](https://curve.readthedocs.io/dao-gauges.html)

* [Curve Governance](https://curve.readthedocs.io/dao-voting.html)

## *Editors*

*wavey, garywackett, draper*

from constants.aesthetic import Emojis


class PS_EMOJIS:
    i = Emojis.info
    rewards = Emojis.rewards


class PS_DESC:
    i = f"""# POWER STATION INFO

- **What is the Power Station?**
> - *A weekly event where teams battle NPC trainers to generate <:power:1478570462928699633> Power.*
> - *The team with the highest total power by Sunday 12am EST controls the station for the following week.*

- **How to Generate Power**
> - *Battle Power Station NPCs (300 - 306) using `;battle npc <name or id>`.*
> - *NPCs grow stronger with each defeat and refresh daily.*
> - *Station NPC scaling resets daily (excluding upgrades).*

- **Boosted Events**
> - *<:power_day:1478573219022770287> Power Day → Power gains doubled, see `;ps`.*
> - *<:power_hour:1478573201561878639> Power Hour → Power gains doubled, enemy levels locked at +200, see `;ps`.*

- **Upgrades (Reset Weekly)**
> - *<:fusion_core:1478584659591037117> Fusion Core → +1 Power per battle (max 10).*
> - *<:turbines:1478584657565061170> Turbines → Reduce NPC scaling by 1 level each (max 50).*
> - *<:smart_grid:1478584655807512676> Smart Grid → +1% chance to double Power per battle (max 50, stacks with Power Day/Hour).*
> - *Buy upgrades with `;ps upgrade <fusion_core/turbines/smart_grid>`.*"""

    rewards = f"""# POWER STATION REWARDS

- **Control Benefits**
> - *The team that controls the Power Station gains:*
>   - *30% boosted Faction points from all activities.*
>   - *25% cheaper prices in the `;faction shop`.*
>   - *25% increased <:pokecoin:1477168709305892874> coin earnings from battling.*

- **Contribution Requirement**
> - *You must contribute either <:power:1478570462928699633> 1,000 Power or at least 5 upgrades in the current week to access these perks.*

- **Consecutive Control Bonus**
> - *If any team controls the station for 2 weeks in a row:*
>   - *Top 5 contributors unlock a battle against the <:masterelectrician:1476569301170524283> Master Electrician.*
>   - *Defeat him for a chance at a unique <:Golden11:1147776276510281818> Pokémon (drop rate boosted by higher team ranking).*
>   - *Earn the <:power:1478570462928699633> Power profile badge and role (`;claim ps`) by defeating him on Scale 100+.*

- **Item Drops**
> - *Station NPCs (300 - 306): 1/50 chance to drop <:rocky_helmet:1478585825674531039> Rocky Helmet or <:safety_goggles:1478585823808065778> Safety Goggles.*
> - *Master Electrician: 1/50 chance to drop <:light_ball:1478585821601988729> Light Ball or <:heavy_duty_boots:1478585819244662813> Heavy-Duty Boots.*"""

    s = f"""**TEAM:**
- **Mimikyu #778**
> Ability: `Disguise`
> Equip: `Ability_Shield`
> Moves: `Trick-Room` `Destiny-Bond` `Magic-Room`
> EVs: `N/A`
- **Shiny Mimikyu #1778**
> Ability: `Disguise`
> Equip: `Ability_Shield`
> Moves: `Trick-Room` `Destiny-Bond` `Magic-Room`
> EVs: `N/A`
- **Donphan #1232**
> Ability: `Sturdy`
> Equip: `Ability_Shield`
> Moves: `Protect` `Endeavor` `Ice-Shard`
> EVs: `N/A`

**STRATEGY:**
- [Mimikyu] Trick-Room
- [Mimikyu] Destiny-Bond
- [Shiny Mimikyu] Magic-Room
- [Shiny Mimikyu] Destiny-Bond
- [Donphan] Protect
- [Donphan] Endeavor
- [Donphan] Ice-Shard

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- For NPC IDS: 300 - 306
- This strat is for enemy teams with Leftovers/Sitrus Berries.
- If Donphan can't learn Ice-Shard, just evolve a Phanphy with Ice-Shard as its 3rd move.
- Ability Shield is only a necessity for when you are up against Zekrom, Reshiram or Pokemons with Mold Breaker Ability.
- If the enemy spam switches just keep on using Destiny-Bond until trick room fades. Use Trick-Room again and just do the strat above."""

    strat_two = f"""**TEAM:**
- **Mega Banette #7124**
> Ability: `Prankster`
> Equip: `Ability_Shield`
> Moves: `Destiny-Bond`
> EVs: `N/A`
- **Sableye #302**
> Ability: `Prankster`
> Equip: `Ability_Shield`
> Moves: `Destiny-Bond`
> EVs: `N/A`
- **Donphan #1232**
> Ability: `Sturdy`
> Equip: `Ability_Shield`
> Moves: `Protect` `Endeavor` `Ice-Shard`
> EVs: `N/A`

**STRATEGY:**
- [Mega Banette] Destiny-Bond
- [Sableye] Destiny-Bond
- [Donphan] Protect
- [Donphan] Endeavor
- [Donphan] Ice-Shard

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- For NPC IDS: 300 - 306
- This strat is for enemy teams without Leftovers/Sitrus Berries.
- You need to set Sableye's ability to Prankster
- If Donphan can't learn Ice-Shard, just evolve a Phanphy with Ice-Shard as its 3rd move.
- Ability Shield is only a necessity for when you are up against Zekrom, Reshiram or Pokemons with Mold Breaker Ability."""

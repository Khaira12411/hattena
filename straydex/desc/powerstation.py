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
- **Donphan #232**
> Ability: `Sturdy`
> Equip: `Ability_Shield`
> Moves: `Protect` `Endeavor` `Ice-Shard (Teach Phanphy then evolve)`
> EVs: `N/A`
OR
- **Sudowoodo #185**
> Ability: `Sturdy`
> Equip: `Ability_Shield`
> Moves: `Protect` `Endeavor` `Sucker-Punch (Teach Bonsly then evolve)`
> EVs: `N/A`

**STRATEGY:**
- [Mimikyu] Trick-Room
- [Mimikyu] Destiny-Bond
- [Shiny Mimikyu] Magic-Room
- [Shiny Mimikyu] Destiny-Bond
- [Donphan | Sudowoodo] Protect
- [Donphan | Sudowoodo] Endeavor
- [Donphan | Sudowoodo] Ice-Shard | Sucker-Punch

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- For NPC IDS: 300 - 306
- This strat is for enemy teams with Leftovers/Sitrus Berries.
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
- **Donphan #232**
> Ability: `Sturdy`
> Equip: `Ability_Shield`
> Moves: `Protect` `Endeavor` `Ice-Shard (Teach Phanphy then evolve)`
> EVs: `N/A`
OR
- **Sudowoodo #185**
> Ability: `Sturdy`
> Equip: `Ability_Shield`
> Moves: `Protect` `Endeavor` `Sucker-Punch (Teach Bonsly then evolve)`
> EVs: `N/A`

**STRATEGY:**
- [Mega Banette] Destiny-Bond
- [Sableye] Destiny-Bond
- [Donphan | Sudowoodo] Endeavor
- [Donphan | Sudowoodo] Ice-Shard | Sucker-Punch

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- For NPC IDS: 300 - 306
- This strat is for enemy teams without Leftovers/Sitrus Berries.
- You need to set Sableye's ability to Prankster
- Ability Shield is only a necessity for when you are up against Zekrom, Reshiram or Pokemons with Mold Breaker Ability."""

    # B1 Team descs for npcs 303 | 304 |305
    B1_Strat = f"""**NPC IDs:** 303 / 304 / 305
**Enemy Team:** Bisharp + Mega Manectric + Magnezone

**TEAM:**
- **Sableye #302**
> Ability: `Prankster`
> Moves: `Destiny-Bond` `Taunt` `Protect` `Fake-Out`
OR
- **Mimikyu #778**
> Moves: `Trick-Room` `Destiny-Bond` `Taunt`

- **Mega Banette #7124**
> Equip: `Cheri_Berry | Lum_Berry`
> Moves: `Destiny-Bond` `Protect` `Taunt` `Shadow-Sneak`
OR
- **Shiny Mimikyu #1778**
> Moves: `Trick-Room` `Destiny-Bond` `Taunt`

- **Sudowoodo #185**
> Equip: `Covert_Cloak | Cheri_Berry | Lum_Berry`
> Moves: `Protect` `Endeavor` `Sucker-Punch (teach Bonsly, then evolve)`

**PROCEDURE:**
- Spam Destiny-Bond, then finish with Sudowoodo’s Endeavor + Sucker-Punch.

**SABLEYE TEAM STRATEGY:**
- Vs Bisharp: Protect/Fake-Out first, then Destiny-Bond → Endeavor + Sucker-Punch.
- If Bisharp Sucker-Punches into Destiny-Bond, repeat Protect + Destiny-Bond.
- If Mega Manectric’s Overheat misses, use Taunt + Destiny-Bond, or keep Endeavor until Sturdy triggers, then Sucker-Punch.

**MIMIKYU TEAM STRATEGY:**
- Vs Bisharp lead: Trick-Room → Taunt → Destiny-Bond spam.
- Vs Magnezone lead: Destiny-Bond → Trick-Room → Destiny-Bond. If Overheat misses, keep spamming Destiny-Bond.
- Vs Mega Manectric lead: Trick-Room (Taunt if Overheat misses) → Destiny-Bond. Follow with Destiny-Bond + Taunt on Magnezone, or Destiny-Bond spam if turns are tight.

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- This strategy is only viable on high enemy level scales.
- With Mimikyu, always spam Destiny-Bond when Bisharp or Manectric switch out.
- Mimikyu only risks losing to double Overheat misses or a miss on turn 2 if Manectric stalls. To reduce this, force Magnezone out.
- Double Destiny-Bond core (Sableye + Mega Banette) is more reliable."""

    B2_Strat = f"""**NPC IDs:** 303 / 304 / 305
**Enemy Team:** Empoleon + Mega Mawile + Mega Metagross

**TEAM:**
- **Mimikyu #778**
> Moves: `Trick-Room` `Destiny-Bond` `Taunt`
- **Shiny Mimikyu #1778**
> Moves: `Trick-Room` `Destiny-Bond` `Taunt`
- **Sudowoodo #185**
> Moves: `Protect` `Endeavor` `Sucker-Punch (teach Bonsly, then evolve)`

**PROCEDURE:**
- Empoleon → Metagross → Mawile: Trick-Room + Destiny-Bond, then Destiny-Bond + Taunt + Destiny-Bond.
- Empoleon → Mawile → Metagross: Trick-Room + Destiny-Bond, then Taunt + Destiny-Bond.
- Metagross lead: Destiny-Bond + Trick-Room + Destiny-Bond, then Destiny-Bond + Taunt + Destiny-Bond.
- Mawile → Metagross → Empoleon: Trick-Room + Taunt + Destiny-Bond, then Destiny-Bond + Taunt + Destiny-Bond.
- Mawile → Empoleon → Metagross: Trick-Room + Taunt + Destiny-Bond, then Taunt + Destiny-Bond.

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- This strategy is only viable on high enemy level scales.
- If Mega Metagross misses Meteor-Mash on Mimikyu, add another Taunt after the first.
- If Mega Metagross misses Meteor-Mash on Sudowoodo, keep using Endeavor until it hits. Then Protect after Endeavor connects, followed by Sucker-Punch to reduce Bullet-Punch chances.
- The procedure forces Mega Metagross to be the last Pokémon. Mega Mawile runs Iron-Head, Sucker-Punch, and often Swords-Dance; Empoleon carries Leftovers and Scald. Metagross is the best matchup for Sudowoodo.
- No Magic-Room is used even if Empoleon has Leftovers, since the plan ensures Metagross is the final opponent.
"""
    B3_Strat = f"""**NPC IDs:** 303 / 304 / 305
**Enemy Team:** Leftovers Mega Steelix + Leftovers Empoleon + Orb Mega Gengar

**TEAM:**
- **Mimikyu #778**
> Equip: `Choice_Band | Choice_Specs`
> Moves: `Trick-Room` `Destiny-Bond` `Protect` `Trick`
- **Shiny Mimikyu #1778**
> Moves: `Trick-Room` `Destiny-Bond` `Magic-Room` `Substitute`
- **Sudowoodo #185**
> Equip: `Rawst_Berry | Lum_Berry`
> Moves: `Protect` `Endeavor` `Sucker-Punch (teach Bonsly, then evolve)`

**PROCEDURE:**
- Steelix lead: Trick → Sudowoodo → Trick-Room → Destiny-Bond, then Protect → Trick → Destiny-Bond.
- Empoleon lead: Trick → Protect → Trick → Destiny-Bond, then Trick-Room → Substitute → Substitute → Destiny-Bond.
- Gengar lead / outspeed: Trick → Protect → Trick-Room → Destiny-Bond, then Magic-Room → Substitute → Destiny-Bond.
- Steelix outspeed lead: Trick → Protect → Sudowoodo → Trick-Room → Destiny-Bond, then Protect → Trick → Destiny-Bond.
- Empoleon outspeed lead: Trick → Protect → Trick-Room → Destiny-Bond, then Trick-Room → Trick-Room → Substitute → Substitute → Destiny-Bond.

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- This strategy is only viable on high enemy level scales.
- Procedure shifts above 200+ scale (marked “outspeed lead”); normal procedure applies for ~100–200 scale or Power Hour strat. Once Mega Steelix outspeeds Mimikyu, switch to outspeed procedure.
- Keep both Mimikyus at identical speed for clean transitions; only risk is rare Steelix and Mimikyu speed ties.
- Trick set is required to prevent Mega Gengar from being the last opponent, since Sudowoodo cannot Endeavor it.
- Main risk: Mega Steelix using Stealth-Rock on turn 1 (Steelix lead) or turn 4 (Empoleon lead). Taunt can prevent this, but Trick-Room on Mimikyu #1 is required for Gengar leads."""

    B4_Strat = f"""**NPC IDs:** 303 / 304 / 305
**Enemy Team:** Leftovers Mega Aggron + Specs Toxtricity-LowKey + Mega Lucario

**TEAM:**
- **Mimikyu #778**
> Moves: `Trick-Room` `Destiny-Bond` `Protect` `Taunt`
- **Shiny Mimikyu #1778**
> Equip: `Cherri_Berry | Lum_Berry`
> Moves: `Trick-Room` `Destiny-Bond` `Taunt` `Substitute`
- **Sudowoodo #185**
> Equip: `Heavy_Duty_Boots`
> Moves: `Protect` `Endeavor` `Sucker-Punch (teach Bonsly, then evolve)`

**PROCEDURE:**
- Aggron → Toxtricity → Lucario: Trick-Room + Destiny-Bond, then Destiny-Bond + Taunt + Destiny-Bond spam (even if Meteor-Mash misses).
- Aggron → Lucario → Toxtricity: Trick-Room + Destiny-Bond, then Taunt + Destiny-Bond spam.
- Toxtricity lead: Trick-Room + Taunt + Destiny-Bond, then Substitute → Substitute → Trick-Room → Taunt → Substitute → Destiny-Bond. If Mega Lucario misses, spam Destiny-Bond on Lucario. After Mimikyu faints, restart with Trick-Room → Taunt → Substitute → Destiny-Bond.
- Lucario → Toxtricity → Aggron: Trick-Room + Taunt + Destiny-Bond, then Substitute → Substitute → Trick-Room → Taunt → Substitute → Destiny-Bond. If Mega Lucario misses and Trick-Room is down, skip the first two Substitutes on Mimikyu #2 and instantly Trick-Room.
- Lucario → Aggron → Toxtricity: Trick-Room + Taunt + Destiny-Bond, then Taunt + Destiny-Bond. If Mega Lucario misses and Trick-Room is down, Trick-Room → Substitute → Substitute → Destiny-Bond.

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- This strategy is only viable on high enemy level scales.
- If Trick-Room isn’t down yet during Substitute setups with Mimikyu #2, use one Substitute before Trick-Room expires, then restart with Trick-Room.
- Always spam Destiny-Bond on Mega Lucario if Meteor-Mash misses.
- Replace the last Substitute with Taunt if Mega Aggron wastes a turn and your Substitute is still active.
- Protect with the last Pokémon if it’s still turn 4 to drain Trick-Room.
- On Lucario → Aggron → Toxtricity, if Meteor-Mash misses, Mega Aggron may use Thunder-Wave — hence the Cherri_Berry.
- Mega Aggron rarely sets Stealth-Rock at random; Heavy_Duty_Boots are optional.
- No Magic-Room is used even if Mega Aggron has Leftovers, since Toxtricity (Low-Key) is forced to be the last opponent.
"""

    # C Team descs for npc 306
    C1_Strat = f"""**NPC IDs:** 306
**Enemy Team:** Leftovers Magearna + Heatran + Regieleki

**TEAM:**
- **Mimikyu #778**
> Equip: `Pecha_Berry | Lum_Berry`
> Moves: `Trick-Room` `Destiny-Bond` `Protect` `Taunt`
- **Shiny Mimikyu #1778**
> Equip: `Pecha_Berry | Lum_Berry`
> Moves: `Trick-Room` `Destiny-Bond` `Taunt` `Substitute`
- **Runerigus #867**
> Moves: `Trick-Room` `Curse` `Taunt`

**PROCEDURE:**
- Switch to Runerigus when Regieleki appears. Use Curse, then disable Trick-Room (if active). Use Taunt on idle turns, then Trick-Room three turns after Curse. Switch to Mimikyu and Destiny-Bond if Disguise is hit; Taunt + Destiny-Bond if Disguise was missed by Magma-Storm/Fleur-Cannon.
- Treat the opponent after Regieleki as a special lead. Follow similar procedure when misses occur. If Regieleki is the first overall, treat the last Pokémon as a second-position mon.
- On any other lead: Trick-Room → Destiny-Bond. If the first hit misses on Disguise, follow with Taunt + Destiny-Bond.
- Vs Magearna: If Calm-Mind or a miss occurs on turn 2, use Substitute → Destiny-Bond. Add Taunt after Substitute if it remains intact.
- Vs Heatran:
  - Miss on turn 2 with Disguise down → Substitute → Taunt → Destiny-Bond.
  - Double miss on turn 2 with Disguise up → Taunt + Destiny-Bond if no switch. If Heatran switches, follow procedure for the new matchup.
  - Triple misses are rare (Heatran alternates Earth-Power 100% and Magma-Storm 75%). If it happens, analyze based on remaining Substitutes, Trick-Room turns, and Disguise status.
- Vs Heatran (second position): Taunt + Destiny-Bond. Spam Taunt until Substitute breaks, then spam Destiny-Bond until KO.
- Vs Magearna (second position): Taunt + Destiny-Bond.

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- This strategy is only viable on high enemy level scales.
- If Trick-Room turns are insufficient and Disguise is still up, stall with Substitutes until “the twisted dimensions returned to normal!” Then reset with Trick-Room and treat it as a lead matchup.
"""
    C2_Strat = f"""**NPC IDs:** 306
**Enemy Team:** Leftovers Heatran + Scarf Genesect + Thundurus

**TEAM:**
- **Mimikyu #778**
> Equip: `Cherri_Berry | Lum_Berry`
> Moves: `Trick-Room` `Destiny-Bond` `Protect` `Taunt`
- **Shiny Mimikyu #1778**
> Moves: `Magic-Room` `Destiny-Bond` `Taunt`
- **Sudowoodo #185**
> Equip: `Cherri_Berry | Lum_Berry`
> Moves: `Protect` `Endeavor` `Sucker-Punch (teach Bonsly, then evolve)`

**PROCEDURE:**
- Thundurus lead: Trick-Room → Protect → Destiny-Bond (use Taunt instead of Protect if Thunder-Wave on turn 1).
- Genesect lead: Trick-Room → Taunt → Destiny-Bond.
- Heatran lead: Trick-Room → Destiny-Bond (if no miss). If miss, Taunt → Destiny-Bond.
- Heatran second: Taunt → (spam Shadow-Sneak until Disguise breaks) → Destiny-Bond.
- Genesect second: Magic-Room → Destiny-Bond.
- Thundurus second: Taunt → Destiny-Bond.

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- This strategy is only viable on high enemy level scales.
- Win rate depends on Heatran’s Magma-Storm accuracy: ~75% hit rate, ~20% manageable with misses. Bonus if Heatran has Leftovers, since you can Taunt if it’s not the last mon.
- If the last Pokémon is still active on turn 4, use Protect to drain Trick-Room. Remember to Endeavor again if Sturdy hasn’t triggered.
- Heatran is the main RNG factor: one miss is manageable, but two or more wasted turns is nearly unwinnable.
"""
    C3_Strat = f"""**NPC IDs:** 306
**Enemy Team:** Scarf Genesect + Cobalion + Tapu Koko

**TEAM:**
- **Sableye #302**
> Ability: `Prankster`
> Moves: `Destiny-Bond`
OR
- **Mimikyu #778**
> Moves: `Trick-Room` `Destiny-Bond` `Taunt` `Trick`

- **Mega Banette #7124**
> Equip: `Cheri_Berry | Lum_Berry`
> Moves: `Destiny-Bond`
OR
- **Shiny Mimikyu #1778**
> Moves: `Trick-Room` `Destiny-Bond` `Taunt` `Trick`

- **Sudowoodo #185**
> Equip: `Covert_Cloak | Cheri_Berry | Lum_Berry`
> Moves: `Protect` `Endeavor` `Sucker-Punch (teach Bonsly, then evolve)`

**PROCEDURE:**
- Spam Destiny-Bond, then finish with Sudowoodo’s Endeavor + Sucker-Punch.

**MIMIKYU TEAM STRATEGY:**
- Genesect lead: Trick-Room → Taunt → Destiny-Bond, then Trick → Destiny-Bond.
- Any other lead: Trick-Room → Destiny-Bond.
- Facing Cobalion/Tapu Koko after lead: Taunt → Destiny-Bond.
- Facing Genesect after lead: Trick → Destiny-Bond.

<a:fidough_wow:1283739703140679703> ***FidNotes***:
- Taunt prevents Cobalion’s Stealth-Rock or Tapu Koko’s Taunt.
- If no Covert-Cloak, equip Cherri-Berry on Sudowoodo and replace Trick with Substitute (mainly on second Mimikyu).
- Genesect lead (second encounter): Use Substitute ×2, then Trick-Room → Taunt → Substitute → Destiny-Bond.
- Genesect second: Taunt ×2 → Destiny-Bond.
"""

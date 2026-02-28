from constants.straydex import SD_EMOJIS
class SD_BATTLE_DESC:
    reg = f"""# BATTLE REGION

**COMMAND:**
**Gym Leader:**
- Kanto: `;b npc 1 to 8`
- Johto: `;b npc 14 to 21`
- Hoenn: `;b npc 27 to 34`
- Sinnoh: `;b npc 40 to 47`
- Unova: `;b npc 53 to 60`
- Kalos: `;b npc 66 to 73`

**Elite Four:**
- Kanto: `;b npc 9 to 12`
- Johto: `;b npc 22 to 25`
- Hoenn: `;b npc 35 to 38`
- Sinnoh: `;b npc 48 to 51`
- Unova: `;b npc 61 to 64`
- Kalos: `;b npc 74 to 77`

**Champion:**
- Kanto: `;b npc 13`
- Johto: `;b npc 26`
- Hoenn: `;b npc 39`
- Sinnoh: `;b npc 52`
- Unova: `;b npc 65`
- Kalos: `;b npc 78`

**TEAM:**
- **Mewtwo**
  Moves: `Psychic`  `Ice Beam`  `Aura Sphere`  `Shadow Ball`
- **Yveltal**
  Moves: `Oblivion Wing`  `Sucker Punch`  `Rock Slide`  `Heat Wave`
- **Xerneas**
  Moves: `Moonblast`  `Close Combat`  `Horn Leech`

---

**STRATEGY:**
- [Mewtwo] spam **Psychic**

> <a:fidough_wow:1283739703140679703> ***FidNotes:** You can turn-on the weakness chart with `/toggle utilities` or use `/lookup weakness <pokemon>`."""
    ti = f"""# BATTLE TOWER INFO

You must pay a registration fee of 25k pokecoins before you can participate in battle tower.

Progress in the tower resets for all trainers at 9:05pm EST every Monday, Wednesday and Friday.

The Battle Tower closes 5 minutes before prizes are handed out, so be sure to update your progress while it's open! It means you have to lose on your current floor so your progress would be updated.

**COMMAND:**
- `;bt register` - to register (Closes at 8pm EST on Mon, Wed, & Fri.)
- `;bt hs` - to view the leaderboard
- `;b npc bt` -  to battle in Battle Tower!

**PRIZE:**
- 1st Place: Golden Rotom, and Shiny Mimikyu Codes
- 2nd to 3rd: Shiny Mimkyu Code

**SPECIAL PRIZE:**
- If you win 1st place by a specific margin, your 1st place prize will be replaced by Golden Groudon. The current margin is 250 wins.

<a:fidough_wow:1283739703140679703> ***FidNotes*:** *The best days to grind for battle tower are Monday to Wednesday, or Wednesday to Friday. Other times would be during a new pokemeow event/golden promo.*"""
    ic = f"""# BATTLE ICON
A battle icon is the sprite next to your name in `;stats` or when you are catching pokemons

**HOW TO GET A BATTLE ICON?**
- There is a 1/1000 chance of a npc dropping their battle icon every time you've defeated them sucessfully.

**COMMAND**:
- `;b view icon` - shows the list of your unlocked battle icons
- `;b set icon <icon_name>` - changes your current battle icon.
- `;b stats` - shows your npc battle stats,  the number of your wins against npcs.
- `;b stats <id_number>` - shows your wins against a specific npc, and the last winning team you've used against them.
- `;co` - shows how many wins you had after getting a battle icon.
- `;hs icons` - shows the top 10 players with the most battle icons unlocked."""

    # -------------------------------------
    cba = f"""# CHALLENGER BASIC: JESSIE
**COMMAND:**  `;b npc 206`
**REQ:** *Receive a battle invitation from Trainer Jessie.*

**TEAM:**
- **Mewtwo**
> Moves: `Psychic`
- **Yveltal**
> Moves: `Oblivion Wing`
- **Groudon**
> Moves: `Earthquake`

**STRATEGY:**
- [Mewtwo] spam Psychic until it dies
- [Yveltal] spam Oblivion Wing
- First two mons can wipe out the whole team"""

    cbo = f"""# CHALLENGER BOSS: GIOVANNI
**COMMAND:**  `;b npc 200`
**REQ:** *Defeat all Kanto NPCs (first 13 NPCs) and receive a Boss Giovanni battle invitation.*

**TEAM:**
- **Mewtwo**
> Equip: `Twisted Spoon`
> Moves: `Psychic` `Energy Ball` `Dark Pulse`
- **Yveltal**
> Moves: `Psychic` `Sucker Punch`
- **Golisopod**
> Moves: `First Impression`

**STRATEGY:**
- [Mewtwo] Psychic on Nidoking
- [Mewtwo] Energy Ball on Rhyperior
- [Yveltal] Psychic on Rhyperior
- [Yveltal] Sucker Punch on Mewtwo
- [Mewtwo] Dark Pulse on Mewtwo
- [Golisopod] First Impression on Mewtwo"""

    cma = f"""# CHALLENGER MASTER: PROFESSOR OAK
**COMMAND:**  `;b npc 904`
**REQ:** *Defeat all 78 NPCs and receive a Professor Oak battle invitation.*
**OS STRAT LINK:** [Link](https://discord.com/channels/664509279251726363/775663491385131009/1269618316129865769)

**TEAM:**
- **Shedinja**
> Ability: `Wonder Guard`
> Equip: `Spell Tag`
> Moves: `Hone Claw` `Heal Block` `Shadow Claw`
> EVs: `ATK 252`

**STRATEGY:**
- [Shedinja] Use 6 Hone Claw
- [Shedinja] Spam Shadow Claw until Venusaur dies
- [Shedinja] Use Heal Block when Gyarados/Mewtwo first enters
- [Shedinja] Spam Shadow Claw till Gyarados/Mewtwo dies"""

    cse = f"""# CHALLENGER BASIC & BOSS
**COMMAND:**  `;b npc 200`to `;b npc 210`
**REQ:** *Receive a Basic or Boss battle invitation.*

**TEAM:**
- **Dugtrio**
> Equip: `Choice Scarf`
> Moves: `Memento`
> EVs: `SPE 252`
- **Whimsicott** | **Latios**
> Equip: `Choice Scarf`
> Moves: `Memento`
> EVs: `SPE 252`
- **Arceus**
> Equip: `Leftovers`
> Moves: `Iron Defense` `Calm Mind` `Judgment` `Recover`
> EVs: `HP 252` `DEF 128` `SPD 128`
or
- **Mew**
> Equip: `Leftovers`
> Moves: `Iron Defense` `Calm Mind` `Dragon Pulse` `Roost`
> EVs: `HP 150` `DEF 180` `SPD 180`

**STRATEGY:**
- [Dugtrio] Memento
- [Whimsicott | Latios] Memento
- [Arceus | Mew] Iron Defense +6
- [Arceus | Mew] Calm Mind +6
- [Arceus | Mew] Judgment | Dragon Pulse spam
- [Arceus | Mew] Recover | Roost when low hp

> <a:fidough_wow:1283739703140679703>  ***FidNotes**: Choice Scarf isn't required but you need atleast one scarf against NPC 208*"""

    leg = f"""# LEGEND: BLUE
**COMMAND:**
- `;b npc 1100`

**TEAM:**
__**1st Position**__
- **Dugtrio**
> Equip: `Choice Scarf`
> Moves: `Memento`

__**2nd Position**__
- **Arceus**
> Equip: `Leftovers`
> Moves: `Cosmic Power`  `Toxic`  `Body Press`  `Recover`

**STRATEGY:**
- [Dugtrio] Memento -2
- [Arceus] Cosmic Power +6
- [Arceus] Toxic
- [Arceus] Body Press spam
- [Arceus] Recover when low hp
"""

    ts = f"""# BATTLE TOWER STRAT
## NON-SETUP TEAM
### TEAM A:
- **Golden Mewtwo**
> Equip: `Choice Cloak` or `Choice Specs`
> Moves: `Dream Eater` `Ice Beam` `Energy Ball` `Shadow Ball`
> EVs: `SPA 252` `SPE 128` `SPD 128`
- **Golden Zacian**
> Equip: `Choice Cloak` or `Choice Band`
> Moves: `Play Rough` `Close Combat` `Crunch` `Wild Charge`
> EVs: `ATK 252` `HP 252` `SPE 6`
- **Golden Zekrom**
> Equip: `Choice Cloak` or `Choice Scarf`
> Moves: `Outrage` `Fusion Bolt` `Crunch` `Earth Power`
> EVs: `ATK 252` `HP 128` `SPE 130`
### TEAM B:
- **Golden Zekrom**
> Equip: `Choice Cloak` or `Choice Scarf`
> Moves: `Outrage` `Fusion Bolt` `Crunch` `Earth Power`
> EVs: `ATK 252` `HP 128` `SPE 130`
- **Golden Zacian**
> Equip: `Choice Cloak` or `Choice Band`
> Moves: `Play Rough` `Close Combat` `Crunch` `Wild Charge`
> EVs: `ATK 252` `HP 252` `SPE 6`
- **Golden Yveltal**
> Equip: `Choice Band`
> Moves: `Sucker Punch` `Oblivion Wing` `Foul Play` `Knock Off`
> EVs: `ATK 252` `SPA 128` `SPD 128`

<a:fidough_wow:1283739703140679703> ***Fidnotes:*** *Non Setup Strats are the fastest to clear Battle Tower Floors but would require you to pay extra attention to every battle, memorize the enemies' weakness, do smart switching, and lots of thinking.*"""

    # -------------------------------------

    cba2 = f"""# CHALLENGER BASIC: JAMES
**COMMAND:**  `;b npc 207`
**REQ:** *Receive a battle invitation from Trainer James.*

**TEAM:**
- **Mewtwo**
> Moves: `Psychic`
- **Yveltal**
> Moves: `Oblivion Wing`
- **Groudon**
> Moves: `Earthquake`

**STRATEGY:**
- [Mewtwo] spam Psychic until it dies
- [Yveltal] spam Oblivion Wing
- First two mons can wipe out the whole team"""

    cbo2 = f"""# CHALLENGER BOSS: MAXIE
**COMMAND:**  `;b npc 201`
**REQ:** *Defeat all Kanto, Johto and Hoenn NPCs (first 39 NPCs) and receive a Boss Maxie battle invitation.*

**TEAM:**
- **Xerneas**
> Moves: `Moonblast` `Horn Leech` `Psychic`
- **Mewtwo**
> Moves: `Psychic` `Ice Beam`
- **Kyogre**EVICE
> Equip: `Mystic Water`
> Moves: `Surf`

**STRATEGY:**
- [Xerneas] Moonblast on Mightyena
- [Xerneas] Psychic on Crobat
- [Mewtwo] Psychic on Crobat
- [Mewtwo] Ice Beam on Groudon
- [Xerneas] Horn Leech on Groudon"""

    cma2 = f"""# CHALLENGER MASTER: CIPHER HEAD
**COMMAND:**  `;b npc 998`
**REQ:** *Defeat all 78 NPCs and receive a Cipher Head Evice battle invitation.*
**OS STRAT LINK:** [Link](https://discord.com/channels/664509279251726363/775663491385131009/1269618386053365770)

**TEAM:**
- **Hawlucha**
> Ability: `Limber`
> Equip: `N/A`
> Moves: `Tailwind` `Close Combat`
> EVs: `DEF 180`
- **Mienshao**
> Ability `Inner Focus`
> Equip: `N/A`
> Moves: `Close Combat`
> EVs: `ATK 252` `SPD 236`
- **Shedinja**
> Ability: `Wonder Guard`
> Equip: `Silver Powder`
> Moves: `Hone Claw` `Heal Block` `Shadow Claw` `Leech Life`
> EVs: `ATK 252`

**STRATEGY:**
- [Hawlucha] Use Tailwind
- [Hawlucha] Spam Close Combat til it dies or til Tyranitar dies then swap to Shedninja
- [Mienshao] If Hawlucha dies to Tyranitar, swap to Mienshao and use Close Combat til Tyranitar dies,
- [Shedninja] Swap to Shedninja when Tyranitar dies, then use 6 Hone Claw and 1 Heal block.
- [Shedninja] Spam Shadow Claw til Salamence dies
- [Shedninja] When Slaking enters, use Leech Life and Heal Block once, then spam Leech Life"""
    cse2 = f"""STRAYDEX: BATTLE
# CHALLENGER MASTER: PROFESSOR OAK
**COMMAND:**  `;b npc 904`
**REQ:** *Defeat all 78 NPCs and receive a Professor Oak battle invitation.*

**TEAM:**
- **Corviknight**
> Equip: `Leftovers`
> Moves: `Bulk Up` `Agility` `Roost` `Power Trip`

**STRATEGY:**
- [Corviknight] Bulk Up +6
- [Corviknight] Agility +6
- [Corviknight] Power Trip spam
- [Corviknight] Roost when low hp"""

    leg2 = f"""# LEGEND: LANCE
**COMMAND:**
- `;b npc 1101`

**TEAM:**
__**1st Position**__
- **Dugtrio**
> Equip: `Choice Scarf`
> Moves: `Memento`

__**2nd Position**__
- **Arceus Fairy**
> Equip: `Leftovers`
> Moves: `Iron Defense`  `Calm Mind`  `Judgment`  `Recover`


**STRATEGY:**
- [Dugtrio] Memento -2
- [Arceus] Iron Defense +6
- [Arceus] Calm Mind +6
- [Arceus] Judgment spam
- [Arceus] Recover when low hp
"""

    ts2 = f"""## SETUP TEAMS
### TEAM A:
- **Zacian-Crowned / Golden Zacian / Zekrom**
> Equip: `Choice Cloak` or `Choice Scarf`
> Moves: `Noble Roar`
> EVs: `HP 252` `DEF 130` `SPD 128`
- **Gigantamax-Corviknight**
> Equip: `Leftovers`
> Moves: `Bulk Up` `Max Airstream` `Power Trip` `Roost`
> EVs: `HP 252` `SPD 252` `DEF 6`
OR
- ** Golden Arceus / Arceus-Ground / Arceus-Electric**
> Equip: `Leftovers`
> Moves: `Calm-Mind` `Iron Defense` `Recover` `Stored Power`
> EVs: `HP 252` `SPD 130` `DEF 128`
- **Arceus-Fairy**
> Equip: `Leftovers`
> Moves: `Calm-Mind` `Iron Defense` `Recover` `Judgment`
> EVs: `HP 252` `SPD 130` `DEF 128`
**STRATEGY: **
- [1st Pokemon]: Noble Roar -6
- [GMAX Corviknight]: +6 Bulk Up, +6 Max Airstream, Spam Power Trip, Roost when low hp.
- [Arceus/Arceus-Forms] : +6 Calm Mind, +6 Iron Defense, then Stored Power/Judgment Spam, Recover when low hp.

<a:fidough_wow:1283739703140679703> ***Fidnotes:*** *When using Arceus and you see a dark type on the enemy's team, set up the fairy type pokemon and let it be your attacking mon.*

### TEAM B:
- **Zacian-Crowned**
> Equip: `Choice Cloak` or `Choice Scarf`
> Moves: `Noble Roar` `Behemoth Blade` `Play Rough` `Crunch`
> EVs: `HP 252` `DEF 130` `SPD 128`
- **Golden Zacian**
> Equip: `Choice Cloak` or `Choice Scarf`
> Moves: `Noble Roar` `Wild Charge` `Play Rough` `Crunch`
> EVs: `HP 252` `DEF 130` `SPD 128`
- ** Golden Mewtwo**
> Equip: `Leftovers`
> Moves: `Calm-Mind` `Bulk Up` `Dream Eater` `Earth Power`
> EVs: `DEF 200` `SPD 200` `HP 110`
**STRATEGY: **
- [1st Pokemon] : Noble Roar -6
- [Golden Mewtwo]: +6 Calm Mind, +6 Bulk Up, then Dream Eater Spam, Use Earth Power when Enemy is immune to Psychic attacks or  has Resistance to it.

<a:fidough_wow:1283739703140679703> ***Fidnotes:*** *Only use one Zacian for Noble Roar as the other would finish off dark type enemies when Golden Mewtwo couldn't.*"""

    # ---------------------------
    cba3 = f"""# CHALLENGER BASIC: WES
**COMMAND:**  `;b npc 208`
**REQ:** *Receive a battle invitation from Trainer Wes.*

**TEAM:**
- **Yveltal**
> Moves: `Sucker Punch` `Rock Slide`
- **Xerneas**
> Moves: `Moonblast`
- **Tyranitar**
> Moves: `Rock Slide`
or
- **Zekrom**  |  **Mewtwo**
> Moves: `Fusion Bolt`  |  `Power Gem`

**STRATEGY:**
- [Yveltal] Super Punch on Espeon
- [Xerneas] Moonblast on Umbreon
- Spam Moonblast until it dies and finish with [3rd Mon]"""

    cbo3 = f"""# CHALLENGER BOSS: ARCHIE
**COMMAND:**  `;b npc 202`
**REQ:** *Defeat all Kanto, Johto and Hoenn NPCs (first 39 NPCs) and receive a Boss Archie battle invitation.*

**TEAM:**
- **Xerneas**
> Moves: `Moonblast` `Horn Leech` `Psychic`
- **Mewtwo**
> Moves: `Psychic` `Thunderbolt`
- **Zekrom**
> Moves: `Fusion Bolt`

**STRATEGY:**
- [Xerneas] Moonblast on Mightyena
- [Xerneas] Psychic on Muk
- [Mewtwo] Psychic on Muk
- [Mewtwo] Thunderbolt on Kyogre
- [Zekrom] Fusion Bolt on Kyogre
- [Xerneas] Horn Leech on Kyogre"""

    cma3 = f"""# CHALLENGER MASTER: MYSTERY TRAINER
**COMMAND:**  `;b npc 999`
**REQ:** *Defeat all 78 NPCs and receive a Mystery Trainer battle invitation.*
**OS STRAT LINK:** [Link](https://discord.com/channels/664509279251726363/775663491385131009/1355279147156635778)

**TEAM:**
- **Sneasel**
> Ability `Inner Focus`
> Equip: `N/A`
> Moves: `Scary Face` `Fake Out`
> EVs: `HP 252`
- **Mienshao**
> Ability `Inner Focus`
> Equip: `N/A`
> Moves: `Close Combat` `Swords Dance` `Vacuum Wave`
> EVs: `ATK 252` `SPD 236`
- **Shedinja**
> Ability: `Wonder Guard`
> Equip: `Silver Powder`
> Moves: `Hone Claw` `Heal Block` `Shadow Claw` `Leech Life`
> EVs: `ATK 252`

**STRATEGY:**
- Use Fake Out then Scary Face once.
- If Sneasel dies after Scary Face, swap to Mienshao. Use Sword Dance and, then Close Combat.
- If Darkrai uses Rest swap to Mienshao. Use Sword Dance, Vacuum Wave and, then Close Combat .
- If Darkrai does not kill Sneasel and does not rest, use Fakeout then Focus Punch.
- [Shedninja] Swap to Shedninja when Darkrai dies, then use 6 Hone Claw and 1 Heal block after Latios/Kyogre enters.
- [Shedninja] Spam Shadow Claw til Latios/Kyogre dies."""
    cse3 = f"""# CHALLENGER MASTER: CIPHER HEAD EVICE
**COMMAND:**  `;b npc 998`
**REQ:** *Defeat all 78 NPCs and receive a Cipher Head Evice battle invitation.*

**TEAM:**
__**1st Position**__
- **Sawk** | **Galarian-Zapdos** | **Marshadow** | **Terrakion** | **Urshifu**
> Equip: `Choice Band | Choice Cloak`
> Moves: `Superpower`
> EVs: `ATK 252` `SPE 252`
> Stats: `ATK 394` `SPE 322`

__**2nd Position**__
- **Jirachi**
> Equip: `Choice Scarf`
> Moves: `Charm`
> EVs: `SPE 128`
> Stats: `SPE 306`

__**3rd Position**__
- **Magearna**
> Equip: `Leftovers`
> Moves: `Iron Defense` `Agility` `Calm Mind` `Stored Power`
> EVs: `HP 144`
> Stats: `SPE 306`
__OR__
- **Bronzong**
> Equip: `Leftovers`
> Moves: `Iron Defense` `Rock Polish` `Calm Mind` `Stored Power`
> EVs: `HP 252` `DEF 152` `SPE 80`
> Stats: `SPE 114`

**STRATEGY:**
- [First Mon] Superpower spam
- [Jirachi] Charm -6
- [Magearna | Bronzong] Iron Defense +6
- [Magearna | Bronzong] Agility +4 | Rock Polish +6
- [Magearna | Bronzong] Calm Mind +4
- [Magearna | Bronzong] Stored Power spam"""

    leg3 = f"""# LEGEND: STEVEN
**COMMAND:**
- `;b npc 1102`

**TEAM:**
__**1st Position**__
- **Dugtrio**
> Equip: `Choice Scarf`
> Moves: `Memento`

__**2nd Position**__
- **Arceus Dark**
> Equip: `Leftovers`
> Moves: `Iron Defense`  `Calm Mind`  `Judgment`  `Recover`
__OR__
- **Gmax Corviknight**
> Equip: `Leftovers`
> Moves: `Power Trip`  `Bulk Up`  `Max Airstream`  `Roost`

**STRATEGY:**
- [Dugtrio] Memento -2
- [Arceus | Corvi] Iron Defense +6 | Bulk Up +6
- [Arceus | Corvi] Calm Mind +6 | Max Airstream +6
- [Arceus | Corvi] Judgment  | Powertrip spam
- [Arceus | Corvi] Recover | Roost when low hp

"""

    ts3 = f"""## SETUP TEAMS
### TEAM C

- **Golden Zacian**
> Equip: `Choice Scarf`
> Moves: `Noble Roar`
> Evs: `HP 252` `DEF 130` `SPD 128`
- ** Eternamax Eternatus**
> Equip: `Leftovers`
> Moves: `Cosmic Power` `Recover` `Max Darkness` `Max Ooze`
> Evs: `HP 252` `SPA 252` `SPE 6`
- **Arceus Electric**
> Equip: `Leftovers`
> Moves: `Calm Mind` `Iron Defense` `Recover` `Flamethrower`
> EVs: `HP 252` `DEF 130` `SPD 128`
**STRATEGY:**
- [Zacian] : Noble Roar -6
- [Eternatus] : Cosmic Power +6, Max Ooze +6, then spam Max Darkness, Recover when low hp.
- [Arceus]: +6 Calm Mind, +6 Iron Defense, then Flamethrower Spam, Recover when low hp.

### TEAM D

- **Golden Zacian**
> Equip: `Choice Scarf`
> Moves: `Noble Roar`
> Evs: `HP 252` `DEF 130` `SPD 128`
- ** GMAX Corvi**
> Equip: `Leftovers`
> Moves: `Bulk Up` `Max Airstream` `Roost `Power Trip`
> Evs: `HP 252` `SPD 252` `DEF 6`
- **Arceus Electric**
> Equip: `Leftovers`
> Moves: `Calm Mind` `Iron Defense` `Recover` `Flamethrower`
> EVs: `HP 252` `DEF 130` `SPD 128`
**STRATEGY:**
- [Zacian] : Noble Roar -6
- [Corviknight] : Bulk Up +6, Max Airstream +6, then spam Power Trip, Roost when low hp.
- [Arceus]: +6 Calm Mind, +6 Iron Defense, then Flamethrower Spam, Recover when low hp."""

    # no cma3
    # ---------------------------
    cba4 = f"""# CHALLENGER BASIC: RED
**COMMAND:**  `;b npc 209`
**REQ:** *Receive a battle invitation from Trainer Red.*

**TEAM:**
- **Yveltal**
> Moves: `Oblivion Wing` `Rock Slide`
- **Kyogre**
> Moves: `Surf` `Thunderbolt`
- **Zekrom**
> Moves: `Fusion Bolt`
or
- **Mewtwo**
> Moves: `Thunderbolt` `Power Gem`

**STRATEGY:**
- [Yveltal] Oblivion Wing on Venusaur
- [Yveltal] Rock Slide on Zard
- [Kyogre] Thunderbolt on Zard
- [3rd] spam Electric on Blastoise"""

    cbo4 = f"""# CHALLENGER BOSS: CYRUS
**COMMAND:**  `;b npc 203`
**REQ:** *Defeat all Kanto, Johto, Hoenn and Sinnoh NPCs (first 52 NPCs) and receive a Boss Cyrus battle invitation.*

**TEAM:**
- **Regigigas**
> Equip: `Black Belt`
> Moves: `Drain Punch`
- **Metagross**
> Equip: `Soft Sand`
> Moves: `Bullet Punch` `Earthquake`
or
- **Dialga**
> Equip: `Soft Sand`
> Moves: `Flash Cannon` `Earth Power`
- **Mewtwo**
> Moves: `Aura Sphere`
or
- **Groudon**
> Moves: `Earthquake`

**STRATEGY:**
- [Regigigas] Drain Punch on Houndoom
- [Regigigas] Drain Punch on Weaville
- [Metagross] Bullet Punch on Weaville
- [Mewtwo] Aura Sphere on Dialga
- [Metagross] Earthquake on Dialga"""
    cse4 = f"""# CHALLENGER MASTER: MYSTERY TRAINER
**COMMAND:**  `;b npc 999`
**REQ:** *Defeat all 78 NPCs and receive a Mystery Trainer battle invitation.*

**TEAM:**
__**1st Position**__
- **Rhyperior**
> Equip: `Black Belt`
> Moves: `Focus Punch` `Stealth Rock`
> EVs: `DEF 252` `HP 236` `ATK 20`
__OR__
- **Steelix**
> Equip: `Zoom Lens`
> Moves: `Dig` `Stealth Rock` `Toxic`
> EVs: `HP 252` `DEF 172`

__**2nd Position**__
- **Jirachi**
> Equip: `Choice Scarf`
> Moves: `Charm`
> EVs: `SPE 252`
> Stats: `SPE 340`
__OR__
- **Magearna**
> Equip: `Leftovers`
> Moves: `Eerie Impulse` `Self Destruct`
> EVs: `HP 252` `SPD 252`

__**3rd Position**__
- **Incineroar (If using Jirachi)**
> Equip: `Leftovers`
> Moves: `Bulk Up` `Trailblaze` `Power Trip`
> EVs: `HP 200`
__OR__
- **Wigglytuff (If using Magearna)**
> Equip: `Leftovers`
> Moves: `Amnesia` `Trailblaze` `Work Up` `Stored Power`
> EVs: `SPD 252` `SPA 184` `HP 72`

**STRATEGY:**
- [Rhyperior | Steelix] 2 Focus Punch | 1 Toxic, 4 Dig, then Stealth Rock spam
- [Jirachi | Magearna] Charm -6 | Eerie Impulse -6 then Self Destruct
- [Incineroar | Wigglytuff] Bulk Up +5 | Amnesia +6
- [Incineroar | Wigglytuff] Trailblaze +4 | Trailblaze +6 then Work Up +6
- [Incineroar | Wigglytuff] Power Trip | Stored Power spam

> <a:fidough_wow:1283739703140679703>  ***FidNotes**: Use Amnesia again whenever Wigglytuff's SPD drops to +4*"""

    leg4 = f"""# LEGEND: CYNTHIA
**COMMAND:**
- `;b npc 1103`

**TEAM:**
__**1st Position**__
- **Dugtrio**
> Equip: `Choice Scarf`
> Moves: `Memento`

__**2nd Position**__
- **Arceus**
> Equip: `Leftovers`
> Moves: `Cosmic Power`  `Toxic`  `Body Press`  `Recover`


**STRATEGY:**
- [Dugtrio] Memento -2
- [Arceus] Cosmic Power +6
- [Arceus] Toxic
- [Arceus] Body Press spam
- [Arceus] Recover when low hp"""

    ts4 = f"""## SETUP TEAMS
### TEAM C

- **Golden Zacian**
> Equip: `Choice Scarf`
> Moves: `Noble Roar`
> Evs: `HP 252` `DEF 130` `SPD 128`
- ** Eternamax Eternatus**
> Equip: `Leftovers`
> Moves: `Cosmic Power` `Recover` `Max Darkness` `Max Ooze`
> Evs: `HP 252` `SPA 252` `SPE 6`
- **Arceus Electric**
> Equip: `Leftovers`
> Moves: `Calm Mind` `Iron Defense` `Recover` `Flamethrower`
> EVs: `HP 252` `DEF 130` `SPD 128`
**STRATEGY:**
- [Zacian] : Noble Roar -6
- [Eternatus] : Cosmic Power +6, Max Ooze +6, then spam Max Darkness, Recover when low hp.
- [Arceus]: +6 Calm Mind, +6 Iron Defense, then Flamethrower Spam, Recover when low hp.

### TEAM D

- **Golden Zacian**
> Equip: `Choice Scarf`
> Moves: `Noble Roar`
> Evs: `HP 252` `DEF 130` `SPD 128`
- ** GMAX Corvi**
> Equip: `Leftovers`
> Moves: `Bulk Up` `Max Airstream` `Roost `Power Trip`
> Evs: `HP 252` `SPD 252` `DEF 6`
- **Arceus Electric**
> Equip: `Leftovers`
> Moves: `Calm Mind` `Iron Defense` `Recover` `Flamethrower`
> EVs: `HP 252` `DEF 130` `SPD 128`
**STRATEGY:**
- [Zacian] : Noble Roar -6
- [Corviknight] : Bulk Up +6, Max Airstream +6, then spam Power Trip, Roost when low hp.
- [Arceus]: +6 Calm Mind, +6 Iron Defense, then Flamethrower Spam, Recover when low hp."""
    # ---------------------------

    cba5 = f"""# CHALLENGER BASIC: STEVEN
**COMMAND:**  `;b npc 210`
**REQ:** *Receive a battle invitation from Trainer Steven.*

**TEAM:**
- **Kyogre**
> Equip: `Mystic Water`
> Moves: `Surf` `Earthquake`
- **Slaking**
> Equip: `Soft Sand`
> Moves: `Earthquake`
- **Groudon**
> Equip: `Soft Sand`
> Moves: `Earthquake`
or
- **Yveltal**
> Moves: `Sucker Punch`

**STRATEGY:**
- [Kyogre] Surf on Aggron
- [All] spam Earthquake
- [Yveltal] Sucker Punch on Metagross"""

    cbo5 = f"""# CHALLENGER BOSS: GHETSIS
**COMMAND:**  `;b npc 204`
**REQ:** *Defeat all Kanto, Johto, Hoenn, Sinnoh and Unova NPCs (first 65 NPCs) and receive a Boss Ghetsis battle invitation.*

**TEAM:**
- **Xerneas**
> Moves: `Close Combat` `Moonblast`
- **Groudon**
> Equip: `Soft Sand`
> Moves: `Earthquake`
- **Dialga**
> Moves: `Outrage`

**STRATEGY:**
- [Xerneas] Close Combat on Bisharp
- [Xerneas] Moonblast on Hydreigon
- [Xerneas] Close Combat on Reshiram
- [Groudon] Earthquake on Reshiram
- [Dialga] Outrage on Reshiram"""

    cma5 = f"""# CHALLENGER BOSS: GHETSIS
**COMMAND:**  `;b npc 204`
**REQ:** *Defeat all Kanto, Johto, Hoenn, Sinnoh and Unova NPCs (first 65 NPCs) and receive a Boss Ghetsis battle invitation.*

**TEAM:**
- **Xerneas**
> Moves: `Close Combat` `Moonblast`
- **Groudon**
> Equip: `Soft Sand`
> Moves: `Earthquake`
- **Dialga**
> Moves: `Outrage`

**STRATEGY:**
- [Xerneas] Close Combat on Bisharp
- [Xerneas] Moonblast on Hydreigon
- [Xerneas] Close Combat on Reshiram
- [Groudon] Earthquake on Reshiram
- [Dialga] Outrage on Reshiram"""

    leg5 = f"""# LEGEND: ALDER
**COMMAND:**
- `;b npc 1104`

**TEAM:**
__**1st Position**__
- **Dugtrio**
> Equip: `Choice Scarf`
> Moves: `Memento`

__**2nd Position**__
- **Arceus Water**
> Equip: `Leftovers`
> Moves: `Iron Defense`  `Calm Mind`  `Judgment`  `Recover`


**STRATEGY:**
- [Dugtrio] Memento -2
- [Arceus] Iron Defense +6
- [Arceus] Calm Mind +6
- [Arceus] Judgment spam
- [Arceus] Recover when low hp
"""
    # ---------------------------
    cbo6 = f"""# CHALLENGER BOSS: LYSANDRE
**COMMAND:**  `;b npc 205`
**REQ:** *Defeat all Kanto, Johto, Hoenn, Sinnoh, Unova and Kalos NPCs (all NPCs except NPC 78) and receive a Boss Lysandre battle invitation.*

**TEAM:**
- **Kyogre**
> Equip: `Mystic Water`
> Moves: `Surf` `Thunderbolt`
- **Zekrom**
> Equip: `Magnet`
> Moves: `Fusion Bolt`
- **Xerneas**
> Moves: `Moonblast`
or
- **Tyranitar**
> Equip: `Hard Stone`
> Moves: `Rock Slide`

**STRATEGY:**
- [Kyogre] Surf on Pyroar
- [Kyogre] Thunderbolt on Gyarados
- [Zekrom] Fusion Bolt on Gyarados
- [Zekrom] Fusion Bolt on Yveltal
- [Kyogre] Thunderbolt on Yveltal
- [Xerneas] Moonblast on Yveltal"""

    leg6 = f"""# LEGEND: SYCAMORE
**COMMAND:**
- `;b npc 1105`

**TEAM:**
__**1st Position**__
- **Dugtrio**
> Equip: `Choice Scarf`
> Moves: `Memento`

__**2nd Position**__
- **Arceus**
> Equip: `Leftovers`
> Moves: `Iron Defense`  `Calm Mind`  `Stored Power`  `Recover`


**STRATEGY:**
- [Dugtrio] Memento -2
- [Arceus] Iron Defense +6
- [Arceus] Calm Mind +6
- [Arceus] Stored Power spam
- [Arceus] Recover when low hp"""


#
class SD_BATTLE_THUMBNAIL:
    cba = "https://media.discordapp.net/attachments/1382540357123965029/1405503297053392909/300aa3900f11fcca84207ad6dd2e6ffa8fdaed9ac18195a138e3d692a6e23b95.png?ex=689f1073&is=689dbef3&hm=a95088c1cc53bb008ea032d484fc03e31c1b7bf0564e9167fe535a3863461283&=&format=webp&quality=lossless&width=210&height=446"

    cbo = "https://media.discordapp.net/attachments/1382540357123965029/1382553462629208164/1081fe7e7981ec228c62a58b8302a7a00346b6052b1edcec4334cd0908e7ff9d.png?ex=689ca700&is=689b5580&hm=193074e9f134dae35dca05c58a55dd54f32bfbae937ff69cef84f1681aefc9c2&=&format=webp&quality=lossless&width=248&height=320"

    cma = "https://media.discordapp.net/attachments/1382540357123965029/1382562850299711600/e855c128ee6d18c291c6135a056ac3312f914e89ed4ac40310ffb7576f7c575f.png?ex=689cafbe&is=689b5e3e&hm=09dd886519eb012460a120b375cb91a6fd6115f91db03e0f4e536c7afdf857f3&=&format=webp&quality=lossless&width=203&height=432"

    leg = "https://media.discordapp.net/attachments/1382540357123965029/1384213535499882767/1373280913013870622.png?ex=689cc250&is=689b70d0&hm=5ed3d852dfda3031e6507aa816405523ffed8cb8a19502c2cd12aeae79b2278e&=&format=webp&quality=lossless&width=68&height=101"
    # ---------------------------
    cba2 = "https://media.discordapp.net/attachments/1382540357123965029/1382545849657331784/236471e7ce1886bbcc37d371b24bb17e99c8a47e57043f8b8198a5bad768c06c.png?ex=689c9fe9&is=689b4e69&hm=59a79417b18ccf6b939a423ea24e3169647ddf60570a00e574f212aafea75487&=&format=webp&quality=lossless&width=179&height=498"

    cbo2 = "https://media.discordapp.net/attachments/1382540357123965029/1382553505105182791/e42e2a9efeda7796f0e835a402d77b37d1dec190f1a34a6cede8db06c87aade0.png?ex=689ca70a&is=689b558a&hm=4f678899b9a04624555d39d7b3860a44b4f71e199f0ba756574f04b0696a1793&=&format=webp&quality=lossless&width=129&height=425"

    cma2 = "https://media.discordapp.net/attachments/1382540357123965029/1382562936828072046/9629ff5f2cb5d69d0911073904b0901c14d9c12ec6c1ef0357d0f7916a72cc56.png?ex=689cafd2&is=689b5e52&hm=dacb1fadb3f6ee435668f664976d2661d70ca320c8ec51c67bbe2ee3d61b0e9d&=&format=webp&quality=lossless&width=90&height=268"

    leg2 = "https://media.discordapp.net/attachments/1382540357123965029/1384213656103030884/1373013775803744388.png?ex=689cc26d&is=689b70ed&hm=c0610ea321e7d9372860b5d43432dfa9110a6fa2400db5c61bd9e2ac8da3d469&=&format=webp&quality=lossless&width=68&height=104"

    # --------------------------

    cba3 = "https://media.discordapp.net/attachments/1382540357123965029/1382545849950797824/c0b36978ca221a84f04cc4bc61aa4bb44fa45c9551f441939422a5dbca8bd434.png?ex=689c9fe9&is=689b4e69&hm=e958ef4540b46931b3349cd78ac8bd4c299a9043cdebd4f487cbcdfa899292b1&=&format=webp&quality=lossless&width=281&height=369"

    cbo3 = "https://media.discordapp.net/attachments/1382540357123965029/1382553535673139291/4e9b6765c1573f7fcecb11c2c6e0e4037cb3119ee2affa8765f70db4c9338928.png?ex=689ca711&is=689b5591&hm=a2950ba450df2b49a7d572b6330a3daabad6ab1544130e5f5070516a67428f64&=&format=webp&quality=lossless&width=203&height=428"

    cma3 = "https://media.discordapp.net/attachments/1382540357123965029/1382563263002316863/eb4d2231fc850910668424f2fc14b1bddfd3343369c4258487333167321c984b.png?ex=689cb020&is=689b5ea0&hm=9521bceb343cb0ddf93f965a56f4c792fec4e54a769800cd7fd751df3e6e824d&=&format=webp&quality=lossless&width=169&height=341"

    leg3 = "https://media.discordapp.net/attachments/1382540357123965029/1384213736067301466/1373288124599369960.png?ex=689cc280&is=689b7100&hm=f7cab752611eb6fb3cbd5d98b49daecd12cf081020e689a3e8d8ac56e12e262d&=&format=webp&quality=lossless&width=68&height=88"
    # --------------------------
    cba4 = "https://media.discordapp.net/attachments/1382540357123965029/1382545850236145754/e3d11f3c392d81275458e6398c841cb7c313081f0b4f9c432fd5053e9ba2fc98.png?ex=689c9fe9&is=689b4e69&hm=cdae33b46299bfc168943edd202adceb15b10975ff69fffdad7e6bc40d0ebd32&=&format=webp&quality=lossless&width=281&height=395"

    cbo4 = "https://media.discordapp.net/attachments/1382540357123965029/1382559214844641330/6caffeb11db19c9d3b9e872eae74d4db97d45895c39dcd77aa92554ccf762560.png?ex=689cac5b&is=689b5adb&hm=deecfa806c6175908882f37c6bf4bfb5162bb32aefb73888ee88c25c9a92ec25&=&format=webp&quality=lossless&width=203&height=367"

    leg4 = "https://media.discordapp.net/attachments/1382540357123965029/1384213827209662568/1373300473087397972.png?ex=689cc295&is=689b7115&hm=8dc6c7107ccc761f73f2c5f88ba3a180b787e9ae6a53862e9e7292d69b381c9b&=&format=webp&quality=lossless&width=118&height=144"
    # --------------------------
    cba5 = "https://media.discordapp.net/attachments/1382540357123965029/1382545850575753368/d3702cd61aecd3bcaf572af3f1c63f82a049de26d3f22fdce53175989c038a6b.png?ex=689c9fe9&is=689b4e69&hm=377973c16ee3913c6ed00e8633e1335f063da2c019a546d58845b515c34941a4&=&format=webp&quality=lossless&width=225&height=414"

    cbo5 = "https://media.discordapp.net/attachments/1382540357123965029/1382559309124206592/cd494e44a20dc9ff5be2498fa89e4e3047b7fad7f3908dd806fdea0183194177.png?ex=689cac72&is=689b5af2&hm=fbf7b08fe74e4d5ba35b0271564e765daba989a5ba0f7d0ff3a6f906603dc2fc&=&format=webp&quality=lossless&width=208&height=334"

    leg5 = "https://media.discordapp.net/attachments/1382540357123965029/1384213898391064810/1373308056196223146.png?ex=689cc2a6&is=689b7126&hm=072aa71e1d098b3a1397821a04b46e91c641b918a2e1cf896c26cd4469d1dceb&=&format=webp&quality=lossless&width=68&height=82"

    # --------------------------
    cbo6 = "https://media.discordapp.net/attachments/1382540357123965029/1382559425218351124/0ce9fc7d74fad4dc6608043f77e71557a1aa3d31a064631ddad1f5cf2d800b6c.png?ex=689cac8d&is=689b5b0d&hm=928139e963a3ffc07ddb2db5e081e109bf7a1c3bbab671db379fa5d272821ad7&=&format=webp&quality=lossless&width=138&height=394"

    leg6 = "https://media.discordapp.net/attachments/1382540357123965029/1384214017605632180/1373306559865688195.png?ex=689cc2c3&is=689b7143&hm=0fbd020602d5081feb0661b096fced4dbe05cd29ecee893cbc2441ae846f6732&=&format=webp&quality=lossless&width=68&height=80"


class SD_BATTLE_BUTTON_LABELS:
    # --- CBA ---
    cba = "Jessie"
    cba2 = "James"
    cba3 = "Wes"
    cba4 = "Red"
    cba5 = "Steven"
    # --- CBO ---
    cbo = "Giovanni"
    cbo2 = "Maxie"
    cbo3 = "Archie"
    cbo4 = "Cyrus"
    cbo5 = "Ghetsis"
    cbo6 = "Lysandre"
    # --- CMA ---
    cma = "Professor Oak"
    cma2 = "Cipher Head Evice"
    cma3 = "Mystery Trainer"
    # --- CSE ---
    cse = "Basic and Boss"
    cse2 = "Professor Oak"
    cse3 = "Cipher Head Evice"
    cse4 = "Mystery Trainer"
    # --- LEG ---
    leg = "Blue"
    leg2 = "Lance"
    leg3 = "Steven"
    leg4 = "Cynthia"
    leg5 = "Alder"
    leg6 = "Sycamore"
    # --- TS ---
    ts = "Non-Setup"
    ts2 = "Setup Team 1"
    ts3 = "Setup Team 2"
    ts4 = "Setup Team 3"


class SD_BATTLE_BUTTON_EMOJIS:
    # --- CBA ---
    cba = "🐱"
    cba2 = "🪻"
    cba3 = "🐺"
    cba4 = "🎒"
    cba5 = "💎"
    # --- CBO ---
    cbo = "👑"
    cbo2 = "🔥"
    cbo3 = "🌊"
    cbo4 = "🌌"
    cbo5 = "🌀"
    cbo6 = "🌹"
    # --- CMA ---
    cma = SD_EMOJIS.professor_oak
    cma2 = SD_EMOJIS.cipher_head_evice
    cma3 = SD_EMOJIS.mystery_trainer
    # --- CSE ---
    cse = "⚔️"
    cse2 = "📖"
    cse3 = "🧥"
    cse4 = "🎭"
    # --- LEG ---
    leg = "🔵"
    leg2 = "🐉"
    leg3 = "💠"
    leg4 = "🗡️"
    leg5 = "🪶"
    leg6 = "🌿"
    # --- TS ---
    ts = "🚫"
    ts2 = "🛠️"
    ts3 = "🧰"
    ts4 = "🪛"


sd_battle_dict = {
    # --- CBA ---
    "cba": {
        "desc": SD_BATTLE_DESC.cba,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cba,
        "button_label": SD_BATTLE_BUTTON_LABELS.cba,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cba,
    },
    "cba2": {
        "desc": SD_BATTLE_DESC.cba2,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cba2,
        "button_label": SD_BATTLE_BUTTON_LABELS.cba2,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cba2,
    },
    "cba3": {
        "desc": SD_BATTLE_DESC.cba3,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cba3,
        "button_label": SD_BATTLE_BUTTON_LABELS.cba3,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cba3,
    },
    "cba4": {
        "desc": SD_BATTLE_DESC.cba4,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cba4,
        "button_label": SD_BATTLE_BUTTON_LABELS.cba4,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cba4,
    },
    "cba5": {
        "desc": SD_BATTLE_DESC.cba5,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cba5,
        "button_label": SD_BATTLE_BUTTON_LABELS.cba5,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cba5,
    },
    # --- CBO ---
    "cbo": {
        "desc": SD_BATTLE_DESC.cbo,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cbo,
        "button_label": SD_BATTLE_BUTTON_LABELS.cbo,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cbo,
    },
    "cbo2": {
        "desc": SD_BATTLE_DESC.cbo2,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cbo2,
        "button_label": SD_BATTLE_BUTTON_LABELS.cbo2,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cbo2,
    },
    "cbo3": {
        "desc": SD_BATTLE_DESC.cbo3,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cbo3,
        "button_label": SD_BATTLE_BUTTON_LABELS.cbo3,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cbo3,
    },
    "cbo4": {
        "desc": SD_BATTLE_DESC.cbo4,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cbo4,
        "button_label": SD_BATTLE_BUTTON_LABELS.cbo4,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cbo4,
    },
    "cbo5": {
        "desc": SD_BATTLE_DESC.cbo5,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cbo5,
        "button_label": SD_BATTLE_BUTTON_LABELS.cbo5,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cbo5,
    },
    "cbo6": {
        "desc": SD_BATTLE_DESC.cbo6,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cbo6,
        "button_label": SD_BATTLE_BUTTON_LABELS.cbo6,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cbo6,
    },
    # --- CMA ---
    "cma": {
        "desc": SD_BATTLE_DESC.cma,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cma,
        "button_label": SD_BATTLE_BUTTON_LABELS.cma,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cma,
    },
    "cma2": {
        "desc": SD_BATTLE_DESC.cma2,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cma2,
        "button_label": SD_BATTLE_BUTTON_LABELS.cma2,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cma2,
    },
    "cma3": {
        "desc": SD_BATTLE_DESC.cma3,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.cma3,
        "button_label": SD_BATTLE_BUTTON_LABELS.cma3,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cma3,
    },
    # --- CSE ---
    "cse": {
        "desc": SD_BATTLE_DESC.cse,
        "thumbnail_url": None,
        "button_label": SD_BATTLE_BUTTON_LABELS.cse,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cse,
    },
    "cse2": {
        "desc": SD_BATTLE_DESC.cse2,
        "thumbnail_url": None,
        "button_label": SD_BATTLE_BUTTON_LABELS.cse2,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cse2,
    },
    "cse3": {
        "desc": SD_BATTLE_DESC.cse3,
        "thumbnail_url": None,
        "button_label": SD_BATTLE_BUTTON_LABELS.cse3,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cse3,
    },
    "cse4": {
        "desc": SD_BATTLE_DESC.cse4,
        "thumbnail_url": None,
        "button_label": SD_BATTLE_BUTTON_LABELS.cse4,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.cse4,
    },
    # --- LEG ---
    "leg": {
        "desc": SD_BATTLE_DESC.leg,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.leg,
        "button_label": SD_BATTLE_BUTTON_LABELS.leg,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.leg,
    },
    "leg2": {
        "desc": SD_BATTLE_DESC.leg2,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.leg2,
        "button_label": SD_BATTLE_BUTTON_LABELS.leg2,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.leg2,
    },
    "leg3": {
        "desc": SD_BATTLE_DESC.leg3,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.leg3,
        "button_label": SD_BATTLE_BUTTON_LABELS.leg3,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.leg3,
    },
    "leg4": {
        "desc": SD_BATTLE_DESC.leg4,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.leg4,
        "button_label": SD_BATTLE_BUTTON_LABELS.leg4,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.leg4,
    },
    "leg5": {
        "desc": SD_BATTLE_DESC.leg5,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.leg5,
        "button_label": SD_BATTLE_BUTTON_LABELS.leg5,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.leg5,
    },
    "leg6": {
        "desc": SD_BATTLE_DESC.leg6,
        "thumbnail_url": SD_BATTLE_THUMBNAIL.leg6,
        "button_label": SD_BATTLE_BUTTON_LABELS.leg6,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.leg6,
    },
    # --- TS ---
    "ts": {
        "desc": SD_BATTLE_DESC.ts,
        "thumbnail_url": None,
        "button_label": SD_BATTLE_BUTTON_LABELS.ts,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.ts,
    },
    "ts2": {
        "desc": SD_BATTLE_DESC.ts2,
        "thumbnail_url": None,
        "button_label": SD_BATTLE_BUTTON_LABELS.ts2,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.ts2,
    },
    "ts3": {
        "desc": SD_BATTLE_DESC.ts3,
        "thumbnail_url": None,
        "button_label": SD_BATTLE_BUTTON_LABELS.ts3,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.ts3,
    },
    "ts4": {
        "desc": SD_BATTLE_DESC.ts4,
        "thumbnail_url": None,
        "button_label": SD_BATTLE_BUTTON_LABELS.ts4,
        "button_emoji": SD_BATTLE_BUTTON_EMOJIS.ts4,
    },
}

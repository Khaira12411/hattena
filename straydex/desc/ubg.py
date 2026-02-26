class SD_UBG:
    cap = f"""# CAPTCHA

**DO NOT** ignore your CAPTCHA. Missing or failing CAPTCHAs can lead to:
- ⏱️ **Temporary ban:** 15 minutes
- ❌ **Perma-ban:** after 5 bans

You have 5 attempts within **1 min 30 sec** per CAPTCHA. Check carefully before answering.

**Server Help & Safety**
- React on the CAPTCHA message to ping <@&1113046418307944510> for help.
- **Critical:** 5 bans = coins & Pokémon lost permanently.
- To unban a permanently banned account, you need 30,000 <:patreon_token:1296818113735819405>
- For more info, check PokéMeow’s `;captcha` command.

**CAPTCHA Tips**
- Always read left → right, even in vertical images.
- If it’s hard to read, just try your best – a new CAPTCHA will appear if it’s wrong.
- Do **not tag anyone** under the CAPTCHA message; it counts as an attempt. Type answers in the original channel only.
- If you have 3 bans, consider a backup account to protect your Pokémon."""

    cas = f"""# CATCH STREAKS
**COMMAND:**  `;streaks`  to check all streaks.

Catching streaks award  `Lootboxes`  at a predefined number of consecutive catches per-rarity tier. The only bonus seems to be the lootbox.

Your Pokemon-catching streaks are tracked per rarity. If you miss catching a pokemon your streak is reset for that Rarity only. Your streak is shown before and after trying to catch a pokemon with  `;p`. Due to this, if you’re close to a streak milestone, you might consider using a better-than-average ball for a rarity type.

- <:Common:1186968566063435786>  Every 15 catches, 1 Lootbox
- <:Uncommon:1186968571839000606>  Every 10 catches, 1 Lootbox
- <:Rare:1142668430634393610>  Every 5 catches, 1 Lootbox
- <:SuperRare:1133025503067000852>  Every 5 catches, 2 Lootboxes
- <:Legendary:1090640224125718570>  Every 5 catches, 3 Lootboxes
- <:Shiny:1090640278999810079>  Every 5 catches, 4 Lootboxes

# LOOTBOX REWARDS
- `PokeCoins`  ||  100% droprate  |  50-1050 coins
- `Pokeball`  ||  100% droprate  |  3-6 balls
- `Greatball`  ||  75% droprate  |  1-4 balls
- `Ultraball`  ||  35% droprate  |  1-2 balls
- `Masterball`  ||  0.5% droprate  |  1 balls
- `Repel`  ||  12% droprate  |  1 ea
- `Grazz`  ||  12% droprate  |  1 ea
- `Egg`  ||  9% droprate  |  1 ea
- `Quest Reset Scroll`  ||  8% droprate  |  1 ea
- `Rare Candy`  ||  1% droprate  |  1 ea

> <a:fidough_wow:1283739703140679703>  ***FidNotes:** Quantity and drop rates are per 1 lootbox. We can open 100 lootbox at a time with  `;lb all`. Legendary Patreon perk boost drop rates +10%.*"""

    cat = f"""# CATCHBOT
Catchbot is a unique feature in Pokemeow that automatically catches a (potentially very large) number of Pokemon in your absence. It needs to be upgraded to reach it’s full potential, but can eventually run a profit even just selling the duplicates it catches back to the game. If you want a full Pokedex, Catchbot will be much faster than good ol’  `;pokemon`.

***IMPORTANT!***
- DO NOT run this bot before you have made Cost lvl6
- Upgrade priority: Cost - Pokémon - Duration
- Luck Upgrade is not a priority
- Upgrade Luck only if you have 25M coins to burn

# CATCHBOT UPGRADE GUIDE
- Command: `;cb upgrade <cost/pokemon/duration/luck>`
***UPGRADE SUGGESTION***
- Cost L6, Pokémon L5, Duration L3
- Cost L9, Pokémon L7, Duration L5
- Cost Max, Pokémon Max, Duration Max

# CATCHBOT CHART
> - LVL0 ||  `1 Mon/hr`  |  `500 Coin/Mon`  |  `for 1hr`
> - LVL1 ||  `4 Mon/hr`  |  `460 Coin/Mon`  |  `for 2hrs`
> - LVL2 ||  `7 Mon/hr`  |  `420 Coin/Mon`  |  `3 hrs`
> - LVL3 ||  `10 Mon/hr`  |  `380 Coin/Mon`  |  `for 4 hrs`
> - LVL4 ||  `13 Mon/hr`  |  `340 Coin/Mon`  |  `for 5 hrs`
> - LVL5 ||  `16 Mon/hr`  |  `300 Coin/Mon`  |  `for 6 hrs`
> - LVL6 ||  `19 Mon/hr`  |  `260 Coin/Mon`  |  `for 7 hrs`
> - LVL7 ||  `22 Mon/hr`  |  `220 Coin/Mon`  |  `for 8 hrs`
> - LVL8 ||  `25 Mon/hr`  |  `180 Coin/Mon`  |  `for 9 hrs`
> - LVL9 ||  `28 Mon/hr`  |  `140 Coin/Mon`  |  `for 10 hrs`
> - LVL10 ||  `31 Mon/hr`  |  `100 Coin/Mon`  |  `for 11 hrs`
> - LVL11 ||  `-NA- Mon/hr`  |  `-NA- Coin/Mon`  |  `for 12 hrs`

> <a:fidough_wow:1283739703140679703> ***FidNotes:** Note that Catchbot catches Pokemon but does not improve streaks, earn Coins, EXP, count for Hunts or Quests, or anything else. You only get the Pokemon. Also, upgrading Luck is not really worth burning 25M coins for. The only benefit we get is a CHANCE to get  <:Golden11:1147776276510281818>  Golden Aron from catchbot.*"""

    cos = f"""# COMMAND SHORTCUT
Use command shortcuts.
They are very useful!

Examples of these are:
- `;p`  instead of  `;pokemon`
- `;d`  instead of  `;pokedex`
- `;s`  instead of  `;shop`
- `;s b`  instead of  `;shop buy`
- `;m` instead of  `;market`
- `;q r` instead of `;quest reset`
- `;res exc` instead of `;research exchange`

You can also use shortcuts for items:
- `;egg use si all`  instead of  `;egg use super_incubator all`
- `;t take mb mewtwo`  instead of  `;team take masterball mewtwo`

To call Pokemons, you can use their number tag instead of their full Pokemon name:
- `;d 150`  instead of  `;pokedex mewtwo`
- `;d 1150`  instead of  `;pokedex shiny mewtwo`
- `;d 9150`  instead of  `;pokedex golden mewtwo`
- `;d 7109`  instead of  `;pokedex mega-mewtwo-x`

You get the idea! They are very convenient, take less time, and are very easy to remember."""

    cur = f"""# CURRENCY

# POKECOINS
- PokeMeow's main currency.
- Can be spent to buy Balls, Swaps, Shop Items, Upgrades, Clan Perks, etc.
- You can also buy and trade Pokémons with other players with PokeCoins.
> ***HOW TO GET:***
> - Catch Pokémons with `;p`
> - Battling NPC with `;b npc`
> - Selling Pokémons on the market `;m`
> - Winning the lottery `;lot`
> - Releasing Pokémons `;r d`
> - Opening Lootboxes `;lb all`
> - Opening Boxes `;op rb all` `;op srb all` `;op lb all` `;op sb all`
> - Completing Quest `;q`
> - Doing your `;daily`
> - Voting Streaks `;v`
> - Patreon
> - Catching Pokémons with `;explore`

# FISH TOKENS
- Can be spent in `;fish shop` to buy items like Diveball, Poke Lure, Misty Lure, better Fishing Rods, etc.
> ***HOW TO GET:***
> - Catch Pokémons with `;f`
> - Completing Fishing Quest `;q`

# PATREON TOKENS
- Can be spent in `;pat shop` to buy Beastball, Super Incubator, bid on Pokémon in `;auction`, etc.
> ***HOW TO GET:***
> - Subscribe to PokeMeow's Patreon Membership
> - Buy or Trade with other players

# VOTE COINS
- Can be spent in `;vote shop` to buy Shiny Charms, Reroll IVs `;bud reroll ivs (stat)`, etc.
> ***HOW TO GET:***
> - You can only get Vote Coins by voting daily. You can vote as many as twice a day `;v`

# SWAP TOKENS
- Swaps a designated Pokémon for another random Pokémon for free using this currency.
> ***HOW TO GET:***
> - Doing your daily `;sw`
> - Completing Quest `;q`

# RESEARCH POINTS
- Can be spent in `;res shop` to buy research related items.
> ***HOW TO GET:***
> - Exchanging Relics, Valuables, and Fossils `;res exc (item) (amount)`

# FACTION POINTS
- Can be spent in `;fa shop` to buy faction related items.
> ***HOW TO GET:***
> - Battling NPCs. Bonus points for defeating opposing Faction NPCs
> - Catching target Pokémon with the correct ball
> - Defeating World Bosses
> - Voting
> - Catch Pokémons with `;p`"""

    dai = f"""# DAILIES
- Checklist  `;cl`  to view your available dailies.
- Daily  `;daily`  to get daily rewards
- Vote  `;v`  to get vote coins - click vote after the timer
- Quest  `;q`  to get new quest for rewards
- Catchbot  `;cb`  to retrieve your catchbot
- Catchbot  `;cb run`  to deploy your catchbot
- Swap  `;sw`  to get swap tickets
- Hunt  `;h`  to get hunt target for rewards
- Lottery  `;lot buy 1`  to buy 1 lottery ticket
- Event Checklist  `;e cl` to check your event progress"""

    fid = f"""# FIDCOINS <:fidCoins:1307109003305680896>

- **WAYS TO EARN FIDCOINS**
> - We can start earning FidCoins  <:fidCoins:1307109003305680896>  by visiting Fidough's  <#1307120351314051182>.
> - We can also play in  <#1298468564855947296>.

- **GUARANTEED FIDCOINS**
> - Use  `!daily`  command to earn FidCoins once a day.
> - Use  `!work`  command to earn FidCoins every hour.

- **RNG FIDCOINS**
> - You can play games with your FidCoins to win more FidCoins! Be warned that you can also lose FidCoins this way. All games has a 1 hour cooldown. You can bet between 1-500 FidCoins.
> - Use  `!rps <amount>`  to play Rock, Paper, Scissors.
> - Use  `!roulette <amount>`  to play Russian Roulette.
> - Use  `!guess <amount>`  to guess the number between 1 and 100.
> - Use  `!dice <amount>`  to throw two dice.

- **OTHER WAYS TO EARN**
> - `!Pray`  at the  <#1060853563221364736>  every 2 hours.
> - Server Events & <#1297214502458232933>.
> - There are more ways to earn but you will have have to explore the server features and discover the rest!

- **EXTRA COMMANDS**
> - Also works in <#1054016462295158805>
> - `!richest`  |  *Shows the richest players leaderboard.*
> - `!coins`  |  *Shows how much FidCoin anyone has.*
> - `!coins <member>`  |  *Shows how much FidCoin a specific member has.*
> - `!economy-info`  |  *Everything you need to know about the economy of the server.*
> - `!games`  |  *Shows info about this server's games.*
> - `!shop`  |  *List items from the shop.*
> - `!shop <item>`  |  *Shows the items description from the shop.*
> - `!buy <item>`  |  *Buy any item from the shop.*
> - `!use <item>`  |  *Use an item from your inventory.*
> - `!items`  |  *List the items you bought from the shop.*
> - `!give-item`  | *Give an item from your inventory to a member.*
> - `!checklist` or `!cl`  | *Displays your command checklist.*
> - `!buffs`  | *Displays your current activated boosts.*
> - `!reminders`  |  *Displays your game command reminder settings.*"""

    fis = f"""# FISHING
**COMMAND:**  `;f`  or  `;fish`

To get started on fishing, you have to get an  `Old Rod`  drop from `;p`. It has a 1/1000 chance of dropping. You cannot fish or buy anything in the fishing shop without getting a Rod first.

Fishing is basically entirely worse than normal catching, except it’s the only way to get **Fish Tokens**.

# FISHING RODS
- **OLD ROD**
>  - Obtain: 1/1000 drop rate from  `;p`.*
>  - Base spawn rate: 50%
>  - Shiny rate: 1/16,385

- **GOOD ROD**
>  - 1,000 Fishing Tokens in Fish Shop
>  - Base spawn rate: 70%
>  - Shiny rate: 1/8,192

- **SUPER ROD**
>  - Obtain: 2,500 Fishing Tokens in the Fish Shop
>  - Base spawn rate: 85%
>  - Shiny rate: 1/4096

- **GOLDEN ROD**
>  - Obtain: 100 Vote Coins in the Fish Shop. Must have both  `Good Rod`  &  `Super Rod`  to unlock.
>  - Base spawn rate: 85%
>  - Shiny rate: 1/4096
>  - Golden rate: 2x

# WATER STATE
**COMMAND:**  `/water-state`

You can also check the current waterstate in <#1050376063965991012>.

**<@&1232861519012958300>**
> *There seems to be a hint of gold in the water...*
> *Catch Rate +10%  |  1 Hour/Day*
- **GOLDEN EXCLUSIVE**
> `Golden Poliwag`  `Golden Tentacool`  `Golden Wailmer`  `Golden Kyogre`
- **SHINY EXCLUSIVE**
> `Shiny Magikarp`  `Shiny Freebas`
- **PATREON EXCLUSIVE**
> `Shiny Relicanth`  `Shiny Clauncher`

**<@&1209352148467454023>**
> *The waters are calm...*
> *Catch Rate +5%  |  8 Hours/Day*
- **SHINY EXCLUSIVE**
> `Shiny Horsea`  `Shiny Tentacool`  `Shiny Goldeen`  `Shiny Finneon`
- **PATREON EXCLUSIVE**
> `Shiny Clauncher`

**Moderate Waters**
> *The current is moderate.*
> *Catch Rate -5%  |  5 Hours/Day*
- **SHINY EXCLUSIVE**
> `Shiny Poliwag`  `Shiny Krabby`

**Strong Waters**
> *The current is strong!*
> *Catch Rate -7%  |  5 Hours/Day*
- **SHINY EXCLUSIVE**
> `Shiny Clamperl`  `Shiny Shellder`

**Intense Waters**
> *The ocean's waves are intense!*
> *Catch Rate -10%  |  5 Hours/Day*
- **SHINY EXCLUSIVE**
> `Shiny Wailmer`  `Shiny Carvanha`"""

    loc = f"""# LOCKS
It is highly recommended to lock important and/or exclusive Pokemon by using the commands:

- `;R LOCK MEGA-LINE`
> *Mega-lines are always in demand since those Pokémons need to be sacrificed before one can attempt a chamber. Each mega chamber has 3 battles, lose once and you have to release the same Pokémons again.*

- `;R LOCK EGG`
> *For example, **Gible** is an uncommon. If you release **Gible**, you will only get 300 coins. But if you sold or trade **Gible** in the market, you can get around 22k coins more!*

- `;R LOCK FOSSIL`
> *Fossils are used with  `;swap`  for a CHANCE to obtain a Shiny.*

- `;R LOCK <pokemon>`
> *Players can also lock their favorite Pokemon with this command.*

> <a:fidough_wow:1283739703140679703> ***FidNotes:** Ohhh we mostly lock Pokémons because they sell more in the market/trade.*"""

    lvl = f"""# SERVER LEVELS
This system rewards members who are consistently active in the server by awarding them XP (experience points) for every message they send. As they accumulate more XP, they level up and unlock new perks and rewards.

**[LVL]**  |  **[XP REQ]**
- 0        0
- 1        100
- 2        255
- 3        475
- 4        770
- 5        1,150
> <@&1048443981824004136>  |  <:fidCoins:1307109003305680896> 500

- 6        1,625
- 7        2,205
- 8        2,900
- 9        3,720
- 10        4,675
> <@&1159887619208003676>  |  <:fidCoins:1307109003305680896>  1,000

- 1 1        5,775
- 12        7,030
- 13        8,450
- 14        10,045
- 15        11,825
> <@&1159890032908324944>  |  <:fidCoins:1307109003305680896>  2,000

- 16        13,800
- 17        15,980
- 18        18,375
- 19        20,995
- 20        23,850
> <@&1159893129730736199>  |  <:fidCoins:1307109003305680896>  4,000

- 21        26,950
- 22        30,305
- 23        33,925
- 24        37,820
- 25        42,000
> <@&1159894833847074967>  |  <:fidCoins:1307109003305680896>  8,000

- 26        46,475
- 27        51,255
- 28        56,350
- 29        61,770
- 30        67,525
> <@&1159970100984688680>  |  <:fidCoins:1307109003305680896> 16,000

- 31        73,625
- 32        80,080
- 33        86,900
- 34        94,095
- 35        101,675
> <@&1159896202314252378>  |  <:fidCoins:1307109003305680896>  40,000

- 36        109,650
- 37        118,030
- 38        126,825
- 39        136,045
- 40        145,700
> <@&1159970623892758648>  |  <:fidCoins:1307109003305680896>  90,000

- 41        155,800
- 42        166,355
- 43        177,375
- 44        188,870
- 45        200,850
- 46        213,325
- 47        226,305
- 48        239,800
- 49        253,820
- 50        268,375
> <@&1159971737576951869>  |  <:fidCoins:1307109003305680896>  200,000

To level up quickly, just continue to participate in the server and send messages or hangout in voice channels. Members can gain between 15-25 XP for one message every minute, so spamming will not help you level up any faster. Discord ranks will reset every 6 months. Level bonuses are accumulative   <:fidCoins:1307109003305680896>  361,500 FC total."""

    pok = f"""# POKEBALLS
Maintain 50+ Pokeball and 1x Masterball available for use at all times.
- You can buy Pokeballs with `;s b 1 <amount>`
- You can check how many you have with `;i` inventory command.

**BALL INFO**
- Pokeball  |  <:PokeCoin:1166253401546436648>  200 PokeCoins  |  10% Base Catch Chance
- Greatball  |  <:PokeCoin:1166253401546436648>  500 PokeCoins  |  25% Base Catch Chance
- Ultraball  |  <:PokeCoin:1166253401546436648>  1500 PokeCoins  |  35% Base Catch Chance
- Premierball  |  <:PokeCoin:1166253401546436648>  10000 PokeCoins  |  50% Base Catch Chance
- Masterball  |  <:PokeCoin:1166253401546436648>  100000 PokeCoins  |  100% Base Catch Chance
- Diveball  |  🎣  50 Fish Coins  |  85% Base Catch Chance
- Beastball  |  <:patreon_token:1296818113735819405>  5 Patreon Tokens  |  0% Base Catch Chance

**POKEBALLS vs POKEMON RARITY**
- Use Pokeball for <:Common:1186968566063435786> Common and <:Uncommon:1186968571839000606> Uncommon
- Use Greatball for <:Rare:1142668430634393610> Rare
- Use Ultraball for <:SuperRare:1133025503067000852> Super Rare
- Use Premier Ball for <:Shiny:1090640278999810079> Full Odds Shiny w/o held item.
- Use Masterball for <:Legendary:1090640224125718570> Legendary & <:Shiny:1090640278999810079> Shiny

> <a:fidough_wow:1283739703140679703> ***FidNotes:** When you achieve a stable  <:PokeCoin:1166253401546436648>  PokeCoin source, you can use Greatballs for <:Common:1186968566063435786> Common and <:Uncommon:1186968571839000606> Uncommon instead for better catch streak. More catch streak = more lootbox!*"""

    res = f"""# RESEARCH

- **HOW TO OBTAIN VALUABLES?**
> - Valuables:  `Nugget`  |  `Big Nugget`  |  `Pearl`  |  `Big Pearl`  |  `Star Piece`  |  `Comet Shard`
> - All valuables with the exception of  `Big Nugget`  &  `Big Pearl`  can be randomly obtained from catching  `;p`  with a ***held item*** icon. Exchange rates for valuables can be found in  `;research`.

- **HOW TO EXCHANGE VALUABLES?**
> -  `;research exchange  <item>  <pc/item>  <amount>`
> - Example:  `;res ex nugget pc 3`  |  `;res ex pearl big_pearl`

- **HOW TO OBTAIN RELIC PIECES?**
> - Relics:  `Relic_Crown`  |  `Relic_Statue`  |  `Relic_Band`  |  `Relic_Vase`
> - Relic pieces can be randomly obtained with  `;p`  with a ***held item*** icon. One of each relic piece may be obtained until all of them are exchanged. After which, you must wait one week to obtain & exchange relic pieces again.

- **WHY EXCHANGE THE RELICS?**
> - Aside from the rewards mentioned in  `;research`, you unlock the ability to find the item  `!KingsRock` from  `;p`.

- **WHERE TO FIND FOSSILS?**
> - After unlocking them from  `;research`, fossils can be randomly obtained from a Pokemon with a ***held item*** icon from  `;p`.
> - You cannot hold multiples of the same fossil. You must exchange the fossil to obtain another.

- **WHAT DO I GET FROM EXCHANGING FOSSILS?**
> - Research points between 15-30.
> - Random number of attempts (between 10-35) to obtain a  <:Shiny:1090640278999810079>  Fossil Pokemon from  `;swap` using the regular version of the Fossil Pokemon.
> - New Fossils are added to the Research Lab occasionally!"""

    swa = f"""# SWAP
Swapping is basically Wonder Trade. You give up a Pokemon to get a random Pokemon back. You need to `;sw` or `;swap` once a day to get `Swap Tickets`, otherwise it cost 5000 PokeCoins each (50% less if you sub Patreon). What Pokemon you swap in does not appear to matter, so use `;box` to find common Pokemons you have extra duplicates of to swap.

You can raise your multiplier for  <:Golden11:1147776276510281818>  Golden or  <:Shiny:1090640278999810079>  Shiny swap odds by 1% every 20 trades per day, up to 10% higher odds. The multiplier resets at end of day even if you didn’t trade 20 Pokemons. Because of this, it’s theoretically best to save up over 200 Swap tickets (with `;quests`, you get several per day) to swap a ton in a day.

**COMMANDS:**
- `;sw`  or  `;swap`
> *Claim daily Swap Tickets. It also used to check your current multiplier.*
- `;sw <pokemon>`
> *Swaps a single Pokemon for a different random Pokemon. Rarity does not seem to matter,  <:Common:1186968566063435786>  can get <:Uncommon:1186968571839000606><:Rare:1142668430634393610><:SuperRare:1133025503067000852>  Pokemon in return.*
- `;sw <shiny/golden> <pokemon>`
> *Swaps a  <:Shiny:1090640278999810079>  or  <:Golden11:1147776276510281818>  Pokemon for a totally random Rarity Pokemon just like normal swap.*

# SWAP EXCLUSIVES
<:Shiny:1090640278999810079>  **SHINY SWAP EXCLUSIVE:**
`Shiny Oddish #1043`  `Shiny Gastly #1092`  `Shiny Shelmet #1616`  `Shiny Tyrogue #1236`  `Shiny Larvitar #1246`  `Shiny Ralts #1280`  `Shiny Snorunt #1361`  `Shiny Beldum #1374`  `Shiny Bronzor #1436`

<:patreon_token:1296818113735819405>  **PATREON SWAP EXCLUSIVE:**
`Shiny Scraggy #1559`  `Shiny Pancham #1674`

<:Golden11:1147776276510281818>  **GOLDEN SWAP EXCLUSIVE**
`Golden Goomy #9704`"""

    tra = f"""# TRADING
**COMMANDS:**
- `;GIVE <@user> <amount>`
***EXAMPLE:***
- `;give @user 1M
> *Give @user 1M PokeCoins.*

# SINGLE TRADE COMMANDS
- `;TR <@user> <your mon> <their mon>`
> *Used for direct trades. Only use if you trust the other person you are trading with.*

***EXAMPLES:***
- `;TR @user wooper mewtwo`  or  `;TR @user 194 150`
> *You trading your `Wooper #194` to the @User's `Mewtwo #150`*
- `;TR @user shinymewtwo mega-charizard-x`
> *You trading your `Shiny Mewtwo` to the @User's `Mega Charizard X`*
- `;TR @user mewtwo shinymega-garchomp`
> *You trading your `Mewtwo` to the @User's `Shiny Mega Garchomp`*

# MULTI TRADE COMMANDS
# STEP 1:
- `;TR <@user> -M`
> *Command to initiate Multi-Trade.*

# STEP 2:
**ADD SINGLE-MULTI POKEMON**
- `-P ADD <pokemon> <amount>`
> *Used for trading multiple amounts of a mon.*
***EXAMPLES:***
- `-P ADD jirachi 3` or `-P ADD 385 3`
> *You are adding 3ea `Jirachi` in the trade.*
- `-P ADD jirachi all` or `-P ADD 385 all`
> *You are adding all `Jirachi` you own in the trade.*

-or-

**ADD MULTI-SINGLE POKEMON**
- `-P MULTI_ADD <dex1> <dex2> <dex3>`
> *You can add up to 10 mons.*
***EXAMPLE:***
- `-P MULTI_ADD 43 67 28`
> *You are adding `1ea Oddish #43`  `1ea Machoke #67`  `1ea Sandslash #28` in the trade.*

-or-

**ADD POKECOINS**
- `-COIN ADD <amount>`
***EXAMPLE:***
- `-coin add 50000`
> *Add 50K PokeCoins in the trade.*

-or-

**ADD PATREON TOKENS**
- `-TOKENS ADD <amount>`
***EXAMPLE:***
- `-tokens add 500`
> *Add 500 Patreon Tokens in the trade.*

> <a:fidough_wow:1283739703140679703> ***FidNotes:** Both parties must click ACCEPT to finish the trade. You only have 2 minutes to finish multi-trade before it expires.*"""


class SD_UBG_IMAGES:
    captcha1 = "https://media.discordapp.net/attachments/1358029599463968798/1405116591036960881/image.png?ex=689da84d&is=689c56cd&hm=37b0c2ff7b547310780b648aa2457032e558286a9845b0ae4e564a3a8f1b018e&=&format=webp&quality=lossless&width=1088&height=639"
    captcha2 = "https://media.discordapp.net/attachments/1358029599463968798/1405111951130099753/20200626_140157-1.png?ex=689da3fa&is=689c527a&hm=b4f64d036773f3d0d26817386e790ad6cf165b17344715552f742a55d2b1ecf6&=&format=webp&quality=lossless"

class SD_MH:
    lo = f"""# MEOWHELPER: LOOKUP

- **`/LOOKUP WEAKNESS`**
> *Displays a Pokemon's weakness chart by name or pokedex number.*
- **`/LOOKUP POKEMON`**
> *Find a Pokemon by name or pokedex number. It also shows its recent market value.*"""

    mi = f"""# MEOWHELPER: MISC

**HUNTS**
- **`/HUNTS CREATE`**
> *Creates a new hunt.*
- **`/HUNTS END`**
> *Ends a hunt.*

**SWAP TRACKER**
- **`/SWAPTRACKER START`**
> *Creates a new swap tracker.*
- **`/SWAPTRACKER END`**
> *Ends a swap tracker.*

**MISC**
- **`/STATISTICS VIEW`**
> *Displays your statistics by category and type.*
- **`/EVENT PROMO VIEW`**
> *View your promo events.*"""

    pi = f"""# MEOWHELPER: PINGS
**COMMAND:**  `/TOGGLE PINGS`

- **TIMER PING**
> *Pings whenever one of your Pokemeow commands is ready to be used again.*
- **RARE PING**
> *Pings whenever you encounter a rare Pokemon.*
- **RARE PING SPAM**
> *Spam ping whenever you encounter a rare Pokemon.*
- **HELD ITEM PING**
> *Pings whenever you encounter a Pokemon holding an item.*
- **PERSONAL GOAL PING**
> *Pings whenever you finish a personal goal.*
- **PERSONAL HUNT PING**
> *Pings whenever you finish a personal hunt or encounter a Pokemon on your personal hunt list.*
- **CLAN HUNT PING**
> *Pings whenever you finish a clan hunt or encounter a Pokemon on your clan hunt list.*
- **FACTION HUNT PING**
> *Pings whenever you encounter a Pokemon on your faction hunt list.*
- **QUEST ALERT**
> *Pings whenever you have a new quest ready.*
- **CATCHBOT ALERT**
> *Pings when your catchbot has returned.*
- **ALERT MODE**
> *Choose between Private Message, Channel, or Off. Choose whether you want your Catchbot/Quest Alert to be sent via Private Message/Channel or just turned off.*"""

    ti = f"""# MEOWHELPER: TIMERS
**COMMAND:**  `/TOGGLE TIMERS`

- **REACT MODE**
> *Meowhelper will react with a checkmark on messages instead of sending a message whenever your command is ready. React Mode is not available for fish and battle timers.*
- **QUIET MODE**
> *When turned off, user will see Meowhelper counting the seconds until the next command is ready.*
- **PING MODE**
> *Pings whenever the user's next command is ready.*

> <a:fidough_wow:1283739703140679703> ***FidNotes:**  When doing Battle Tower or Mega Chamber, its better to turn-off your battle timer in  `/toggle timers`  to avoid accidentally pressing the  `Forfeit`  button.*"""

    ut = f"""# MEOWHELPER: UTILITIES
**COMMAND:**  `/TOGGLE UTILITIES`

- **FISH RARITY**
> *Shows the fish rarity whenever you fish.*
- **FISH EMBED**
> *Shows the fish rarity in a embed message whenever you fish.*
- **RECOMMENDED BALL**
> *Get a recommended ball whenever you encounter a rare spawn.*
- **RARE SPAWN PRIVACY**
> *Show or hide your name in your server's rare spawn channel.*
- **RARE SPAWN VALUE**
> *Shows the latest market value of a rare spawn whenever you encounter one.*
- **WEAKNESS MODE**
> *Full, Medium, Truncated, or Off. Shows weakness chart of an enemy team in different modes.*
>  - **FULL:**  *shows all the full details of an enemy's weakness (4x, 2x, 1x, 0x).*
>  - **MEDIUM:**  *only shows 4x, 2x, and 1x type effectiveness against an enemy.*
>  - **TRUNCATED:**  *only shows 4x, and 2x type effectiveness against an enemy.*
>  - **OFF:**  *disable the weakness chart.*

> <a:fidough_wow:1283739703140679703> ***FidNotes:**  It is better to turn-off your fish embeds in  `/toggle utilities`  and turn-on  `react mode`  in  `/toggle timers`  so your message won't be pushed up too much by Meowhelper when fishing.*"""
    go = f"""# MEOWHELPER: GOAL

- **`/GOAL VIEW`**
> *View a personal or clan goals.*
- **`/GOAL CREATE`**
> *Create a new personal or clan goal.*
- **`/GOAL RESET`**
> *Reset the catch progress of a personal or clan goal.*
- **`/GOAL DELETE`**
> *Delete a personal or clan goal by name.*
- **`/GOAL UPDATE`**
> *Update a personal or clan goal by name.*"""

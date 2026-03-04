from constants.aesthetic import Emojis
class TCG_EMOJIS:
    info = Emojis.info
    items = "📦"
    commands = "⚙️"
    quality_conditions = "🎴"
    trading = "🤝"
    market = "🛒"


class TCG_DESC:
    info = f"""# TCG OVERVIEW

- **What is Pokemeow TCG?**
> - *A feature inspired by the Pokémon TCG where players collect, trade, and buy cards, packs, and boxes (no battle system yet).*

- **How can I obtain TCG cards?**
> - *Buy from the `;tcg shop`.*
> - *Earn 1 free pack every 3 `;votes`.*
> - *Participate in [TCG Giveaways](https://discord.com/channels/664509279251726363/1394128056624611478).*
> - *Patreon rewards via `;daily`:*
>   - *<:Shiny:1090640278999810079> Shiny Patreons: 1 free pack*
>   - *<:Golden11:1147776276510281818> Golden Patreons: 5 free packs*

- **Card & Pack Conditions**
> - *Cards start at **Near Mint** (5 → Damaged 1).*
> - *Packs/Boxes start at **Perfect** (5 → Poor 1).*
> - *Condition/quality drops every 3 months if unprotected.*

- **Protection Options**
> - *Use <:acrylic_box_case:1478547550742122632> Acrylic Box Cases, <:acrylic_box_case:1478547550742122632> Pack Sleeves, or <:toploader:1478547546992410747> Toploaders.*
> - *Commands: `;tcg protect <item-id>` or `;tcg protect all_<itemtype>`.*
> - *Auto-protect toggle available (`;tcg toggle auto-protect`).*

- **Special Features**
> - *Each set rotation (e.g., EX Ruby & Sapphire) has unique challenges for PROMO rewards.*
> - *Settings when opening packs: auto-skip to Rare (🔨), show full contents (📦).*"""

    commands = f"""# TCG Commands

- ** /tcg home | ;tcg**
> - *Shows general TCG info, current set rotation, and menus (binder, inventory, shop, info).*

- ** /tcg shop | ;tcg shop**
> - *Displays the shop with booster boxes, packs, and protection items. Buy with coins or Patreon tokens.*

- ** /tcg binder [set] | ;tcg binder**
> - *Shows your card collection, including serial numbers, condition, and protection status.*

- ** /tcg inventory | ;tcg inv**
> - *Lists all boxes and packs you own with quality and protection details.*

- ** /tcg help [topic] | ;tcg help [topic]**
> - *Provides help menus for trade, market, accessories, challenges, or toggles.*

- ** /tcg carddex [set] | ;tcg carddex [set]**
> - *Shows your card dex with navigation and sorting options.*

- ** /tcg lookup <item> | ;tcg lookup <item>**
> - *Looks up cards or items by name/ID, showing rarity, owner, circulation, and condition.*

- ** /tcg toggle <setting> | ;tcg toggle <setting>**
> - *Toggles settings like auto-protect for new items.*

- ** /tcg buy <item> <amount> | ;tcg buy <item> <amount>**
> - *Buys items from the shop using Pokecoins.*

- ** /tcg buy-using-tokens <item> <amount> | ;tcg bt <item> <amount>**
> - *Buys items from the shop using Patreon tokens.*

- ** /tcg open <item> | ;tcg op <item>**
> - *Opens a box or pack to reveal its contents.*

- ** /tcg challenges | ;tcg ch**
> - *Shows set challenges and available promo cards.*

- ** /tcg trade <@user> | ;tcg tr <@user>**
> - *Starts a trade with another user (slash command disabled, semicolon only).*

- ** /tcg gift <@user> <items> | ;tcg gift <@user> <items>**
> - *Gifts up to 20 items to another player.*

- ** /tcg giveaways | ;tcg giveaways**
> - *Shows info on official server giveaways.*

- ** /tcg giveaway | ;tcg giveaway**
> - *Starts or views giveaway events.*

- ** /tcg market <history|recent> | ;tcg market / ;tc m**
> - *Shows market listings, history, or recent trades.*

- ** /tcg market history:view <item> | ;tcg market history:view <item> / ;tc mview <item>**
> - *Views market history for a specific item.*

- ** /tcg mbuy <item> | ;tcg mbuy <item>**
> - *Buys items listed on the market.*

- ** /tcg mlist <item> <price> | ;tcg mlist <item> <price>**
> - *Lists your item for sale on the market.*

- ** /tcg market history:offers | ;tcg moffers**
> - *Shows offers made in the market.*

- ** /tcg mrem <item> | ;tcg mrem <item>**
> - *Removes your item from the market.*

- ** /tcg protect <item> | ;tcg prot <item>**
> - *Protects cards, packs, or boxes from condition loss.*

- ** /tcg protect-other <item> | ;tcg protect-other <item>**
> - *Protects another user’s items.*

- ** /tcg unprotect <item> | ;tcg unprot <item>**
> - *Removes protection from an item.*

- ** /tcg server <server ID> | ;tcg server**
> - *Shows server-specific TCG info.*

- ** /tcg highscores | ;tcg hs / ;tcg highscores**
> - *Displays TCG highscores.*

- ** /tcg stats | ;tcg stat**
> - *Shows your TCG stats.*"""

    items = f"""# TCG Items

- <:acrylic_box_case:1478547550742122632> **Acrylic Box Case**
> - *Protects booster boxes from quality deterioration.*
> - *Use `;tcg protect <box-id>` or toggle auto-protect.*
> - *Cost: <:pokecoin:1477168709305892874> 100,000 (`;tc buy abc`).*

- <:pack_sleeve:1478547548972126499> **Pack Sleeve**
> - *Protects booster packs from quality deterioration.*
> - *Auto-applied to packs from voting/daily rewards.*
> - *Cost: <:pokecoin:1477168709305892874> 10,000 (`;tc buy pack_sleeve`).*

- <:toploader:1478547546992410747> **Toploader**
> - *Protects cards from condition deterioration.*
> - *Use `;tcg protect <card-id>` or toggle auto-protect.*
> - *Cost: <:pokecoin:1477168709305892874> 1,000 (`;tc buy toploader`).*

- <:booster_box:1478547544803115171> **Booster Box**
> - *Contains 36 booster packs of a specific set.*
> - *Card contents vary depending on the set.*
> - *Cost: <:pokecoin:1477168709305892874> 15,000,000 (`;tc buy <set>-box`) or <:patreon_token:1477168705338081340> 1,250 (`;tc bt <set>-box`).*

- <:booster_card:1478547542974140557> **Booster Pack**
> - *Contains random cards (varies by set).*
> - *Guarantees 1 Energy card and 1 Rare card.*
> - *Cost: <:pokecoin:1477168709305892874> 500,000 (`;tc buy <set>-pack`) or <:patreon_token:1477168705338081340> 35 (`;tc bt <set>-pack`).*
> - *Other ways via of obtaining:*
>   - *Opening <:booster_box:1478547544803115171> Booster Boxes*
>   - *Voting (1 pack every 3 votes)*
>   - *<:Shiny:1348638393554178129> Shiny Patreons: 1 free pack from `;daily`*
>   - *<:Golden11:1147776276510281818> Golden Patreons: 5 free packs `;daily`*"""

    quality_conditions = f"""# TCG Qualities & Conditions

- **Card Conditions**
> - *Cards start at **Near Mint** (5).*
> - *Levels:*
>   - 🟩 5 = Near Mint
>   - 🟨 4 = Lightly Played
>   - 🟡 3 = Moderately Played
>   - 🟠 2 = Heavily Played
>   - 🔴 1 = Damaged
> - *Condition decreases by 1 level every 3 months if unprotected.*

- **Box/Pack Quality**
> - *Boxes and packs start at **Perfect** (5).*
> - *Levels:*
>   - 🔷 5 = Perfect
>   - 🟢 4 = Excellent
>   - 🟡 3 = Good
>   - 🟠 2 = Fair
>   - 🔴 1 = Poor
> - *Quality decreases by 1 level every 3 months if unprotected.*

- **Protection Methods**
> - *Use <:acrylic_box_case:1478547550742122632> Acrylic Box Cases, <:pack_sleeve:1478547548972126499> Pack Sleeves, or <:toploader:1478547546992410747> Toploaders to prevent deterioration.*
> - *Commands: `;tcg protect <item-id>` or `;tcg protect all_<itemtype>`.*"""

    trading = f"""# TCG TRADING AND GIFTING

- **Starting a Trade**
> - *Use `!tcg trade @user` to begin a trade.*
> - *Receiver must accept to start.*
> - *Limit: 10 items per user per trade.*

- **Adding Items to a Trade**
> - *Command: `--offer/add <item-id> <# toks> <# coins>`.*
> - *Example: `--offer bs1-box-1 bs1-pack-31 100 toks 915000 coins`.*
> - *Max: 10 items per trade.*

- **Removing Items from a Trade**
> - *Command: `--remove <item-id> <# toks> <# coins>`.*
> - *Example: `--remove bs1-4-5 ju-9-1 100 toks`.*

- **Fast Trading**
> - *Command: `!tcg trade @user <your-items> for <their-items>`.*
> - *Example: `!tcg trade @user bs1-pack 3 4 5 100 toks for bs1-box 2 3`.*
> - *Can set up trade fully in one command.*

- **Gifting Items**
> - *Command: `!tcg gift @user <items>`.*
> - *Send up to 20 items with no return required.*
> - *Example: `!tcg gift user_id bs1-pack-1 bs1-box-1`.*
> - *Confirmation required before sending.*
> - *Receiver gets a DM, and gift history can be viewed with `!tcg gift`.*"""

    market = f"""# TCG Market

- **Overview**
> - *You can list all TCG items for <:pokecoin:1477168709305892874> PokeCoins or <:patreon_token:1477168705338081340> Patreon Tokens.*
> - *Sellers are automatically sent coins/tokens and notified via DM when items are bought.*
> - *Note: 5% fee on sales (waived for Patron+ supporters).*

- **View Recent Listings**
> - *Command: `;tcg market recent`.*
> - *Shows the 50 most recent listings.*
> - *Use `;tcg mview <item-id or name>` to view specific items.*

- **Buying Items**
> - *Command: `;tcg mbuy <item-id>`.*
> - *Buy up to 5 items at once.*
> - *Example: `;tcg mbuy bs1-box-1 ju-pack-2 bss-3-1`.*

- **Listing Items for Sale**
> - *Command: `;tcg mlist <item-id> <price>`.*
> - *List up to 5 items at once.*
> - *Example: `;tcg mlist bs1-box-1 100k ju-pack-2 350 tokens`.*

- **Check Listing Status**
> - *Command: `;tcg moffers`.*
> - *Shows the status of your current listings.*

- **Removing Items**
> - *Command: `;tcg mrem <item-id or all>`.*
> - *Remove up to 10 items at once.*
> - *Example: `;tcg mrem bs1-box-1 bs1-pack-5`.*
> - *Remove all: `;tcg mrem all`.*

- **Market History**
> - *Command: `;tcg m history`.*
> - *Shows your personal TCG market history.*"""

def get_faction_value(main_faction: str, category: str, variation: str = None):
    """
        Safely get a value from the FACTIONS dict.

    Parameters:
    - main_faction (str): The main faction key (e.g., "fl", "aq", "ga")
    - category (str): The category to get. Possible values:
        "color", "content", "thumbnail", "header_text", "footer_text",
        "header_icon", "footer_icon", "button_label", "desc"
    - variation (str, optional): The variation key if category is nested (e.g., "fl2", "ye3")

        Returns:
        - The value if found, else None

        Examples:
        >>> # Get main color
        >>> color_fl = get_faction_value(main_faction="fl", category="color")
        >>> print(color_fl)  # SD_FA_COLOR.fl

        >>> # Get a description variation
        >>> desc_ye2 = get_faction_value(main_faction="ye", category="desc", variation="ye2")
        >>> print(desc_ye2)  # SD_FA_DESC.ye2

        >>> # Get button label
        >>> button_pl3 = get_faction_value(main_faction="pl", category="button_label", variation="pl3")
        >>> print(button_pl3)  # "Leader"

        >>> # Try a non-existent variation safely
        >>> missing = get_faction_value(main_faction="sk", category="desc", variation="sk4")
        >>> print(missing)  # None
    """
    faction_data = FACTIONS.get(main_faction)
    if not faction_data:
        return None

    cat_data = faction_data.get(category)
    if cat_data is None:
        return None

    if variation:
        return cat_data.get(variation)

    return cat_data


def get_faction_value_dynamic(
    category: str, main_faction: str = None, variation: str = None
):
    """
    Fetch a faction value dynamically.
    If main_faction is None but variation is given, it will auto-detect main_faction.
    """
    # If no main_faction, infer from variation
    if main_faction is None and variation is not None:
        main_faction = variation.rstrip("0123456789")

    # If category is 'desc', use SD_FA_DESC; otherwise map category to class
    category_map = {
        "color": SD_FA_COLOR,
        "content": SD_FA_CONTENT,
        "thumbnail": SD_FA_THUMBNAIL,
        "header_text": SD_FA_HEADER_TEXT,
        "footer_text": SD_FA_FOOTER_TEXT,
        "header_icon": SD_FA_HEADER_ICON,
        "footer_icon": SD_FA_FOOTER_ICON,
        "button_label": SD_FA_BUTTON_LABEL,
        "button_emoji": SD_FA_BUTTON_EMOJIS,
        "desc": SD_FA_DESC,
    }

    cls = category_map.get(category)
    if cls is None:
        return None

    key_to_fetch = variation if variation is not None else main_faction
    return getattr(cls, key_to_fetch, None)


"""# ────────────── Usage ──────────────
desc_ye2 = get_faction_value_dynamic(category="desc", variation="ye2")
print(desc_ye2)  # SD_FA_DESC.ye2

desc_ye = get_faction_value_dynamic(category="desc", main_faction="ye")
print(desc_ye)  # SD_FA_DESC.ye"""


class SD_FA_COLOR:
    aq = 5951477

    fl = 16103770

    ga = 16250031

    ma = 16285827

    pl = 5951477

    sk = 16777215

    ye = 16285827

    ro = 16285827


class SD_FA_CONTENT:
    aq = "# FACTION: AQUA"

    fl = "# FACTION: FLARE"

    ga = "# FACTION: GALACTIC"

    ma = "# FACTION: MAGMA"

    pl = "# FACTION: PLASMA"

    sk = "# FACTION: SKULL"

    ye = "# FACTION: YELL"

    ro = "# FACTION: ROCKET"


class SD_FA_THUMBNAIL:
    aq = "https://media.discordapp.net/attachments/1383207791061241987/1383208505938284684/e4b02fcb66dec84f06f9837cdf06562e4ae9e272067634db29fecf027f13018a.png?ex=684df4ce&is=684ca34e&hm=8a6a659ce829b8fc4be758bb9cc259567475c8a94ec0fe11c48a0f5c0ceb20ef&=&format=webp&quality=lossless&width=90&height=91"

    fl = "https://media.discordapp.net/attachments/1383207791061241987/1383215968704139335/c2d3c4c89c85370f79faaac82cb3f5a1b4f5c4f2db1fde77233ff2eae46a759e.png?ex=684dfbc1&is=684caa41&hm=de77f98a565f630f1e3d678b26d695ba8080f02dbf59bf8e5fb241cd03280b10&=&format=webp&quality=lossless&width=90&height=106"

    ga = "https://media.discordapp.net/attachments/1383207791061241987/1383222644500860978/e089be0215e0182302fb0dd299031d941990f35fb3273628ab1460b9516054b7.png?ex=684e01f9&is=684cb079&hm=1887b966da6e734c90b30fe9bca2a8827aad2ab7a6a6431c52d23e28d5fe3248&=&format=webp&quality=lossless&width=90&height=144"

    ma = "https://media.discordapp.net/attachments/1383207791061241987/1383244480936808589/c320d92c958bf65fec96804850ed935e4ff2895506144f6906ef483981e75b14.png?ex=684e164f&is=684cc4cf&hm=a7c073c684a67b2164dec8c73f408d5649e157ffc485a400c190930e764a482f&=&format=webp&quality=lossless&width=90&height=69"

    pl = "https://media.discordapp.net/attachments/1383207791061241987/1383244874345611376/fa651738c8fb9e42204cf173fb1e1ec809b6242712b9c883e0ccb7544fa8ed3b.png?ex=684e16ad&is=684cc52d&hm=e5178ee92024cbe039e51345d704b10be9741882a48a96a9452ac438fd9ab1fc&=&format=webp&quality=lossless&width=90&height=107"

    sk = "https://media.discordapp.net/attachments/1383207791061241987/1383245567911526491/28ff3ea14f93f0a3adafe2f638d2477428655f8536ed9ec5e0eb6add416a6f3b.png?ex=684e1752&is=684cc5d2&hm=a6738899345cc41e3f706cc765d4cda4fd65188290aee1f4e2970716378ee8c9&=&format=webp&quality=lossless&width=90&height=90"

    ye = "https://media.discordapp.net/attachments/1383207791061241987/1383245806215237723/a12060802a643cbd0df2ec1e36fd97092791d9ce6edbef1ddb44492d42d51b4c.png?ex=684e178b&is=684cc60b&hm=2aa8a1aa46860fb04b18d6cdfcbe0009afb1aac3644306694203a248d7e1a248&=&format=webp&quality=lossless&width=90&height=90"

    ro = "https://media.discordapp.net/attachments/1383207791061241987/1383245318765674659/c661b79626ce127f7439f96ad16f290d802f9c36c5d4de39e0d04fb705e27173.png?ex=684e1717&is=684cc597&hm=9b9d0f08c54e85da191e2694257ff6d386eaf2813231331c62d8596de387d9d0&=&format=webp&quality=lossless&width=90&height=86"


class SD_FA_HEADER_TEXT:
    aq = "GRUNT MALE #807 & FEMALE #808"

    aq2 = "ADMIN MATT #809 & SHELLY #810"

    aq3 = "LEADER ARCHIE #811"

    fl = "GRUNT MALE #829 & FEMALE #830"

    fl2 = "ADMIN MALE #831 & FEMALE #832"

    fl3 = "LEADER LYSANDRE #833"

    ga = "GRUNT MALE #817 & FEMALE #818"

    ga2 = "ADMIN MARS #819 & CHARON #820"

    ga3 = "ADMIN JUPITER #821 & SATURN #822"

    ga4 = "LEADER CYRUS #823"

    ma = "GRUNT MALE #812 & FEMALE #813"

    ma2 = "ADMIN COURTNEY #814 & TABITHA #815"

    ma3 = "LEADER MAXIE #816"

    pl = "GRUNT MALE #824 & FEMALE #825"

    pl2 = "ADMIN SHADOW #826 & N #827"

    pl3 = "LEADER GHETSIS #828"

    sk = "GRUNT MALE #834 & FEMALE #835"

    sk2 = "ADMIN PLUMERIA #836"

    sk3 = "LEADER GUZMA #837"

    ye = "GRUNT MALE #838 & FEMALE #839"

    ye2 = "ADMIN MARNIE #840"

    ye3 = "LEADER PIERS #841"

    ro = "GRUNT MALE #800 & FEMALE #801"

    ro2 = "ADMIN ARIANA #802 & ARCHER #803"

    ro3 = "ADMIN PROTON #804 & PRETEL #805"

    ro4 = "LEADER GIOVANNI #806"


class SD_FA_FOOTER_TEXT:
    aq = "GRUNT FEMALE #808"

    aq2 = "ADMIN SHELLY #810"

    aq3 = None

    fl = "GRUNT FEMALE #830"

    fl2 = "ADMIN FEMALE #832"

    fl3 = None

    ga = "GRUNT FEMALE #818"

    ga2 = "ADMIN CHARON #820"

    ga3 = "ADMIN SATURN #822"

    ga4 = None

    ma = "GRUNT FEMALE #813"

    ma2 = "ADMIN TABITHA #815"

    ma3 = None

    pl = "GRUNT FEMALE #825"

    pl2 = "ADMIN N #827"

    pl3 = None

    sk = "GRUNT FEMALE #835"

    sk2 = "ADMIN FEMALE #832"

    sk3 = None

    ye = "GRUNT FEMALE #830"

    ye2 = "ADMIN FEMALE #832"

    ye3 = None

    ro = "GRUNT FEMALE #801"

    ro2 = "ADMIN ARCHER #803"

    ro3 = "ADMIN PRETEL #805"

    ro4 = None


class SD_FA_HEADER_ICON:
    aq = "https://media.discordapp.net/attachments/1383207791061241987/1383208091104972881/1286464731246362729.png?ex=684df46b&is=684ca2eb&hm=0e3599e0131c3b56760edee0289821305d85de5812351708427e9787e81fc21a&=&format=webp&quality=lossless&width=34&height=45"

    aq2 = "https://media.discordapp.net/attachments/1383207791061241987/1383208091721535508/1286464779011231757.png?ex=684df46b&is=684ca2eb&hm=5ab03709edfa50a80e3f88b73614cfba91043dffcb28b585f21b5d95d7310b2e&=&format=webp&quality=lossless&width=36&height=47"

    aq3 = "https://media.discordapp.net/attachments/1383207791061241987/1383208092451209318/1286464829309059075.png?ex=684df46c&is=684ca2ec&hm=34d657e96344a25545a00c3bce8f7bd416614c24d0d10864a52bd19952eba6ff&=&format=webp&quality=lossless&width=34&height=45"

    fl = "https://media.discordapp.net/attachments/1383207791061241987/1383215969052393482/1286812515619176550.png?ex=684dfbc1&is=684caa41&hm=3d0733e493b8f6bac84f13b1676ffb58c01ed105f8ea4c64f3c8b877f55b614a&=&format=webp&quality=lossless&width=19&height=28"

    fl2 = "https://media.discordapp.net/attachments/1383207791061241987/1383215969626882058/1286812556458987551.png?ex=684dfbc2&is=684caa42&hm=39234b4043cce11b15c808a06cda76f1cc65b160e13ba490bde00135e42ed1fd&=&format=webp&quality=lossless&width=19&height=27"

    fl3 = "https://media.discordapp.net/attachments/1383207791061241987/1383215970050375731/1286812598834302986.png?ex=684dfbc2&is=684caa42&hm=228a06caddaf0b2ba4c40456296cf410957f3a8f091505660fb5c13ce2a84218&=&format=webp&quality=lossless&width=61&height=65"

    ga = "https://media.discordapp.net/attachments/1383207791061241987/1383222644718960742/1286485934807973909.png?ex=684e01f9&is=684cb079&hm=e6800fc0ed2ac27de60f2b6bd30b42e1564b731947dfd88b8f76007e42856877&=&format=webp&quality=lossless&width=19&height=27"

    ga2 = "https://media.discordapp.net/attachments/1383207791061241987/1383222645142589580/1286485982316728361.png?ex=684e01f9&is=684cb079&hm=ed62185b159b2bb7c312edce75b52da26cb77bf9bb6041a3d0fe97d5a530dce7&=&format=webp&quality=lossless&width=24&height=28"

    ga3 = "https://media.discordapp.net/attachments/1383207791061241987/1383222645599899688/1286486026503585863.png?ex=684e01f9&is=684cb079&hm=a2b1529d37942b08a6b2f1d0bd7609c9b25fb26799aadb04a3e0b3d4a42b816e&=&format=webp&quality=lossless&width=19&height=32"

    ga4 = "https://media.discordapp.net/attachments/1383207791061241987/1383222646136901714/1286486072825614431.png?ex=684e01f9&is=684cb079&hm=96a045f9858d71f92be06a724447ec1f41e5a1b4da3408615b98df23133ed95e&=&format=webp&quality=lossless&width=41&height=68"

    ma = "https://media.discordapp.net/attachments/1383207791061241987/1383244481213632623/1286459121582997568.png?ex=684e164f&is=684cc4cf&hm=3f97fb5aeca9298c89571ecabb9c33c03edb770383ee4deb07995e4fc55006f4&=&format=webp&quality=lossless&width=36&height=45"

    ma2 = "https://media.discordapp.net/attachments/1383207791061241987/1383244488654196829/1286459133138178068.png?ex=684e1651&is=684cc4d1&hm=45abdf5d191fb7e9626e82e4dc2af1225491b72a3f2d9043f4ea0dd1ec37574f&=&format=webp&quality=lossless&width=21&height=28"

    ma3 = "https://media.discordapp.net/attachments/1383207791061241987/1383244489304444989/1286459150368374806.png?ex=684e1651&is=684cc4d1&hm=1dc052833d54a080c0df1cf64d4c71f3c53c7420b39c444e55b108f6cd522d05&=&format=webp&quality=lossless&width=19&height=27"

    pl = "https://media.discordapp.net/attachments/1383207791061241987/1383244874538553414/1286657959388119041.png?ex=684e16ad&is=684cc52d&hm=e169c1d9246ec376ee6554be25ffba96fa1eb0349a38f2faa49420b7c5cc59c9&=&format=webp&quality=lossless&width=19&height=27"

    pl2 = "https://media.discordapp.net/attachments/1383207791061241987/1383244875021160558/1286658001385684993.png?ex=684e16ad&is=684cc52d&hm=2d32a2891f708a70fbc11ae1753455250bd8dc77f312f1e85925b8fa6d066af5&=&format=webp&quality=lossless&width=21&height=28"

    pl3 = "https://media.discordapp.net/attachments/1383207791061241987/1383244875457101885/1286658051947888712.png?ex=684e16ad&is=684cc52d&hm=618c99ce62c95c251f8e69e271af1197c5a756322667be3988b79b83f264f24c&=&format=webp&quality=lossless&width=26&height=28"

    sk = "https://media.discordapp.net/attachments/1383207791061241987/1383245568326893729/1286604206576238643.png?ex=684e1752&is=684cc5d2&hm=66fb5f8dc210bf21af21e7721e32b833a53f09ead9f8ce7f9ca733de911a1fe7&=&format=webp&quality=lossless&width=19&height=27"

    sk2 = "https://media.discordapp.net/attachments/1383207791061241987/1383245568775557120/1286604251501559820.png?ex=684e1753&is=684cc5d3&hm=879a8524e1f0909a0b6c13cabc2d78db0d446b5bdb7ee000a4a011d290e75469&=&format=webp&quality=lossless&width=27&height=23"

    sk3 = "https://media.discordapp.net/attachments/1383207791061241987/1383245569077543053/1286604285827612734.png?ex=684e1753&is=684cc5d3&hm=6971510b1541a13838487716f021e194c7b30111cd0847788f7297a35f2bfba9&=&format=webp&quality=lossless&width=21&height=30"

    ye = "https://media.discordapp.net/attachments/1383207791061241987/1383245806450114621/1286810460837908612.png?ex=684e178b&is=684cc60b&hm=a126be153fccedc8a8359c76f6e5ac3f43d1f8f9aae49b0c0c924b3a9d10a9ae&=&format=webp&quality=lossless&width=21&height=33"

    ye2 = "https://media.discordapp.net/attachments/1383207791061241987/1383245806894579752/1286810491154468905.png?ex=684e178b&is=684cc60b&hm=5abb2f1c462fbca913dd54000ea6b4193846f13d9c5530cf14ddf57522840295&=&format=webp&quality=lossless&width=30&height=28"

    ye3 = "https://media.discordapp.net/attachments/1383207791061241987/1383245807091978240/1286810518149136505.png?ex=684e178b&is=684cc60b&hm=c13bac71c1b3982aa979aa88b093476855bb81711bfc6adc85361ed396714ab4&=&format=webp&quality=lossless&width=27&height=32"

    ro = "https://media.discordapp.net/attachments/1383207791061241987/1383245318984044685/1286680783221952554.png?ex=684e1717&is=684cc597&hm=974080b9cbc9b057886850523115f39319fc87e3caf5ec430e61d62963c734c0&=&format=webp&quality=lossless&width=19&height=28"

    ro2 = "https://media.discordapp.net/attachments/1383207791061241987/1383245319579373618/1286680820802781247.png?ex=684e1717&is=684cc597&hm=12a818710a5cdf479ad87fe6ae5e73bd5558d8d8587ca3c05c65bd27a816b657&=&format=webp&quality=lossless&width=19&height=32"

    ro3 = "https://media.discordapp.net/attachments/1383207791061241987/1383245320128823416/1286680856722669671.png?ex=684e1717&is=684cc597&hm=18cedc5bdde276c7fbb3b2958eb28ffc83c5f94dbbb0017b5c1122469ae8127d&=&format=webp&quality=lossless&width=21&height=29"

    ro4 = "https://media.discordapp.net/attachments/1383207791061241987/1383245320644853850/1286680906265788457.png?ex=684e1717&is=684cc597&hm=420bd476e99f0e4147578c870850f53bb458ed8bfcc553de3c6a0aa61c173a53&=&format=webp&quality=lossless&width=19&height=27"


class SD_FA_FOOTER_ICON:
    aq = "https://media.discordapp.net/attachments/1383207791061241987/1383208091457421373/1286464748862570629.png?ex=684df46b&is=684ca2eb&hm=0af851a036039241ebdba68ca84fde5add0ddfe04f520f9828b7167c3c60dea9&=&format=webp&quality=lossless&width=34&height=43"

    aq2 = "https://media.discordapp.net/attachments/1383207791061241987/1383208092053012500/1286464799827300445.png?ex=684df46b&is=684ca2eb&hm=75a2f4584ebec52b27416fb86b3be105130b072c8fcd37ba9bafba292e4b4ad6&=&format=webp&quality=lossless&width=36&height=45"

    aq3 = None

    fl = "https://media.discordapp.net/attachments/1383207791061241987/1383215969425424395/1286812529636409399.png?ex=684dfbc2&is=684caa42&hm=b026cedcd955d6164aa6e4b83b54ee5f3b9a9973a33739defe9456c24ad56515&=&format=webp&quality=lossless&width=26&height=28"

    fl2 = "https://media.discordapp.net/attachments/1383207791061241987/1383215969819951144/1286812573173420112.png?ex=684dfbc2&is=684caa42&hm=6ddc234f820f6fa4ecb97f747735e45fa4093bc1aa534ca429781958baf1bdf9&=&format=webp&quality=lossless&width=36&height=45"

    fl3 = None

    ga = "https://media.discordapp.net/attachments/1383207791061241987/1383222644920422503/1286485951195119616.png?ex=684e01f9&is=684cb079&hm=a60bc3e82977993a07bfd9661c7006450322ddcaa54c48b6df454ccc54b2e739&=&format=webp&quality=lossless&width=19&height=27"

    ga2 = "https://media.discordapp.net/attachments/1383207791061241987/1383222645360951458/1286486009449676852.png?ex=684e01f9&is=684cb079&hm=4db723278b3d496cf5a15e4616f82de384e49fda1425c1fa97a4bab387847967&=&format=webp&quality=lossless&width=24&height=25"

    ga3 = "https://media.discordapp.net/attachments/1383207791061241987/1383222645830455386/1286486042597396560.png?ex=684e01f9&is=684cb079&hm=37e9bd47554ebfea21c32c73db80d0cb7171dcad8344c67cc7e9ba1c6385a509&=&format=webp&quality=lossless&width=19&height=28"

    ga4 = None

    ma = "https://media.discordapp.net/attachments/1383207791061241987/1383244481465421915/1286459126628614178.png?ex=684e164f&is=684cc4cf&hm=b8dc147537489af8cd354e509a511abf133593ea190a2c8e7a5e748bec6a29b7&=&format=webp&quality=lossless&width=32&height=43"

    ma2 = "https://media.discordapp.net/attachments/1383207791061241987/1383244488918437919/1286459139018588183.png?ex=684e1651&is=684cc4d1&hm=a7b41fd90497da0a0a3087334de4e266d9179e04fd7bba853aa22d3c2d129c21&=&format=webp&quality=lossless&width=24&height=29"

    ma3 = None

    pl = "https://media.discordapp.net/attachments/1383207791061241987/1383244874798731324/1286657974877687891.png?ex=684e16ad&is=684cc52d&hm=e23cc56b38358678360064f0bf25bc8232ae19dc67b49364b2bf72fac173b3f9&=&format=webp&quality=lossless&width=19&height=27"

    pl2 = "https://media.discordapp.net/attachments/1383207791061241987/1383244875243323442/1286658021174415422.png?ex=684e16ad&is=684cc52d&hm=7891aeabc568e28af0819712a254de1cd973301ec2c5116da6d35e026f25759a&=&format=webp&quality=lossless&width=47&height=59"

    pl3 = None

    sk = "https://media.discordapp.net/attachments/1383207791061241987/1383245568582615172/1286604222804262922.png?ex=684e1753&is=684cc5d3&hm=90d5d7828d5971618e75893d682b93814e5787f89849ca2daee53ac1f4ffd048&=&format=webp&quality=lossless&width=21&height=27"

    sk2 = "https://media.discordapp.net/attachments/1383207791061241987/1383215969819951144/1286812573173420112.png?ex=684dfbc2&is=684caa42&hm=6ddc234f820f6fa4ecb97f747735e45fa4093bc1aa534ca429781958baf1bdf9&=&format=webp&quality=lossless&width=36&height=45"

    sk3 = None

    ye = "https://media.discordapp.net/attachments/1383207791061241987/1383245806668091413/1286810476864344114.png?ex=684e178b&is=684cc60b&hm=808c7f58772cfacb8b0d1db53d6d2bed47b5fc359cea410bf2c2d13ff0271b32&=&format=webp&quality=lossless&width=19&height=28"

    ye2 = "https://media.discordapp.net/attachments/1383207791061241987/1383215969819951144/1286812573173420112.png?ex=684dfbc2&is=684caa42&hm=6ddc234f820f6fa4ecb97f747735e45fa4093bc1aa534ca429781958baf1bdf9&=&format=webp&quality=lossless&width=36&height=45"

    ye3 = None

    ro = "https://media.discordapp.net/attachments/1383207791061241987/1383245319306875001/1286680798929358929.png?ex=684e1717&is=684cc597&hm=dfb4297dbd2e84edc3174f778309847b6f34883253dc5a2d1d6445f23341fca3&=&format=webp&quality=lossless&width=19&height=28"

    ro2 = "https://media.discordapp.net/attachments/1383207791061241987/1383245319906660422/1286680836648865915.png?ex=684e1717&is=684cc597&hm=57f61f3069c835ba9590792a2cd459a0b25971b86f99bc97ee8bcaa9e04291a0&=&format=webp&quality=lossless&width=19&height=27"

    ro3 = "https://media.discordapp.net/attachments/1383207791061241987/1383245320367902831/1286680873361473578.png?ex=684e1717&is=684cc597&hm=6c40d8115c79108aad5d9d5aae83b9b24940942e2c4b42a7d612520dadf1588d&=&format=webp&quality=lossless&width=19&height=28"

    ro4 = None


class SD_FA_BUTTON_EMOJIS:
    aq = "<:1_:1286464731246362729>"
    aq2 = "<:1_:1286464779011231757>"
    aq3 = "<:1_:1286464829309059075>"

    fl = "<:1_:1286812515619176550>"
    fl2 = "<:1_:1286812556458987551>"
    fl3 = "<:1_:1286812598834302986>"

    ga = "<:1_:1286485934807973909>"
    ga2 = "<:1_:1286485982316728361>"
    ga3 = "<:1_:1286486026503585863>"
    ga4 = "<:1_:1286486072825614431>"

    ma = "<:magma_male_grunt:1286459121582997568>"
    ma2 = "<:magma_captain:1286459133138178068>"
    ma3 = "<:magma_leader:1286459150368374806>"

    pl = "<:1_:1286657959388119041>"
    pl2 = "<:1_:1286658001385684993>"
    pl3 = "<:1_:1286658051947888712>"

    sk = "<:1_:1286604206576238643>"
    sk2 = "<:1_:1286604251501559820>"
    sk3 = "<:1_:1286604285827612734>"

    ye = "<:1_:1286810460837908612>"
    ye2 = "<:1_:1286810491154468905>"
    ye3 = "<:1_:1286810518149136505>"

    ro = "<:1_:1286680783221952554>"
    ro2 = "<:1_:1286680820802781247>"
    ro3 = "<:1_:1286680856722669671>"
    ro4 = "<:1_:1286680906265788457>"


class SD_FA_BUTTON_LABEL:
    aq = "Grunt"

    aq2 = "Admin"

    aq3 = "Leader"

    fl = "Grunt"

    fl2 = "Admin"

    fl3 = "Leader"

    ga = "Grunt"

    ga2 = "Admin Pt1"

    ga3 = "Admin Pt2"

    ga4 = "Leader"

    ma = "Grunt"

    ma2 = "Admin"

    ma3 = "Leader"

    pl = "Grunt"

    pl2 = "Admin"

    pl3 = "Leader"

    sk = "Grunt"

    sk2 = "Admin"

    sk3 = "Leader"

    ye = "Grunt"

    ye2 = "Admin"

    ye3 = "Leader"

    ro = "Grunt"

    ro2 = "Admin"

    ro3 = "Admin Pt2"

    ro4 = "Leader"


class SD_FA_DESC:

    i = f"""# FACTION INFO

- **What are Factions?**
> *Factions are a team-based challenge, similar to clans. You and your team must earn points via various methods. Using your points you can then buy different items in the  `;faction shop`  based on your rank. The items in the shop help with the newly introduced EV training, World Boss, and much more.*

- **What is the best Faction to join?**
> *There is no such thing as a "best" Faction as it is personal preference. Each Faction gives the same amount of benefits. As of right now, you do not get any benefits from choosing a certain Faction over another.*

- **What is each Factions unique  <:Golden11:1147776276510281818>  pokemon?**
>  - Plasma  `Golden Scraggy`
>  - Magma  `Golden Numel`
>  - Aqua  `Golden Carvanha`
>  - Rocket  `Golden Grimer`
>  - Yell  `Golden Galarian-Zigzagoon`
>  - Skull  `Golden Yungoos`
>  - Flare  `Golden Litleo`
>  - Galactic  `Golden Croagunk`

- **What are the best ways to earn Faction points?**
> *You can see the complete list of earning Faction points in the "Info" page in the  `;faction`  command.*

- **Which ball should I use to catch other faction target Pokémon?**
> *You should be using your own faction ball.*

- **Once I have chosen a Faction, can I change to a different one?**
> *In order to change your Faction, you must buy a Team Medallion in the  `;patreon shop`  for 1000  <:patreon_token:1296818113735819405>  Patreon Tokens. You can only change your Faction once a month.

> <a:fidough_wow:1283739703140679703>  ***FidNotes:** There is also a role for you to claim once you have chosen your Faction. To do this type  `;fac claim_role`. You will be granted access to a private channel to talk to your team members.*"""
    aq = f"""**TEAM:**
- **Zekrom**
> Equip: `Magnet` `Dragon Fang` `Expert Belt`
> Moves: `Fusion Bolt` `Outrage` `Roost`
> EVs: `Max ATK`
- **Mewtwo**
> Equip: `Twisted Spoon` `Black Belt` `Magnet` `Expert Belt`
> Moves: `Psychic``Aura Sphere` `Thunderbolt` `Earth Power`
> EVs: `Max SPA` `Max DEF`
- **Slaking** [OPTIONAL]
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`


**STRATEGY:**
- [Zekrom] Fusion Bolt on Carvanha & Sharpedo
- [Zekrom] Outrage against Mightyena
- [Mewtwo] Aura Sphere on Mightyena
- [Mewtwo] Thunderbolt on Carvanha & Sharpedo to finish them off"""

    fl = f"""**TEAM:**
- **Slaking**
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Mewtwo**
> Equip: `Twisted Spoon` `Black Belt` `Magnet` `Expert Belt`
> Moves: `Psychic``Aura Sphere` `Thunderbolt` `Earth Power`
> EVs: `Max SPA` `Max DEF`
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`

**STRATEGY:**
- [Slaking] Focus Punch on Mightyena & Houndoom
- [Slaking] Thunder Punch on Crobat
- [Mewtwo] Psychic on Swalot & Crobat

> <a:FidoughLove:1127656671590752387> ***FidNotes:** Use moves according to enemy weakness.*"""

    ga = f"""**TEAM:**
- **Mewtwo**
> Equip: `Twisted Spoon` `Black Belt` `Magnet` `Expert Belt`
> Moves: `Psychic``Aura Sphere` `Thunderbolt` `Earth Power`
> EVs: `Max SPA` `Max DEF`
- **Slaking**
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Groudon** [OPTIONAL]
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`

**STRATEGY:**
- [Mewtwo] Psychic everything except Bronzong
- [Slaking] Focus Punch Purugly"""

    ma = f"""**TEAM:**
- **Slaking**
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Kyogre**
> Equip: `Mystic Water` `Expert Belt`
> Moves: `Water Spout`

**STRATEGY:**
- [Slaking] Focus Punch only for Mightyena
- Then just spam the moves suggested above"""

    pl = f"""**TEAM:**
- **Slaking**
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Mewtwo**
> Equip: `Twisted Spoon` `Black Belt` `Magnet` `Expert Belt`
> Moves: `Psychic` `Aura Sphere` `Thunderbolt` `Earth Power`
> EVs: `Max SPA` `Max DEF`
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`

> <a:FidoughLove:1127656671590752387> ***FidNotes:** Use moves according to enemy weakness.*"""

    sk = f"""**TEAM:**
- **Mewtwo**
> Equip: `Twisted Spoon` `Black Belt` `Magnet` `Expert Belt`
> Moves: `Psychic` `Aura Sphere` `Thunderbolt` `Earth Power`
> EVs: `Max SPA` `Max DEF`
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Slaking**
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`

**STRATEGY:**
- [Slaking] on Gengar to bait ghost move then use Earthquake & Sucker Punch combo

> <a:FidoughLove:1127656671590752387> ***FidNotes:** Use moves according to enemy weakness.*"""

    ye = f"""**TEAM:**
- **Xerneas**
> Equip: `Expert Belt`
> Moves: `Moonblast`
> EVs: `Max SPA` `Max HP`
- **Slaking**
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`

**STRATEGY:**
- [Xerneas] almost sweeps the whole team
- [Groudon] on Skuntank"""

    ro = f"""**TEAM:**
- **Arceus Fairy**
> Equip: `Expert Belt` `Leftovers` `Soft Sand`
> Moves: `Judgment` `Earthquake` `Dark Pulse` `Recover`
> EVs: `Max HP` `Half SPE` `Half DEF`
- **Mega Mewtwo X**
> Equip: `Choice Band` `Expert Belt` `Soft Sand`
> Moves: `Drain Punch` `Psychic` `Earthquake`
> EVs: `Max ATK` `Half HP` `Half SPE`
- **Groudon**
> Equip: `Soft Sand`
> Moves: `Earthquake`
> EVs: `Max SPD` `Max ATK`


**STRATEGY:**
- [Arceus & MMX] Earthquake spam will usually take out the entire team
- [Arceus] Judgment on Gallade and Recover if low HP
- Metagross might take out first two mons so use [Groudon] to finish off the rest of the team

> *Credits: <@693154342995361882>*"""
    # ---------------------------
    aq2 = f"""**TEAM:**
- **Yveltal**
> Equip: `Expert Belt` `Sharp Beak` `Twisted Spoon`
> Moves: `Psychic` `Oblivion Wing` `Sucker Punch`
- **Xerneas**
> Equip: `Expert Belt`
> Moves: `Moonblast`
> EVs: `Max ATK` `Max HP`
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`

**STRATEGY:**
- [Groudon] for Muk
- [Xerneas] for Mightyana
- [Yveltal] for others"""

    fl2 = f"""**TEAM:**
- **Yveltal**
> Equip: `Expert Belt` `Sharp Beak` `Twisted Spoon`
> Moves: `Psychic` `Oblivion Wing` `Sucker Punch`
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`

**STRATEGY:**
- [Yveltal] Oblvion Wing against those weak to Flying
- [Yveltal] Psychic against those weak to Psychic
- [Yveltal] Sucker Punch opponents when it has Low HP
- [Groudon] Earthquake spam for Electric type
- [Groudon] Earthquake for Houndoom
- [Groudon] Body Press spam for Mightyana"""

    ga2 = f"""**TEAM:**
- **Yveltal**
> Equip: `Expert Belt` `Sharp Beak` `Twisted Spoon`
> Moves: `Psychic` `Oblivion Wing` `Sucker Punch`
- **Xerneas**
> Equip: `Expert Belt`
> Moves: `Moonblast`
> EVs: `Max ATK` `Max HP`

**STRATEGY:**
- [Yveltal] Oblvion Wing against those weak to Flying
- [Yveltal] Psychic against those weak to Psychic
- [Yveltal] Sucker Punch opponents when it has Low HP
- Sacrifice [3rd] on Absol & Tyranitar then use [Xerneas]"""

    ma2 = f"""**TEAM:**
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Xerneas**
> Equip: `Expert Belt`
> Moves: `Moonblast`
> EVs: `Max ATK` `Max HP`

**STRATEGY:**
- [Groudon] Earthquake if Morpeko-Hangry lead then sacrifice [3rd]
- [Xerneas] on Grimmsnarl
- Finish with [Groudon] if [Xerneas] dies
- Sacrifies [3rd] if Grimmsnarl is lead
- [Xerneas] Moonblast spam
- [Xerneas] on Mightyana
- [Groudon] for the rest

> <a:FidoughLove:1127656671590752387>  ***FidNotes:**  [Xerneas] is good if max SPA EV, others are good to go without it. You can train if you want to get better win-rate. All battles are doable without items, but your win-rate might go down. Remember they are meant to be as cheap as possible so better teams will work too.*"""

    pl2 = f"""**TEAM:**
- **Yveltal**
> Equip: `Expert Belt` `Sharp Beak` `Twisted Spoon`
> Moves: `Psychic` `Oblivion Wing` `Sucker Punch`
- **Reshiram**
> Equip: `Expert Belt` `Charcoal`
> Moves: `Fusion Flare`
- **Xerneas**
> Equip: `Expert Belt`
> Moves: `Moonblast`
> EVs: `Max ATK` `Max HP`

**STRATEGY:**
- If Bisharp locks to steel move switch to [Reshiram] Fusion Flare
- If Bisharp locks to foul play switch to [Xerneas] Moonblast"""

    sk2 = f"""**TEAM:**
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Yveltal**
> Equip: `Expert Belt` `Sharp Beak` `Twisted Spoon`
> Moves: `Psychic` `Oblivion Wing` `Sucker Punch`

**STRATEGY:**
- Sacrifice [3rd] if Lurantis or Toxapex lead then switch to [Yvental] Oblivion Wing or Psychic spam
- [Groudon] can kill Alolan-Muk & Salazzle easily"""

    ye2 = f"""**TEAM:**
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake`
> EVs: `Max ATK` `Max SPD`
- **Xerneas**
> Equip: `Expert Belt`
> Moves: `Moonblast`
> EVs: `Max SPA` `Max HP`

**STRATEGY:**
- [Groudon] Earthquake if Morpeko-Hangry lead then sacrifice [3rd]
- [Xerneas] on Grimmsnarl
- Finish with [Groudon] if [Xerneas] dies
- Sacrifies [3rd] if Grimmsnarl is lead
- [Xerneas] Moonblast spam
- [Xerneas] on Mightyana
- [Groudon] for the rest

> <a:FidoughLove:1127656671590752387> ***FidNotes:** [Xerneas] is good if max SPA EV, others are good to go without it. You can train if you want to get better win-rate. All battles are doable without items, but your win-rate might go down. Remember they are meant to be as cheap as possible so better teams will work too.*"""

    ro2 = f"""**TEAM:**
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake` `Thunderbolt`
> EVs: `Max ATK` `Max SPD`
- **Yveltal**
> Equip: `Sharp Beak` `Twisted Spoon` `Expert Belt`
> Moves: `Psychic` `Oblivion Wing` `Sucker Punch`
- **Slaking**
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`

**STRATEGY:**
- [Yveltal] Oblivion Wing on Vileplume, Psychic on Poison Types
- [Slaking] Focus Punch Dark Types
- [Groudon] Earthquake
- [Yveltal]  Sucker Punch those who have less HP"""
    aq3 = f"""⚠️ Under Construction
Send your strategy in #🌱﹢gard-helpdesk﹐❀﹒"""

    fl3 = f"""⚠️ Under Construction
Send your strategy in #🌱﹢gard-helpdesk﹐❀﹒"""

    ga3 = f"""**TEAM:**
- **Yveltal**
> Equip: `Expert Belt` `Sharp Beak` `Twisted Spoon`
> Moves: `Psychic` `Oblivion Wing` `Sucker Punch`
- **Xerneas**
> Equip: `Expert Belt`
> Moves: `Moonblast`
> EVs: `Max ATK` `Max HP`

**STRATEGY:**
- [Yveltal] Oblvion Wing against those weak to Flying
- [Yveltal] Psychic against those weak to Psychic
- [Yveltal] Sucker Punch opponents when it has Low HP
- Sacrifice [3rd] on Absol & Tyranitar then use [Xerneas]"""

    ma3 = f"""⚠️ Under Construction
Send your strategy in #🌱﹢gard-helpdesk﹐❀﹒"""

    pl3 = f"""⚠️ Under Construction
Send your strategy in #🌱﹢gard-helpdesk﹐❀﹒"""

    sk3 = f"""⚠️ Under Construction
Send your strategy in #🌱﹢gard-helpdesk﹐❀﹒"""

    ye3 = f"""⚠️ Under Construction
Send your strategy in #🌱﹢gard-helpdesk﹐❀﹒"""

    ro3 = f"""**TEAM:**
- **Groudon**
> Equip: `Soft Sand` `Expert Belt`
> Moves: `Earthquake` `Thunderbolt`
> EVs: `Max ATK` `Max SPD`
- **Yveltal**
> Equip: `Sharp Beak` `Twisted Spoon` `Expert Belt`
> Moves: `Psychic` `Oblivion Wing` `Sucker Punch`
- **Slaking**
> Equip: `Black Belt` `Magnet` `Expert Belt`
> Moves: `Focus Punch` `Thunder Punch` `Earthquake`
> EVs: `Max ATK` `Max SPD`

**STRATEGY:**
- [Yveltal] Oblivion Wing on Vileplume, Psychic on Poison Types
- [Slaking] Focus Punch Dark Types
- [Groudon] Earthquake
- [Yveltal]  Sucker Punch those who have less HP"""
    # ---------------------------
    ga4 = f"""⚠️ Under Construction
Send your strategy in #🌱﹢gard-helpdesk﹐❀﹒"""

    ro4 = f"""⚠️ Under Construction
Send your strategy in #🌱﹢gard-helpdesk﹐❀﹒"""


FACTIONS = {
    "aq": {
        "color": SD_FA_COLOR.aq,
        "content": SD_FA_CONTENT.aq,
        "thumbnail": SD_FA_THUMBNAIL.aq,
        "header_text": {
            "aq": SD_FA_HEADER_TEXT.aq,
            "aq2": SD_FA_HEADER_TEXT.aq2,
            "aq3": SD_FA_HEADER_TEXT.aq3,
        },
        "header_icon": {
            "aq": SD_FA_HEADER_ICON.aq,
            "aq2": SD_FA_HEADER_ICON.aq2,
            "aq3": SD_FA_HEADER_ICON.aq3,
        },
        "footer_text": {
            "aq": SD_FA_FOOTER_TEXT.aq,
            "aq2": SD_FA_FOOTER_TEXT.aq2,
            "aq3": SD_FA_FOOTER_TEXT.aq3,
        },
        "footer_icon": {
            "aq": SD_FA_FOOTER_ICON.aq,
            "aq2": SD_FA_FOOTER_ICON.aq2,
            "aq3": SD_FA_FOOTER_ICON.aq3,
        },
        "button_label": {
            "aq": SD_FA_BUTTON_LABEL.aq,
            "aq2": SD_FA_BUTTON_LABEL.aq2,
            "aq3": SD_FA_BUTTON_LABEL.aq3,
        },
        "button_emoji": {
            "aq": SD_FA_BUTTON_EMOJIS.aq,
            "aq2": SD_FA_BUTTON_EMOJIS.aq2,
            "aq3": SD_FA_BUTTON_EMOJIS.aq3,
        },
        "desc": {"aq": SD_FA_DESC.aq, "aq2": SD_FA_DESC.aq2, "aq3": SD_FA_DESC.aq3},
    },
    "fl": {
        "color": SD_FA_COLOR.fl,
        "content": SD_FA_CONTENT.fl,
        "thumbnail": SD_FA_THUMBNAIL.fl,
        "header_text": {
            "fl": SD_FA_HEADER_TEXT.fl,
            "fl2": SD_FA_HEADER_TEXT.fl2,
            "fl3": SD_FA_HEADER_TEXT.fl3,
        },
        "header_icon": {
            "fl": SD_FA_HEADER_ICON.fl,
            "fl2": SD_FA_HEADER_ICON.fl2,
            "fl3": SD_FA_HEADER_ICON.fl3,
        },
        "footer_text": {
            "fl": SD_FA_FOOTER_TEXT.fl,
            "fl2": SD_FA_FOOTER_TEXT.fl2,
            "fl3": SD_FA_FOOTER_TEXT.fl3,
        },
        "footer_icon": {
            "fl": SD_FA_FOOTER_ICON.fl,
            "fl2": SD_FA_FOOTER_ICON.fl2,
            "fl3": SD_FA_FOOTER_ICON.fl3,
        },
        "button_label": {
            "fl": SD_FA_BUTTON_LABEL.fl,
            "fl2": SD_FA_BUTTON_LABEL.fl2,
            "fl3": SD_FA_BUTTON_LABEL.fl3,
        },
        "button_emoji": {
            "fl": SD_FA_BUTTON_EMOJIS.fl,
            "fl2": SD_FA_BUTTON_EMOJIS.fl2,
            "fl3": SD_FA_BUTTON_EMOJIS.fl3,
        },
        "desc": {"fl": SD_FA_DESC.fl, "fl2": SD_FA_DESC.fl2, "fl3": SD_FA_DESC.fl3},
    },
    "ga": {
        "color": SD_FA_COLOR.ga,
        "content": SD_FA_CONTENT.ga,
        "thumbnail": SD_FA_THUMBNAIL.ga,
        "header_text": {
            "ga": SD_FA_HEADER_TEXT.ga,
            "ga2": SD_FA_HEADER_TEXT.ga2,
            "ga3": SD_FA_HEADER_TEXT.ga3,
            "ga4": SD_FA_HEADER_TEXT.ga4,
        },
        "header_icon": {
            "ga": SD_FA_HEADER_ICON.ga,
            "ga2": SD_FA_HEADER_ICON.ga2,
            "ga3": SD_FA_HEADER_ICON.ga3,
            "ga4": SD_FA_HEADER_ICON.ga4,
        },
        "footer_text": {
            "ga": SD_FA_FOOTER_TEXT.ga,
            "ga2": SD_FA_FOOTER_TEXT.ga2,
            "ga3": SD_FA_FOOTER_TEXT.ga3,
            "ga4": SD_FA_FOOTER_TEXT.ga4,
        },
        "footer_icon": {
            "ga": SD_FA_FOOTER_ICON.ga,
            "ga2": SD_FA_FOOTER_ICON.ga2,
            "ga3": SD_FA_FOOTER_ICON.ga3,
            "ga4": SD_FA_FOOTER_ICON.ga4,
        },
        "button_label": {
            "ga": SD_FA_BUTTON_LABEL.ga,
            "ga2": SD_FA_BUTTON_LABEL.ga2,
            "ga3": SD_FA_BUTTON_LABEL.ga3,
            "ga4": SD_FA_BUTTON_LABEL.ga4,
        },
        "button_emoji": {
            "ga": SD_FA_BUTTON_EMOJIS.ga,
            "ga2": SD_FA_BUTTON_EMOJIS.ga2,
            "ga3": SD_FA_BUTTON_EMOJIS.ga3,
            "ga4": SD_FA_BUTTON_EMOJIS.ga4,
        },
        "desc": {
            "ga": SD_FA_DESC.ga,
            "ga2": SD_FA_DESC.ga2,
            "ga3": SD_FA_DESC.ga3,
            "ga4": SD_FA_DESC.ga4,
        },
    },
    "ma": {
        "color": SD_FA_COLOR.ma,
        "content": SD_FA_CONTENT.ma,
        "thumbnail": SD_FA_THUMBNAIL.ma,
        "header_text": {
            "ma": SD_FA_HEADER_TEXT.ma,
            "ma2": SD_FA_HEADER_TEXT.ma2,
            "ma3": SD_FA_HEADER_TEXT.ma3,
        },
        "header_icon": {
            "ma": SD_FA_HEADER_ICON.ma,
            "ma2": SD_FA_HEADER_ICON.ma2,
            "ma3": SD_FA_HEADER_ICON.ma3,
        },
        "footer_text": {
            "ma": SD_FA_FOOTER_TEXT.ma,
            "ma2": SD_FA_FOOTER_TEXT.ma2,
            "ma3": SD_FA_FOOTER_TEXT.ma3,
        },
        "footer_icon": {
            "ma": SD_FA_FOOTER_ICON.ma,
            "ma2": SD_FA_FOOTER_ICON.ma2,
            "ma3": SD_FA_FOOTER_ICON.ma3,
        },
        "button_label": {
            "ma": SD_FA_BUTTON_LABEL.ma,
            "ma2": SD_FA_BUTTON_LABEL.ma2,
            "ma3": SD_FA_BUTTON_LABEL.ma3,
        },
        "button_emoji": {
            "ma": SD_FA_BUTTON_EMOJIS.ma,
            "ma2": SD_FA_BUTTON_EMOJIS.ma2,
            "ma3": SD_FA_BUTTON_EMOJIS.ma3,
        },
        "desc": {"ma": SD_FA_DESC.ma, "ma2": SD_FA_DESC.ma2, "ma3": SD_FA_DESC.ma3},
    },
    "pl": {
        "color": SD_FA_COLOR.pl,
        "content": SD_FA_CONTENT.pl,
        "thumbnail": SD_FA_THUMBNAIL.pl,
        "header_text": {
            "pl": SD_FA_HEADER_TEXT.pl,
            "pl2": SD_FA_HEADER_TEXT.pl2,
            "pl3": SD_FA_HEADER_TEXT.pl3,
        },
        "header_icon": {
            "pl": SD_FA_HEADER_ICON.pl,
            "pl2": SD_FA_HEADER_ICON.pl2,
            "pl3": SD_FA_HEADER_ICON.pl3,
        },
        "footer_text": {
            "pl": SD_FA_FOOTER_TEXT.pl,
            "pl2": SD_FA_FOOTER_TEXT.pl2,
            "pl3": SD_FA_FOOTER_TEXT.pl3,
        },
        "footer_icon": {
            "pl": SD_FA_FOOTER_ICON.pl,
            "pl2": SD_FA_FOOTER_ICON.pl2,
            "pl3": SD_FA_FOOTER_ICON.pl3,
        },
        "button_label": {
            "pl": SD_FA_BUTTON_LABEL.pl,
            "pl2": SD_FA_BUTTON_LABEL.pl2,
            "pl3": SD_FA_BUTTON_LABEL.pl3,
        },
        "button_emoji": {
            "pl": SD_FA_BUTTON_EMOJIS.pl,
            "pl2": SD_FA_BUTTON_EMOJIS.pl2,
            "pl3": SD_FA_BUTTON_EMOJIS.pl3,
        },
        "desc": {"pl": SD_FA_DESC.pl, "pl2": SD_FA_DESC.pl2, "pl3": SD_FA_DESC.pl3},
    },
    "sk": {
        "color": SD_FA_COLOR.sk,
        "content": SD_FA_CONTENT.sk,
        "thumbnail": SD_FA_THUMBNAIL.sk,
        "header_text": {
            "sk": SD_FA_HEADER_TEXT.sk,
            "sk2": SD_FA_HEADER_TEXT.sk2,
            "sk3": SD_FA_HEADER_TEXT.sk3,
        },
        "header_icon": {
            "sk": SD_FA_HEADER_ICON.sk,
            "sk2": SD_FA_HEADER_ICON.sk2,
            "sk3": SD_FA_HEADER_ICON.sk3,
        },
        "footer_text": {
            "sk": SD_FA_FOOTER_TEXT.sk,
            "sk2": SD_FA_FOOTER_TEXT.sk2,
            "sk3": SD_FA_FOOTER_TEXT.sk3,
        },
        "footer_icon": {
            "sk": SD_FA_FOOTER_ICON.sk,
            "sk2": SD_FA_FOOTER_ICON.sk2,
            "sk3": SD_FA_FOOTER_ICON.sk3,
        },
        "button_label": {
            "sk": SD_FA_BUTTON_LABEL.sk,
            "sk2": SD_FA_BUTTON_LABEL.sk2,
            "sk3": SD_FA_BUTTON_LABEL.sk3,
        },
        "button_emoji": {
            "sk": SD_FA_BUTTON_EMOJIS.sk,
            "sk2": SD_FA_BUTTON_EMOJIS.sk2,
            "sk3": SD_FA_BUTTON_EMOJIS.sk3,
        },
        "desc": {"sk": SD_FA_DESC.sk, "sk2": SD_FA_DESC.sk2, "sk3": SD_FA_DESC.sk3},
    },
    "ye": {
        "color": SD_FA_COLOR.ye,
        "content": SD_FA_CONTENT.ye,
        "thumbnail": SD_FA_THUMBNAIL.ye,
        "header_text": {
            "ye": SD_FA_HEADER_TEXT.ye,
            "ye2": SD_FA_HEADER_TEXT.ye2,
            "ye3": SD_FA_HEADER_TEXT.ye3,
        },
        "header_icon": {
            "ye": SD_FA_HEADER_ICON.ye,
            "ye2": SD_FA_HEADER_ICON.ye2,
            "ye3": SD_FA_HEADER_ICON.ye3,
        },
        "footer_text": {
            "ye": SD_FA_FOOTER_TEXT.ye,
            "ye2": SD_FA_FOOTER_TEXT.ye2,
            "ye3": SD_FA_FOOTER_TEXT.ye3,
        },
        "footer_icon": {
            "ye": SD_FA_FOOTER_ICON.ye,
            "ye2": SD_FA_FOOTER_ICON.ye2,
            "ye3": SD_FA_FOOTER_ICON.ye3,
        },
        "button_label": {
            "ye": SD_FA_BUTTON_LABEL.ye,
            "ye2": SD_FA_BUTTON_LABEL.ye2,
            "ye3": SD_FA_BUTTON_LABEL.ye3,
        },
        "button_emoji": {
            "ye": SD_FA_BUTTON_EMOJIS.ye,
            "ye2": SD_FA_BUTTON_EMOJIS.ye2,
            "ye3": SD_FA_BUTTON_EMOJIS.ye3,
        },
        "desc": {"ye": SD_FA_DESC.ye, "ye2": SD_FA_DESC.ye2, "ye3": SD_FA_DESC.ye3},
    },
    "ro": {
        "color": SD_FA_COLOR.ro,
        "content": SD_FA_CONTENT.ro,
        "thumbnail": SD_FA_THUMBNAIL.ro,
        "header_text": {
            "ro": SD_FA_HEADER_TEXT.ro,
            "ro2": SD_FA_HEADER_TEXT.ro2,
            "ro3": SD_FA_HEADER_TEXT.ro3,
            "ro4": SD_FA_HEADER_TEXT.ro4,
        },
        "header_icon": {
            "ro": SD_FA_HEADER_ICON.ro,
            "ro2": SD_FA_HEADER_ICON.ro2,
            "ro3": SD_FA_HEADER_ICON.ro3,
            "ro4": SD_FA_HEADER_ICON.ro4,
        },
        "footer_text": {
            "ro": SD_FA_FOOTER_TEXT.ro,
            "ro2": SD_FA_FOOTER_TEXT.ro2,
            "ro3": SD_FA_FOOTER_TEXT.ro3,
            "ro4": SD_FA_FOOTER_TEXT.ro4,
        },
        "footer_icon": {
            "ro": SD_FA_FOOTER_ICON.ro,
            "ro2": SD_FA_FOOTER_ICON.ro2,
            "ro3": SD_FA_FOOTER_ICON.ro3,
            "ro4": SD_FA_FOOTER_ICON.ro4,
        },
        "button_label": {
            "ro": SD_FA_BUTTON_LABEL.ro,
            "ro2": SD_FA_BUTTON_LABEL.ro2,
            "ro3": SD_FA_BUTTON_LABEL.ro3,
            "ro4": SD_FA_BUTTON_LABEL.ro4,
        },
        "button_emoji": {
            "ro": SD_FA_BUTTON_EMOJIS.ro,
            "ro2": SD_FA_BUTTON_EMOJIS.ro2,
            "ro3": SD_FA_BUTTON_EMOJIS.ro3,
            "ro4": SD_FA_BUTTON_EMOJIS.ro4,
        },
        "desc": {
            "ro": SD_FA_DESC.ro,
            "ro2": SD_FA_DESC.ro2,
            "ro3": SD_FA_DESC.ro3,
            "ro4": SD_FA_DESC.ro4,
        },
    },
}

# ─────────────────────────────
# 🔹 Helper: Check if message is a PokéMeow reply
# ─────────────────────────────
import discord


def is_pokemeow_reply(message: discord.Message) -> discord.Member | bool:
    """
    Check if a message is from PokéMeow and is a reply to a user.

    Parameters
    ----------
    message : discord.Message
        The message to check.

    Returns
    -------
    discord.Member | bool
        Returns the member the message is replying to if valid, else False.
    """
    author_str = str(message.author).lower()
    if "pokémeow" not in author_str and "pokemeow" not in author_str:
        return False

    if not getattr(message, "reference", None):
        return False

    replied_msg = getattr(message.reference, "resolved", None)
    if not isinstance(replied_msg, discord.Message):
        return False

    return (
        replied_msg.author if isinstance(replied_msg.author, discord.Member) else False
    )


# ─────────────────────────────
# 🔹 Sample usage
# ─────────────────────────────
# async def on_message(message: discord.Message):
#     user = is_pokemeow_reply(message)
#     if user:
#         print(f"PokéMeow replied to {user.display_name}")


async def get_pokemeow_reply_member(message: discord.Message) -> discord.Member | None:
    """
    Determines if the message is a PokéMeow bot reply.
    If yes, returns the member that PokéMeow replied to.
    Returns None otherwise.
    """
    # 🛑 Only process messages from PokéMeow
    author_str = str(message.author).lower()
    if "pokémeow" not in author_str and "pokemeow" not in author_str:
        return None

    # 🛑 Ensure the message is a reply
    if not getattr(message, "reference", None):
        return None

    resolved_msg = getattr(message.reference, "resolved", None)
    if not isinstance(resolved_msg, discord.Message):
        return None

    member = (
        resolved_msg.author if isinstance(resolved_msg.author, discord.Member) else None
    )
    return member


def get_message_interaction_member(message: discord.Message) -> discord.Member | None:
    """
    Returns the member who triggered the interaction that created this message, if available.
    Returns None if not an interaction-created message or not a guild interaction.
    """
    interaction_metadata = getattr(message, "interaction_metadata", None)
    if not interaction_metadata:
        return None

    # Try member first
    member = getattr(interaction_metadata, "member", None)
    if isinstance(member, discord.Member):
        return member

    # Try user (may be discord.User, not Member)
    user = getattr(interaction_metadata, "user", None)
    if isinstance(user, discord.Member):
        return user
    elif isinstance(user, discord.User) and message.guild:
        # Try to fetch member from guild
        fetched_member = message.guild.get_member(user.id)
        if fetched_member:
            return fetched_member

    return None


async def get_pokemeow_command_user(message: discord.Message) -> discord.Member | None:
    """
    Checks if the message is a PokéMeow reply and returns the member it replied to.
    Returns None if not a PokéMeow reply or if the replied-to author is not a member.
    """
    member = await get_pokemeow_reply_member(message)
    if not member:
        # Fallback: Check if it's an interaction message from PokéMeow
        member = get_message_interaction_member(message)
        if not member:
            return None

    return member

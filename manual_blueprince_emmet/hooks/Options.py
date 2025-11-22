# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class TwoExtraAllowanceWeight(Range):
    """Weight of Two Extra Allowance Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0."""
    display_name = "Two Extra Allowance Weight"
    range_start = 0
    range_end = 100
    default = 3

class TwoExtraStarsWeight(Range):
    """Weight of Two Extra Stars Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0."""
    display_name = "Two Extra Stars Weight"
    range_start = 0
    range_end = 100
    default = 3

class TwoExtraLockpickingWeight(Range):
    """Weight of Two Extra Lockpicking Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0."""
    display_name = "Two Extra Lockpicking Weight"
    range_start = 0
    range_end = 100
    default = 3

class TwoExtraLuckWeight(Range):
    """Weight of Two Extra Luck Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0. Requires the luck mod to work."""
    display_name = "Two Extra Luck Weight"
    range_start = 0
    range_end = 100
    default = 2

class OneExtraStartingKeyWeight(Range):
    """Weight of One Extra Starting Key Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0. Requires the well prepared mod to work."""
    display_name = "One Extra Starting Key Weight"
    range_start = 0
    range_end = 100
    default = 2

class OneExtraStartingGemWeight(Range):
    """Weight of One Extra Starting Gem Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0. Requires the well prepared mod to work."""
    display_name = "One Extra Starting Gem Weight"
    range_start = 0
    range_end = 100
    default = 2

class FiveExtraStartingStepsWeight(Range):
    """Weight of Five Extra Starting Steps Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0. Requires the well prepared mod to work."""
    display_name = "Five Extra Starting Steps Weight"
    range_start = 0
    range_end = 100
    default = 2

class TwoExtraStartingDiceWeight(Range):
    """Weight of Two Extra Starting Dice Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0. Requires the well prepared mod to work."""
    display_name = "Two Extra Starting Dice Weight"
    range_start = 0
    range_end = 100
    default = 2

class TwoMirrorRoomsWeight(Range):
    """Weight of Two Mirror Rooms Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0. Refers to the stuff on line 424 and below."""
    display_name = "Two Mirror Rooms Weight"
    range_start = 0
    range_end = 100
    default = 1

class TwoRoomRarityShiftsWeight(Range):
    """Weight of Two Room Rarity Shifts Filler Items. Set to 0 to disable. Don't set all Filler Item weights to 0. Refers to the stuff on line 1843 above and below, requires more work to use than other filler items"""
    display_name = "Two Room Rarity Shifts Weight"
    range_start = 0
    range_end = 100
    default = 0

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["two_extra_allowance_weight"] = TwoExtraAllowanceWeight
    options["two_extra_stars_weight"] = TwoExtraStarsWeight
    options["two_extra_lockpicking_weight"] = TwoExtraLockpickingWeight
    options["two_extra_luck_weight"] = TwoExtraLuckWeight
    options["one_extra_starting_key"] = OneExtraStartingKeyWeight
    options["one_extra_starting_gem_weight"] = OneExtraStartingGemWeight
    options["five_extra_starting_steps_weight"] = FiveExtraStartingStepsWeight
    options["two_extra_starting_dice_weight"] = TwoExtraStartingDiceWeight
    options["two_random_mirror_rooms_weight"] = TwoMirrorRoomsWeight
    options["two_room_rarity_shifts_weight"] = TwoRoomRarityShiftsWeight
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups

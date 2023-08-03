from typing import Optional


def space_in_postcode(postcode):
    if len(postcode) in [5, 6, 7]:
        return postcode[:-3] + " " + postcode[-3:]
    else:
        return postcode


def full_address(
    street1: str,
    city: str,
    post_code: str,
    county: Optional[str] = None,
    building_name: Optional[str] = None,
    sub_building: Optional[str] = None,
):
    postcode = space_in_postcode(post_code)
    if county is None:
        street_address = f"{street1}, {city}, {postcode}"
    else:
        street_address = f"{street1}, {city}, {county}, {postcode}"
    if building_name is not None and len(building_name) > 0:
        street_address = f"{building_name}, {street_address}"
    if sub_building is not None and len(sub_building) > 0:
        street_address = f"{sub_building}, {street_address}"
    return street_address


def short_address(
    street1: str,
    post_code: str,
    building_name: Optional[str] = None,
    sub_building: Optional[str] = None,
):
    street_address = f"{street1}, {space_in_postcode(post_code)}"
    if building_name is not None and len(building_name) > 0:
        street_address = f"{building_name} {street_address}"
    if sub_building is not None and len(sub_building) > 0:
        street_address = f"{sub_building} {street_address}"
    return street_address


def first_line(
    street1: str,
    building_name: Optional[str] = None,
    sub_building: Optional[str] = None,
):
    street_address = street1
    if building_name is not None and len(building_name) > 0:
        street_address = f"{building_name} {street_address}"
    if sub_building is not None and len(sub_building) > 0:
        street_address = f"{sub_building} {street_address}"
    return street_address

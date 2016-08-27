def normalize_spacing(query):
    query = " ".join(query.replace("\n", " ").split())
    return query


def insert_stat(skill_type, is_percent, value):
    if is_percent is True:
        is_percent = 'true'
    elif is_percent is False:
        is_percent = 'false'
    insert = (
    """
INSERT INTO
    stats (skill_type_id, is_percent, value)
VALUES
    ( ( SELECT
          skill_type_id
        FROM
          skill_types
        WHERE
          skill_type = '{}')
    , {}
    , {})
RETURNING
    stat_id
;
""".format(skill_type, is_percent, value))
    insert = normalize_spacing(insert)
    print(insert)
    return insert

def insert_rune(level, stars, position, rune_type, main_stat, fake, substat_1,
        substat_2, substat_3, substat_4):
    insert = (
"""
INSERT INTO
    runes (level, stars, position, rune_type_id, main_stat, fake_stat,
           substat_1, substat_2, substat_3, substat_4)
VALUES
    ({}
    , {}
    , {}
    ,  ( SELECT
            rune_type_id
        FROM
            rune_types
        WHERE
            rune_type = '{}')
    , {}, {}. {}, {}, {}, {})
RETURNING
    rune_id
;
""".format(level, stars, position, rune_type, main_stat, fake,
           substat_1, substat_2, substat_3, substat_4))
    insert = normalize_spacing(insert)
    print(insert)
    return insert

def full_insert_rune(level, stats, position, rune_type, main_stat, fake,
        substat_1, substat_2, substat_3, substat_4):
    stat_ids = []
    for stat in (main_stat, fake, substat_1, substat_2, substat_3, substat_4):
        insert_stat(**stat)
        ## insert_stat should return stat_id just created
        ## figure out how to make sure it returns null when appropriate
        ##stat_ids.append(stat_id)
    insert_rune(level, stats, position, rune_type, *stat_ids)
    ## return rune_id

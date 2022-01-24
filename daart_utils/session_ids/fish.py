"""Hard-coded session combinations for training/testing daart models on fish data."""

label_names = ['background', 'flaring', 'tailbeating']

# test ids that are not used for testing
SESS_IDS_TEST = [
    '1.1.1R',
    '1.1.28L',
    '1.2.28L',
    '2.1.1L',
    '2.1.28R',
    # '2.2.28L',
    # '3.1.28L',
    '3.2.28R',
    '4.1.28R',
    '4.2.28R',
    '5.1.1R',
    '5.1.2L',
]

SESS_IDS_TRAIN_10 = [[
    '1.1.1L',
    '1.1.28R',  # 546 flaring
    '1.2.28R',  # 80 flaring
    '2.1.1R',
    '2.1.28L',
    '2.2.28R',  # 86 flaring
    '3.1.28R',
    '3.2.28L',  # 1346 flaring
    '4.1.28L',
    '4.2.28L',
    '5.1.1L',
    '5.1.2R',
]]

# test ids that are not used for testing
# SESS_IDS_TEST = [
#     # '1.1.1L',
#     # '1.1.1R',
#     '1.1.28L',
#     '1.1.28R',  # 451 flaring
#     # '1.2.28L',
#     # '1.2.28R',  # 80 flaring
#     '2.1.28L',
#     '2.1.28R',
#     # '2.2.28L',  ?
#     '2.2.28R',  # 451 flaring
#     # '3.1.28L',
#     '3.1.28R',
#     '3.2.28L',  # 1346 flaring
#     '3.2.28R',
#     '4.1.28L',
#     '4.1.28R',
#     '4.2.28L',
#     '4.2.28R',
# ]
# SESS_IDS_TRAIN_10 = [[
#     '2.1.1L',
#     '2.1.1R',
#     '5.1.2L',
#     '5.1.2R',
#     '5.1.1L',
#     '5.1.1R',
# ]]

# commented out sessions don't have any tailbeating
SESS_IDS_ALL = [
    '1.1.1L',
    '1.1.1R',
    '1.1.28L',
    '1.1.28R',
    '1.2.28L',
    '1.2.28R',  #
    '2.1.1L',
    '2.1.1R',
    '2.1.28L',
    '2.1.28R',
    '2.2.28L',  #
    '2.2.28R',  #
    '3.1.28L',  #
    '3.1.28R',
    '3.2.28L',
    '3.2.28R',
    '4.1.28L',
    '4.1.28R',
    '4.2.28L',
    '4.2.28R',
    '5.1.1L',
    '5.1.1R',
    '5.1.2L',
    '5.1.2R',
]

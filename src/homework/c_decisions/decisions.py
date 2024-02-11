def get_options_ratio(option, total):
    if total == 0:
        return 0
    else:
        return option / total

def get_faculty_rating(ratio):
    # this should rate the ratio
    if ratio >= 0.9:
        return "excellent!"
    elif ratio > 0.8:
        return "very good."
    elif ratio > 0.7:
        return "good."
    elif ratio > 0.6:
        return "needs improvement."
    else:
        return "unacceptable."
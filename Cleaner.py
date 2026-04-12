def clean_heartrate_data(data: list) -> tuple:
    """
    Clean raw heart-rate data by removing malformed or impossible values.
    """
    cleaned_data = []
    removed_count = 0
    for line in data:
        if len(line) == 0 or not line.isdigit():
            data.remove(line)
            removed_count += 1
        else:
            line = int(line)
            cleaned_data.append(line)
    return cleaned_data, "rows skipped:",removed_count
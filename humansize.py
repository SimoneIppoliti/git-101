SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB']

def approximate_size(size = 10000):
    """ Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in byte

    Returns: string
    """
    multiple = 1024
    for suffix in SUFFIXES:
        size /= multiple
        if size < multiple:
            return f'{size} {suffix}'
    raise ValueError('Number too large')
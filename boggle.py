def make_grid(width, height):
    """
    Creates a grid that holds all tiles for the boggle game
    """
    return{(row, col):' ' for row in range(height)for col in range(width)
    }
    
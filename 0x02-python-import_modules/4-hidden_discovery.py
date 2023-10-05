#!/usr/bin/python3

if __name__ == "__main__":
    """This function give all name difined by hidden."""
    import hidden_4

    daniel = dir(hidden_4)
    for dan in daniel:
        if dan[:2] != "__":
            print(dan)

def styled(text, style):
    if (style == "red"):
        return "\033[31m"+ text + "\033[0m"
    if (style == "yellow"):
        return "\033[33m"+ text + "\033[0m"
    if (style == "green"):
        return "\033[32m"+ text + "\033[0m"
    if (style == "bold"):
        return "\033[1m"+ text + "\033[0m"


def print_error(text):
    print(styled("Ошибка.", "red") + " " + text)

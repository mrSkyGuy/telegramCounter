import rich


def print_name():
    print(
        """
████████╗░██████╗░░█████╗░░█████╗░██╗░░░██╗███╗░░██╗████████╗███████╗██████╗░
╚══██╔══╝██╔════╝░██╔══██╗██╔══██╗██║░░░██║████╗░██║╚══██╔══╝██╔════╝██╔══██╗
░░░██║░░░██║░░██╗░██║░░╚═╝██║░░██║██║░░░██║██╔██╗██║░░░██║░░░█████╗░░██████╔╝
░░░██║░░░██║░░╚██╗██║░░██╗██║░░██║██║░░░██║██║╚████║░░░██║░░░██╔══╝░░██╔══██╗
░░░██║░░░╚██████╔╝╚█████╔╝╚█████╔╝╚██████╔╝██║░╚███║░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░░╚═════╝░░╚════╝░░╚════╝░░╚═════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
"""
    )


def print_info():
    def raw_info(s):
        res = ""
        is_opened_bracket = False
        for symbol in s:
            if symbol == "[":
                is_opened_bracket = True
            if symbol == "]":
                is_opened_bracket = False
                continue
            if is_opened_bracket:
                continue
            res += symbol
        return res

    def get_info(s):
        return "| " + s.strip() + " " * (max_length - len(raw_info(s))) + " |"

    info = [
        "A tool for getting [b red]statistics[/b red] of the history of messages in the",
        "[i cyan]telegram messenger[/i cyan]"
    ]

    max_length = max([len(raw_info(line.strip())) for line in info])
    border = "+-" + "-" * (max_length) + "-+"

    print(border)
    for line in info:
        rich.print(get_info(line))
    print(border)


def print_commands():
    ...


if __name__ == "__main__":
    print_name()
    print_info()
    print_commands()
    input()

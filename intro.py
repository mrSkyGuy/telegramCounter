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
        "[i cyan]telegram messenger[/i cyan]",
        "",
        "[bold purple]Author[/bold purple]: [bold underline]SkyGuy[/bold underline]",
        "[bold purple]Link on github[/bold purple]: [bold underline]https://github.com/mr-skydev[/bold underline]",
        "[bold purple]Link on Telegram[/bold purple]: [bold underline]https://t.me/skyguy[/bold underline]",
        "If u have any questions or ideas, plz [bold green]chat me[/bold green] <3"
    ]

    max_length = max([len(raw_info(line.strip())) for line in info])
    border = "+-" + "-" * (max_length) + "-+"

    print(border)
    for line in info:
        if line:
            rich.print(get_info(line))
        else:
            print("| " + "-" * max_length + " |")
    print(border)


def print_commands():
    rich.print("\n[bold red underline]COMMANDS:[/bold red underline]")
    rich.print("- [bold purple][1][/bold purple] show top 10 the most common words")
    rich.print("- [bold purple][2][/bold purple] show the top 10 days on which the most messages were sent")
    rich.print("- [bold purple][3][/bold purple] show the average number of messages per day")
    rich.print("- [bold purple][4][/bold purple] show the most active interlocutor")


if __name__ == "__main__":
    print_name()
    print_info()
    print_commands()
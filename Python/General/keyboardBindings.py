import keyboard
import subprocess


def volume_up():
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "+5%"])


def volume_down():
    subprocess.run(["pactl", "set-sink-volume", "@DEFAULT_SINK@", "-5%"])


def mute():
    subprocess.run(["pactl", "set-sink-mute", "@DEFAULT_SINK@", "toggle"])


def play_pause():
    subprocess.run(["playerctl", "play-pause"])


def next_track():
    subprocess.run(["playerctl", "next"])


def previous_track():
    subprocess.run(["playerctl", "previous"])


def main():
    print("Press 'u' to increase volume")
    print("Press 'd' to decrease volume")
    print("Press 'm' to mute/unmute")
    print("Press 'p' to play/pause")
    print("Press 'n' to skip to the next track")
    print("Press 'b' to go back to the previous track")
    print("Press 'q' to quit")

    keyboard.add_hotkey("u", volume_up)
    keyboard.add_hotkey("d", volume_down)
    keyboard.add_hotkey("m", mute)
    keyboard.add_hotkey("p", play_pause)
    keyboard.add_hotkey("n", next_track)
    keyboard.add_hotkey("b", previous_track)

    keyboard.wait("q")
    print("Quitting...")


if __name__ == "__main__":
    main()

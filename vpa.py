from mptpkg import voice_to_text, print_say
import mywakeup, timer, timer2, joke, myemail

# Put the script in standby
while True:
    # Capture your voice command quietly in standby mode
    wake_up = wakeup()
    # Wakeup VPA saying "Hello python"
    while wake_up == 'Activated':
        print_say("How may I help you?")
        inp = voice_to_text().lower()
        print_say(f"You said: {inp}")
        if 'back' in inp and 'stand' in inp:
            print_say("Ok, back to standby; let me know if you need help!")
            break
        # Activate the timer module
        elif 'timer for' in inp and ("hour" in inp or "minute" in inp or "second" in inp):
            timer(inp)
            continue
        # Activate the alarm module
        elif 'alarm for' in inp and ("a.m." in inp or "p.m." in inp):
            alarm(inp)
            continue
        # Activate the joke module
        elif 'joke' in inp:
            joke()
            continue
        # Activate the email module
        elif 'send' in inp and "email" in inp:
            email()
            continue
        else:
            continue
    if wake_up == 'ToQuit':
        print_say("Shutting down. Goodbye!")
        break
            
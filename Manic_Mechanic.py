# Manic Mechanic - Halloween 2014
# by Sean Clay
# Rev. 1.5.0 - 10/31/2014
# Relays added in 1.2.0
# Twitch removed and Insults removed in 1.3.0
# Reworked the kicking routine and added endless loop with 'try' 1.4.0
# Final version of this program for 2014
# Made a change on this line

# Initialize
import pygame, time, sys
from pylibftdi import BitBangDevice
pygame.mixer.pre_init(44100, -16, 2, 4096)
pygame.init()

def buttonPressed():
        pygame.mixer.music.stop()
        relay_on(fog_strobe)
        print ("Strobe & Fog on!")
        pygame.init()
        pygame.mixer.music.load(bad_sound[0])
        pygame.mixer.music.play()
        print ("Playing Gone Bad Sound Effects")
        time.sleep (9)
        print ("Start kicking legs!")
        relay_on(leg_kick)
        time.sleep(15)
        relay_off(leg_kick)
        print ("Stop kicking legs!")
        relay_off(fog_strobe)
        print ("Stop Fog & Strobe!")
        pygame.mixer.music.stop()
        time.sleep(10)
        print ("Done with playing this sound")
        relay_off(255) # All Relays Off!


def relay_on(relay):
        with BitBangDevice() as bb:
            bb.port |= relay

def relay_off(relay):
        with BitBangDevice() as bb:
            bb.port &= ~relay

good_sound = ['TurnTheKey.wav', 'AFewAdjustments.wav', 'StartsRunsDies.wav', 'ABitMore.wav']
bad_sound = ['AllGoneBad.wav']

# Assign Relays - All accessed by binary numbers 1 - 128
fog_strobe = 1  # Relay #1 Strobe light & Fog machine
leg_kick = 2    # Relay #2 Kick Legs

max_good = len(good_sound)-1
max_bad = len(bad_sound)-1
good = 0 # Counter for which 'good' sound we are on
bad = 0  # Plays different 'bad' sound (not functional yet)


# Main Loop
while 1 == 1:
    try:
        # All Good
        pygame.init()
        pygame.mixer.music.load(good_sound[good])
        pygame.mixer.music.set_volume(1)
        print ("Loaded ", good_sound[good])
        good = good + 1
        if good > max_good:
            good = 0
            print ("stupid routine to trigger gone bad")
            buttonPressed()
            pygame.mixer.music.load(good_sound[good])

        print ("good=",good)
        print ("all relays off, stupid")
        relay_off(255) # All Relays Off!
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        time.sleep(4) #time between next sound
    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        break
print ("All done!")

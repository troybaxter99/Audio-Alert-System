from subprocess import call
from os import walk

class AUDIO:
    # espeak commands
    espeak_beg = 'espeak '
    espeak_end = ' 2>/dev/null'
    espeak_gap = '-g'
    
    # Aplay command
    aplay_cmd = 'aplay '
    
    # Initializes AUDIO Class.
    # *** If desired, the user can change the location of the audio files that will be called. Must include '/' at end
    # *** Otherwise, the class defaults to the Audio Alert System's Audio-Files directory.
    def __init__(self, newAudioLocation = "/home/pi/Audio-Alert-System/Audio-Files/"):
        self.audioLoc = newAudioLocation
        self.gap = 0 # 0 centi-second gap between each word
    
    # This function's purpose is to allow the user to enter a desired delay between each word
    # set_espeak_gap takes a time value in ms and sets the gap time in centiseconds
    def set_espeak_gap(self, time_ms):
        self.gap = time_ms/10
    
    
    # This function's purpose is to play a desired message through espeak
    def play_message(self, message):
        # Create command message to be sent to terminal
        cmd_message = ' "' + message + '"'
        command = self.espeak_beg + self.espeak_gap + str(self.gap) + cmd_message + self.espeak_end
        
        # Call terminal with espeak message
        call([command], shell = True)
    
    
    # This function's purpose is to play a called audio file.
    # ***This audio file must exist***
    def play_audio(self, audioFile):
        # Create command to be sent to the terminal
        audio_cmd = self.audioLoc + audioFile
        command = self.aplay_cmd + audio_cmd
        
        # Call terminal with desired audio file
        call([command], shell = True)
            
    # The purpose of this function is to list all .wav files in a folder  
    def list_audio(self):
        # Gets list of all files in audioLoc directory
        filenames = next(walk(self.audioLoc), (None, None, []))[2] # [] if no file
        
        # Prints all file names that end in .wav
        for file in filenames:
            if (file[-4:] == ".wav"):
                print("\t" + file)

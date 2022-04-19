from subprocess import call

# Beginning and end of command line commands to call espeak. Speech will be inserted between these two variables
cmd_beg = 'espeak '
cmd_end = ' 2>/dev/null'

# Alert to Command Line
alert = "OVER HEATING!"
cmd_alert = ' "' + alert + '"'

# Gap between words
gap = 10 # centiseconds
cmd_gap = '-g' +  str(gap)

# Command to be sent to command line
command = cmd_beg + cmd_gap + cmd_alert + cmd_end
print(command)

# Play Audio File
audioFile = 'Gary-Come-Home.wav'
audioLocation = '/home/pi/Audio-Alert-System/Audio-Files/'
cmd_audio = 'aplay '

audioCommand = cmd_audio + audioLocation + audioFile

# Call Commands
call([command], shell=True)
call([audioCommand], shell=True)

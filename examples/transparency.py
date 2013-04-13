import atexit

import pywingo

# The transparency to use for unfocused and focused clients.
# 1 is completely opaque and 0 is completely transparent.
alpha = {
    'unfocused': 0.85,
    'focused': 1.0,
}

# Does the initial connection with Wingo. `w` can now be used to run commands.
w = pywingo.Wingo()

# Use Python decorators to bind functions to specific events.
@w.bind('FocusedClient')
def focused(ev):
    w.SetOpacity(ev.Id, alpha['focused'])

@w.bind('UnfocusedClient')
def focused(ev):
    w.SetOpacity(ev.Id, alpha['unfocused'])

# Set the transparency of all clients upon subscription.
@w.bind('Subscribed')
def startup(ev):
    active = w.GetActive()
    for cid in w.GetAllNormalClients():
        if cid == active:
            w.SetOpacity(cid, alpha['focused'])
        else:
            w.SetOpacity(cid, alpha['unfocused'])

# Use the special `atexit.register` decoration in the Python standard
# library to do any clean up if your program quits.
@atexit.register
def shutdown():
    # If the program quits unexpectedly, return opacity
    # to normal levels.
    for cid in w.GetAllNormalClients():
        w.SetOpacity(cid, 1.0)

# Start the main event loop. This should be the last thing in your program.
w.loop()


import sys

import pywingo

W = pywingo.Wingo()

@W.bind('ChangedActiveClient')
@W.bind('ChangedClientName')
@W.bind('Subscribed')
def changed_active(_):
    print W.GetClientName(W.GetActive())
    sys.stdout.flush()

W.loop()


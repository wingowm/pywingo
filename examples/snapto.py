import sys

import pywingo

if len(sys.argv) != 3 \
    or sys.argv[1] not in ('grow', 'shrink', 'move') \
    or sys.argv[2] not in ('top', 'bot', 'left', 'right'):
    print >> sys.stderr, \
             'Usage: snapto (grow | shrink | move) (top | bot | left | right)'
    sys.exit(1)

def edges(client):
    '''
    Returns a dictionary of edges for the given client.
    '''
    eleft, etop = W.GetClientX(client), W.GetClientY(client)
    w, h = W.GetClientWidth(client), W.GetClientHeight(client)
    eright, ebot = eleft + w, etop + h
    return {
        'left': eleft, 'top': etop,
        'right': eright, 'bot': ebot,
    }

def flatten(lst):
    '''
    Flattens a list: [[a]] -> [a].
    '''
    flattened = []
    for sublst in lst:
        for x in sublst:
            flattened.append(x)
    return flattened

def newpos(vertical, order, default, include):
    '''
    Finds a new edge for the client from a list of edges corresponding
    to all relevant surfaces.

    `vertical` should be True if the client is moving/growing/shrinking in
    a vertical direction (top/bot). Should be False otherwise.

    `order` should either be `min` or `max`, and is used to retrieve the
    next edge to move/grow/shrink to from a list of candidate edges.

    `default` is the edge of last resort if no other edges were found.
    (e.g., the head boundary.)

    `include` is the comparison criterion for edges. It should return
    True if the given edge is a possible choice.
    (e.g., all edges less than the active client's left edge when
           growing in the left direction.)
    '''
    def extract(edges):
        if vertical:
            return [edges['top'], edges['bot']]
        else:
            return [edges['left'], edges['right']]
    candidates = filter(include, flatten(map(extract, alledges)))
    return order(candidates) if candidates else default

# Initialization. Connect and grab the edges/geometry of the active client.
action = sys.argv[1]
direction = sys.argv[2]
W = pywingo.Wingo()

win = W.GetActive()
if not W.MatchClientMapped(win):
    print >> sys.stderr, 'Window %d is not visible' % win
    sys.exit(1)
wine = edges(win)
wine_width = wine['right'] - wine['left']
wine_height = wine['bot'] - wine['top']

# Find the geometry of the active head and compute the edges for all
# clients on the head.
wrk = W.GetClientWorkspace(win)
head = W.WorkspaceHead(wrk)
headw, headh = W.GetHeadWidth(head), W.GetHeadHeight(head)
clients = filter(lambda c: W.MatchClientMapped(c), W.GetClientList(wrk))
alledges = []
for c in clients:
    if c == win:
        continue
    alledges.append(edges(c))

def grow():
    if direction == 'top':
        newtop = max(0, newpos(True, max, 0, lambda e: e < wine['top']))

        W.MoveRelative(win, wine['left'], newtop)
        W.Resize(win, wine_width, wine_height + wine['top'] - newtop)
    elif direction == 'left':
        newleft = max(0, newpos(False, max, 0, lambda e: e < wine['left']))

        W.MoveRelative(win, newleft, wine['top'])
        W.Resize(win, wine_width + wine['left'] - newleft, wine_height)
    elif direction == 'bot':
        newbot = min(headh, newpos(True, min, headh, lambda e: e > wine['bot']))

        W.Resize(win, wine_width, newbot - wine['top'])
    elif direction == 'right':
        newright = newpos(False, min, headw, lambda e: e > wine['right'])
        newright = min(headw, newright)

        W.Resize(win, newright - wine['left'], wine_height)
    else:
        assert False, 'bug'

def shrink():
    if direction == 'top':
        newtop = newpos(True, min, wine['top'],
                        lambda e: e > wine['top'] and e < wine['bot'])

        print newtop
        # W.MoveRelative(win, wine['left'], newtop) 
        # W.Resize(win, wine_width, wine_height + wine['top'] - newtop) 
    elif direction == 'left':
        newleft = newpos(False, max, 0, lambda e: e < wine['left'])

        W.MoveRelative(win, newleft, wine['top'])
        W.Resize(win, wine_width + wine['left'] - newleft, wine_height)
    elif direction == 'bot':
        newbot = newpos(True, min, headh, lambda e: e > wine['bot'])

        W.Resize(win, wine_width, newbot - wine['top'])
    elif direction == 'right':
        newright = newpos(False, min, headw, lambda e: e > wine['right'])

        W.Resize(win, newright - wine['left'], wine_height)
    else:
        assert False, 'bug'

if action == 'grow':
    grow()
elif action == 'shrink':
    shrink()
else:
    assert False, 'bug'

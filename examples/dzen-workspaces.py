import sys

import pywingo

markup = {
    'current':  '^fg(#00FF00)%s^fg()',
    'visible':  '^fg(#FF0000)%s^fg()',
    'hidden':   '^fg(#FFA500)%s^fg()',
    'empty':    '^fg(#FFFFFF)%s^fg()',
}

W = pywingo.Wingo()

@W.bind('AddedWorkspace')
@W.bind('RemovedWorkspace')
@W.bind('ChangedWorkspace')
@W.bind('ChangedVisibleWorkspace')
@W.bind('ChangedWorkspaceNames')
@W.bind('ManagedClient')
@W.bind('UnmanagedClient')
@W.bind('Subscribed')
def show(_):
    current = W.GetWorkspace()
    visible = W.GetVisibleWorkspaceList()
    hidden = W.GetHiddenWorkspaceList()

    vtagged = []
    for space in visible:
        if space == current:
            vtagged.append(markup['current'] % space)
        else:
            vtagged.append(markup['visible'] % space)
    htagged = []
    for space in hidden:
        if W.IsEmpty(space):
            htagged.append(markup['empty'] % space)
        else:
            htagged.append(markup['hidden'] % space)

    print '[%s] %s' % (' '.join(vtagged), ' '.join(htagged))
    sys.stdout.flush()

W.loop()


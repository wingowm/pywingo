package main

import (
	"bytes"
	"fmt"
	"sort"
	"strings"

	"github.com/BurntSushi/ty/fun"
	"github.com/BurntSushi/wingo/commands"
)

var (
	pyInstances = map[string]string{
		"string": "basestring",
		"int": "int",
		"float": "float",
	}
)

func main() {
	cmds := allCommands()

	fmt.Println("class WingoCommands(object):")
	fmt.Println("    def __init__(self):")
	fmt.Println("        assert False, 'cannot create WingoCommands directly'")
	fmt.Println("")

	for _, c := range cmds {
		fmt.Println(c)
		fmt.Println("")
	}
}

type cmd struct {
	Name string
	ArgNames []string
	ArgTypes [][]string
	Help string
}

func (c cmd) String() string {
	buf := new(bytes.Buffer)
	out := func(indent int, format string, v ...interface{}) {
		fmt.Fprintf(buf, strings.Repeat("    ", indent) + format, v...)
	}

	out(1, "def %s(%s):\n", c.Name,
		strings.Join(append([]string{"self"}, c.ArgNames...), ", "))
	out(2, "'''\n%s\n        '''\n", c.Help)

	// Do some type checking on arguments to make debugging for
	// Pythonistas less painful.
	if len(c.ArgNames) > 0 {
		for i := 0; i < len(c.ArgNames); i++ {
			arg := c.ArgNames[i]

			toPyInstance := func(t string) string { return pyInstances[t] }
			types := fun.Map(toPyInstance, c.ArgTypes[i]).([]string)
			out(2, "self._assert_arg_type('%s', %s, [%s])\n",
				arg, arg, strings.Join(types, ", "))
		}
	}

	out(0, "\n")
	out(2, "arg_str = self._gribble_arg_str([%s])\n",
		strings.Join(c.ArgNames, ", "))
	out(2, "val = self.gribble('%s %%s' %% arg_str)\n", c.Name)
	out(2, "return self._from_str('%s', val)", c.Name)

	return buf.String()
}

func allCommands() []cmd {
	cmds := make([]cmd, 0, 10)
	commands.Env.Each(func(name, help string) {
		argNames := commands.Env.ArgNames(name)
		argTypes := commands.Env.ArgTypes(name)
		if len(argNames) != len(argTypes) {
			panic("arguments is not same length as arg types for " + name)
		}
		cmds = append(cmds, cmd{name, argNames, argTypes, help})
	})
	sort.Sort(cmdsAlpha(cmds))
	return cmds
}

type cmdsAlpha []cmd

func (cs cmdsAlpha) Len() int {
	return len(cs)
}

func (cs cmdsAlpha) Swap(i, j int) {
	cs[i], cs[j] = cs[j], cs[i]
}

func (cs cmdsAlpha) Less(i, j int) bool {
	return cs[i].Name < cs[j].Name
}

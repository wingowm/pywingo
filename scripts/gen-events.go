package main

import (
	"fmt"
	"go/ast"
	"go/parser"
	"go/token"
	"log"
	"os"
	"path"
	"strings"

	"github.com/BurntSushi/ty/fun"
)

func main() {
	if len(os.Args) != 2 {
		log.Fatalf("Usage: %s path/to/wingo/event/events.go",
			path.Base(os.Args[0]))
	}
	gosrc := os.Args[1]

	fset := token.NewFileSet()
	f, err := parser.ParseFile(fset, gosrc, nil, 0)
	if err != nil {
		log.Fatalf("go/parser error: %s", err)
	}

	fmt.Println("from collections import namedtuple\n\n")

	typeName := ""
	ast.Inspect(f, func(n ast.Node) bool {
		switch node := n.(type) {
		case *ast.TypeSpec:
			typeName = node.Name.Name
		case *ast.StructType:
			fields := make([]string, 0)
			for _, fieldDecl := range node.Fields.List {
				for _, field := range fieldDecl.Names {
					fields = append(fields, field.Name)
				}
			}
			printEvent(typeName, fields)
		}
		return true
	})
}

func printEvent(typeName string, fields []string) {
	index := func(f string) string { return "j['" + f + "']" }
	indexed := fun.Map(index, fields).([]string)
	fmt.Printf("def _new_%s(j):\n", typeName)
	fmt.Printf("    assert j['EventName'] == '%s'\n", typeName)
	fmt.Printf("    return %s(%s)\n", typeName, strings.Join(indexed, ", "))

	quote := func(f string) string { return "'" + f + "'" }
	quoted := fun.Map(quote, fields).([]string)
	fmt.Printf("%s = namedtuple('%s', [%s])\n\n\n", typeName, typeName,
		strings.Join(quoted, ", "))
}

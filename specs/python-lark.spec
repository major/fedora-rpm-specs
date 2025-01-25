Name:           python-lark
Version:        1.2.2
Release:        %autorelease
Summary:        Lark is a modern general-purpose parsing library for Python
# License breakdown:
# lark/tools/standalone.py - MPL-2.0
# lark/__pyinstaller/hook-lark.py - GPL-2.0-or-later
# the rest is MIT
License:        MIT AND MPL-2.0 AND GPL-2.0-or-later
Url:            https://github.com/lark-parser/lark
Source:         %{pypi_source lark}

# Python 3.14 compatibility
Patch:          https://github.com/lark-parser/lark/pull/1483.patch

BuildArch:      noarch

%description
Lark is a modern general-purpose parsing library for Python.

Lark focuses on simplicity and power. It lets you choose between
two parsing algorithms:

Earley : Parses all context-free grammars (even ambiguous ones)!
It is the default.

LALR(1): Only LR grammars. Outperforms PLY and most if not all
other pure-python parsing libraries.

Both algorithms are written in Python and can be used interchangeably
with the same grammar (aside for algorithmic restrictions).
See "Comparison to other parsers" for more details.

Lark can auto magically build an AST from your grammar, without any
more code on your part.

Features:

- EBNF grammar with a little extra
- Earley & LALR(1)
- Builds an AST auto magically based on the grammar
- Automatic line & column tracking
- Automatic token collision resolution (unless both tokens are regexps)
- Python 2 & 3 compatible
- Unicode fully supported

%package -n python3-lark
Summary:        %{summary}
BuildRequires:  python3-devel
%py_provides    python3-lark-parser
Obsoletes:      python3-lark-parser < 1

%description -n python3-lark
Lark is a modern general-purpose parsing library for Python. With Lark, you can
parse any context-free grammar, efficiently, with very little code.

Main Features:
    - Builds a parse-tree (AST) automagically, based on 
      the structure of the grammar
    - Earley parser
    - Can parse all context-free grammars
    - Full support for ambiguous grammars
    - LALR(1) parser
    - Fast and light, competitive with PLY
    - Can generate a stand-alone parser
    - CYK parser, for highly ambiguous grammars
    - EBNF grammar
    - Unicode fully supported
    - Automatic line & column tracking
    - Standard library of terminals (strings, numbers, names, etc.)
    - Import grammars from Nearley.js
    - Extensive test suite
    - And much more! Since version 1.0, only Python versions 3.6 and up
      are supported.

%prep
%autosetup -p1 -n lark-%{version}

# Fix wrong-file-end-of-line-encoding.
sed -i 's/\r$//' README.md examples/*.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lark

%check
%{python3} -m tests

%files -n python3-lark -f %{pyproject_files}
%doc README.md examples

%changelog
%autochangelog

%global giturl  https://github.com/mjambon/yamlx

Name:           ocaml-yamlx
Version:        0.3.0
Release:        %autorelease
Summary:        Pure OCaml YAML 1.2 parser with lossless comment-preserving AST

License:        AGPL-3.0-only
URL:            https://mjambon.github.io/yamlx/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/yamlx-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.14.0
%ifarch %{x86_64}
BuildRequires:  ocaml-afl-persistent-devel
%endif
BuildRequires:  ocaml-dune >= 3.20
BuildRequires:  ocaml-ppx-deriving-devel
BuildRequires:  ocaml-testo-devel
BuildRequires:  ocaml-yaml-devel

%description
A pure-OCaml YAML 1.2 and 1.1 library with a lossless, comment-preserving AST.
Features:

- Full YAML 1.2 compliance — passes all 371 tests from the yaml-test-suite.
- Pure OCaml — no C bindings, no external runtime dependencies.
- Lossless AST — the parsed node tree preserves scalar styles (plain,
  'single-quoted', "double-quoted", | literal, > folded), flow vs. block
  collection style, tags, anchors, and source positions.
- Best-effort comment preservation — standalone (head) comments before a node,
  inline (line) comments after a value, and trailing (foot) comments after the
  last item of a block collection are attached to the nearest node and
  re-emitted by the printer.
- Pretty-printer — `Nodes.to_yaml` serializes a node list back to a YAML
  string, preserving all of the above.
- Plain-YAML printer — `Nodes.to_plain_yaml_exn` produces a restricted subset
  with no anchors, no aliases (expanded inline), no tags, no flow collections,
  and no complex mapping keys — the fragment of YAML that most people
  recognize on sight.
- Typed-value resolver — `Values.of_yaml` applies the YAML 1.2 JSON schema and
  returns value list with `Null | Bool | Int | Float | String | Seq | Map`
  constructors.
- Multi-document streams — both the node and value APIs handle streams
  containing more than one ----separated document.
- Correct anchor scoping — anchors are document-local; an alias in document N
  cannot refer to an anchor defined in document N−1.
- Structured errors — `Scan_error` and `Parse_error` carry a pos record with
  line, column, and byte offset.  `catch_errors` wraps any of these into a
  `(_, string)` result with a human-readable message, optionally prefixed with
  a file name.
- Command-line tool — the yamlx binary reads YAML from a file or stdin and
  prints it in one of several formats.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n yamlx-%{version}

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE

%files devel -f .ofiles-devel

%changelog
%autochangelog

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

Name:           not-ocamlfind
Version:        0.14
Release:        %autorelease
Summary:        Front-end to ocamlfind that adds a few new commands

License:        MIT
URL:            https://github.com/chetmurthy/not-ocamlfind
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  m4
BuildRequires:  ocaml
BuildRequires:  ocaml-camlp-streams-devel
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib-devel >= 1.8.0
BuildRequires:  ocaml-fmt-devel >= 0.8.8
BuildRequires:  ocaml-ocamlgraph-devel >= 2.0.0
BuildRequires:  ocaml-rresult-devel >= 0.6.0
BuildRequires:  which

Requires:       ocaml-findlib%{?_isa}

Recommends:     %{py3_dist xdot}

%description
The command not-ocamlfind is a pass-thru to ocamlfind, but adds three
new commands: preprocess, reinstall-if-diff and package-graph.

- reinstall-if-diff does what it says on the label: only reinstalls
  (remove then install) if the file-content of the package has changed.

- preprocess produces the source and does not attempt to compile it; as
  an added benefit, it prints (to stderr) the commands it executed to
  produce that source.   So you can use this for debugging multi-stage
  PPX rewriter sequences.

- package-graph outputs a graph in the format accepted by the dot
  command of graphviz.  By default you get the package-dependency graph,
  with sizes of the archives for each packages as part of the
  node-label.  If you add -dominator-from <node>, it will compute the
  dominator-tree from that node, and if you add -xdot, it will
  automatically invoke xdot on the graph.

%prep
%autosetup

%build
# The build wants us to use a patched vendored version of findlib.  However,
# the findlib in Fedora already has the patches, and is a later version.  Do
# not use the configure script or Makefile until it is possible to build
# without the vendored findlib.
%ifarch %{ocaml_native_compiler}
ocamlfind ocamlopt \
  -I +findlib findlib.cmxa \
%else
ocamlfind ocamlc \
  -I +findlib findlib.cma \
%endif
  -g \
  -package str,unix,fmt,rresult,ocamlgraph,camlp-streams \
  -linkall \
  -linkpkg \
  fsmod.ml frontend.ml main.ml \
  -o not-ocamlfind

%ifarch %{ocaml_native_compiler}
ocamlfind ocamlopt \
  -I +findlib findlib.cmxa \
%else
ocamlfind ocamlc \
  -I +findlib findlib.cma \
%endif
  -g \
  -package str,unix,compiler-libs.common \
  -linkall \
  -linkpkg \
  papr_official.ml \
  -o papr_official.exe

%install
# The makefile ignores DESTDIR, and there are only 4 files to install anyway...
mkdir -p %{buildroot}%{_bindir}
cp -p not-ocamlfind %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{ocamldir}/not-ocamlfind
cp -p META opam papr_official.exe %{buildroot}%{ocamldir}/not-ocamlfind

%check
# Upstream provides no tests, so we just check that simple usage gives us a
# zero exit code
./not-ocamlfind package-graph -predicates true -package findlib

%files
%doc CHANGES README.md
%license LICENSE
%{_bindir}/not-ocamlfind
%{ocamldir}/not-ocamlfind/

%changelog
%autochangelog

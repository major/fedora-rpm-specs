%global giturl  https://github.com/ocaml-ppx/ppxlib

Name:           ocaml-ppxlib
Epoch:          1
Version:        0.35.0
Release:        %autorelease
Summary:        Base library and tools for ppx rewriters

License:        MIT
URL:            https://ocaml-ppx.github.io/ppxlib/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/ppxlib-%{version}.tar.gz
# Fedora does not have, and does not need, stdlib-shims
Patch:          %{name}-stdlib-shims.patch

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-cinaps-devel >= 0.12.1
BuildRequires:  ocaml-cmdliner-devel >= 1.3.0
BuildRequires:  ocaml-compiler-libs-janestreet-devel >= 0.11.0
BuildRequires:  ocaml-dune >= 3.8
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ppx-derivers-devel >= 1.0
BuildRequires:  ocaml-re-devel >= 1.9.0
BuildRequires:  ocaml-sexplib0-devel >= 0.15

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

# This can be removed when F40 reaches EOL
Obsoletes:      %{name}-doc < 1:0.26.0-3

%description
The ppxlib project provides the basis for the ppx system, which is
currently the officially supported method for meta-programming in Ocaml.
It offers a principled way to generate code at compile time in OCaml
projects.  It features:
- an OCaml AST / parser/ pretty-printer snapshot, to create a full
  frontend independent of the version of OCaml;
- a library for ppx rewriters in general, and type-driven code generators
  in particular;
- a full-featured driver for OCaml AST transformers;
- a quotation mechanism for writing values representing OCaml AST in the
  OCaml syntax;
- a generator of open recursion classes from type definitions.

%package        tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description    tools
The %{name}-tools package contains command line tools for
%{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       %{name}-tools%{?_isa} = 1:%{version}-%{release}
Requires:       ocaml-compiler-libs-janestreet-devel%{?_isa}
Requires:       ocaml-ppx-derivers-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%prep
%autosetup -n ppxlib-%{version} -p1

%build
# Do not build the benchmark suite
%dune_build -p ppxlib,ppxlib-tools

%install
# Do not install the benchmark suite
%dune_install -s ppxlib ppxlib-tools

# Merge the tools devel package into the tools package
cat .ofiles-ppxlib-tools-devel >> .ofiles-ppxlib-tools

%check
# Do not run the benchmark suite
%dune_check -p ppxlib,ppxlib-tools

%files -f .ofiles-ppxlib
%doc CHANGES.md HISTORY.md README.md
%license LICENSE.md

%files tools -f .ofiles-ppxlib-tools

%files devel -f .ofiles-ppxlib-devel

%changelog
%autochangelog

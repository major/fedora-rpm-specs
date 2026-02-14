# Whether to build the manual
%bcond manual %[!0%{?rhel}]

%global giturl  https://gitlab.inria.fr/fpottier/menhir

Name:           ocaml-menhir
Version:        20260209
Release:        %autorelease
Summary:        LR(1) parser generator for OCaml

# The generator is GPL-2.0-only
License:        GPL-2.0-only
URL:            https://gallium.inria.fr/~fpottier/menhir/
VCS:            git:%{giturl}.git
Source:         %{giturl}/-/archive/%{version}/menhir-%{version}.tar.bz2

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml
BuildRequires:  ocaml-dune

%if %{with manual}
BuildRequires:  ImageMagick
BuildRequires:  hevea
BuildRequires:  tex(latex)
BuildRequires:  tex(moreverb.sty)
BuildRequires:  tex(stmaryrd.sty)
BuildRequires:  texlive-times
%endif

Provides:       bundled(ocaml-fix) = 20250919
Provides:       bundled(ocaml-pprint) = 20230830

Requires:       ocaml-menhirlib-devel%{?_isa} = %{version}-%{release}

# This can be removed when F42 reaches EOL
Obsoletes:      coq-menhirlib < 20230608-1

%description
Menhir is a LR(1) parser generator for the Objective Caml programming
language.  That is, Menhir compiles LR(1) grammar specifications down to OCaml
code.  Menhir was designed and implemented by François Pottier and Yann
Régis-Gianas.

%package     -n ocaml-menhirlib
Summary:        Runtime library for parsers produced by Menhir
# The library is LGPL-2.0-only with a linking exception.
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception

%description -n ocaml-menhirlib
This package contains the runtime library for parsers produced by Menhir.

%package     -n ocaml-menhirlib-devel
Summary:        Development files for ocaml-menhirlib
# The library is LGPL-2.0-only with a linking exception.
License:        LGPL-2.0-only WITH OCaml-LGPL-linking-exception
Requires:       ocaml-menhirlib%{?_isa} = %{version}-%{release}

%description -n ocaml-menhirlib-devel
This ocaml-menhirlib-devel package contains libraries and signature files for
building applications with a parser produced by Menhir.

%prep
%autosetup -n menhir-%{version}

%build
%dune_build

%if %{with manual}
cd doc
rm manual.pdf
pdflatex -interaction=nonstopmode manual
bibtex manual
pdflatex -interaction=nonstopmode manual
pdflatex -interaction=nonstopmode manual
pdflatex -interaction=nonstopmode manual
cd -
%endif

%install
%dune_install -s

# We do not install *.ml files by default, but this one is needed
cp -p _build/default/lib/pack/menhirLib.ml %{buildroot}%{ocamldir}/menhirLib

# Even though coq is disabled, dune still puts a META file and dune-package here
rm -rf %{buildroot}%{ocamldir}/coq-menhirlib/

# Put something interesting into the main package META file
cat > %{buildroot}%{ocamldir}/menhir/META << EOF
version = "%{version}"
description = "Menhir command-line tool"
requires = ""
EOF

%files
%if %{with manual}
%doc doc/manual.pdf
%endif
%license LICENSE
%{_bindir}/menhir
%{_mandir}/man1/menhir.1*
%{ocamldir}/menhir/
%{ocamldir}/menhirCST/
%{ocamldir}/menhirGLR/
%{ocamldir}/menhirSdk/

%files -n ocaml-menhirlib -f .ofiles-menhirLib
%license LICENSE

%files -n ocaml-menhirlib-devel -f .ofiles-menhirLib-devel

%changelog
%autochangelog

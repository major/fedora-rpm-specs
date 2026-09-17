Name:           ocaml-stdcompat
Version:        22.0
Release:        %autorelease
Summary:        Compatibility module for the OCaml standard library

License:        LGPL-2.1-or-later
URL:            https://github.com/ocamllibs/stdcompat
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/stdcompat-%{version}.tar.gz
# Temporary patch to support OCaml 5.5.1
Patch:          %{name}-ocaml5.5.1.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildRequires:  ocaml >= 4.11
BuildRequires:  ocaml-dune >= 2.0

%description
Stdcompat is a compatibility layer allowing programs to use some recent
additions to the OCaml standard library while preserving the ability to be
compiled on former versions of OCaml.

The Stdcompat API is not intended to be stable, but there will be efforts to
allow future versions of Stdcompat to be compiled on a large range of versions
of OCaml: Stdcompat should compile (at least) on every version of OCaml from
3.08 (inclusive).

The module Stdcompat provides some definitions for values and types introduced
in recent versions of the standard library.  These definitions are just
aliases to the matching definition of the standard library if the latter is
recent enough.  Otherwise, the module Stdcompat provides an alternative
implementation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n stdcompat-%{version} -p1

%check
sed -r \
    -e 's/.*@(BEGIN|END)_(WITH_UNIX|WITHOUT_WIN32)@//' \
    -e 's/@BEGIN_(WITHOUT_UNIX|WITH_WIN32)@/\  (*/' \
    -e 's/@END_(WITHOUT_UNIX|WITH_WIN32)@/\  *)/' \
    stdcompat_tests.ml.in > _build/default/stdcompat_tests.ml
OCAMLFLAGS='-I .stdcompat.objs/byte -cclib -L. -o stdcompat_tests'
cd _build/default
%ifarch %{ocaml_native_compiler}
ocamlopt $OCAMLFLAGS stdcompat.cmxa stdcompat_tests.ml
%else
ocamlc $OCAMLFLAGS stdcompat.cma stdcompat_tests.ml
%endif
./stdcompat_tests
cd -

%files -f .ofiles
%doc AUTHORS CHANGES.md README.md
%license COPYING

%files devel -f .ofiles-devel

%changelog
%autochangelog

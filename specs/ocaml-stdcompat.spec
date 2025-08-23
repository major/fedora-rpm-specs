Name:           ocaml-stdcompat
Version:        21.1
Release:        %autorelease
Summary:        Compatibility module for the OCaml standard library

License:        LGPL-2.1-or-later
URL:            https://github.com/ocamllibs/stdcompat
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/stdcompat-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.11
BuildRequires:  ocaml-dune >= 2.0

%description
Stdcompat is a compatibility layer allowing programs to use some recent
additions to the OCaml standard library while preserving the ability to
be compiled on former versions of OCaml.

The Stdcompat API is not intended to be stable, but there will be
efforts to allow future versions of Stdcompat to be compiled on a large
range of versions of OCaml: Stdcompat should compile (at least) on every
version of OCaml from 3.08 (inclusive).

The module Stdcompat provides some definitions for values and types
introduced in recent versions of the standard library.  These
definitions are just aliases to the matching definition of the standard
library if the latter is recent enough.  Otherwise, the module Stdcompat
provides an alternative implementation.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n stdcompat-%{version} -p1

%build
%dune_build

%install
%dune_install

%ifarch %{ocaml_native_compiler}
# The tests assume that ocamlopt is available
%check
%dune_check
%endif

%files -f .ofiles
%doc AUTHORS CHANGES.md README.md
%license COPYING

%files devel -f .ofiles-devel

%changelog
%autochangelog

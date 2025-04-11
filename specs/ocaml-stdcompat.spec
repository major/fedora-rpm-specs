Name:           ocaml-stdcompat
Version:        20.1
Release:        %autorelease
Summary:        Compatibility module for the OCaml standard library

License:        BSD-2-Clause
URL:            https://github.com/ocamllibs/stdcompat
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/stdcompat-%{version}.tar.gz
# Fix detection of OCaml tools
# https://github.com/thierry-martinez/stdcompat/pull/31
Patch:          %{name}-configure.patch
# Add support for OCaml 5.3
# https://github.com/thierry-martinez/stdcompat/pull/35
Patch:          %{name}-ocaml5.3.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros

# Needed only until the configure patch is merged upstream
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

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

%conf
# Regenerate configure after Patch0 and Patch1
autoreconf -fi .

# Generate debuginfo
sed -i 's/-nolabels/-g &/' Makefile.in

%build
%configure --libdir=%{ocamldir}

# Parallel make does NOT work; there seem to be missing dependencies
make all

%install
%make_install

# We do not want the ml files
find %{buildroot}%{ocamldir} -name \*.ml -delete

# Install the mli files
cp -p *.mli %{buildroot}%{ocamldir}/stdcompat

# Install the opam file
cp -p stdcompat.opam %{buildroot}%{ocamldir}/stdcompat/opam

# Remove spurious executable bits
chmod a-x %{buildroot}%{ocamldir}/stdcompat/{META,*.{a,cma,cmi,cmt,h}}
%ifarch %{ocaml_native_compiler}
chmod a-x %{buildroot}%{ocamldir}/stdcompat/*.{cmx,cmxa}
%endif

%ocaml_files

%ifarch %{ocaml_native_compiler}
# The tests assume that ocamlopt is available
%check
LD_LIBRARY_PATH=$PWD make test
%endif

%files -f .ofiles
%doc AUTHORS CHANGES.md README.md
%license COPYING

%files devel -f .ofiles-devel

%changelog
%autochangelog

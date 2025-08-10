Name:           ocaml-pyml
Version:        20250807
Release:        %autorelease
Summary:        OCaml bindings for Python

# The project is BSD-2-Clause except for pycaml.mli, which is LGPLv2+
License:        BSD-2-Clause AND LGPL-2.1-or-later
URL:            https://github.com/ocamllibs/pyml
VCS:            git:%{url}.git
Source:         %{url}/archive/%{version}/pyml-%{version}.tar.gz
# Fix various incompatibilities with python 3.13.  See:
# https://github.com/thierry-martinez/pyml/issues/84
Patch:          %{name}-python3.13.patch
# Guard against passing NULL to memcpy
Patch:          %{name}-memcpy.patch

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.11.0
BuildRequires:  ocaml-dune >= 2.8
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-stdcompat-devel >= 18
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist numpy}

%description
py.ml provides OCaml bindings for Python 2 and Python 3.  This library
subsumes the pycaml library, which is no longer actively maintained.

The Python library is linked at runtime and the same executable can be
run in a Python 2 or a Python 3 environment.  py.ml does not require any
Python library at compile time.  The only compile time dependency is
Stdcompat to ensure compatibility with all OCaml compiler versions from
3.12.

Bindings are split in three modules:

- Py provides the initialization functions and some high-level bindings,
  with error handling and naming conventions closer to OCaml usages.

- Pycaml provides a signature close to the old Pycaml module, so as to
  ease migration.

- Pywrappers provides low-level bindings, which follow closely the
  conventions of the C bindings for Python.  Submodules
  Pywrappers.Python2 and Pywrappers.Python3 contain version-specific
  bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-stdcompat-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup -n pyml-%{version} -p1

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

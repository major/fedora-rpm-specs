# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl  https://github.com/ocurrent/ocaml-version

Name:           ocaml-version
Version:        3.7.3
Release:        %autorelease
Summary:        Manipulate, parse and generate OCaml compiler version strings

License:        ISC
URL:            https://ocurrent.github.io/ocaml-version/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  ocaml >= 4.07.0
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-dune >= 3.6

%description
This library provides facilities to parse version numbers of the OCaml
compiler, and enumerates the various official OCaml releases and
configuration variants.

OCaml version numbers are of the form `major.minor.patch+extra`, where
the `patch` and `extra` fields are optional.  This library offers the
following functionality:

- Functions to parse and serialize OCaml compiler version numbers
- Enumeration of official OCaml compiler version releases
- Test compiler versions for a particular feature (e.g. the `bytes`
  type)
- opam compiler switch enumeration

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog

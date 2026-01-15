%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

%global giturl  https://github.com/OCamlPro/swhid_core

Name:           ocaml-swhid-core
Version:        0.1
Release:        %autorelease
Summary:        Library for persistent identifiers used by Software Heritage

License:        ISC
URL:            https://ocamlpro.github.io/swhid_core/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/swhid_core-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildRequires:  ocaml >= 4.03
BuildRequires:  ocaml-dune >= 1.11

%description
swhid_core is an OCaml library to work with persistent identifiers used by
Software Heritage, also known as swhid.  This is the core library; for most
use cases you should use the swhid library instead.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n swhid_core-%{version}

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

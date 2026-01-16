Name:           ocaml-afl-persistent
Version:        1.4
Release:        %autorelease
Summary:        Persistent-mode American Fuzzy Lop for OCaml

License:        MIT
URL:            https://github.com/stedolan/ocaml-afl-persistent
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# The american-fuzzy-lop package is currently only built for x86_64
ExclusiveArch:  %{x86_64}

BuildRequires:  american-fuzzy-lop
BuildRequires:  ocaml >= 4.05
BuildRequires:  ocaml-dune >= 2.9

Requires:       american-fuzzy-lop

%description
This package enables running the American Fuzzy Lop fuzzing tool in persistent
mode in OCaml projects.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.

%prep
%autosetup

%build
./config.sh
%dune_build

%install
%dune_install

%check
cd test
./test.sh

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog

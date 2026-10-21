%global srcname checkseum
%global giturl  https://github.com/mirage/checkseum

Name:           ocaml-%{srcname}
Version:        0.5.4
Release:        %autorelease
Summary:        Checksum algorithms in OCaml

License:        MIT
URL:            https://mirage.github.io/checkseum/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildRequires:  ocaml >= 4.07.0
BuildRequires:  ocaml-dune >= 2.6.0
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-optint-devel >= 0.3.0

# Test dependencies
BuildRequires:  ocaml-alcotest-devel
BuildRequires:  ocaml-astring-devel
BuildRequires:  ocaml-bos-devel
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-fpath-devel
BuildRequires:  ocaml-rresult-devel

%description
Checkseum is a library which implements ADLER-32 and CRC32C Cyclic Redundancy
Check.  It provides 2 implementation, the first in C and the second in OCaml.
The library is on top of optint to get the best representation of the CRC in
the OCaml world.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-optint-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog

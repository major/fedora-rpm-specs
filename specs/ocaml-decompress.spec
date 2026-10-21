%global srcname decompress
%global giturl  https://github.com/mirage/decompress

Name:           ocaml-%{srcname}
Version:        1.6.1
Release:        %autorelease
Summary:        Pure OCaml implementation of Zlib

License:        MIT
URL:            https://mirage.github.io/decompress/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{srcname}-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildRequires:  ocaml >= 4.07.0
BuildRequires:  ocaml-checkseum-devel >= 0.2.0
BuildRequires:  ocaml-dune >= 2.8.0
BuildRequires:  ocaml-cmdliner-devel >= 1.1.0
BuildRequires:  ocaml-optint-devel >= 0.1.0

# Test dependencies
# The ocaml-crowbar package is only available on x86_64
%ifarch %{x86_64}
BuildRequires:  ocaml-alcotest-devel >= 1.7.0
BuildRequires:  ocaml-base64-devel >= 3.0.0
BuildRequires:  ocaml-bstr-devel >= 0.0.4
BuildRequires:  ocaml-bytesrw-devel
BuildRequires:  ocaml-crowbar-devel >= 0.2
BuildRequires:  ocaml-fmt-devel >= 0.8.7
BuildRequires:  ocaml-zip-devel >= 1.10
BuildRequires:  pkgconfig(zlib)
%endif

%description
This package contains an OCaml library that implements:

- RFC1951
- Zlib
- Gzip
- LZO

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-checkseum-devel%{?_isa}
Requires:       ocaml-optint-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{srcname}-%{version}

%check
# The ocaml-crowbar package is only available on x86_64
%ifarch %{x86_64}
%dune_check
%endif

%files -f .ofiles
%doc AUTHORS.md CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog

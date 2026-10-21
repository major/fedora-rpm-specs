%global giturl  https://github.com/mirage/ocaml-tar

Name:           ocaml-tar
Version:        3.5.0
Release:        %autorelease
Summary:        Pure OCaml library to read and write tar files

License:        ISC
URL:            https://mirage.github.io/ocaml-tar/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildOption(build): -p tar,tar-unix
BuildOption(install): tar tar-unix
BuildOption(check): -p tar,tar-unix

BuildRequires:  git-core
BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-decompress-devel >= 1.5.1
BuildRequires:  ocaml-dune >= 2.9
BuildRequires:  ocaml-fpath-devel >= 0.7.3
BuildRequires:  ocaml-logs-devel >= 0.8.0
BuildRequires:  ocaml-lwt-devel >= 5.7.0

%description
This package contains a simple library to read and write tar files with an
emphasis on streaming.  This is pure OCaml code, no C bindings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-decompress-devel%{?_isa}
Requires:       ocaml-fpath-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-lwt-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup

%files -f .ofiles
%doc CHANGES.md MAINTAINERS README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog

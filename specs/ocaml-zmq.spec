%global giturl  https://github.com/andersfugmann/ocaml-zmq

Name:           ocaml-zmq
Version:        6.0.0
Release:        %autorelease
Summary:        ZeroMQ bindings for OCaml

License:        MIT
URL:            https://andersfugmann.github.io/ocaml-zmq/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/zmq-%{version}.tbz

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

BuildSystem:    dune
BuildOption(build): -p zmq,zmq-lwt
BuildOption(install): -s zmq zmq-lwt
BuildOption(check): -p zmq,zmq-lwt

BuildRequires:  ocaml >= 4.03.0
BuildRequires:  ocaml-dune >= 3.18
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-lwt-devel >= 2.6.0
BuildRequires:  ocaml-ounit2-devel
BuildRequires:  pkgconfig(libzmq)

%description
This library contains basic OCaml bindings for ZeroMQ.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zeromq-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%package        lwt
Summary:        LWT-aware ZeroMQ bindings for OCaml
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    lwt
This library contains lwt-aware OCaml bindings for ZeroMQ.

%package        lwt-devel
Summary:        Development files for %{name}-lwt
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Requires:       %{name}-lwt%{?_isa} = %{version}-%{release}
Requires:       ocaml-lwt-devel%{?_isa}

%description    lwt-devel
The %{name}-lwt-devel package contains libraries and signature files for
developing applications that use %{name}-lwt.

%prep
%autosetup -n zmq-%{version} -p1

%files -f .ofiles-zmq
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-zmq-devel

%files lwt -f .ofiles-zmq-lwt

%files lwt-devel -f .ofiles-zmq-lwt-devel

%changelog
%autochangelog

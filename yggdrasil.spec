%bcond_without check

# https://github.com/redhatinsights/yggdrasil
%global goipath         github.com/redhatinsights/yggdrasil
Version:                0.3.2
%global tag             %{version}

%gometa -f

%global common_description %{expand:
yggdrasil is a system daemon that subscribes to topics on an MQTT broker and
routes any data received on the topics to an appropriate child "worker" process,
exchanging data with its worker processes through a D-Bus message broker.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           yggdrasil
Release:        %autorelease
Summary:        Remote data transmission and processing client

License:        GPL-3.0-only
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  systemd-rpm-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(bash-completion)

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%build
%undefine _auto_set_build_flags
export %gomodulesmode
%{?gobuilddir:export GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"}
%meson "-Dgobuildflags=[%(echo %{expand:%gocompilerflags} | sed -e s/"^"/"'"/ -e s/" "/"', '"/g -e s/"$"/"'"/), '-tags', '"rpm_crashtraceback\ ${BUILDTAGS:-}"', '-a', '-v', '-x']" -Dgoldflags='%{?currentgoldflags} -B 0x%(head -c20 /dev/urandom|od -An -tx1|tr -d " \n") -compressdwarf=false -linkmode=external -extldflags "%{build_ldflags} %{?__golang_extldflags}"'
%meson_build

%global gosupfiles ./ipc/com.redhat.Yggdrasil1.Dispatcher1.xml ./ipc/com.redhat.Yggdrasil1.Worker1.xml
%install
%meson_install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/%{name}
%{_unitdir}/*
%{_userunitdir}/*
%{_datadir}/bash-completion/completions/*
%{_datadir}/dbus-1/{interfaces,system-services,system.d}/*
%{_datadir}/doc/%{name}/*
%{_mandir}/man1/*

%gopkgfiles

%changelog
%autochangelog

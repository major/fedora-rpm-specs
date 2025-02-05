%bcond_without check

# https://github.com/redhatinsights/yggdrasil
%global goipath         github.com/redhatinsights/yggdrasil
Version:                0.4.4
%global tag             v%{version}

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
Source:         %{url}/releases/download/%{tag}/yggdrasil-%{version}.tar.xz
Source1:        yggdrasil.sysusers

BuildRequires:  systemd-rpm-macros
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(bash-completion)
%{?sysusers_requires_compat}

%{?systemd_requires}

%description %{common_description}

%package devel
Summary:        %{name} development files

%description devel
%{common_description}

Contains files needed for yggdrasil worker development.

%package examples
Summary:       %{name} example workers

Requires: %{name} = %{version}-%{release}

%description examples
%{common_description}

Contains example workers for yggdrasil.

%gopkg

%prep
%goprep %{?rhel:-k}

%if %{undefined rhel}
%generate_buildrequires
%go_generate_buildrequires
%endif

%build
%undefine _auto_set_build_flags
export %gomodulesmode
%{?gobuilddir:export GOPATH="%{gobuilddir}:${GOPATH:+${GOPATH}:}%{?gopath}"}
%meson -Dexamples=True "-Dgobuildflags=[%(echo %{expand:%gocompilerflags} | sed -e s/"^"/"'"/ -e s/" "/"', '"/g -e s/"$"/"'"/), '-tags', '"rpm_crashtraceback\ ${BUILDTAGS:-}"', '-a', '-v', '-x']" -Dgoldflags='%{?currentgoldflags} -B 0x%(head -c20 /dev/urandom|od -An -tx1|tr -d " \n") -compressdwarf=false -linkmode=external -extldflags "%{build_ldflags} %{?__golang_extldflags}"'
%meson_build

%global gosupfiles ./ipc/com.redhat.Yggdrasil1.Dispatcher1.xml ./ipc/com.redhat.Yggdrasil1.Worker1.xml
%install
%meson_install
%__install -d -m 0755 %{buildroot}%{_localstatedir}/lib/yggdrasil
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%pre
%sysusers_create_compat %{SOURCE1}

%post
%systemd_post %{name}.service
%systemd_user_post %{name}.service

%preun
%systemd_preun %{name}.service
%systemd_user_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
%systemd_user_postun_with_restart %{name}.service

%files
%license LICENSE
%if %{defined rhel}
%license vendor/modules.txt
%endif
%doc CONTRIBUTING.md README.md
%{_bindir}/yggd
%{_bindir}/yggctl
%config(noreplace) %{_sysconfdir}/%{name}
%{_unitdir}/yggdrasil-bus@.service
%{_unitdir}/yggdrasil-bus@.socket
%{_unitdir}/yggdrasil@.service
%{_unitdir}/yggdrasil.service
%{_userunitdir}/yggdrasil.service
%{_sysusersdir}/yggdrasil.conf
%{_datadir}/bash-completion/completions/yggd
%{_datadir}/bash-completion/completions/yggctl
%{_datadir}/dbus-1/interfaces/com.redhat.Yggdrasil1.xml
%{_datadir}/dbus-1/interfaces/com.redhat.Yggdrasil1.Worker1.xml
%{_datadir}/dbus-1/interfaces/com.redhat.Yggdrasil1.Dispatcher1.xml
%{_datadir}/dbus-1/system.d/yggd.conf
%{_datadir}/dbus-1/system-services/com.redhat.Yggdrasil1.service
%{_datadir}/doc/%{name}/tags.toml
%{_mandir}/man1/yggctl.1.gz
%{_mandir}/man1/yggd.1.gz
%attr(0755, yggdrasil, yggdrasil) %{_localstatedir}/lib/yggdrasil

%files devel
%{_libdir}/pkgconfig/yggdrasil.pc

%files examples
%{_libexecdir}/yggdrasil/echo
%{_datadir}/dbus-1/system.d/com.redhat.Yggdrasil1.Worker1.echo.conf
%{_datadir}/dbus-1/system-services/com.redhat.Yggdrasil1.Worker1.echo.service
%{_unitdir}/com.redhat.Yggdrasil1.Worker1.echo.service

%gopkgfiles

%changelog
%autochangelog

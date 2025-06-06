# Generated by go2rpm
%bcond_without check

# https://github.com/nats-io/nats-server
%global goipath         github.com/nats-io/nats-server
Version:                2.11.4

%gometa -f

%global goname          nats-server
%global goaltipaths     github.com/nats-io/gnatsd github.com/nats-io/nats-server/v2

%global common_description %{expand:
A High Performance NATS Server written in Go and hosted by the Cloud Native
Computing Foundation (CNCF).}

%global golicenses      LICENSE
%global godocs          CODE-OF-CONDUCT.md GOVERNANCE.md MAINTAINERS.md\\\
                        README.md TODO.md

Name:           %{goname}
Release:        %autorelease
Summary:        High-Performance server for NATS, the cloud native messaging system

# Upstream license specification: Apache-2.0
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  systemd-rpm-macros
BuildRequires:  help2man
Requires(pre):  shadow-utils

%description
%{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}


%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_sbindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_sbindir}/
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
help2man --no-discard-stderr --no-info --version-string=%{version} %{buildroot}%{_sbindir}/%{name} > %{buildroot}%{_mandir}/man1/%{name}.1
install -m 0755 -vd                      %{buildroot}%{_unitdir}
install -m 0755 -vp util/%{name}.service %{buildroot}%{_unitdir}/
install -m 0755 -vd                         %{buildroot}%{_sysconfdir}
install -m 0755 -vp docker/nats-server.conf %{buildroot}%{_sysconfdir}/
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

%pre
getent group nats >/dev/null || groupadd -r nats
getent passwd nats >/dev/null || \
    useradd -r -g nats -d %{_sharedstatedir}/%{name} -s /sbin/nologin \
    -c "NATS Server account" nats
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%if %{with check}
%check
# logger: needs access to syslog
# server, test: need network
# server/avl: intermittent timeout errors
%gocheck -d logger -d server -d server/avl -d server/pse -d test
%endif

%files
%license LICENSE
%doc CODE-OF-CONDUCT.md GOVERNANCE.md MAINTAINERS.md README.md TODO.md
%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service
%attr(0750, nats, nats) %dir %{_sharedstatedir}/%{name}

%gopkgfiles

%changelog
%autochangelog

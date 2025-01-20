Name:		pgbouncer
Version:	1.23.1
Release:	3%{?dist}
Summary:	Lightweight connection pooler for PostgreSQL
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:		https://www.pgbouncer.org

Source0:	%{url}/downloads/files/%{version}/%{name}-%{version}.tar.gz
Source3:	%{name}.logrotate
Source4:	%{name}.service
Source6:	%{name}.pam

Patch0:		%{name}-ini.patch

BuildRequires:	c-ares-devel >= 1.11
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	openssl-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(libevent)
# For Fedora and EL9+ systemd-rpm-macros would be enough:
BuildRequires:	systemd-devel

Requires:	systemd
Requires:	logrotate
Requires:	python3-psycopg2
Requires:	c-ares >= 1.11

Requires(pre):	shadow-utils

%description
pgbouncer is a lightweight connection pooler for PostgreSQL and uses libevent
for low-level socket handling.

%prep
%autosetup -p0

sed -i -e 's|/usr/bin/env python.*|%__python3|g' etc/mkauth.py

%build
# Building with systemd flag tries to enable notify support:
%configure \
	--enable-debug \
	--with-cares \
	--with-pam \
	--with-systemd

%make_build V=1

%install
%make_install

# Configuration
install -p -d %{buildroot}%{_sysconfdir}/%{name}/
install -p -m 640 etc/%{name}.ini %{buildroot}%{_sysconfdir}/%{name}
install -p -m 600 etc/userlist.txt %{buildroot}%{_sysconfdir}/%{name}
install -p -m 700 etc/mkauth.py %{buildroot}%{_sysconfdir}/%{name}/

# Install pam configuration file
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
install -p -m 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/pam.d/%{name}

# Temporary folder
mkdir -p %{buildroot}%{_rundir}/%{name}

# Log folder
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

# systemd unit
install -d %{buildroot}%{_unitdir}
install -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service

# tmpfiles.d configuration
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/%{name}.conf <<EOF
d %{_rundir}/%{name} 0755 %{name} %{name} -
EOF

# logrotate file
install -p -d %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Let RPM pick up docs in the files section
rm -fr %{buildroot}%{_docdir}/%{name}

%pre
getent group %{name} >/dev/null || groupadd -r %{name} &>/dev/null || :
getent passwd %{name} >/dev/null || useradd -r -s /sbin/nologin \
    -d / -M -c "PgBouncer Server" -g %{name} %{name} &>/dev/null || :
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license COPYRIGHT
%doc NEWS.md README.md doc/*.md
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/mkauth.py*
%config(noreplace) %attr(600,%{name},%{name}) %{_sysconfdir}/%{name}/%{name}.ini
%config(noreplace) %attr(600,%{name},%{name}) %{_sysconfdir}/%{name}/userlist.txt
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%{_mandir}/man1/%{name}.*
%{_mandir}/man5/%{name}.*
%attr(700,%{name},%{name}) %{_localstatedir}/log/%{name}

%attr(755,%{name},%{name}) %dir %{_rundir}/%{name}
%ghost %{_rundir}/%{name}/%{name}.pid
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/%{name}.service

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.23.1-2
- convert license to SPDX

* Mon Aug 05 2024 Simone Caronni <negativo17@gmail.com> - 1.23.1-1
- Update to 1.23.1.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Mar 05 2024 Simone Caronni <negativo17@gmail.com> - 1.22.1-1
- Update to 1.22.1.

* Fri Feb 09 2024 Simone Caronni <negativo17@gmail.com> - 1.22.0-1
- Update to 1.22.0.

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 18 2023 Devrim Gündüz <devrim@gunduz.org> - 1.21.0-1
- Update to 1.21.0, per changes described at:
  https://www.pgbouncer.org/changelog.html#pgbouncer-121x

* Thu Aug 10 2023 Devrim Gündüz <devrim@gunduz.org> - 1.20.1-1
- Update to 1.20.1, per changes described at:
  https://www.pgbouncer.org/changelog.html#pgbouncer-120x

* Mon Aug 07 2023 Simone Caronni <negativo17@gmail.com> - 1.20.0-1
- Update to 1.20.0.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 06 2023 Simone Caronni <negativo17@gmail.com> - 1.19.1-1
- Update to 1.19.1.

* Wed May 24 2023 Simone Caronni <negativo17@gmail.com> - 1.19.0-2
- Adjust python interpreter for mkauth.py.

* Wed May 24 2023 Simone Caronni <negativo17@gmail.com> - 1.19.0-1
- Update to 1.19.0.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Simone Caronni <negativo17@gmail.com> - 1.16.1-2
- Update SPEC file.

* Tue Dec 21 2021 Devrim Gunduz <devrim@gunduz.org> - 1.16.1-1
- Update to 1.16.1, per changes described at:
  http://www.pgbouncer.org/changelog.html#pgbouncer-116x
- Add c-ares support.
- Remove RHEL 6 support from spec file.

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.14.0-9
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.14.0-7
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 20:42:50 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.14.0-5
- Rebuilt for libevent 2.1.12

* Tue Sep 15 2020 Devrim Gündüz <devrim@gunduz.org> - 1.14.0-4
- Rebuild against new libevent

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Simone Caronni <negativo17@gmail.com> - 1.14.0-2
- Do not enable notify support on RHEL/CentOS 7.

* Wed Jul 22 2020 Simone Caronni <negativo17@gmail.com> - 1.14.0-1
- Update to 1.14.0.
- Update URL.
- Enable systemd support at compile time so notify/socket support is built in.

* Thu Jul 02 2020 Simone Caronni <negativo17@gmail.com> - 1.13.0-2
- Enable notify in systemd unit.

* Fri May 29 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.13.0-1
- Update to new upstream version 1.13.0

* Thu Apr 23 2020 Simone Caronni <negativo17@gmail.com> - 1.12.0-5
- Change configuration file permissions and also add a template user list.

* Wed Apr 15 2020 Simone Caronni <negativo17@gmail.com> - 1.12.0-4
- Update SPEC file (build & runtime requirements, macros, rpmlint fixes, etc.).
- Fix build on RHEL/CentOS 6/7/8.
- Do not use a normal home folder and shell for the user.
- Do not remove/change files in the scriptlets.
- Do not start in daemon mode in systemd units.
- Trim changelog.

* Wed Mar 04 2020 Aaron Burnett <golanv@adelie.io> - 1.12.0-3
- Fixes bug #1810267
- Fixes bug #1801301

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 3 2019 Devrim Gündüz <devrim@gunduz.org> - 1.12.0-1
- Update to 1.12.0
- Fix bz #1736426

* Fri Aug 9 2019 Devrim Gündüz <devrim@gunduz.org> - 1.10.0-1
- Update to 1.10.0
- Use more macros.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 4 2019 Devrim Gündüz <devrim@gunduz.org> - 1.9.0-1
- Update to 1.9.0
* Mon Feb 4 2019 Devrim Gündüz <devrim@gunduz.org> - 1.9.0-1
- Update to 1.9.0
- Add patch for Python3 compatibility.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

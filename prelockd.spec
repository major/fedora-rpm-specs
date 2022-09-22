Name: prelockd
Version: 0.9
Release: 6%{?dist}
Summary: Lock binaries and libraries in memory to improve system responsiveness
BuildArch: noarch

License: MIT
URL: https://github.com/hakavlad/prelockd
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
%if 0%{?rhel} >= 7
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

Requires: python3 >= 3.3

%description
prelockd is a daemon that locks memory mapped binaries and libraries in memory
to improve system responsiveness under low-memory conditions.


%prep
%autosetup -p1

# Drop non-RPM stuff from Makefile install stage
sed -i 's|base units useradd chcon daemon-reload|base units|' Makefile

sed -i 's|/env python3|/python3|' %{name}


%install
%make_install \
    DOCDIR=%{_pkgdocdir} \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir} \
    SYSTEMDUNITDIR=%{_unitdir}

%pre
# Create prelockd user
getent passwd %{name} >/dev/null || \
    useradd -r -s /sbin/nologin \
    -c "Lock binaries and libraries in memory to improve system responsiveness" %{name}
exit 0


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%{_datadir}/%{name}/
%{_mandir}/man8/*.8.*
%{_pkgdocdir}/
%{_sbindir}/%{name}
%{_sharedstatedir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec  3 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.9-1
- build(update): 0.9

* Mon Oct 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8-2
- build: make 'systemd-rpm-macros' conditional due epel7 support

* Sun Oct 11 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.8-1
- build(update): 0.8

* Tue Oct  6 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7-2
- build: drop %{?systemd_requires} macros
- build: drop custom patch in favour of sed

* Tue Oct  6 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.7-1
- build(update): 0.7

* Sun Oct  4 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6-1
- Initial package

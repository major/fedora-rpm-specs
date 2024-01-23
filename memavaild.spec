Name: memavaild
Version: 0.6
Release: 9%{?dist}
Summary: Improve responsiveness during heavy swapping
BuildArch: noarch

License: MIT
URL: https://github.com/hakavlad/memavaild
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: systemd-rpm-macros

Requires: python3 >= 3.3

%description
Improve responsiveness during heavy swapping: keep amount of available memory.


%prep
%autosetup -p1

# Drop non-RPM stuff from Makefile install stage
sed -i 's|base units useradd chcon daemon-reload|base units|' Makefile

sed -i 's|/env python3|/python3|' memavaild


%install
%make_install \
    DOCDIR=%{_pkgdocdir} \
    PREFIX=%{_prefix} \
    SYSCONFDIR=%{_sysconfdir} \
    SYSTEMDUNITDIR=%{_unitdir}


%pre
# Create memavaild user
getent passwd %{name} >/dev/null || \
    useradd -r -s /sbin/nologin \
    -c "Improve responsiveness during heavy swapping" %{name}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%files
%license LICENSE
%{_pkgdocdir}/
%{_datadir}/%{name}/
%{_mandir}/man*/*.8.*
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.6-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.6-1
- build(update): 0.6

* Tue Oct  6 17:27:54 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5-2
- build: drop %{?systemd_requires} macros
- build: drop custom patch in favour of sed

* Wed Sep 16 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.5-1
- Update to 0.5

* Tue Sep 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.1-2
- Initial package

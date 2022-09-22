%global _hardened_build 1

Name:           reportd
Version:        0.7.4
Release:        9%{?dist}
Summary:        Service reporting org.freedesktop.Problems2 entries

License:        GPLv2+
URL:            https://github.com/abrt/%{name}
Source0:        https://github.com/abrt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libreport) >= 2.13.0
BuildRequires:  meson
BuildRequires:  systemd

%if 0%{?centos}
Recommends:     libreport-centos
%endif

%if 0%{?fedora}
Recommends:     libreport-fedora
%endif

%description
A D-Bus service that exports libreport functionality.


%prep
%autosetup


%build
%meson
%meson_build


%install
%meson_install


%check
%meson_test


%files
%doc NEWS README
%license COPYING
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/org.freedesktop.%{name}.service
%{_datadir}/dbus-1/system-services/org.freedesktop.%{name}.service
%{_datadir}/dbus-1/system.d/org.freedesktop.%{name}.conf
%{_unitdir}/%{name}.service
%{_userunitdir}/%{name}.service


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 25 2020 - Ernestas Kulik <ekulik@redhat.com> - 0.7.4-3
- Rebuild against new libreport

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Ernestas Kulik <ekulik@redhat.com> - 0.7.4-1
- new upstream release: 0.7.4

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 10 2019 Ernestas Kulik <ekulik@redhat.com> - 0.7.3-1
- new upstream release: 0.7.3

* Sat Oct 19 2019 Ernestas Kulik <ekulik@redhat.com> - 0.7.2-1
- new upstream release: 0.7.2

* Mon Oct 07 2019 Ernestas Kulik <ekulik@redhat.com> - 0.7.1-1
- new upstream release: 0.7.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Ernestas Kulik <ekulik@redhat.com> - 0.7.0-1
- Update to 0.7.0

* Mon May 6 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6.7-1
- Update to 0.6.7

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.6.6-2
- Rebuild with Meson fix for #1699099

* Fri Apr 12 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6.6-1
- Update to 0.6.6

* Sun Apr 7 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6.5-1
- Update to 0.6.5

* Thu Mar 21 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6.4-1
- Update to 0.6.4

* Wed Mar 20 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6.3-2
- Add back systemd BuildRequires

* Wed Mar 20 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6.3-1
- Update to 0.6.3

* Thu Mar 7 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6.2-1
- Update to 0.6.2

* Mon Mar 4 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6.1-1
- Update to 0.6.1

* Fri Feb 22 2019 Ernestas Kulik <ekulik@redhat.com> - 0.6-1
- Update to 0.6

* Mon Feb 4 2019 Ernestas Kulik <ekulik@redhat.com> - 0.5-1
- Update to 0.5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 2 2019 Ernestas Kulik <ekulik@redhat.com> - 0.4.1-1
- Update to 0.4.1
- Move to Meson
- Add dummy check section

* Thu Dec 20 2018 Ernestas Kulik <ekulik@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Thu Dec 20 2018 Ernestas Kulik <ekulik@redhat.com> - 0.2-2
- Fix Source0 URL yet again

* Tue Dec 18 2018 Ernestas Kulik <ekulik@redhat.com> - 0.2-1
- Drop patches, fixes are upstream
- Fix summary formatting

* Mon Dec 17 2018 Ernestas Kulik <ekulik@redhat.com> - 0.1-3
- Fix Source0 URL
- Use more modern macros
- Fix autoreconf invocation to install files

* Thu May 19 2016 Jakub Filak <jfilak@redhat.com> - 0.1-2
- Add all BuildRequires
- Verbose command line argument
- Cache moved to /var/run/user/reportd

* Thu Apr 14 2016 Jakub Filak <jfilak@redhat.com> - 0.1-1
- Initial packaging

%if 0%{?fedora} < 28 && 0%{?rhel} < 8
%bcond_without libnm_glib
%else
# Disable the legacy version by default
%bcond_with libnm_glib
%endif

%if 0%{?fedora} < 36 && 0%{?rhel} < 10
%bcond_with gtk4
%else
# Use GTK4 for Fedora 36
%bcond_without gtk4
%endif

# Uses common git repository with strongswan:
# https://github.com/strongswan/strongswan/tree/master/src/frontends/gnome

Name:      NetworkManager-strongswan
Version:   1.6.0
Release:   9%{?dist}
Summary:   NetworkManager strongSwan IPSec VPN plug-in
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:   GPL-2.0-or-later
URL:       https://www.strongswan.org/
Source0:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2
Source1:   https://download.strongswan.org/NetworkManager/%{name}-%{version}.tar.bz2.sig
Source2:   https://keys.openpgp.org/vks/v1/by-fingerprint/12538F8F689B5F1F15F07BE1765FE26C6B467584#/strongswan.asc

BuildRequires: make
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(libnm) >= 1.1.0
BuildRequires: pkgconfig(libnma) >= 1.1.0
BuildRequires: intltool
BuildRequires: libtool
%if 0%{?fedora}
BuildRequires: gnupg2
%endif

%if %{with gtk4}
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libnma-gtk4)
%endif

%if %{with libnm_glib}
BuildRequires: pkgconfig(dbus-glib-1) >= 0.30
BuildRequires: pkgconfig(NetworkManager) >= 1.1.0
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-glib-vpn)
BuildRequires: pkgconfig(libnm-gtk)
%endif

Requires: NetworkManager
Requires: strongswan-charon-nm >= 5.8.3

%global __provides_exclude ^libnm-.*\\.so

%description
This package contains software for integrating the strongSwan IPSec VPN
with NetworkManager.


%package gnome
Summary: NetworkManager VPN plugin for strongswan - GNOME files

Requires: NetworkManager-strongswan = %{version}-%{release}

%description gnome
This package contains software for integrating the strongSwan IPSec VPN
with the graphical desktop.


%prep
%if 0%{?fedora}
%gpgverify -k 2 -d 0 -s 1
%endif
%autosetup -p1


%build
%configure \
        --disable-static \
%if %{with gtk4}
        --with-gtk4 \
%endif
%if %{without libnm_glib}
        --without-libnm-glib \
%endif
        --with-charon=%{_libexecdir}/strongswan/charon-nm \
        --enable-more-warnings=no
%make_build


%install
%make_install
%find_lang %{name}

rm -f %{buildroot}%{_libdir}/NetworkManager/libnm-*.la

%files -f %{name}.lang
%{_prefix}/lib/NetworkManager/VPN/nm-strongswan-service.name
%doc NEWS


%files gnome
%if %{with gtk4}
%{_libdir}/NetworkManager/libnm-gtk4-vpn-plugin-strongswan-editor.so
%endif
%{_prefix}/lib/NetworkManager/nm-strongswan-auth-dialog
%{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan-editor.so
%{_libdir}/NetworkManager/libnm-vpn-plugin-strongswan.so
%{_datadir}/metainfo/NetworkManager-strongswan.metainfo.xml

%if %{with libnm_glib}
%{_libdir}/NetworkManager/libnm-*-properties.so
%{_sysconfdir}/NetworkManager/VPN/nm-strongswan-service.name
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Anatolii Vorona <vorona.tolik@gmail.com> - 1.6.0-1
- Update to 1.6.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Petr Menšík <pemensik@redhat.com> - 1.5.2-1
- Update to 1.5.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 12 2020 Mikhail Zabaluev <mikhail.zabaluev@gmail.com> - 1.5.0-1
- Updated to 1.5.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Mikhail Zabaluev <mikhail.zabaluev@gmail.com> - 1.4.5-1
- Update to 1.4.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Aug 18 2018 Mikhail Zabaluev <mikhail.zabaluev@gmail.com> - 1.4.4-1
- new version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.4.3-1
- Update to 1.4.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.4.2-1
- Update to 1.4.2

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.4.0-2
- Bring back the D-Bus policy until new charon-nm is released

* Wed Sep 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.4.0-1
- New upstream release that integrates our NetworkManager 1.2 support

* Wed Mar 30 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-3.20160330libnm
- Update the NetworkManager 1.2 support patchset

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3.20151023libnm
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 23 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-2.20151023libnm
- Add the NetworkManager 1.2 support patchset

* Mon Oct 19 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-1
- Initial packaging

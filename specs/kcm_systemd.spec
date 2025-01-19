%undefine __cmake_in_source_build
Name:           kcm_systemd
Version:        1.2.1
Release:        28%{?dist}
Summary:        Systemd control module for KDE

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://kde-apps.org/content/show.php/Kcmsystemd?content=161871
Source0:        http://download.kde.org/stable/systemd-kcm/systemd-kcm-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  systemd-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-rpm-macros

# for /usr/share/kservices5/settings-system-administration.desktop
# That file was previously shipped in this package, but now upstreamed to
# plasma-systemsettings 5.16.90.
Requires:       plasma-systemsettings >= 5.16.90

%description
Systemd control module for KDE. It provides a graphical frontend for the systemd
daemon, which allows for viewing and controlling systemd units, as well as
modifying configuration files. In integrates in the System Settings dialogue in
KDE.

%prep
%setup -q -n systemd-kcm-%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install
%find_lang systemd-kcm
# fix file conflict with plasma-systemsettings >= 5.16.90
rm -f %{buildroot}%{_kf5_datadir}/kservices5/settings-system-administration.desktop

%files -f systemd-kcm.lang
%license COPYING
%doc NEWS README.md
%{_kf5_qtplugindir}/kcm_systemd.so
%{_kf5_libexecdir}/kauth/kcmsystemdhelper
%{_kf5_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmsystemd.conf
%{_kf5_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsystemd.service
%{_kf5_datadir}/kservices5/kcm_systemd.desktop
%{_kf5_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsystemd.policy

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.1-27
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.2.1-15
- Remove /usr/share/kservices5/settings-system-administration.desktop
- Add Requires: plasma-systemsettings >= 5.16.90 (which now ships this file)

* Sat Aug 10 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.2.1-14
- Update D-Bus .conf file directory for KAuth >= 5.59.0, fixes FTBFS (#1735915)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-7
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-5
- Rebuilt for Boost 1.63

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-4
- Rebuilt for Boost 1.63

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.2.1-2
- Rebuilt for Boost 1.60

* Sat Sep 26 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.2.1-1
- Update to 1.2.1 (#1266684)
- Update Source0 URL: use download.kde.org and new tarball naming scheme
- License changed from GPLv3+ to GPLv2+, LICENSE file was renamed to COPYING
- Add BuildRequires: pkgconfig gcc-c++
- Add BuildRequires: kf5-kcrash-devel kf5-kio-devel kf5-kwidgetsaddons-devel
- Don't BR version >= 209 of systemd-devel, old versions now supported again
- Remove BuildRequires: boost-devel, not needed anymore with C++11 compiler
- Update the name of the translation domain from kcmsystemd to systemd-kcm

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-6
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.1.0-4
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Mar 03 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1.0-1
- Update to 1.1.0 (#1198121)
- BR systemd-devel >= 209 for libsystemd.so (new dependency)
- Upstream added translations, package them (BR gettext, use %%find_lang)

* Mon Feb 23 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.0.0-1
- Update to 1.0.0 (#1195092, KF5 port)
- Update BuildRequires (remove kdelibs4-devel, add cmake, ECM, Qt 5 and KF5)
- Use kf5 RPM macros instead of kde4 ones
- Use %%license instead of %%doc for LICENSE

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 0.7.0-3
- Rebuild for boost 1.57.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 03 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.7.0-1
- Update to 0.7.0 (#1124165)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 0.6.1-2
- Rebuild for boost 1.55.0

* Mon Apr 07 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.6.1-1
- Rename package from kcm-systemd to kcm_systemd
- Update to 0.6.1
- Point URL and Source0 to kde-apps.org (released tarball) instead of github
- Line-wrap %%description and fix a spelling/grammar error in it

* Wed Dec 25 2013 Mario Blättermann <mario.blaettermann@gmail.com> - 0.4.0-2
- Use kdelibs4 instead of kdelibs

* Wed Dec 18 2013 Mario Blättermann <mariobl@fedoraproject.org> 0.4.0-1
- Initial package

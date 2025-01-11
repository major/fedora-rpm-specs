Name:       gsmartcontrol
Version:    2.0.1
Release:    1%{?dist}
Summary:    Graphical user interface for smartctl

# Note that the "Whatever" license is effectively the MIT license.  See email
# from Tom Callaway to Fedora-legal-list on 18-APR-2011.
# Automatically converted from old format: (GPLv2 or GPLv3) and BSD and zlib and Boost and MIT - review is highly recommended.
License:    (GPL-2.0-only OR GPL-3.0-only) AND LicenseRef-Callaway-BSD AND Zlib AND BSL-1.0 AND LicenseRef-Callaway-MIT

URL:        http://gsmartcontrol.sourceforge.net
Source0:    https://github.com/ashaduri/gsmartcontrol/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  gtkmm30-devel
BuildRequires:  pcre-devel
BuildRequires:  desktop-file-utils
BuildRequires:  make
Requires:       smartmontools >= 5.43
Requires:       hicolor-icon-theme
Requires:       xterm

%description
GSmartControl is a graphical user interface for smartctl (from
smartmontools package), which is a tool for querying and controlling
SMART (Self-Monitoring, Analysis, and Reporting Technology) data on
modern hard disk drives. It allows you to inspect the drive's SMART
data to determine its health, as well as run various tests on it.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license LICENSE.txt LICENSE.LGPL3.txt
%{_bindir}/%{name}-root
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/polkit-1/actions/org.%{name}.policy
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/%{name}-root.1.*
%{_pkgdocdir}
%{_datadir}/metainfo/gsmartcontrol.appdata.xml

%changelog
* Thu Jan 09 2025 Vasiliy Glazov <vascom2@gmail.com> - 2.0.1-1
- Update to 2.0.1

* Mon Nov 18 2024 Vasiliy Glazov <vascom2@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.4-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.4-3
- Added Requires xterm #2133082

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.4-1
- Update to 1.1.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Dec 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.3-1
- Update to 1.1.3

* Tue Oct 10 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Thu Sep 21 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.0-2
- Drop consolehelper

* Tue Sep 12 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.0-1
- Update to 1.1.0
- Drop pcrecpp patch
- Cleanup spec

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Mon Jun 19 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.1-1
- Update to 1.0.1

* Sat Jun 17 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.0-1
- Update to 1.0.0

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Thu May 11 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.0-1
- Update to 0.9.0
- Update source url

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 28 2016 Vasiliy N. Glazov <vascom2@gmail.com> - 0.8.7-10
- Use system pcrecpp (#1119134)
- Require usermode-gtk (#1368430)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.8.7-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 13 2013 Ville Skyttä <ville.skytta@iki.fi> - 0.8.7-4
- Install docs to %%{_pkgdocdir} where available (#993808).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Oct 26 2012 Eric Smith <eric@brouhaha.com>  0.8.7-1
- Update to latest upstream.
- Dropped patches 1 and 2.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 0.8.6-6
- Rebuild against PCRE 8.30

* Mon Jan 16 2012 Eric Smith <eric@brouhaha.com>  0.8.6-5
- Patch to compile with GCC 4.7.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 12 2011 Eric Smith <eric@brouhaha.com>  0.8.6-3
- Patch to work around deprecated g_static_mutex.

* Sat Dec 03 2011 Eric Smith <eric@brouhaha.com>  0.8.6-2
- Updated per package review comments.

* Sat Oct 08 2011 Eric Smith <eric@brouhaha.com>  0.8.6-1
- Updated to latest upstream release.
- Removed obsolte BuildRoot tag, clean section, defattr, etc.
- Added runtime requirements for smartmontools and hicolor-icon-theme,
  per the suggestions in the package review (bug 697247).

* Mon Apr 18 2011 Eric Smith <eric@brouhaha.com>  0.8.5-2
- Changed "Whatever" to "MIT" in license tag, based on Tom Callaway's
  post to Fedora-legal-list.

* Sun Apr 17 2011 Eric Smith <eric@brouhaha.com>  0.8.5-1
- Initial version

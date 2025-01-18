Name:          glogg
Version:       1.1.4
Release:       34%{?dist}
Summary:       Smart interactive log explorer
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           http://glogg.bonnefon.org
Source:        http://glogg.bonnefon.org/files/%{name}-%{version}.tar.gz
# We're using python-markdown2
# thus we need to rename markdown -> markdown2
Patch0:        %{name}-python-markdown.patch
# Look for Qt5DBus rather than QtDBus
Patch1:        %{name}-qt5dbus.patch

BuildRequires:  gcc-c++
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-markdown2
BuildRequires:  qt5-qtbase-devel
BuildRequires: make


%description
%{name} is a multi-platform GUI application to browse and search through
long or complex log files. It is designed with programmers and system
administrators in mind. %{name} can be seen as a graphical, interactive
combination of grep and less.


%prep
%autosetup


%build
%{qmake_qt5}
make %{?_smp_flags}


%install
make INSTALL_ROOT=%{buildroot}%{_prefix} install
rm -rf %{buildroot}%{_datadir}/doc
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc COPYING README.md TODO doc/documentation.html
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.4-33
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-29
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-27
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.1.4-24
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-22
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-19
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-16
- Rebuilt for Boost 1.73

* Fri Jan 31 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.4-15
- Switch to use python3 markdown2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-11
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.4-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Feb 24 2018 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.4-8
- Add missing BR (gcc-c++)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-6
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-3
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.4-2
- Rebuilt for Boost 1.64

* Fri May 19 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.4-1
- New upstream release 1.1.4, rhbz#1444577

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Apr 18 2017 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.3-1
- New upstream release 1.1.3, rhbz#1434627
- Switch to use autosetup
- Drop patch merged upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.2-2
- Rebuilt for Boost 1.63 and patched for GCC 7.

* Tue Nov 15 2016 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.2-1
- New upstream release 1.1.2, rhbz#1390393

* Sat May 07 2016 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.1.1-1
- New upstream release 1.1.1, rhbz#1329862

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 1.0.3-3
- use %%qmake_qt5 macro to ensure proper build flags

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.3-2
- Rebuilt for Boost 1.60

* Wed Nov 11 2015 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.3-1
- update to the latest available version, rhbz#1280115.
- remove qdatastream patch.

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.2-8
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 1.0.2-7
- Added patch for missing headers.

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.2-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.2-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.0.2-2
- Rebuild for boost 1.57.0

* Fri Jan 16 2015 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.2-1
- update to the latest available version.

* Thu Sep 18 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.1-1
- update to the latest available version.
- switch to compile against qt5.

* Tue Sep 16 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 1.0.0-1
- update to the latest available version.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.99.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.99.1-2
- Rebuild for boost 1.55.0 once again

* Fri May 23 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.99.1-1
- update to the latest available version, rhbz#1100415

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.99.0-2
- Rebuild for boost 1.55.0

* Thu Jan 30 2014 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.99.0-1
- update to the latest available version, rhbz#1059571

* Thu Oct 10 2013 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.2-1
- update to the latest available version.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.9.1-4
- Rebuild for boost 1.54.0

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.1-3
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.1-2
- Rebuild for Boost-1.53.0

* Fri Dec 21 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.9.1-1
- update to the latest available version.

* Thu Nov 01 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.8.3-4
- switch to use the python-markdown2 for generating the documentation.

* Mon Oct 29 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.8.3-3
- icon cache refreshing scriplets added.
- superfluous BR removed.

* Wed Oct 03 2012 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 0.8.3-1
- initial RPM release.

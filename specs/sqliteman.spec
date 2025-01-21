Summary:       Manager for sqlite - Sqlite Databases Made Easy
Name:          sqliteman
Version:       1.2.2
Release:       40%{?dist}
# src is GPLv2+, icons are LGPLv2+
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://sqliteman.yarpen.cz/
Patch0:        sqliteman-1.2.2-desktop.patch   
Source:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# converted from logo_design/logo-original.ai by gimp
Source1:       sqliteman.png
Requires:      qt-sqlite
Requires:      sqlite
BuildRequires: cmake
BuildRequires: qt4-devel >= 4.2.0
BuildRequires: desktop-file-utils
%description
If you are looking for a tool for tuning SQL statements, manage
tables, views, or triggers, administrate the database space and index
statistics then Sqliteman is the perfect choice.

If you are looking for a graphical queries creation wizards, user
interface designers for your database, or an universal report tool try
the applications designed for tasks such this (Kexi, knoda).

%prep
%autosetup -p1

%build
%cmake -DWANT_INTERNAL_QSCINTILLA=1
%cmake_build

%install
%cmake_install
desktop-file-install   \
    --delete-original  \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

# fix location of desktop icon
rm %{buildroot}%{_datadir}/icons/hicolor/%{name}.png
install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -rf %{buildroot}%{_datadir}/icons

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.2-39
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-37
- Use autosetup macro

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-28
- Fix cmake macro usage

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun May 26 2019 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-25
- Rebuild to fix rhbz#1701576

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Björn Esser <besser82@fedoraproject.org> - 1.2.2-23
- Append curdir to CMake invokation. (#1668512)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-21
- Fix date

* Tue Jun 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-20
- Some clean up

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.2-13
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 12 2015 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-12
- Fix icon (bz #1157577)

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-9
- /usr/bin/sqlite3 is needed (bz #994586)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 1.2.2-7
- Remove --vendor from desktop-file-install for F19+. https://fedorahosted.org/fesco/ticket/1077

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Mar 20 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-3
- add patch to fix desktop file (#689155)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.2-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Terje Rosten <terje.rosten@ntnu.no> - 1.2.2-1
- 1.2.2

* Wed Sep  8 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-4
- switch to explicit qt4 buildreq

* Wed Jun 16 2010 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-3
- add patch to build with qt-4.7, thanks to Alec Moskvin

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 29 2009 Terje Rosten <terje.rosten@ntnu.no> - 1.2.1-1
- 1.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Aug 12 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.2.0-3
- build with internal qscintilla

* Tue Aug 12 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.2.0-1
- 1.2.0
- add qscintilla-devel to build req

* Sat Feb  9 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-4
- rebuild

* Thu Jan  3 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-3
- fix license again
- improve comment about movement of desktop icon 

* Thu Jan  3 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-2
- fix license
- fix desktop patch

* Tue Jan  1 2008 Terje Rosten <terje.rosten@ntnu.no> - 1.0.1-1
- initial build


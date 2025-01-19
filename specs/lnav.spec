Name:          lnav
Version:       0.12.3
Release:       2%{?dist}
Summary:       Curses-based tool for viewing and analyzing log files
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD

URL:           http://lnav.org
Source0:       https://github.com/tstack/lnav/releases/download/v%{version}/%{name}-%{version}.tar.bz2

BuildRequires: bzip2-devel
BuildRequires: gcc-c++
BuildRequires: libarchive-devel
BuildRequires: libcurl-devel
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: openssh
BuildRequires: openssl-devel
BuildRequires: pcre2-devel
BuildRequires: readline-devel
BuildRequires: sqlite-devel
BuildRequires: zlib-devel

%description
%{name} is an enhanced log file viewer that takes advantage of any semantic
information that can be gleaned from the files being viewed, such as
timestamps and log levels. Using this extra semantic information, it can
do things like interleaving messages from different files, generate
histograms of messages over time, and providing hotkeys for navigating
through the file. It is hoped that these features will allow the user to
quickly and efficiently zero in on problems.


%prep
%setup -q

%build
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install


%files
%doc AUTHORS NEWS.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 22 2024 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.12.3-1
- resolves: #2326844
  updated to 0.12.3

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.12.2-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.12.2-1
- resolves: #2272272
  updated to 0.12.2

* Fri Feb 23 2024 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.12.0-1
- resolves: #2262512
  updated to 0.12.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.11.2-1
- resolves: #2215471
  updated to 0.11.2

* Mon Feb 20 2023 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.11.1-3
- resolves: #2171598
  fix FTBFS on F38+

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 28 2022 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.11.1-1
- resolves: #2128322
  updated to 0.11.1
  migrated to pcre2

* Sun Sep 25 2022 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.11.0-1
- resolves: #2118081
  updated to 0.11.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.10.1-3
- resolves: #2046721
  fix FTBFS on F36+

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 07 2021 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.10.1-1
- resolves: #2010455
  updated to 0.10.1

* Thu Sep 23 2021 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.10.0-1
- resolves: #1974009
  updated to 0.10.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 0.9.0-4
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Jeff Law <law@redhat.com> - 0.9.0-2
- Force C++14 as this code is not C++17 ready

* Fri Oct 23 2020 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.9.0-1
- resolves: #1791451 #1822427
  updated to 0.9.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.8.5-5
- drop python3 BuildRequires
  it's not needed since version 0.8.0

* Mon Feb 03 2020 Petr Viktorin <pviktori@redhat.com> - 0.8.5-4
- Switch BuildRequires to python3

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 13 2019 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.8.5-1
- resolves: #1689512
  updated to 0.8.5

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.4-3
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 05 2018 Peter Schiffer <peter+fedora@pschiffer.eu> - 0.8.4-1
- resolves: #1562275
  updated to 0.8.4

* Tue Jul 24 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.8.3-4
- resolves: #1604716
  add missing BuildRequires on gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.3-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Feb 12 2018 Peter Schiffer <pschiffe@redhat.com> - 0.8.3-1
- resolves: #1439968
  updated to 0.8.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.8.1-2
- Rebuild for readline 7.x

* Tue Aug 09 2016 Peter Schiffer <pschiffe@redhat.com> - 0.8.1-1
- resolves: #1365238
  updated to 0.8.1

* Tue Mar 01 2016 Raphael Groner <projects.rg@smart.ms> - 0.8.0-1
- new version

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.2-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 05 2015 Christopher Meng <rpm@cicku.me> - 0.7.2-1
- Update to 0.7.2

* Tue Nov 25 2014 Christopher Meng <rpm@cicku.me> - 0.7.1-1
- Update to 0.7.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Dan Horák <dan[at]danny.cz> - 0.7.0-2
- fix build on big endian arches

* Tue Apr 01 2014 Christopher Meng <rpm@cicku.me> - 0.7.0-1
- Update to 0.7.0

* Thu Nov 21 2013 Christopher Meng <rpm@cicku.me> - 0.6.2-1
- Update to 0.6.2

* Thu Sep 12 2013 Christopher Meng <rpm@cicku.me> - 0.6.1-1
- Update to 0.6.1
- Add python BR for environ detection.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 09 2013 Christopher Meng <rpm@cicku.me> - 0.5.1-2
- Cleanup old stuffs.

* Fri May 03 2013 Christopher Meng <rpm@cicku.me> - 0.5.1-1
- Update to 0.5.1

* Fri May 03 2013 Christopher Meng <rpm@cicku.me> - 0.5.0-2
- Patch with automake foreign option in order to support aarch64

* Sat Apr 27 2013 Christopher Meng <rpm@cicku.me> - 0.5.0-1
- Initial Package.

%global gitver 26b1454a
%global date   20130626

Summary:       Visual tool for Git
Name:          teamgit
Version:       0.0.12
Release:       40.%{date}%{?dist}
Epoch:         1
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:       GPL-2.0-only
URL:           http://gitorious.org/projects/teamgit
# Source0:     http://ppa.launchpad.net/bain-devslashzero/ubuntu/pool/main/t/teamgit/teamgit_0.0.10ubuntu1.tar.gz
# Tarball created by
# $ git clone git://gitorious.org/teamgit/mainline.git
# $ cd mainline
# $ git checkout origin/master
# $ git archive --format=tar --prefix=teamgit-%{version}/ %{gitver} | xz > teamgit-%{version}-%{date}.tar.xz
Source0:       teamgit-%{version}-%{date}.tar.xz
Patch01:       teamgit-0.0.12.format.patch
BuildRequires: make
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: source-highlight-qt-devel
BuildRequires: qt-devel
Requires:      git
%description
This package provides a visual tool for Git, a distributed revision
control system.

%prep
%autosetup -p1

%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"
%{qmake_qt4} ./teamgit.pro
make
#{?_smp_mflags} don't work

%install
make INSTALL_ROOT=%{buildroot} install
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop 

%files
%doc COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-rebase
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}_icon.png
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-40.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.0.12-39.20130626
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-38.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Terje Rosten <terje.rosten@ntnu.no> - 1:0.0.12-37.20130626
- Use autopatch macro

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-36.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-35.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-34.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-33.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-32.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-31.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-30.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-29.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Jeff Law <law@redhat.com> - 1:0.0.12-28.20130626
- Force C++14 as this code is not C++17 ready

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-27.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-26.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Kalev Lember <klember@redhat.com> - 1:0.0.12-25.20130626
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-24.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Terje Rosten <terje.rosten@ntnu.no> - 1:0.0.12-23.20130626
- Minor clean up

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-22.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 14 2017 Terje Rosten <terje.rosten@ntnu.no> - 1:0.0.12-21.20130626
- Add format patch

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-20.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-19.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1:0.0.12-18.20130626
- Rebuilt for Boost 1.64

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-17.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 30 2017 Jonathan Wakely <jwakely@redhat.com> - 1:0.0.12-16.20130626
- Rebuilt for Boost 1.63

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.0.12-15.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 1:0.0.12-14.20130626
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1:0.0.12-13.20130626
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1:0.0.12-12.20130626
- Rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 0.0.12-11.
- Rebuilt for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.12-10.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 03 2015 Kalev Lember <kalevlember@gmail.com> - 1:0.0.12-9.20130626
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 07 2015 Terje Rosten <terje.rosten@ntnu.no> - 1:0.0.12-8.20130626
- fix date

* Sat Feb 07 2015 Terje Rosten <terje.rosten@ntnu.no> - 1:0.0.12-7.20130626
- rebuild for boost 1.57.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.12-6.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.12-5.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1:0.0.12-4.20130626
- rebuild for boost 1.55.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.12-3.20130626
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 29 2013 Petr Machata <pmachata@redhat.com> - 1:0.0.12-2.20130626
- Rebuild for boost 1.54.0

* Wed Jun 26 2013 Terje Rosten <terje.rosten@ntnu.no> - 1:0.0.12-1.20130626
- Update from git

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.10-3.20120202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.10-2.20120202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Feb 03 2012 Terje Rosten <terje.rosten@ntnu.no> - 1:0.0.10-1.20120202
- Update from git

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.9-6.20090205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.9-5.20090205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.9-4.20090205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.0.9-3.20090205
- Fix desktop file (bz #487868)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.0.9-2.20090205
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 05 2009 Terje Rosten <terje.rosten@ntnu.no> - 0.0.9-1.20090205
- 0.0.9 + man page crash fix

* Fri Dec 26 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.0.8-2.20081226
- add git to req.
- update to git snapshot 2008-12-26

* Sun Nov 23 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.0.8-1
- 0.0.8
- add man page
- icon has moved
- remove %%post scripts

* Tue Oct 07 2008 Terje Rosten <terje.rosten@ntnu.no> - 0.3.0-1
- initial build


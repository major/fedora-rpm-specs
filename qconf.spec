Summary:        Tool for generating configure script for qmake-based projects
Name:           qconf
Version:        2.4
Release:        11%{?dist}
Epoch:          1

License:        GPLv2+ with exceptions
URL:            https://github.com/psi-plus/qconf
Source0:        https://github.com/psi-plus/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Fedora has gridengine package with /usr/bin/qconf
# So I need to use another name
Patch1:         qconf-1.4-rename-binary.patch

BuildRequires: make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Xml)

%description
QConf allows you to have a nice configure script for your
qmake-based project. It is intended for developers who don't need
(or want) to use the more complex GNU autotools. With qconf/qmake,
it is easy to maintain a cross-platform project that uses a
familiar configuration interface on unix.


%prep
%autosetup -p1


%build
%{qmake_qt5}  PREFIX=%{_prefix}    \
              BINDIR=%{_bindir}    \
              DATADIR=%{_datadir}  \
              QTDIR=%{_qt5_prefix}
              
make %{?_smp_mflags}


%install
make INSTALL_ROOT=%{buildroot} install

# Avoid extra questions like as https://bugzilla.redhat.com/show_bug.cgi?id=1408580
ln -v %{buildroot}%{_bindir}/qconf-qt4 %{buildroot}%{_bindir}/qconf-qt5


%files
%license COPYING
%doc README.md TODO AUTHORS
%{_bindir}/qconf-qt4
%{_bindir}/qconf-qt5
%{_datadir}/%{name}


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Ivan Romanov <drizt72@zoho.eu> - 1:2.4-1
- Bump to v2.4

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Ivan Romanov <drizt@land.ru> - 1:2.3-1
- New upstream version 2.3
- New upstream URL
- Change tarball format
- Use autosetup in prep section

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan  7 2017 Ivan Romanov <drizt@land.ru> - 1:2.0-5
- Add qconf-qt5 binary name

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb 01 2016 Rex Dieter <rdieter@fedoraproject.org> 2.0-3
- use %%qmake_qt5 macro to ensure proper build flags

* Fri Jan 22 2016 Rex Dieter <rdieter@fedoraproject.org> 2.0-2
- use %%_qt5_prefix macro (instead of hard-coded %%_libdir/qt5)

* Wed Dec  9 2015 Ivan Romanov <drizt@land.ru> - 1:2.0-1
- New upstream version 2.0
- Use pkgconfig() style
- Drop qconf-2.0-optflags patch (went to upstream)
- Clean .spec file
- Link to Qt5

* Sun Oct 25 2015 Ivan Romanov <drizt@land.ru> - 1:1.4-2
- bump release

* Tue Sep 15 2015 Ivan Romanov <drizt@land.ru> - 1:1.4-1
- Use epoch after wrong 1.5 version in Koji

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.4-11
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Jan 01 2012 Rex Dieter <rdieter@fedoraproject.org> 1.4-4
- BR: qt4-devel (#751249)

* Sun Jan 1 2012 Ivan Romanov <drizt@land.ru> - 1.4-3
- Added qt epoch to ruquires. Resolved #751249
- Two minutes before New Year holiday ;)

* Sat Apr 9 2011 Ivan Romanov <drizt@land.ru> - 1.4-2
- added patch to support optflags
- used qmake for build stage instead configure
- changed summary
- corrected codestyle
- fix build requires (thanks to Alexey Panov)
- binary renamed to qconf-qt4

* Thu Nov 12 2009 Arkady L. Shane <ashejn@yandex-team.ru> - 1.4-1
- initial build for Fedora

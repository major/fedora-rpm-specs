Name:       qterm
Version:    0.7.4
Release:    10%{?dist}
Summary:    BBS client for X Window System written in Qt
License:    GPLv2+
URL:        https://github.com/qterm/qterm
Source0:    https://github.com/qterm/qterm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel >= 5.3
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  openssl-devel >= 1.0
BuildRequires:  cmake >= 2.8.11
BuildRequires:  desktop-file-utils
Requires:   hicolor-icon-theme


%description
QTerm is a BBS client for X Window System. It supports Telnet, SSH1 and SSH2
protocols. It also supports ZMODEM, URL analysis and mouse gesture.

%prep
%setup -q

%build
%cmake -DQT5=YES
%cmake_build

%install
%cmake_install

# rename the executable to QTerm to prevent conflict with torque-client
mv %buildroot%{_bindir}/{qterm,QTerm}
sed -i 's/Exec=qterm/Exec=QTerm/' %buildroot%{_datadir}/applications/%{name}.desktop

desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    --remove-category Application \
    --add-category RemoteAccess \
    %buildroot%{_datadir}/applications/*.desktop

%files
%doc README* RELEASE_NOTES TODO doc/*
%license COPYRIGHT
%{_bindir}/QTerm
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.7.4-6
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Aug  6 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.7.4-3
- Improve compatibility with new CMake macro

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Robin Lee <cheeselee@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4 (RHBZ#1834749)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug  1 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3 (BZ#1610326, BZ#1606052, BZ#1529834)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 0.7.2-6
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.2-4
- Remove obsolete scriptlets

* Sat Sep 23 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.7.2-3
- Update to 0.7.2 (BZ#1494766)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 13 2017 Robin Lee <cheeselee@fedoraproject.org> - 0.7.1-1
- Upate to 0.7.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 16 2016 Robin Lee <cheeselee@fedoraproject.org> - 0.5.12-13
- Fix FTBFS with GCC 6 (BZ#1307971)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.5.12-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug  7 2013 Robin Lee <cheeselee@fedoraproject.org> - 0.5.12-7
- Fix description to use unversioned docdir (BZ#993924)
- Update URL

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 16 2012 Robin Lee <cheeselee@fedoraproject.org> - 0.5.12-3
- Fix build with F17
- rename the executable to QTerm to prevent conflict with torque-client
- Specfile untabified

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 24 2011 Robin Lee <cheeselee@fedoraproject.org> - 0.5.12-1
- Update to 0.5.12 (#715246)
- Conflicts torque-client (#587554)
- URL updated
- Description revised

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun 15 2010 Chen Lei <supercyper@163.com> - 0.5.11-1
- Upstream to 0.5.11

* Sun Apr 25 2010 Chen Lei <supercyper@163.com> - 0.5.10-2
- Add patch for building against qt-4.7 

* Sun Jan 17 2010 Chen Lei <supercyper@163.com> - 0.5.10-1
- Upstream to 0.5.10

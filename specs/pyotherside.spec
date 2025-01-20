Summary: Asynchronous Python 3 Bindings for Qt 5
Name: pyotherside
Version:    1.6.1
Release:    3%{?dist}
Source0: https://github.com/thp/pyotherside/archive/%{version}/%{name}-%{version}.tar.gz
URL: http://thp.io/2011/pyotherside/
License: ISC
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-private-devel

BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: xorg-x11-server-Xvfb

Requires: python3

%description
A QML Plugin that provides access to a Python 3 interpreter from QML.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%{qmake_qt5}
%make_build

%check
xvfb-run ./tests/tests

%install
make INSTALL_ROOT=%{buildroot} install

%files
%doc README.md
%license LICENSE
%dir %{_qt5_archdatadir}/qml/io/
%dir %{_qt5_archdatadir}/qml/io/thp/
%{_qt5_archdatadir}/qml/io/thp/pyotherside
%exclude %{_qt5_prefix}/tests/qtquicktests

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Leigh Scott <leigh123linux@gmail.com> - 1.6.1-1
- Update to 1.6.1, fixes rhbz#2251082

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.6.0-8
- Rebuilt for Python 3.13

* Fri May 17 2024 Martin Kolman <mkolman@redhat.com> - 1.6.0-7
- backport Python 3.12 compatibility fix

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.6.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Martin Kolman <mkolman@redhat.com> - 1.6.0-1
- Update to 1.6.0
- version 1.6.0 adds support for Qt 6 but we still build with Qt 5 for now

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 1.5.9-15
- Rebuild (qt5)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.9-14
- Rebuilt for Python 3.11

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 1.5.9-13
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 1.5.9-12
- Rebuild (qt5)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.5.9-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 23 07:54:15 CET 2020 Jan Grulich <jgrulich@redhat.com> - 1.5.9-7
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 1.5.9-6
- rebuild (qt5)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.9-4
- Rebuilt for Python 3.9

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.5.9-3
- rebuild (qt5)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Martin Kolman <mkolman@redhat.com> - 1.5.9-1
- Update to 1.5.9
- this should fix build issues with Python 3.9

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 1.5.8-6
- rebuild (qt5)

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 1.5.8-5
- rebuild (qt5)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.8-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.5.8-2
- rebuild (qt5)

* Wed Jun 19 2019 Martin Kolman <mkolman@redhat.com> - 1.5.8-1
- Update to 1.5.8
- this should fix build issues with Python 3.8

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 1.5.4-6
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 1.5.4-5
- rebuild (qt5)

* Wed Mar 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.5.4-4
- rebuild (qt5)

* Tue Feb 12 2019 Martin Kolman <mkolman@redhat.com> - 1.5.4-3
- Rebuilt to prove last build failure was just mass rebuild related breakage

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 28 2019 Martin Kolman <mkolman@redhat.com> - 1.5.4-1
- Updated to 1.5.4

* Thu Dec 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.5.3-15
- rebuild (qt5)

* Fri Sep 21 2018 Jan Grulich <jgrulich@redhat.com> - 1.5.3-14
- rebuild (qt5)

* Wed Aug 22 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.5.3-13
- better exclude fix

* Tue Jul 17 2018 Martin Kolman <mkolman@redhat.com> - 1.5.3-12
- fix exclude for qtquicktests

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-10
- Rebuilt for Python 3.7

* Thu Jun 21 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.5.3-9
- rebuild (qt5)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5.3-8
- Rebuilt for Python 3.7

* Sun May 27 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.5.3-7
- rebuild (qt)
- use %%make_build %%license

* Wed Feb 14 2018 Jan Grulich <jgrulich@redhat.com> - 1.5.3-6
- rebuild (qt5)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.5.3-4
- rebuild (qt5)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.5.3-3
- rebuild (qt5)

* Thu Nov 16 2017 Christian Dersch <lupinix@fedoraproject.org> - 1.5.3-2
- rebuilt (Qt 5.9.2)

* Mon Oct 16 2017 Martin Kolman <mkolman@redhat.com> - 1.5.3-1
- Updated to 1.5.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.5.1-5
- BuildRequires: qt5-qtbase-private-devel

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 Martin Kolman <mkolman@redhat.com> - 1.5.1-2
- exclude a test related executable

* Mon Mar 20 2017 Martin Kolman <mkolman@redhat.com> - 1.5.1-1
- updated to 1.5.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-3
- Rebuild for Python 3.6

* Wed Jun 15 2016 Martin Kolman <mkolman@redhat.com> - 1.5.0-2
- add missing pkgconfig(Qt5Svg) dependency

* Wed Jun 15 2016 Martin Kolman <mkolman@redhat.com> - 1.5.0-1
- updated to 1.5.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 Rex Dieter <rdieter@fedoraproject.org> 1.4.0-4
- drop needless ldconfig scriptlets
- drop deprecated .spec tags
- use %%qmake_qt5, %%{_qt5_archdatadir} macros

* Fri Apr 10 2015 Martin Kolman <mkolman@redhat.com> - 1.4.0-3
- fix QML plugin directory ownership

* Thu Apr 02 2015 Martin Kolman <mkolman@redhat.com> - 1.4.0-2
- add a changelog
- call ldconfig correctly
- run the test suite in check

* Thu Apr 02 2015 Martin Kolman <mkolman@redhat.com> - 1.4.0-1
- update to upstream release 1.4.0

* Wed Dec 10 2014 Martin Kolman <mkolman@redhat.com> - 1.3.0-1
- Initial package

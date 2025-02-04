%{?mingw_package_header}

%global pypi_name PyQt5

Name:           mingw-python-qt5
Summary:        MinGW Windows PyQt5
Version:        5.15.11
Release:        1%{?dist}
BuildArch:      noarch

# Some examples are BSD-3-Clause and MIT, but examples are not packaged
License:        GPL-3.0-only
Url:            http://www.riverbankcomputing.com/software/pyqt/
Source0:        %{pypi_source}


BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 102
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-python3
BuildRequires:  mingw32-python3-PyQt-builder
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtlocation
BuildRequires:  mingw32-qt5-qtmultimedia
BuildRequires:  mingw32-qt5-qtsensors
BuildRequires:  mingw32-qt5-qtserialport
BuildRequires:  mingw32-qt5-qtsvg
BuildRequires:  mingw32-qt5-qttools
BuildRequires:  mingw32-qt5-qtwebkit
BuildRequires:  mingw32-qt5-qtxmlpatterns
BuildRequires:  mingw32-qt5-qtwebchannel
BuildRequires:  mingw32-sip >= 6.0.0

BuildRequires:  mingw64-filesystem >= 102
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-python3
BuildRequires:  mingw64-python3-PyQt-builder
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtlocation
BuildRequires:  mingw64-qt5-qtmultimedia
BuildRequires:  mingw64-qt5-qtsensors
BuildRequires:  mingw64-qt5-qtserialport
BuildRequires:  mingw64-qt5-qtsvg
BuildRequires:  mingw64-qt5-qttools
BuildRequires:  mingw64-qt5-qtwebkit
BuildRequires:  mingw64-qt5-qtxmlpatterns
BuildRequires:  mingw64-qt5-qtwebchannel
BuildRequires:  mingw64-sip >= 6.0.0


%description
MinGW Windows PyQt5


%package -n mingw32-python3-qt5
Summary:       MinGW Windows Python3-Qt5
Requires:      mingw32-python3-pyqt5-sip

%description -n mingw32-python3-qt5
MinGW Windows Python3-Qt5


%package -n mingw64-python3-qt5
Summary:       MinGW Windows Python3-Qt5
Requires:      mingw64-python3-pyqt5-sip

%description -n mingw64-python3-qt5
MinGW Windows Python3-Qt5


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pypi_name}-%{version}


%build
mingw32-sip-build --build-dir=build_win32 --no-make --qt-shared --confirm-license --qmake=%{_bindir}/mingw32-qmake-qt5 --no-tools --verbose
mingw64-sip-build --build-dir=build_win64 --no-make --qt-shared --confirm-license --qmake=%{_bindir}/mingw64-qmake-qt5 --no-tools --verbose
%mingw_make_build


%install
%mingw_make_install INSTALL_ROOT=%{buildroot}


%files -n mingw32-python3-qt5
%license LICENSE
%{mingw32_libdir}/qt5/plugins/designer/pyqt5.dll
%{mingw32_libdir}/qt5/plugins/PyQt5/
%{mingw32_python3_sitearch}/%{pypi_name}/
%{mingw32_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%files -n mingw64-python3-qt5
%license LICENSE
%{mingw64_libdir}/qt5/plugins/designer/pyqt5.dll
%{mingw64_libdir}/qt5/plugins/PyQt5/
%{mingw64_python3_sitearch}/%{pypi_name}/
%{mingw64_python3_sitearch}/%{pypi_name}-%{version}.dist-info/


%changelog
* Sun Feb 02 2025 Sandro Mani <manisandro@gmail.com> - 5.15.11-1
- Update to 5.15.11

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 27 2024 Sandro Mani <manisandro@gmail.com> - 5.15.10-10
- Fix requires

* Wed Dec 25 2024 Sandro Mani <manisandro@gmail.com> - 5.15.10-9
- Rebuild (sip)

* Sun Dec 08 2024 Sandro Mani <manisandro@gmail.com> - 5.15.10-8
- Rebuild (mingw-sip)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Sandro Mani <manisandro@gmail.com> - 5.15.10-6
- Rebuild (sip)

* Sat Feb 24 2024 Sandro Mani <manisandro@gmail.com> - 5.15.10-5
- Rebuild (sip)

* Sat Jan 27 2024 Sandro Mani <manisandro@gmail.com> - 5.15.10-4
- Rebuild (sip)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Sandro Mani <manisandro@gmail.com> - 5.15.10-1
- Update to 5.15.10

* Mon Aug 14 2023 Sandro Mani <manisandro@gmail.com> - 5.15.9-5
- Rebuild (sip)

* Sat Jul 29 2023 Sandro Mani <manisandro@gmail.com> - 5.15.9-4
- Rebuild (sip)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Apr 26 2023 Sandro Mani <manisandro@gmail.com> - 5.15.9-2
- Rebuild (sip)

* Tue Feb 07 2023 Sandro Mani <manisandro@gmail.com> - 5.15.9-1
- Update to 5.15.9

* Thu Feb 02 2023 Sandro Mani <manisandro@gmail.com> - 5.15.8-1
- Update to 5.15.8

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-11
- Rebuild (sip)

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-10
- Rebuild (python-3.11)

* Fri Jul 22 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-9
- Rebuild (sip)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-7
- Rebuild with mingw-gcc-12

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-6
- Rebuild (sip)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-5
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 5.15.6-4
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Sandro Mani <manisandro@gmail.com> - 5.15.6-2
- Rebuild (sip)

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 5.15.6-1
- Update to 5.15.6

* Wed Oct 13 2021 Sandro Mani <manisandro@gmail.com> - 5.15.4-4
- Rebuild (sip-6.3.1)

* Tue Oct 05 2021 Sandro Mani <manisandro@gmail.com> - 5.15.4-3
- Rebuild (sip)

* Fri Oct 01 2021 Sandro Mani <manisandro@gmail.com> - 5.15.4-2
- Require mingw-python3-PyQt5_sip

* Wed Sep 15 2021 Sandro Mani <manisandro@gmail.com> - 5.15.4-1
- Update to 5.15.4

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 5.15.0-6
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 10:08:39 CET 2020 Sandro Mani <manisandro@gmail.com> - 5.15.0-4
- Rebuild (qt5)

* Thu Oct  8 09:25:25 CEST 2020 Sandro Mani <manisandro@gmail.com> - 5.15.0-3
- Rebuild (qt5)

* Tue Sep 15 2020 Sandro Mani <manisandro@gmail.com> - 5.15.0-2
- Rebuild (qt5)

* Tue Aug 18 2020 Sandro Mani <manisandro@gmail.com> - 5.15.0-1
- Update to 5.15.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-2
- Rebuild (python-3.9)

* Sat Apr 11 2020 Sandro Mani <manisandro@gmail.com> - 5.14.2-1
- Update to 5.14.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-3
- Rebuild (qt5)

* Thu Dec 12 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-2
- Rebuild (qt5)

* Tue Nov 05 2019 Sandro Mani <manisandro@gmail.com> - 5.13.2-1
- Update to 5.13.2

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 5.13.1-2
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Oct 01 2019 Sandro Mani <manisandro@gmail.com> - 5.13.1-1
- Update to 5.13.1

* Fri Sep 27 2019 Sandro Mani <manisandro@gmail.com> - 5.13.0-3
- Rebuild (python 3.8, qt 5.12.5)

* Wed Aug 28 2019 Sandro Mani <manisandro@gmail.com> - 5.13.0-2
- Rebuild (qt5-qtwebkit)

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 5.13.0-1
- Update to 5.13.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-3
- Actually apply patch

* Fri Jul 19 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-2
- Backport python2 fix

* Thu Jul 18 2019 Sandro Mani <manisandro@gmail.com> - 5.12.3-1
- Update to 5.12.3

* Tue May 07 2019 Sandro Mani <manisandro@gmail.com> - 5.12.2-1
- Update to 5.12.2

* Wed May 01 2019 Sandro Mani <manisandro@gmail.com> - 5.12.1-2
- Add python3 subpackages

* Sat Apr 20 2019 Sandro Mani <manisandro@gmail.com> - 5.12.1-1
- Update to 5.12.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Sandro Mani <manisandro@gmail.com> - 5.11.3-2
- Rebuild for qt5-5.11.3

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 5.11.3-1
- Update to 5.11.3

* Mon Sep 24 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-5
- Bump qt_ver

* Sun Sep 23 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-4
- Rebuild for qt5-5.11.2

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-3
- Fix incorrect requires

* Sun Jul 29 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-2
- Require private PyQt5 sip modules

* Fri Jul 20 2018 Sandro Mani <manisandro@gmail.com> - 5.11.2-1
- Update to 5.11.2
- Enable qtserialport bindings

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-0.3.dev1805251538
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 21 2018 Sandro Mani <manisandro@gmail.com> - 5.10.2-0.2.dev1805251538
- Rebuild for qt5-5.11.1

* Fri Jun 01 2018 Sandro Mani <manisandro@gmail.com> - 5.10.2-0.1.dev1805251538
- Update to 5.10.2.dev1805251538

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 5.10.1-1
- Update to 5.10.1

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 5.10-5
- Add missing BR: gcc-c++, make

* Sat Feb 17 2018 Sandro Mani <manisandro@gmail.com> - 5.10-4
- Bump qt_ver to 5.10.1

* Fri Feb 16 2018 Sandro Mani <manisandro@gmail.com> - 5.10-3
- Rebuild for qt5-5.10.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Sandro mani <manisandro@gmail.com> - 5.10-1
- Update to 5.10

* Mon Jan 08 2018 Sandro Mani <manisandro@gmail.com> - 5.9.2-3
- Support Qt5 newer than just 5.9.3 (+5.9.4,5.10.0,5.10.1)

* Thu Dec 21 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-2
- Rebuild for qt5-5.10.0

* Mon Nov 27 2017 Sandro Mani <manisandro@gmail.com> - 5.9.2-1
- Update to 5.9.2

* Sat Nov 04 2017 Sandro Mani <manisandro@gmail.com> - 5.9.1-1
- Update to 5.9.1

* Wed Oct 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9-6
- Also build qtlocation, qtmultimedia and qtsensor bindings

* Wed Oct 11 2017 Jan Grulich <jgrulich@redhat.com> - 5.9-5
- Bump qt_ver to 5.9.2

* Tue Sep 19 2017 Sandro Mani <manisandro@gmail.com> - 5.9-4
- Rebuild (mingw-filesystem)

* Tue Sep 05 2017 Sandro Mani <manisandro@gmail.com> - 5.9-3
- Require mingw{32,64}-qt5-qttools for directory ownership

* Wed Aug 09 2017 Sandro Mani <manisandro@gmail.com> - 5.9-2
- Bump qt_ver to 5.9.1

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 5.9-1
- Update to 5.9

* Sat May 06 2017 Sandro Mani <manisandro@gmail.com> - 5.8.2-1
- Initial package

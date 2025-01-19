%{?mingw_package_header}

%global pkgname qscintilla
%global scintilla_ver 3.5.4

Name:          mingw-%{pkgname}
Summary:       MinGW Windows %{pkgname} library
Version:       2.14.1
Release:       6%{?dist}
BuildArch:     noarch

License:       GPL-3.0-only
Url:           http://www.riverbankcomputing.com/software/qscintilla/
Source0:       https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_src-%{version}.tar.gz

BuildRequires: make

BuildRequires: mingw32-filesystem >= 102
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-python3
BuildRequires: mingw32-qt5-qtbase
BuildRequires: mingw32-qt5-qtscript
BuildRequires: mingw32-qt5-qttools
BuildRequires: mingw32-python3-PyQt-builder
BuildRequires: mingw32-python3-qt5
BuildRequires: mingw32-sip

BuildRequires: mingw64-filesystem >= 102
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-python3
BuildRequires: mingw64-qt5-qtbase
BuildRequires: mingw64-qt5-qtscript
BuildRequires: mingw64-qt5-qttools
BuildRequires: mingw64-python3-PyQt-builder
BuildRequires: mingw64-python3-qt5
BuildRequires: mingw64-sip

Provides: bundled(scintilla) = %{scintilla_ver}


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 library

%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 library.


%package -n mingw32-python3-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 Python 3 bindings
Requires:      mingw32-%{pkgname}-qt5 = %{version}-%{release}
Requires:      mingw32-python3-qt5

%description -n mingw32-python3-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 Python 3 bindings.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 library

%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 library.


%package -n mingw64-python3-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname}-qt5 Python 3 bindings
Requires:      mingw64-%{pkgname}-qt5 = %{version}-%{release}
Requires:      mingw64-python3-qt5

%description -n mingw64-python3-%{pkgname}-qt5
MinGW Windows %{pkgname}-qt5 Python 3 bindings.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n QScintilla_src-%{version}


%build
pushd src
%mingw_qmake_qt5 ../qscintilla.pro
%mingw_make_build
popd

pushd Python
ln -s pyproject-qt5.toml pyproject.toml
mingw32-sip-build --build-dir=build_win32 --no-make --qmake=%{_bindir}/mingw32-qmake-qt5 --verbose \
    --qsci-include-dir=../src --qsci-library-dir=../src/build_win32/release --qsci-features-dir=../src/features
mingw64-sip-build --build-dir=build_win64 --no-make --qmake=%{_bindir}/mingw64-qmake-qt5 --verbose \
    --qsci-include-dir=../src --qsci-library-dir=../src/build_win64/release --qsci-features-dir=../src/features
%mingw_make_build
popd



%install
pushd src
%mingw_make_install INSTALL_ROOT=%{buildroot}
popd
pushd Python
%mingw_make_install INSTALL_ROOT=%{buildroot}
popd

%find_lang qscintilla --with-qt
grep "%{mingw32_datadir}/qt5/translations" qscintilla.lang > mingw32-qscintilla-qt5.lang
grep "%{mingw64_datadir}/qt5/translations" qscintilla.lang > mingw64-qscintilla-qt5.lang

# Fix library names and installation folders
mkdir -p %{buildroot}%{mingw32_bindir}
mkdir -p %{buildroot}%{mingw64_bindir}
mv %{buildroot}%{mingw32_libdir}/qscintilla2_qt5.dll %{buildroot}%{mingw32_bindir}/qscintilla2_qt5.dll
mv %{buildroot}%{mingw64_libdir}/qscintilla2_qt5.dll %{buildroot}%{mingw64_bindir}/qscintilla2_qt5.dll


%files -n mingw32-%{pkgname}-qt5 -f mingw32-qscintilla-qt5.lang
%license LICENSE
%{mingw32_bindir}/qscintilla2_qt5.dll
%{mingw32_libdir}/libqscintilla2_qt5.dll.a
%{mingw32_includedir}/qt5/Qsci/
%{mingw32_datadir}/qt5/mkspecs/features/qscintilla2.prf

%files -n mingw32-python3-%{pkgname}-qt5
%{mingw32_python3_sitearch}/PyQt5/bindings/Qsci/
%{mingw32_python3_sitearch}/PyQt5/Qsci.pyd
%{mingw32_python3_sitearch}/QScintilla-%{version}.dist-info/
%{mingw32_datadir}/qt5/qsci/


%files -n mingw64-%{pkgname}-qt5 -f mingw64-qscintilla-qt5.lang
%license LICENSE
%{mingw64_bindir}/qscintilla2_qt5.dll
%{mingw64_libdir}/libqscintilla2_qt5.dll.a
%{mingw64_includedir}/qt5/Qsci/
%{mingw64_datadir}/qt5/mkspecs/features/qscintilla2.prf

%files -n mingw64-python3-%{pkgname}-qt5
%{mingw64_python3_sitearch}/PyQt5/bindings/Qsci/
%{mingw64_python3_sitearch}/PyQt5/Qsci.pyd
%{mingw64_python3_sitearch}/QScintilla-%{version}.dist-info/
%{mingw64_datadir}/qt5/qsci/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 27 2024 Sandro Mani <manisandro@gmail.com> - 2.14.1-5
- Rebuild (sip)

* Tue Dec 10 2024 Sandro Mani <manisandro@gmail.com> - 2.14.1-4
- Rebuild (sip)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Sandro Mani <manisandro@gmail.com> - 2.14.1-2
- Rebuild (sip)

* Thu Jun 20 2024 Sandro Mani <manisandro@gmail.com> - 2.14.1-1
- Update to 2.14.1

* Sat Feb 24 2024 Sandro Mani <manisandro@gmail.com> - 2.13.4-9
- Rebuild (sip)

* Sat Jan 27 2024 Sandro Mani <manisandro@gmail.com> - 2.13.4-8
- Rebuild (sip)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Aug 14 2023 Sandro Mani <manisandro@gmail.com> - 2.13.4-5
- Rebuild (sip)

* Sun Jul 30 2023 Sandro Mani <manisandro@gmail.com> - 2.13.4-4
- Rebuild (sip)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 27 2023 Sandro Mani <manisandro@gmail.com> - 2.13.4-2
- Rebuild (sip)

* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 2.13.4-1
- Update to 2.13.4

* Tue Feb 07 2023 Sandro Mani <manisandro@gmail.com> - 2.13.0-16
- Rebuild (sip)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Sandro Mani <manisandro@gmail.com> - 2.13.0-14
- Rebuild (sip)

* Wed Oct 19 2022 Sandro Mani <manisandro@gmail.com> - 2.13.0-13
- Rebuild (python-3.11)

* Thu Aug 04 2022 Sandro Mani <manisandro@gmail.com> - 2.13.0-12
- Rebuild (sip)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.13.0-10
- Rebuild with mingw-gcc-12

* Fri Feb 18 2022 Sandro Mani <manisandro@gmail.com> - 2.13.0-9
- Rebuild (sip)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.13.0-8
- Rebuild for new python dependency generator (take two)

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.13.0-7
- Rebuild for new python dependency generator

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 23 2021 Sandro Mani <manisandro@gmail.com> - 2.13.0-5
- Rebuild (sip)

* Mon Nov 01 2021 Sandro Mani <manisandro@gmail.com> - 2.13.0-4
- Rebuild (sip)

* Wed Oct 13 2021 Sandro Mani <manisandro@gmail.com> - 2.13.0-3
- Rebuild (sip-6.3.1)

* Tue Oct 05 2021 Sandro Mani <manisandro@gmail.com> - 2.13.0-2
- Rebuild (sip)

* Wed Sep 15 2021 Sandro Mani <manisandro@gmail.coM> - 2.13.0-1
- Update to 2.13.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 05 2021 Sandro Mani <manisandro@gmail.coM> - 2.11.6-1
- Update to 2.11.6

* Fri Jun 11 2021 Sandro Mani <manisandro@gmail.com> - 2.11.5-3
- Rebuild (python-3.10)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Sandro Mani <manisandro@gmail.com> - 2.11.5-1
- Update to 2.11.5

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Sandro Mani <manisandro@gmail.com> - 2.11.2-9
- Rebuild (python-3.9)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-7
- Rebuild (Changes/Mingw32GccDwarf2)

* Mon Sep 30 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-6
- Rebuild (python 3.8)

* Mon Aug 05 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-5
- Drop python2 bindings

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-3
- Fix another incorrect requires

* Mon Jul 22 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-2
- Fix incorrect requires

* Fri Jul 19 2019 Sandro Mani <manisandro@gmail.com> - 2.11.2-1
- Update to 2.11.2

* Thu May 02 2019 Sandro Mani <manisandro@gmail.com> - 2.11.1-2
- Fix debug file in non-debug subpackage
- Add python3 subpackages
- Drop Qt4 build support

* Mon Feb 18 2019 Sandro Mani <manisandro@gmail.com> - 2.11.1-1
- Update to 2.11.1

* Wed Feb 13 2019 Sandro Mani <manisandro@gmail.com> - 2.11-1
- Update to 2.11

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 2.10.8-1
- Update to 2.10.8

* Tue Jul 31 2018 Sandro Mani <manisandro@gmail.com> - 2.10.7-1
- Update to 2.10.7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 17 2018 Sandro Mani <manisandro@gmail.com> - 2.10.4-1
- Update to 2.10.4

* Thu Mar 08 2018 Sandro Mani <manisandro@gmail.com> - 2.10.3-1
- Update to 2.10.3

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Sandro Mani <manisandro@gmail.com> - 2.10.2-1
- Update to 2.10.2

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 2.10.1-3
- Rebuild (mingw-filesystem)

* Wed Sep 06 2017 Sandro Mani <manisandro@gmail.com> - 2.10.1-2
- Disable qt4 build by default

* Thu Aug 10 2017 Sandro Mani <manisandro@gmail.com> - 2.10.1-1
- Update to 2.10.1

* Tue May 09 2017 Sandro Mani <manisandro@gmail.com> - 2.10.0-2
- Add Qt5 python bindings

* Thu Apr 20 2017 Sandro Mani <manisandro@gmail.com> - 2.10.0-1
- Update to 2.10.0

* Tue Jan 17 2017 Sandro Mani <manisandro@gmail.com> - 2.9.4-1
- Update to 2.9.4

* Fri Jan 22 2016 Sandro Mani <manisandro@gmail.com> - 2.9.1-1
- Update to 2.9.1

* Thu Aug 13 2015 Sandro Mani <manisandro@gmail.com> - 2.9-2
- Enable python bindings

* Fri Jun 26 2015 Sandro Mani <manisandro@gmail.com> - 2.9-1
- Initial package

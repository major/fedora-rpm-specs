%{?mingw_package_header}

%global pkgname qextserialport
%global libver 1
%global pre rc

Name:          mingw-%{pkgname}
Version:       1.2
Release:       0.20%{?pre:.%pre}%{?dist}
Summary:       MinGW Windows %{pkgname} library
BuildArch:     noarch

License:       MIT
URL:           https://github.com/qextserialport/qextserialport
Source0:       https://github.com/qextserialport/qextserialport/archive/%{version}%{pre}/%{pkgname}-%{version}%{pre}.tar.gz
# A private qt4 header, just grab it separately instead of adding a mingw-qt-private subpackage, since qt4 will not receive any updates anymore anyway
Source1:       https://raw.githubusercontent.com/qt/qt/4.8/src/corelib/kernel/qwineventnotifier_p.h

# Only do a release build
Patch0:        qextserialport_releasebuild.patch
# Use bundled qwineventnotifier_p.h (see SOURCE1)
Patch1:        qextserialport_qwineventnotifier_p.patch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-qt5-qtbase

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-qt5-qtbase


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} Qt5 library

%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname} Qt5 library.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} Qt5 library

%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname} Qt5 library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}%{pre}
cp -a %{SOURCE1} src/


%build
mkdir build_qt5
pushd build_qt5
%mingw_qmake_qt5 ../..
%mingw_make_build
popd


%install
pushd build_qt5
%mingw_make install INSTALL_ROOT=%{buildroot}
popd

# Remove duplicate dlls
rm -f %{buildroot}%{mingw32_libdir}/Qt5ExtSerialPort%{libver}.dll
rm -f %{buildroot}%{mingw64_libdir}/Qt5ExtSerialPort%{libver}.dll

# Fix import library names
mv %{buildroot}%{mingw32_libdir}/libQt5ExtSerialPort%{libver}.dll.a %{buildroot}%{mingw32_libdir}/libQt5ExtSerialPort.dll.a
mv %{buildroot}%{mingw64_libdir}/libQt5ExtSerialPort%{libver}.dll.a %{buildroot}%{mingw64_libdir}/libQt5ExtSerialPort.dll.a

# Remove unused files
rm -f %{buildroot}%{mingw32_libdir}/Qt5ExtSerialPort.prl
rm -f %{buildroot}%{mingw64_libdir}/Qt5ExtSerialPort.prl


%files -n mingw32-%{pkgname}-qt5
%license LICENSE
%{mingw32_bindir}/Qt5ExtSerialPort%{libver}.dll
%{mingw32_libdir}/libQt5ExtSerialPort.dll.a
%{mingw32_includedir}/qt5/QtExtSerialPort/
%{mingw32_datadir}/qt5/mkspecs/features/extserialport.prf

%files -n mingw64-%{pkgname}-qt5
%license LICENSE
%{mingw64_bindir}/Qt5ExtSerialPort%{libver}.dll
%{mingw64_libdir}/libQt5ExtSerialPort.dll.a
%{mingw64_includedir}/qt5/QtExtSerialPort/
%{mingw64_datadir}/qt5/mkspecs/features/extserialport.prf


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.20.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.19.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.18.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.17.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.16.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.15.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.14.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.2-0.13.rc
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.12.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.11.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.10.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.9.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.8.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.2-0.7.rc
- Rebuild (Changes/Mingw32GccDwarf2)
- Drop qt4 build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.6.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.5.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.4.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-0.3.rc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Apr 20 2017 Sandro Mani <manisandro@gmail.com> - 1.2-0.2.rc
- Update to 1.2-rc

* Wed Jun 24 2015 Sandro Mani <manisandro@gmail.com> - 1.2-0.1.beta2
- Initial package

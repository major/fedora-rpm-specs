%{?mingw_package_header}

%global pkgname qwtpolar

Name:           mingw-%{pkgname}
Version:        1.1.1
Release:        13%{?dist}
Summary:        MinGW Windows %{pkgname} library
BuildArch:      noarch

License:        LGPLv2 with exceptions
URL:            http://qwtpolar.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{pkgname}/%{pkgname}-%{version}.tar.bz2

# Use system qt_install paths
Patch0:        qwtpolar-1.1.1-qt_install_paths.patch
# Mingw fixes
Patch1:        qwtpolar-1.1.1_mingw.patch
# Place built libraries inside build directory to prevent mingw64 build
# overwriting mingw32 built
Patch2:        qwtpolar-1.1.1_libdestdir.patch
# Add versioned qt suffix to library name
Patch3:        qwtpolar-1.1.1_libname.patch

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-qwt-qt5

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-qwt-qt5


%description
MinGW Windows %{pkgname} library.


%package -n mingw32-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} library
Obsoletes:     mingw32-%{pkgname} < 1.1.1-6

%description -n mingw32-%{pkgname}-qt5
MinGW Windows %{pkgname} library.


%package -n mingw64-%{pkgname}-qt5
Summary:       MinGW Windows %{pkgname} library
Obsoletes:     mingw64-%{pkgname} < 1.1.1-6

%description -n mingw64-%{pkgname}-qt5
MinGW Windows %{pkgname} library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}

chmod 644 COPYING

# Don't build designer plugin
sed -i 's|QWT_POLAR_CONFIG     += QwtPolarDesigner|# QWT_POLAR_CONFIG     += QwtPolarDesigner|' qwtpolarconfig.pri


%build
%mingw_qmake_qt5 ../%{pkgname}.pro
%mingw_make_build


%install
%mingw_make install INSTALL_ROOT=%{buildroot}

# Fix library names and installation folders
mkdir -p %{buildroot}%{mingw32_bindir}
mv %{buildroot}%{mingw32_libdir}/qwtpolar-qt51.dll %{buildroot}%{mingw32_bindir}/qwtpolar-qt51.dll
mv %{buildroot}%{mingw32_libdir}/libqwtpolar-qt51.dll.a %{buildroot}%{mingw32_libdir}/libqwtpolar-qt5.dll.a

mkdir -p %{buildroot}%{mingw64_bindir}
mv %{buildroot}%{mingw64_libdir}/qwtpolar-qt51.dll %{buildroot}%{mingw64_bindir}/qwtpolar-qt51.dll
mv %{buildroot}%{mingw64_libdir}/libqwtpolar-qt51.dll.a %{buildroot}%{mingw64_libdir}/libqwtpolar-qt5.dll.a

# Delete documentation
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}

%files -n mingw32-%{pkgname}-qt5
%license COPYING
%{mingw32_bindir}/qwtpolar-qt51.dll
%{mingw32_libdir}/libqwtpolar-qt5.dll.a
%{mingw32_datadir}/qt5/mkspecs/features/%{pkgname}*
%{mingw32_includedir}/qt5/qwt_polar*.h

%files -n mingw64-%{pkgname}-qt5
%license COPYING
%{mingw64_bindir}/qwtpolar-qt51.dll
%{mingw64_libdir}/libqwtpolar-qt5.dll.a
%{mingw64_datadir}/qt5/mkspecs/features/%{pkgname}*
%{mingw64_includedir}/qt5/qwt_polar*.h


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.1.1-12
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.1.1-6
- Rebuild (Changes/Mingw32GccDwarf2)
- Switch to qt5

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jun 24 2015 Sandro Mani <manisandro@gmail.com>  - 1.1.1-1
- Initial package

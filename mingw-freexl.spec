%{?mingw_package_header}

%global pkgname freexl

Name:          mingw-%{pkgname}
Version:       1.0.6
Summary:       MinGW Windows freexl library
Release:       6%{?dist}

BuildArch:     noarch
License:       MPLv1.1 or GPLv2+ or LGPLv2+
URL:           https://www.gaia-gis.it/fossil/freexl/index
Source0:       http://www.gaia-gis.it/gaia-sins/%{pkgname}-sources/%{pkgname}-%{version}.tar.gz

BuildRequires: make
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-libcharset

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-libcharset


%description
MinGW Windows freexl library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows freexl library

%description -n mingw32-%{pkgname}
MinGW Windows freexl library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows freexl library

%description -n mingw64-%{pkgname}
MinGW Windows freexl library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_configure --enable-gcov=no --disable-static
%mingw_make_build


%install
%mingw_make_install

find %{buildroot} -name *.la -delete


%files -n mingw32-%{pkgname}
%license COPYING
%{mingw32_bindir}/libfreexl-1.dll
%{mingw32_includedir}/freexl.h
%{mingw32_libdir}/libfreexl.dll.a
%{mingw32_libdir}/pkgconfig/freexl.pc

%files -n mingw64-%{pkgname}
%license COPYING
%{mingw64_bindir}/libfreexl-1.dll
%{mingw64_includedir}/freexl.h
%{mingw64_libdir}/libfreexl.dll.a
%{mingw64_libdir}/pkgconfig/freexl.pc


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.0.6-5
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 03 2020 Sandro Mani <manisandro@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Sandro Mani <manisandro@gmail.com> - 1.0.5-1
- Update to 1.0.5

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Mon Jul 31 2017 Sandro Mani <manisandro@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Fri Jan 22 2016 Sandro Mani <manisandro@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Mon May 11 2015 Sandro Mani <manisandro@gmail.com> - 1.0.1-1
- Initial package

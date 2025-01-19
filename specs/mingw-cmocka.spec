%?mingw_package_header

Name:           mingw-cmocka
Version:        1.1.0
Release:        23%{?dist}
Summary:        MinGW Lightweight library to simplify and generalize unit tests for C

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://www.cmocka.org/

Source0:        https://cmocka.org/files/1.1/cmocka-%{version}.tar.xz
Patch0:         mingw-cmocka-1.1.0-win64.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++

BuildRequires:  cmake
BuildRequires:  pkgconfig


%description
Lightweight library to simplify and generalize unit tests for C.
This library is cross-compiled for MinGW.


# Win32
%package -n mingw32-cmocka
Summary:        MinGW GnuTLS TLS/SSL encryption library
Requires:       pkgconfig

%description -n mingw32-cmocka
Lightweight library to simplify and generalize unit tests for C.
This library is cross-compiled for MinGW.

# Win64
%package -n mingw64-cmocka
Summary:        MinGW GnuTLS TLS/SSL encryption library
Requires:       pkgconfig

%description -n mingw64-cmocka
Lightweight library to simplify and generalize unit tests for C.
This library is cross-compiled for MinGW.

# Win32/static
%package -n mingw32-cmocka-static
Summary:        Static version of the MinGW Windows cmocka library
Requires:       mingw32-cmocka = %{version}-%{release}

%description -n mingw32-cmocka-static
Static version of the MinGW Windows cmocka library.

# Win64/static
%package -n mingw64-cmocka-static
Summary:        Static version of the MinGW Windows cmocka library
Requires:       mingw64-cmocka = %{version}-%{release}

%description -n mingw64-cmocka-static
Static version of the MinGW Windows cmocka library.


%?mingw_debug_package


%prep
%setup -q -n cmocka-%{version}

%patch -P0 -p1 -b .win64

%build
if test ! -e "obj"; then
  mkdir obj
fi
pushd obj
%mingw_cmake \
  -DWITH_CMOCKERY_SUPPORT=ON \
  -DUNIT_TESTING=ON \
  %{_builddir}/cmocka-%{version}

%mingw_make %{?_smp_mflags} VERBOSE=1
popd

%install
pushd obj
%mingw_make_install DESTDIR=%{buildroot}
popd
mkdir -p %{buildroot}%{mingw64_libdir}/cmake/cmocka %{buildroot}%{mingw32_libdir}/cmake/cmocka
test -d %{buildroot}%{mingw64_prefix}/CMake/cmocka && mv %{buildroot}%{mingw64_prefix}/CMake/cmocka/*.cmake %{buildroot}%{mingw64_libdir}/cmake/cmocka
test -d %{buildroot}%{mingw32_prefix}/CMake/cmocka && mv %{buildroot}%{mingw32_prefix}/CMake/cmocka/*.cmake %{buildroot}%{mingw32_libdir}/cmake/cmocka
#There is a spurious -Llib/ in the pkgconfig file
sed -i 's/-Llib//g' %{buildroot}%{mingw64_libdir}/pkgconfig/cmocka.pc
sed -i 's/-Llib//g' %{buildroot}%{mingw32_libdir}/pkgconfig/cmocka.pc
test -f %{buildroot}%{mingw64_bindir}/libcmocka.dll && mv %{buildroot}%{mingw64_bindir}/libcmocka.dll %{buildroot}%{mingw64_bindir}/cmocka.dll
test -f %{buildroot}%{mingw32_bindir}/libcmocka.dll && mv %{buildroot}%{mingw32_bindir}/libcmocka.dll %{buildroot}%{mingw32_bindir}/cmocka.dll

%files -n mingw64-cmocka-static
%{mingw64_libdir}/libcmocka.a

%files -n mingw64-cmocka
%license COPYING
%doc AUTHORS README ChangeLog
%{mingw64_libdir}/libcmocka.dll.a
%{mingw64_bindir}/cmocka.dll
%{mingw64_includedir}/*.h
%{mingw64_includedir}/cmockery*
%{mingw64_libdir}/pkgconfig/cmocka.pc
%{mingw64_libdir}/cmake/cmocka*

%files -n mingw32-cmocka-static
%{mingw32_libdir}/libcmocka.a

%files -n mingw32-cmocka
%license COPYING
%doc AUTHORS README ChangeLog
%{mingw32_libdir}/libcmocka.dll.a
%{mingw32_bindir}/cmocka.dll
%{mingw32_includedir}/*.h
%{mingw32_includedir}/cmockery*
%{mingw32_libdir}/pkgconfig/cmocka.pc
%{mingw32_libdir}/cmake/cmocka*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.0-22
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.1.0-15
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.1.0-9
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct  3 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.1.0-2
- Corrected package names

* Thu Sep 29 2016 Nikos Mavrogiannopoulos <nmav@redhat.com> - 1.1.0-1
- Initial release


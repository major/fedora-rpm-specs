Name: msgpuck
Version: 2.0.36
Release: 6%{?dist}
Summary: MsgPack binary serialization library in a self-contained header
License: BSD
URL: https://github.com/tarantool/msgpuck
Source0: https://github.com/rtsisyk/msgpuck/archive/%{version}/msgpuck-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires: gcc
BuildRequires: coreutils
BuildRequires: cmake >= 2.8
BuildRequires: doxygen >= 1.6.0

# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_Header_Only_Libraries
# Nothing to add to -debuginfo package - this library is header-only
%global debug_package %{nil}

%package devel
Summary: MsgPack serialization library in a self-contained header file
Provides: msgpuck-static = %{version}-%{release}

%description
MsgPack is a binary-based efficient object serialization library.
It enables to exchange structured objects between many languages like JSON.
But unlike JSON, it is very fast and small.

msgpuck is very lightweight header-only library designed to be embedded to
your application by the C/C++ compiler. The library is fully documented and
covered by unit tests.

%description devel
MsgPack is a binary-based efficient object serialization library.
It enables to exchange structured objects between many languages like JSON.
But unlike JSON, it is very fast and small.

msgpuck is very lightweight header-only library designed to be embedded to
your application by the C/C++ compiler. The library is fully documented and
covered by unit tests.

This package provides a self-contained header file and a static library.
The static library contains generated code for inline functions and
global tables needed by the some library functions.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake . -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build
%cmake_build --target man

%check
%ctest
make -C %{__cmake_builddir} test

%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man3
install -Dpm 0644 %{__cmake_builddir}/doc/man/man3/msgpuck.h.3* %{buildroot}%{_mandir}/man3/

%files devel
%{_libdir}/libmsgpuck.a
%{_includedir}/msgpuck.h
%{_mandir}/man3/msgpuck.h.3*
%doc README.md
%{!?_licensedir:%global license %doc}
%license LICENSE AUTHORS

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.36-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 19 2020 Roman Tsisyk <rtsisyk@fedoraproject.org> - 2.0.36-2
- Re-enable tests.

* Sat Sep 19 2020 Roman Tsisyk <rtsisyk@fedoraproject.org> - 2.0.36-1
- New minor release.
- Use `cmake_build` && `cmake_install` instead of `make` && `make install`.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Roman Tsisyk <roman@tsisyk.com> 2.0.10-1
- Drop MP_SOURCE support, please link libmsgpuck.a.
- Add -fPIC to libmsgpuck.a to allow using from shared libraries.
- Add helpers to decode any number to int64/double.
- Fix possible integer overflow in mp_check().
- Fix a typo in MP_HINT decoding.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Roman Tsisyk <roman@tsisyk.com> 1.1.3-1
- Add mp_snprint() function.
- Change mp_fprint() to return the number of bytes printed instead of 0.
- Fix CVE-2016-9036.

* Tue Aug 09 2016 Roman Tsisyk <roman@tsisyk.com> 1.0.3-1
- Add mp_decode_strbin() and mp_decode_strbinl()
- Add mp_fprint() for debug output

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Roman Tsisyk <roman@tsisyk.com> 1.0.2-1
- Add coreutils and make to BuildRequires (#1295217)
- Use `install -Dpm` instead of `cp -p`
- Fix GCC 6.0 and Doxygen warnings

* Mon Jan 25 2016 Roman Tsisyk <roman@tsisyk.com> 1.0.1-3
- Add `BuildRequires: gcc` (#1295217)

* Sun Jan 24 2016 Roman Tsisyk <roman@tsisyk.com> 1.0.1-2
- Fix msgpuck-devel dependencies after removing empty msgpuck package

* Fri Jan 22 2016 Roman Tsisyk <roman@tsisyk.com> 1.0.1-1
- Changes according to Fedora review #1295217
- Fix SIGBUS on processesor without HW support for unaligned access

* Thu Jul 09 2015 Roman Tsisyk <roman@tsisyk.com> 1.0.0-1
- Initial version of the RPM spec

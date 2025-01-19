%{?mingw_package_header}

Name:           mingw-hamlib
Version:        3.3
Release:        14%{?dist}
Summary:        Run-time library to control radio transceivers and receivers

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://hamlib.sourceforge.net
Source0:        http://downloads.sourceforge.net/hamlib/hamlib-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libusbx

BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw64-binutils


%description
Hamlib provides a standardized programming interface that applications
can use to send the appropriate commands to a radio.

Also included in the package is a simple radio control program 'rigctl',
which lets one control a radio transceiver or receiver, either from
command line interface or in a text-oriented interactive interface.


%package -n mingw32-hamlib
Summary:        Run-time library to control radio transceivers and receivers for Win32

%description -n mingw32-hamlib


%package -n mingw64-hamlib
Summary:        Run-time library to control radio transceivers and receivers for Win64

%description -n mingw64-hamlib


%{?mingw_debug_package}


%prep
%autosetup -n hamlib-%{version}


%build
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}

find %{buildroot} -name "*.la" -delete

rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -rf %{buildroot}%{mingw32_datadir}/{doc,info,man}
rm -f %{buildroot}%{mingw64_bindir}/*.exe
rm -rf %{buildroot}%{mingw64_datadir}/{doc,info,man}


%files -n mingw32-hamlib
%{mingw32_bindir}/libhamlib-2.dll
%{mingw32_bindir}/libhamlib++-2.dll
%{mingw32_libdir}/libhamlib.dll.a
%{mingw32_libdir}/libhamlib++.dll.a
%{mingw32_libdir}/pkgconfig/hamlib.pc
%{mingw32_includedir}/hamlib/
%{mingw32_datadir}/aclocal/


%files -n mingw64-hamlib
%{mingw64_bindir}/libhamlib-2.dll
%{mingw64_bindir}/libhamlib++-2.dll
%{mingw64_libdir}/libhamlib.dll.a
%{mingw64_libdir}/libhamlib++.dll.a
%{mingw64_libdir}/pkgconfig/hamlib.pc
%{mingw64_includedir}/hamlib/
%{mingw64_datadir}/aclocal/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3-13
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.3-6
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Nov 21 2018 Richard Shaw <hobbes1069@gmail.com> - 3.3-1
- Update to 3.3.

* Tue Jul  4 2017 Richard Shaw <hobbes1069@gmail.com> - 3.1-1
- Initial packaging.

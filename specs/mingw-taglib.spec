%{?mingw_package_header}

%global _basename taglib

%bcond_without tests

Name:       mingw-%{_basename}
Summary:    Audio Meta-Data Library
Version:    1.12
Release:    13%{?dist}

# Automatically converted from old format: LGPLv2 or MPLv1.1 - review is highly recommended.
License:    LicenseRef-Callaway-LGPLv2 OR LicenseRef-Callaway-MPLv1.1
URL:        https://taglib.github.io/
Source0:    https://taglib.github.io/releases/%{_basename}-%{version}.tar.gz
Patch0:     taglib-1.12-multilib.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-zlib

BuildRequires:  cmake
%if %{with tests}
#BuildRequires: cppunit-devel
%endif

%description
TagLib is a library for reading and editing the meta-data of several
popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3
files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC,
Speex, WavPack, TrueAudio files, as well as APE Tags.


%package -n mingw32-%{_basename}
Summary: MinGW Windows version of TagLib for the win32 target

%description -n mingw32-%{_basename}
TagLib is a library for reading and editing the meta-data of several
popular audio formats.
This is the MinGW version, built for the win32 target.

%package -n mingw64-%{_basename}
Summary: MinGW Windows version of TagLib for the win64 target

%description -n mingw64-%{_basename}
TagLib is a library for reading and editing the meta-data of several
popular audio formats.
This is the MinGW version, built for the win64 target.


%{?mingw_debug_package}


%prep
%autosetup -n %{_basename}-%{version} -p1


%build
%{mingw_cmake} \
  %{?with_tests:-DBUILD_TESTS:BOOL=ON} \
  ..
%{mingw_make} %{?_smp_mflags}


%install
%{mingw_make} install/fast DESTDIR=%{buildroot}


%files -n mingw32-%{_basename}
%doc AUTHORS NEWS
%license COPYING.LGPL COPYING.MPL
%{mingw32_bindir}/libtag.dll
%{mingw32_bindir}/libtag_c.dll
%{mingw32_bindir}/taglib-config.cmd
%{mingw32_includedir}/taglib/
%{mingw32_libdir}/libtag.dll.a
%{mingw32_libdir}/libtag_c.dll.a
%{mingw32_libdir}/pkgconfig/taglib.pc
%{mingw32_libdir}/pkgconfig/taglib_c.pc

%files -n mingw64-%{_basename}
%doc AUTHORS NEWS
%license COPYING.LGPL COPYING.MPL
%{mingw64_bindir}/libtag.dll
%{mingw64_bindir}/libtag_c.dll
%{mingw64_bindir}/taglib-config.cmd
%{mingw64_includedir}/taglib/
%{mingw64_libdir}/libtag.dll.a
%{mingw64_libdir}/libtag_c.dll.a
%{mingw64_libdir}/pkgconfig/taglib.pc
%{mingw64_libdir}/pkgconfig/taglib_c.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12-12
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.12-5
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Apr 02 2021 David King <amigadave@amigadave.com> - 1.12-2
- Copy multilib patch from Fedora packaging

* Tue Feb 16 2021 David King <amigadave@amigadave.com> - 1.12-1
- Update to 1.12 (#1751547)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.11.1-9
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 05 2017 David King <amigadave@amigadave.com> - 1.11.1-4
- Add fix for CVE-2017-12678 (#1483961)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 David King <amigadave@amigadave.com> - 1.11.1-1
- Update to 1.11.1

* Thu Jun 09 2016 David King <amigadave@amigadave.com> - 1.11-1
- Update to 1.11

* Fri Mar 18 2016 David King <amigadave@amigadave.com> - 1.11-0.2.beta2
- Update to 1.11beta2

* Thu Feb 11 2016 David King <amigadave@amigadave.com> - 1.11-0.1.beta
- Update to 1.11beta

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 13 2015 David King <amigadave@amigadave.com> - 1.10-1
- Update to 1.10

* Wed Aug 26 2015 David King <amigadave@amigadave.com> - 1.10-0.1.beta
- Update to 1.10beta

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 25 2014 David King <amigadave@amigadave.com> 1.9.1-3
- Update to 1.9.1-3 from Fedora (#1077935)

* Fri May 17 2013 Steven Boswell <ulatekh@yahoo.com> 1.8-3.20121215git
- Ported Fedora package to MinGW

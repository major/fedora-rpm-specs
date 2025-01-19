%global		soversion	2.1

Name:		nvidia-texture-tools
Version:	2.1.2
Release:	12%{?dist}
Summary:	Collection of image processing and texture manipulation tools
# Automatically converted from old format: MIT and ASL 2.0 and BSD - review is highly recommended.
License:	LicenseRef-Callaway-MIT AND Apache-2.0 AND LicenseRef-Callaway-BSD
URL:		https://github.com/castano/nvidia-texture-tools/wiki
Source0:	https://github.com/castano/%{name}/archive/%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	help2man
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	libGL-devel
BuildRequires:	libGLU-devel

Patch0:		%{name}-libs.patch
Patch1:		%{name}-check.patch
Patch2:		%{name}-docs.patch
# add MIPS support
Patch3:		%{name}-mips.patch
# add S390 support
Patch4:		%{name}-s390.patch
# add PPCLE support
Patch5:		%{name}-ppcle.patch
# add aarch64 support
Patch6:		%{name}-aarch64.patch
# Do not presume SSE is available
Patch7:		%{name}-simd.patch
# Do not force compiler flags
Patch8:		%{name}-flags.patch
# Only implemented for x86
Patch9:		%{name}-debug.patch

%description
The NVIDIA Texture Tools is a collection of image processing and texture
manipulation tools, designed to be integrated in game tools and asset
conditioning pipelines.

The primary features of the library are mipmap and normal map generation,
format conversion and DXT compression.

DXT compression is based on Simon Brown's squish library. The library also
contains an alternative GPU-accelerated compressor that uses CUDA and is
one order of magnitude faster.

%package	devel
Summary:	Development libraries/headers for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
Headers and libraries for development with %{name}.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p0
%patch -P3 -p0
%patch -P4 -p0
%patch -P5 -p0
%patch -P6 -p0
%patch -P7 -p0
%patch -P8 -p0
%ifnarch %{ix86} x86_64
%patch -P9 -p0
%endif

%build
%cmake -DNVTT_SHARED=1 -DCMAKE_SKIP_RPATH=1	\
%ifnarch %{ix86} x86_64
	-DBUILD_SQUISH_WITH_SSE2=OFF		\
%endif
%if 0
%ifarch ppc64 ppc64le
	-DBUILD_SQUISH_WITH_ALTIVEC=ON		\
%endif
%endif

%cmake_build

sed -e 's/\r//' -i LICENSE

%install
%cmake_install
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
pushd $RPM_BUILD_ROOT/%{_bindir}
    export LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:
    for bin in *; do
	help2man --no-info ./$bin > $RPM_BUILD_ROOT/%{_mandir}/man1/$bin.1
    done
popd

%check
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT/%{_libdir}:
%ctest

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_libdir}/lib*.%{version}
%{_libdir}/lib*.%{soversion}
%{_mandir}/man1/*

%files		devel
%doc ChangeLog
%{_includedir}/nvtt
%{_libdir}/lib*.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.2-11
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 Kalev Lember <klember@redhat.com> - 2.1.2-5
- Drop unused openjpeg-devel build dep

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Feb 22 2021 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.1.2-1
- Update to version 2.1.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 19 2020 Kalev Lember <klember@redhat.com> - 2.0.8-25
- Fix FTBFS with new cmake macros (#1865080)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-24
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Nov 15 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-17
- Correct FTBFS in rawhide (#1424003)
- Add support for MIPS (#1366716)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 17 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-13
- Correct FTBFS in rawhide (#1307810)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.8-10
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.8-8
- add patch to fix ftbfs on aarch64

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jul 30 2013 Dennis Gilmore <dennis@ausil.us> - 2.0.8-6
- fix build on arm

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 2.0.8-4
- rebuild due to "jpeg8-ABI" feature drop

* Wed Dec 19 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-3
- Correct source url (#823096).
- No need for a -progs subpackage (#823096).

* Wed May 30 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-2
- Rename tools subpackage to progs.

* Fri May 18 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.0.8-1
- Initial nvidia-texture-tools spec.

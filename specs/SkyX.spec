%undefine __cmake_in_source_build
%global libversion 0.3.1
%global soversion 0

Name:           SkyX
Version:        0.4
Release:        39%{?dist}
Summary:        Photo-realistic sky simulator

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.paradise-sandbox.com/#hydraxskyx.php

# Source archives were manually extracted from rar files and re-compressed into
# gzip-ed tar files to remove the need for the unar tool during build.
# Original source files located at:
# http://modclub.rigsofrods.com/xavi/SkyX/SkyX-v0.4.rar
# http://modclub.rigsofrods.com/xavi/SkyX/SkyX-v0.3_CMake.rar
# Recompressed with commands:
# unar SkyX-v0.4.rar 
# tar caf SkyX-v0.4.tar.gz SkyX-v0.4
# unar SkyX-v0.3_CMake.rar 
# tar caf SkyX-v0.3_CMake.tar.gz SkyX-v0.3
Source0:        SkyX-v0.4.tar.gz
Source1:        SkyX-v0.3_CMake.tar.gz

# This patch contains some modifications made by the Gazebo project.
# It is mostly comment changes, but there are some API extensions needed
# by the gazebo robot simulator.
Patch0:         skyx_gazebo.patch
# This patch fixes some issues with building against Ogre 1.9.
# Not submitted upstream
Patch1:         %{name}-0.4-ogre19.patch
# Use boost shared libs
Patch2:         %{name}-0.4-boostshared.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  boost-devel
BuildRequires:  ogre-devel
BuildRequires:  ois-devel
BuildRequires:  dos2unix

%description
SkyX is a photo-realistic, simple and fast sky simulator.  It can be used
with the OGRE engine.

%package devel
Summary: Development files and libraries for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -T -c
tar -xf %{SOURCE0}
mv SkyX-v0.4/* .
tar -xf %{SOURCE1}
cp -r SkyX-v0.3/* .
rm -rf SkyX-v0.*
rm -f SkyXCommon/Bin/Media/packs/OgreCore.zip

%patch 0 -p1
%patch 1 -p0 -b .ogre19
%patch 2 -p0 -b .boostshared

# Remove Windows line endings
dos2unix Readme.txt License.txt
# Convert to UTF8
iconv -f ISO-8859-15 -t UTF-8 License.txt > License.conv && mv -f License.{conv,txt}
iconv -f ISO-8859-15 -t UTF-8 Readme.txt > Readme.conv && mv -f Readme.{conv,txt}

%build
%cmake \
  -DSKYX_BUILD_SAMPLES=OFF \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
mv %{buildroot}/SKYX/cmake %{buildroot}%{_datadir}/SKYX
%if "%{_lib}" == "lib64"
mv %{buildroot}/%{_usr}/lib %{buildroot}%{_libdir}
%endif

%files
%doc License.txt Readme.txt
%{_libdir}/*.so.%{libversion}
%{_libdir}/*.so.%{soversion}
%exclude %{_datadir}/SKYX/cmake
%{_datadir}/SKYX

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/SKYX
%{_datadir}/SKYX/cmake

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4-38
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Nov 23 2023 Rich Mattes <richmattes@gmail.com> - 0.4-34
- Fix boost linkage
- Resolves: rhbz#2114519

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Feb 12 2022 Rich Mattes <richmattes@gmail.com> - 0.4-31
- Re-compress sources as tar files to work around unar failre on s390

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-28
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 02 2020 Björn Esser <besser82@fedoraproject.org> - 0.4-26
- Fix string quoting for rpm >= 4.16

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4-18
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 31 2017 Jonathan Wakely <jwakely@redhat.com> - 0.4-16
- Rebuilt for Boost 1.63

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 0.4-14
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 0.4-12
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4-10
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 0.4-9
- Rebuild for boost 1.57.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Rich Mattes <richmattes@gmail.com> - 0.4-7
- Rebuild for ogre 1.9
- Update upstream URL

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Petr Machata <pmachata@redhat.com> - 0.4-5
- Rebuild for boost 1.55.0

* Sun Oct 20 2013 Rich Mattes <richmattes@gmail.com> - 0.4-4
- Fix build on i686 systems
- Correct project URL
- Correct license field (License.txt indicates LGPLv2+)

* Sun Oct 06 2013 Rich Mattes <richmattes@gmail.com> - 0.4-3
- Added patch containing Gazebo extensions

* Tue Aug 06 2013 Rich Mattes <richmattes@gmail.com> - 0.4-2
- Use upstream sources and unar

* Sun Jun 09 2013 Rich Mattes <richmattes@gmail.com> - 0.4-1
- Update to release 0.4

* Sun Jun 09 2013 Rich Mattes <richmattes@gmail.com> - 0.3.1-1
- Initial release

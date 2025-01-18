%undefine __cmake_in_source_build
%global libversion 1.0.0
Name:           gearbox
Version:        10.11
Release:        34%{?dist}
Summary:        A collection of usable peer-reviewed robotics-related libraries

# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            http://gearbox.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Moves the library installation path from libdir/name to libdir
Patch0:         gearbox-9.11.fixinstallpaths.patch
# Fixes DSO-related link errors.  Not yet submitted upstream
Patch1:         gearbox-9.11.fixdso.patch
# Fix build errors with gcc-4.7
Patch2:         gearbox-9.11.gcc47.patch
# Mark any 64-bit architecture as such
Patch3:         gearbox-64bit.patch
# Disable version check on gcc
Patch4:         gearbox-10.11-gcc10.patch


BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz


%description
Gearbox provides a collection of usable peer-reviewed robotics-related
libraries. Gearbox is not an integration framework. It provides a set
of implementations, without insisting on a standard API, for use by
any number of existing frameworks.  Gearbox includes cross-platform
libraries to communicate over TCP, UDP, and serial, and implements the
communication protocols of many popular sensors.


%package devel
Summary: Header files and libraries for %{name}
Requires: %{name} = %{version}-%{release}
Requires: cmake
%description devel
Contains the header files and libraries for %{name}. 
If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%setup -q
# Moves shared libraries from libdir/gearbox to libdir, as per FHS standards
%patch -P0 -p1 -b .fixinstallpaths
%patch -P1 -p1 -b .fixdso
%patch -P2 -p0 -b .gcc48
%patch -P3 -p1 -b .64bit
%patch -P4 -p1 -b .gcc10
%build
%cmake \
  -DENABLE_LIB_FLEXIPORT=OFF \
  -DENABLE_LIB_BASICEXAMPLE=OFF \
  -DENABLE_LIB_GBXUTILACFR=ON \
  -DENABLE_LIB_GBXGARMINACFR=ON \
  -DENABLE_LIB_GBXSERIALACFR=ON \
  -DHOKUYO_AIST_BUILD_BINDINGS=OFF \
  -DGBX_BUILD_TESTS=ON \
  -DCMAKE_SKIP_RPATH:BOOL=ON\
%ifarch ppc64 
 -DENABLE_LIB_GBXSICKACFR=OFF\
%else
 -DENABLE_LIB_GBXSICKACFR=ON\
%endif
 -DCMAKE_BUILD_TYPE=Release

%cmake_build
pushd doc
doxygen doxyfile
popd

%install
%cmake_install
# Remove the examples that gearbox installs.  If needed
# they can be built from source contained in the datadir
rm $RPM_BUILD_ROOT%{_bindir}/*


%files
%doc LICENSE
%{_libdir}/*.so.%{libversion}

%files devel
%doc doc/html
%doc doc/images
%{_libdir}/*.so
%{_libdir}/%{name}
%{_includedir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_datadir}/%{name}



%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 10.11-33
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-23
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 10.11-11
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 18 2014 Rich Mattes <richmattes@gmail.com> - 10.11-10
- Remove ice requirement in devel subpackage

* Tue Nov 18 2014 Rich Mattes <richmattes@gmail.com> - 10.11-9
- Remove ice requirement

* Thu Oct 02 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 10.11-8
- handle 64-bit architectures as such
- dropped s390x patch as not needed anymore

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 04 2013 Rich Mattes <richmattes@gmail.com> - 10.11-4
- Rebuild for new ice

* Sun Feb 03 2013 Kevin Fenzi <kevin@scrye.com> - 10.11-3
- Rebuild for broken deps in rawhide

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 07 2012 Rich Mattes <richmattes@gmail.com> - 10.11-1
- Update to 10.11
- Remove flexiport and hokuyo_aist (they are in separate packages now)
- Remove flexiport and hokuyo_aist licenses from spec

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.11-10
- Rebuilt for c++ ABI breakage

* Wed Jan 11 2012 Rich Mattes <richmattes@gmail.com> - 9.11-9
- gcc 4.8 build error fixes

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jun 20 2010 Dan Horák <dan[at]danny.cz> - 9.11-7
- add detection of s390x architecture

* Fri Mar 19 2010 Mary Ellen Foster <mefoster@gmail.com> - 9.11-6
- Rebuild with new Ice

* Thu Mar 11 2010 Rich Mattes <richmattes@gmail.com> - 9.11-5
- Fixed DSO related compile issues
- Removed -ice subpackage
- Fixed directory ownership
- Removed rpath
- Fixed source download URL

* Sat Feb 13 2010 Rich Mattes <richmattes@gmail.com> - 9.11-4
- Fixed pkg-config files from requiring non-existent packages

* Mon Jan 18 2010 Rich Mattes <richmattes@gmail.com> - 9.11-3
- Fixed package versioning
- Fixed sourceforge download URL
- Fixed gearbox-ice post operations

* Sat Jan 9 2010 Rich Mattes <richmattes@gmail.com> - 9.11-2
- Split libraries that use ICE into gearbox-ice subpackage
- Gearbox now builds on ppc64 without gearbox-ice subpackage

* Fri Nov 20 2009 Rich Mattes <richmattes@gmail.com> - 9.11-1
- Updated to version 9.11
- Updated package description

* Sun Nov 8 2009 Rich Mattes <richmattes@gmail.com> - 9.07-3
- Fixed cmake module install paths
- Fixed cmake file generation
- Aligned licenses with upstream
- Enabled ppc build

* Thu Oct 22 2009 Rich Mattes <richmattes@gmail.com> - 9.07-2
- Fixed library install path
- Fixed build order problem
- Fixed cmake module install path

* Wed Oct 21 2009 Rich Mattes <richmattes@gmail.com> - 9.07-1
- First build
- Fixed cmake 64 bit install paths
- Fixed license file

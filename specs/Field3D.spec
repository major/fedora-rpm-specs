Name:           Field3D
Version:        1.7.3
Release:        32%{?dist}
Summary:        Library for storing voxel data

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://sites.google.com/site/field3d/

Source0:        https://github.com/imageworks/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         Field3D-openexr.patch

BuildRequires:  cmake gcc-c++ doxygen
BuildRequires:  hdf5-devel
BuildRequires:  boost-devel
%if 0%{?fedora} > 34
# OpenEXR is only needed for OpenEXRConfig.h
BuildRequires:  cmake(OpenEXR)
BuildRequires:  cmake(Imath)
%else
BuildRequires:  ilmbase-devel
BuildRequires:  openexr-devel
%endif

Requires:       hdf5 = %{_hdf5_version}


%description
Field3D is an open source library for storing voxel data. It provides C++
classes that handle in-memory storage and a file format based on HDF5 that
allows the C++ objects to be written to and read from disk.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and documentation for %{name}.

# Need devel-docs subpackage.

%prep
%autosetup -p1


%build
export CXXFLAGS="%{optflags} -DH5_USE_110_API -DBOOST_TIMER_ENABLE_DEPRECATED"
%cmake -DINSTALL_DOCS=OFF

%cmake_build


%install
%cmake_install

install -D -m 0644 man/f3dinfo.1 %{buildroot}%{_mandir}/man1/f3dinfo.1


%check
pushd %{_vpath_builddir}
./unitTest


%files
%doc CHANGES README
%license COPYING
%{_bindir}/f3dinfo
%{_libdir}/libField3D.so.*
%{_mandir}/man1/f3dinfo.1*

%files devel
%doc docs/html/
%{_includedir}/Field3D/
%{_libdir}/libField3D.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Orion Poplawski <orion@nwra.com> - 1.7.3-31
- Rebuild for hdf5 1.14.5

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.3-30
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 1.7.3-28
- Rebuilt for openexr 3.2.4

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.7.3-25
- Rebuilt for Boost 1.83

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 06 2023 Patrick Palka <ppalka@redhat.com> - 1.7.3-23
- Fix build with boost-1.83.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.7.3-21
- Rebuilt for Boost 1.81

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.7.3-18
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 1.7.3-16
- Rebuild for hdf5 1.12.1

* Fri Aug 20 2021 Richard Shaw <hobbes1069@gmail.com> - 1.7.3-15
- Rebuild for OpenEXR/Imath 3.1.

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 1.7.3-14
- Rebuild for hdf5 1.10.7

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.7.3-13
- Rebuilt for Boost 1.76

* Sat Jul 31 2021 Richard Shaw <hobbes1069@gmail.com> - 1.7.3-12
- Add minimal patch for OpenEXR/Imath 3.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.7.3-10
- Rebuilt for removed libstdc++ symbol (#1937698)

* Fri Jan 29 2021 Richard Shaw <hobbes1069@gmail.com> - 1.7.3-9
- Add openexr to build requirements.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.7.3-7
- Rebuilt for Boost 1.75

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 1.7.3-6
- Rebuild for OpenEXR 2.5.3.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Orion Poplawski <orion@cora.nwra.com> - 1.7.3-3
- Rebuild for hdf5 1.10.6

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.7.3-2
- Rebuilt for Boost 1.73

* Thu Mar 12 2020 Richard Shaw <hobbes1069@gmail.com> - 1.7.3-1
- Update to 1.7.3.

* Mon Feb 03 2020 Kalev Lember <klember@redhat.com> - 1.7.2-18
- Avoid hardcoding man page compression

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Richard Shaw <hobbes1069@gmail.com> - 1.7.2-15
- Rebuild for OpenEXR 2.3.0.

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.7.2-14
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-12
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-9
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-6
- Rebuilt for Boost 1.64

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.7.2-5
- Rebuilt for Boost 1.63

* Tue Dec 06 2016 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-4
- Rebuild for hdf5 1.8.18

* Mon Oct 17 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7.2-3
- Add patch to fix unit tests on big endian systems.

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 1.7.2-2
- Rebuild for hdf5 1.8.17

* Mon Jun 20 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7.2-1
- Update to latest upstream release.

* Mon May 16 2016 Jonathan Wakely <jwakely@redhat.com> - 1.7.1-2
- Rebuilt for linker errors in boost (#1331983)

* Wed Mar  2 2016 Richard Shaw <hobbes1069@gmail.com> - 1.7.1-1
- Update to latest upstream release.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-10
- Rebuild for hdf5 1.8.16

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-9
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.6.1-8
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.6.1-6
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 17 2015 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-4
- Rebuild for hdf5 1.8.15

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.6.1-3
- Rebuilt for GCC 5 C++11 ABI change

* Sat Feb 21 2015 Orion Poplawski <orion@cora.nwra.com> - 1.6.1-2
- Rebuild for gcc 5 C++11 ABI

* Tue Feb 10 2015 Richard Shaw <hobbes1069@gmail.com> - 1.6.0-1
- Update to latest upstream release.

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.4.3-4
- Rebuild for boost 1.57.0

* Wed Jan 07 2015 Orion Poplawski <orion@cora.nwra.com> - 1.4.3-3
- Rebuild for hdf5 1.8.4

* Wed Nov 26 2014 Rex Dieter <rdieter@fedoraproject.org> 1.4.3-2
- rebuild (ilmbase), add matching/missing popd's

* Fri Sep  5 2014 Richard Shaw <hobbes1069@gmail.com> - 1.4.3-1
- Update to latest upstream release.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 10 2014 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-18
- Rebuild for hdf 1.8.13

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.3.2-16
- Rebuild for boost 1.55.0

* Fri Dec 27 2013 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-15
- Rebuild for hdf5 1.8.12

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-14
- rebuild (ilmbase)

* Sun Sep 08 2013 Rex Dieter <rdieter@fedoraproject.org> 1.3.2-13
- rebuild (ilmbase)

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 1.3.2-11
- Rebuild for boost 1.54.0

* Thu May 16 2013 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-10
- Rebuild for hdf5 1.8.11

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.3.2-9
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 1.3.2-8
- Rebuild for Boost-1.53.0

* Mon Dec  3 2012 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-7
- Rebuild for hdf5 1.8.10

* Wed Aug  8 2012 David Malcolm <dmalcolm@redhat.com> - 1.3.2-6
- rebuild against boost-1.50

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-3
- Rebuild for hdf5 1.8.9
- Explicitly require the version of hdf5 built with

* Fri Mar 23 2012 Richard Shaw <hobbes1069@gmail.com> - 1.3.2-2
- Bump EVR for oops with F17 package to make sure rawhide package is newer.

* Tue Feb 28 2012 Richard Shaw <hobbes1069@gmail.com> - 1.3.2-1
- Update to latest release.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-4
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jan 05 2012 Richard Shaw <hobbes1069@gmail.com> - 1.2.1-2
- Fixed building under GCC 4.7.0.

* Sat Nov 12 2011 Richard Shaw <hobbes1069@gmail.com> - 1.2.1-1
- Initial release.

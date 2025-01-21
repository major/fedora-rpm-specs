Name:           smesh
Version:        9.8.0.2
Release:        12%{?dist}
Summary:        OpenCascade based MESH framework

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            https://github.com/trelau/SMESH

# Upstream uses git submodules
# git clone https://github.com/trelau/SMESH.git
# cd SMESH
# git archive --prefix smesh-<VERSION>/ -o smesh-<VERSION>.tar v<VERSION TAG>
# pip intall "patch==1.*"
# python prepare.py
# tar --transform='s,^src,smesh-<VERSION>/src,' -rf smesh-<VERSION>.tar src/*
# gzip smesh-<VERSION>.tar
Source0:        https://github.com/trelau/SMESH/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         smesh-cmake.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2047018
Patch1:         smesh-std_swap.patch
Patch2:         netgen_sizet.patch


BuildRequires:  cmake gcc-c++ make
BuildRequires:  doxygen graphviz
BuildRequires:  boost-devel
BuildRequires:  catch-devel
BuildRequires:  opencascade-devel
BuildRequires:  libXmu-devel
BuildRequires:  vtk-devel

# Dependencies for optional NETGENPlugin library.
BuildRequires:  netgen-mesher-devel
BuildRequires:  netgen-mesher-devel-private

# Documentation is no longer built
Obsoletes:      %{name}-doc < 6.7.5-9


%description
A complete OpenCascade based MESH framework.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files and headers for %{name}.


%prep
%autosetup -p1


%build
LDFLAGS='-Wl,--as-needed'; export LDFLAGS
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo \
       -DENABLE_NETGEN=ON \
       -DNEW_NETGEN_INTERFACE=ON \
       -DENABLE_MED=OFF \
       -DBUILD_TESTS=TRUE

%cmake_build


%install
%cmake_install


%check
%ctest


%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/*.so

%files devel
%{_includedir}/smesh/
#{_libdir}/*.so
%{_libdir}/cmake/*.cmake


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 9.8.0.2-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 9.8.0.2-8
- Rebuilt for Boost 1.83

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 9.8.0.2-6
- Rebuilt for Boost 1.81

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jan 15 2023 Orion Poplawski <orion@nwra.com> - 9.8.0.2-4
- Rebuild for vtk 9.2.5

* Sat Jan 14 2023 Richard Shaw <hobbes1069@gmail.com> - 9.8.0.2-3
- Rebuild for opencascade.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 17 2022 Richard Shaw <hobbes1069@gmail.com> - 9.8.0.2-1
- Update to 9.8.0.2.

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 9.7.0.1-2
- Rebuilt for Boost 1.78

* Sun Jan 30 2022 Richard Shaw <hobbes1069@gmail.com> - 9.7.0.1-1
- Update to 9.7.0.1.

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 25 2021 Orion Poplawski <orion@nwra.com> - 9.6.0.2-3
- Rebuild for vtk 9.1.0

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 9.6.0.2-2
- Rebuilt for Boost 1.76

* Sat Jul 24 2021 Richard Shaw <hobbes1069@gmail.com> - 9.6.0.2-1
- Update to 9.6.0.2.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jan 31 2021 Orion Poplawski <orion@nwra.com> - 8.3.0.4-4
- Rebuild for VTK 9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 8.3.0.4-2
- Rebuilt for Boost 1.75

* Sun Nov 08 2020 Richard Shaw <hobbes1069@gmail.com> - 8.3.0.4-1
- Update to 8.3.0.4.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 8.3.0.3-2
- Rebuilt for Boost 1.73

* Tue May 05 2020 Richard Shaw <hobbes1069@gmail.com> - 8.3.0.3-1
- Update to 8.3.0.3.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 6.7.5-5
- Rebuilt for Boost 1.69

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 6.7.5-2
- Rebuilt for Boost 1.66

* Thu Aug 24 2017 Richard Shaw <hobbes1069@gmail.com> - 6.7.5-1
- Update to latest upstream release.

* Thu Jun  1 2017 Richard Shaw <hobbes1069@gmail.com> - 6.7.4-1
- Update to latest upstream release.

* Sat May 13 2017 Richard Shaw <hobbes1069@gmail.com> - 6.7.3-1
- Update to latest upstream release.

* Wed May 10 2017 Richard Shaw <hobbes1069@gmail.com> - 6.7.2-1
- Update to latest upstream release.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
 
* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 6.6-2
- Rebuilt for Boost 1.63

* Mon Jul 18 2016 Richard Shaw <hobbes1069@gmail.com> - 6.7-1
- Update to latest upstream release.

* Tue Apr  5 2016 Richard Shaw <hobbes1069@gmail.com> - 6.6-1
- Update to latest upstream release.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 6.5.3.1-10
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 6.5.3.1-9
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 6.5.3.1-7
- rebuild for Boost 1.58

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.5.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 6.5.3.1-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 29 2015 Jiri Kastner <jkastner@redhat.com> - 6.5.3.1-4
- fix build for ppc64 on rhel6 and OCE-0.16.1

* Wed Apr 29 2015 Jiri Kastner <jkastner@redhat.com> - 6.5.3.1-3
- fix problems with boost on rhel6

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 6.5.3.1-2
- Rebuild for boost 1.57.0

* Tue Dec  9 2014 Richard Shaw <hobbes1069@gmail.com> - 6.5.3.1-1
- Update to latest upstream release.

* Fri Nov 28 2014 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.4-1
- Move to forked project as original is no longer maintained.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-13
- Add patch for freecad specific tweaks.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 5.1.2.2-11.svn55
- Rebuild for boost 1.55.0

* Thu May 15 2014 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-10.svn55
- Fix license reference in spec file.

* Fri Feb 14 2014 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-9.svn55
- Bump revision to update package license reference.

* Thu Oct 10 2013 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-8.svn55
- Rebuild for OCE-0.13.

* Mon Jul 15 2013 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-7.svn55
- Rebuild for updated OCE.

* Fri Jun 21 2013 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-6.svn55
- Rebuild for OCE 0.12.

* Fri Feb 15 2013 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-1.svn55
- Update for compatibility with new OCE.

* Mon Oct 22 2012 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-5.svn54
- Remove build requirement for fortran (f2c).
- Initial packaging for EPEL 6.

* Wed Sep 26 2012 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-4.svn54
- Rebuild due to package not being signed in F-18 repo.

* Thu Mar 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 5.1.2.2-3.svn54
- Rebuilt for c++ ABI breakage

* Thu Jan 19 2012 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-2.svn54
- Minor updates to spec file.

* Tue Dec 20 2011 Richard Shaw <hobbes1069@gmail.com> - 5.1.2.2-1.svn54
- Initial release.

%global soversion 17
%global apiversion 1.6

Name:           ompl
Version:        1.6.0
Release:        7%{?dist}
Summary:        The Open Motion Planning Library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://ompl.kavrakilab.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  boost-devel >= 1.42.0
BuildRequires:  cmake >= 3.5.0
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  flann-devel
BuildRequires:  graphviz
BuildRequires:  ode-devel

# Move the installed CMake configuration from datadir to libdir.
# Refelects best practice with respect to arch-ful CMake configuration.
# Disable build/installation of plannerarena.
# Not submitted upstream.
Patch0: ompl-1.5.0-cmakeinstall.patch

%description
The Open Motion Planning Library (OMPL) consists of many state-of-the-art 
sampling-based motion planning algorithms. OMPL itself does not contain 
any code related to, e.g., collision checking or visualization. This is 
a deliberate design choice, so that OMPL is not tied to a particular 
collision checker or visualization front end.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
# Get rid of bundled libs
rm -rf src/external/
rm -rf scripts/plannerarena
%patch -P0 -p0 -b .cmakeinstall

%build
# Python bindings are disabled because dependencies pygccxml and pyplusplus are not packaged for Fedora
%cmake  \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_SKIP_RPATH=ON \
  -DOMPL_BUILD_PYBINDINGS=OFF \
  -DOMPL_LIB_INSTALL_DIR=%{_lib} \
  -DBOOST_LIBRARYDIR=%{_libdir} \
  -DODE_LIB_PATH=%{_libdir} \
  -DBUILD_OMPL_TESTS=ON  \
  -DOMPL_ODESOLVER=ON \
  -DOMPL_REGISTRATION=OFF

%cmake_build
%cmake_build --target ompl_doc
rm -f ompl_doc/installdox

%install
%cmake_install

rm -f %{buildroot}%{_datadir}/%{name}/demos/*.py
rm -rf %{buildroot}%{_includedir}/%{name}/CMakeFiles
rm -rf %{buildroot}%{_bindir}
rm -f %{buildroot}%{_mandir}/man1/plannerareana*
rm -rf %{buildroot}%{_datadir}/ament_index

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
# Test failures can be triggered by builder CPU speed.
# Accept test failures for slow builders.
%ctest || exit 0


%files
%doc LICENSE README.md
%{_libdir}/libompl.so.%{version}
%{_libdir}/libompl.so.%{soversion}
%{_mandir}/man1/*.1.*

%files devel
%doc %{_vpath_builddir}/ompl_doc
%{_libdir}/libompl.so
%{_includedir}/%{name}-%{apiversion}
%{_datadir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_libdir}/%{name}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.6.0-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Jonathan Wakely <jwakely@redhat.com> - 1.6.0-2
- Rebuilt for Boost 1.83

* Fri Nov 24 2023 Rich Mattes <richmattes@gmail.com> - 1.6.0-1
- Update to release 1.6.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.5.0-14
- Rebuilt for Boost 1.81

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 24 2022 Robert-André Mauchin <zebob.m@gmail.com> - 1.5.0-12
- Rebuilt for Ode soname bump

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.5.0-10
- Rebuilt for Boost 1.78

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Jonathan Wakely <jwakely@redhat.com> - 1.5.0-8
- Rebuilt for Boost 1.76

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 1.5.0-6
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.5.0-4
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Rich Mattes <richmattes@gmail.com> - 1.5.0-1
- Update to release 1.5.0

* Sat Apr 18 2020 Rich Mattes <richmattes@gmail.com> - 1.4.2-1
- Update to release 1.4.2 (rhbz#1428196)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-6
- Rebuilt for Boost 1.69

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 1.3.2-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.3.2-2
- Rebuilt for Boost 1.66

* Tue Nov 28 2017 Rich Mattes <richmattes@gmail.com> - 1.3.2-1
- Update to release 1.3.2 (rhbz#1428196)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 1.0.0-15
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-12
- Rebuilt for Boost 1.63

* Tue May 17 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-11
- Rebuilt for linker errors in boost (#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-9
- Patched for C++11 compatibility

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-8
- Rebuilt for Boost 1.60

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.0-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.0-5
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-3
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 Petr Machata <pmachata@redhat.com> - 1.0.0-2
- Rebuild for boost 1.57.0

* Fri Oct 31 2014 Rich Mattes <richmattes@gmail.com> - 1.0.0-1
- Update to release 1.0.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Rich Mattes <rmattes@fedoraproject.org> - 0.14.2-1
- Update to release 0.14.2

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 0.13.0-2
- Rebuild for boost 1.55.0

* Wed Aug 21 2013 Rich Mattes <richmattes@gmail.com> - 0.13.0-1
- Update to release 0.13.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 27 2013 pmachata@redhat.com - 0.12.2-2
- Rebuild for boost 1.54.0

* Wed May 01 2013 Rich Mattes <richmattes@gmail.com> - 0.12.2-1
- Update to release 0.12.2
- Remove bundled odeint

* Sun Feb 10 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.11.1-4
- Rebuild for Boost-1.53.0

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.11.1-3
- Rebuild for Boost-1.53.0

* Mon Aug 20 2012 Jon Ciesla <limburgher@gmail.com> - 0.11.1-2
- Rebuild for new ode.

* Thu Aug 09 2012 Rich Mattes <richmattes@gmail.com> - 0.11.1-1
- Update to release 0.11.1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Rich Mattes <richmattes@gmail.com> - 0.10.2-1
- Update to release 0.10.2

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-4
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 20 2011 Rich Mattes <richmattes@gmail.com> - 0.9.5-2
- Rebuilt for new boost

* Sun Oct 9 2011 Rich Mattes <richmattes@gmail.com> - 0.9.5-1
- Update to release 0.9.5

* Thu Jul 21 2011 Rich Mattes <richmattes@gmail.com> - 0.9.3-2
- Add python build requirement

* Sun May 15 2011 Rich Mattes <richmattes@gmail.com> - 0.9.3-1
- Update to 0.9.3
- Remove upstreamed patches

* Sun Apr 24 2011 Rich Mattes <richmattes@gmail.com> - 0.9.2-2
- Add patch to fix missing soname
- Removed CMakeFiles being installed in the includedir
- Fixed download directory

* Sun Jan 23 2011 Rich Mattes <richmattes@gmail.com> - 0.9.2-1
- Initial Package

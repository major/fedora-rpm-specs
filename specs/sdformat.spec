%undefine __cmake_in_source_build
%global apiver_major 6
%global apiver %{apiver_major}.3

Name:		sdformat
Version:	6.3.1
Release:	6%{?dist}
Summary:	The Simulation Description Format

License:	Apache-2.0
URL:		http://sdformat.org/
Source0:    https://github.com/gazebosim/%{name}/archive/sdformat6_%{version}/%{name}-%{version}.tar.gz
# Disable doxygen latex documentation
Patch0:         %{name}-2.0.1-latex.patch
# Make ruby install path configurable
# Fix Ruby exists?
Patch2:         %{name}-6.3.1-fixruby.patch
# Use URDF include directory
Patch3:         %{name}-6.3.1-urdfinclude.patch

BuildRequires:  gcc-c++
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	gtest-devel
BuildRequires:  ignition-cmake-devel
BuildRequires:  ignition-math-devel >= 4
BuildRequires:  ruby-devel >= 1.9
BuildRequires:  /usr/bin/ruby
BuildRequires:  rubygem-multi_xml
BuildRequires:  rubygem-rexml
BuildRequires:	texlive-refman
BuildRequires:	tinyxml-devel
BuildRequires:	urdfdom-devel

#Test dependencies
BuildRequires:  python3

%description
The Simulation Description Format (SDF) is an XML file format used to
describe all the elements in a software simulation environment. Originally
part of the Gazebo 3D robotic simulator, %{name} is a C++ library for reading
and writing files in the sdf format.

%package devel
Summary:	Development files and libraries for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
# For libdir/cmake directory
Requires:	cmake
Requires:	tinyxml-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:	Documentation for %{name}

%description doc
The %{name}-doc package contains development documentation for
%{name}.

%prep
%setup -q -n %{name}-%{name}6_%{version}
%patch 0 -p0 -b .latex
%patch 2 -p0 -b .fixruby
%patch 3 -p0 -b .urdfinclude
# Remove bundled urdf components
rm -rf src/urdf
sed -i 's/unset/#unset/g' CMakeLists.txt

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DLIB_INSTALL_DIR:STRING=%{_lib} \
  -DRUBY_LIB_INSTALL_DIR:STRING=%{ruby_vendorlibdir} \
  -DUSE_EXTERNAL_URDF=ON \
  -DSSE3_FOUND=false \
  -DSSSE3_FOUND=false \
  -DSSE4_1_FOUND=false \
  -DSSE4_2_FOUND=false \
%ifnarch x86_64
  -DSSE2_FOUND=false \
%endif
  -DUSE_UPSTREAM_CFLAGS=false \


%cmake_build
%cmake_build --target doc

%install
%cmake_install

%check
# The INTEGRATION_schema_test uses xmllint to validate flies
# against schemas.  It requires an internet connection, so it
# fails when built on koji
export GTEST_COLOR=no
%ctest --verbose --exclude-regex INTEGRATION_schema_test

%files
%license LICENSE COPYING
%doc AUTHORS README.md Changelog.md Migration.md
%{_datadir}/%{name}
%{_datadir}/ignition/sdformat%{apiver_major}.yaml
%{ruby_vendorlibdir}/ignition/cmdsdformat%{apiver_major}.rb
%{_libdir}/*.so.%{apiver_major}
%{_libdir}/*.so.%{version}

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}-%{apiver}
%{_libdir}/cmake/%{name}

%files doc
%license LICENSE COPYING
%doc %{_vpath_builddir}/doxygen/html

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 03 2024 Rich Mattes <richmattes@gmail.com> - 6.3.1-4
- Rebuild for urdfdom-4.0.0

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 13 2023 Rich Mattes <richmattes@gmail.com> - 6.3.1-1
- Update to release 6.3.1
- migrated to SPDX license
- Fix use of deprecated ruby function
- Resolves: rhbz#2165939

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Rich Mattes <richmattes@gmail.com> - 6.0.0-6
- Switch from python2 to python3 for tests (rhbz#1808342)
- Update spec to install libraries by version and soversion

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Jonathan Wakely <jwakely@redhat.com> - 6.0.0-2
- Rebuilt for Boost 1.69

* Fri Nov 23 2018 Till Hofmann <thofmann@fedoraproject.org> - 6.0.0-1
- Update to release 6.0.0
- Install ruby script into %%{ruby_vendorlibdir}
- Remove obsolete %%post and %%postun ldconfig scriptlets

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 18 2018 Iryna Shcherbina <ishcherb@redhat.com> - 5.2.0-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 5.2.0-2
- Rebuilt for Boost 1.66

* Sun Aug 20 2017 Rich Mattes <richmattes@gmail.com> - 5.2.0-1
- Update to release 5.2.0

* Sun Aug 20 2017 Rich Mattes <richmattes@gmail.com> - 5.1.0-5
- Add a fix for a cmake syntax error

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Björn Esser <besser82@fedoraproject.org> - 5.1.0-3
- Rebuilt for Boost 1.64

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 25 2017 Rich Mattes <richmattes@gmail.com> - 5.1.0-1
- Update to release 5.1.0

* Wed Feb 08 2017 Kalev Lember <klember@redhat.com> - 4.2.0-3
- Rebuilt for Boost 1.63

* Wed Jan 11 2017 Rich Mattes <richmattes@gmail.com> - 4.2.0-2
- Add tinyxml-devel to sdformat-devel's requirements

* Sun Oct 16 2016 Rich Mattes <richmattes@gmail.com> - 4.2.0-1
- Update to release 4.2.0 (rhbz#1383544)

* Sun Jul 17 2016 Rich Mattes <richmattes@gmail.com> - 4.1.1-1
- Update to release 4.1.1 (rhbz#1246705)

* Tue Jul 05 2016 Rich Mattes <richmattes@gmail.com> - 3.7.0-4
- Update for boost/gcc-6.1.1 symbol generation change (rhbz#1331983)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Jonathan Wakely <jwakely@redhat.com> - 3.7.0-2
- Rebuilt for Boost 1.60

* Mon Jan 04 2016 Rich Mattes <richmattes@gmail.com> - 3.7.0-1
- Update to release 3.7.0 (rhbz#1246705)

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 2.3.2-7
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 2.3.2-5
- rebuild for Boost 1.58

* Sun Jul 05 2015 Rich Mattes <richmattes@gmail.com> - 2.3.2-4
- Rebuild for boost (rhbz#1239159)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Rich Mattes <richmattes@gmail.com> - 2.3.2-2
- Update to release 2.3.2 (rhbz#1225680)

* Sat May 23 2015 Rich Mattes <richmattes@gmail.com> - 2.3.0-1
- Update to release 2.3.0
- Use license macro
- Remove upstream patches

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Sat Jan 31 2015 Rich Mattes <richmattes@gmail.com> - 2.0.1-3
- Disable latex documentation generation

* Thu Jan 29 2015 Petr Machata <pmachata@redhat.com> - 2.0.1-3
- Rebuild for boost 1.57.0

* Sun Sep 07 2014 Rich Mattes <richmattes@gmail.com> - 2.0.1-2
- Added CMake version script

* Sat Aug 23 2014 Rich Mattes <richmattes@gmail.com> - 2.0.1-1
- Update to release 2.0.1
- Apply upstream patch for urdfdom 0.3 support

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 26 2014 Rich Mattes <richmattes@gmail.com> - 2.0.0-3
- Apply patch for urdf 0.3.0 compatibility

* Sun May 25 2014 Petr Machata <pmachata@redhat.com> - 2.0.0-3
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 2.0.0-2
- rebuild for boost 1.55.0

* Tue Apr 15 2014 Rich Mattes <richmattes@gmail.com> - 2.0.0-1
- Update to release 2.0

* Sun Feb 09 2014 Rich Mattes <richmattes@gmail.com> - 1.4.11-3
- Rebuild for console-bridge 0.2.5

* Sun Jan 26 2014 Rich Mattes <richmattes@gmail.com> - 1.4.11-2
- Declare LIB_INSTALL_DIR relative to CMAKE_INSTALL_PREFIX (rhbz#1057939)

* Wed Nov 27 2013 Rich Mattes <richmattes@gmail.com> - 1.4.11-1
- Update to release 1.4.11

* Tue Nov 19 2013 Rich Mattes <richmattes@gmail.com> - 1.4.10-2
- Moved documentation into a separate subpackage
- Removed bundled gtest

* Sat Nov 16 2013 Rich Mattes <richmattes@gmail.com> - 1.4.10-1
- Update to release 1.4.10
- Add BuildRequres for tinyxml

* Wed Oct 09 2013 Rich Mattes <richmattes@gmail.com> - 1.4.8-2
- Unbundle urdfdom and urdfdom-headers

* Sun Oct 06 2013 Rich Mattes <richmattes@gmail.com> - 1.4.8-1
- Update to release 1.4.8

* Tue Aug 20 2013 Rich Mattes <richmattes@gmail.com> - 1.4.5-2
- Updated description field

* Sat Aug 17 2013 Rich Mattes <richmattes@gmail.com> - 1.4.5-1
- Initial package

%global sover 1.5
Name:       orocos-kdl
Version:    1.5.1
Release:    5%{?dist}
Summary:    A framework for modeling and computation of kinematic chains

License:    LGPLv2+
URL:        http://www.orocos.org/kdl.html
Source0:    https://github.com/orocos/orocos_kinematics_dynamics/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:     orocos-kdl.pybind11.patch
Patch1:     orocos-kdl.python-site-packages.patch

BuildRequires:  cmake
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  eigen3-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz

Requires:   eigen3

%description
The Kinematics and Dynamics Library (KDL) develops an application independent 
framework for modeling and computation of kinematic chains, such as robots, 
bio-mechanical human models, computer-animated figures, machine tools, etc. 
It provides class libraries for geometrical objects (point, frame, line,... ), 
kinematic chains of various families (serial, humanoid, parallel, mobile,... ),
and their motion specification and interpolation.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
The %{name}-doc package contains documentation for %{name}.

%package     -n python%{python3_pkgversion}-pykdl
Summary:        Python module for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pybind11
%{?python_provide:%python_provide python%{python3_pkgversion}-pykdl}

%description -n python%{python3_pkgversion}-pykdl
The python%{python3_pkgversion}-pykdl package contains the Python module
for %{name}.


%prep
%autosetup -p 1 -n orocos_kinematics_dynamics-%{version}


%build
pushd orocos_kdl
%cmake \
  -DENABLE_TESTS:BOOL=ON
%cmake_build
%cmake_build --target docs
# remove doxygen tag file, it is faulty and we do not need it
rm %{_vpath_builddir}/doc/kdl.tag

popd

pushd python_orocos_kdl
mkdir -p %{_vpath_builddir}/include/kdl
cp -a ../orocos_kdl/src/* %{_vpath_builddir}/include/kdl
cp -a ../orocos_kdl/%{_vpath_builddir}/src/* %{_vpath_builddir}/include/kdl
ln -s ../../../orocos_kdl/src %{_vpath_builddir}/include/kdl
CXXFLAGS="${CXXFLAGS:-%optflags} -Iinclude" \
  %cmake \
  -DPYTHON_SITE_PACKAGES_INSTALL_DIR=%{python3_sitearch} \
  -DPYTHON_VERSION=3
%cmake_build
popd


%install
pushd orocos_kdl
%cmake_install
popd

pushd python_orocos_kdl
%cmake_install
popd


%check
pushd orocos_kdl
%cmake_build --target check
popd


%files
%doc README.md
%license orocos_kdl/COPYING
%{_libdir}/*.so.%{sover}*

%files devel
%{_includedir}/*
%{_datadir}/orocos_kdl
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%doc orocos_kdl/%{_vpath_builddir}/doc/api/html

%files -n python%{python3_pkgversion}-pykdl
%{python3_sitearch}/PyKDL.so


%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.5.1-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.5.1-2
- Rebuilt for Python 3.11

* Tue Apr 12 2022 Till Hofmann <thofmann@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4.0-12
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 05 2020 Till Hofmann <thofmann@fedoraproject.org> - 1.4.0-10
- Adapt to cmake out-of-source builds
- Switch to pybind11 to fix FTBFS
- Remove unneeded patch

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-7
- Rebuilt for Python 3.9

* Tue Mar 10 2020 Scott K Logan <logans@cottsay.net> - 1.4.0-6
- Add python subpackage for PyKDL

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0
- Remove upstreamed patch
- Update patch to increase failure threshold, fixes tests on i686

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 29 2016 Rich Mattes <richmattes@gmail.com> - 1.3.1-2
- Rebuild for eigen3-3.3.1

* Tue May 03 2016 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.1-1
- Update to 1.3.1
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Sat Jun 27 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-6
- Add upstream patch to fix tests on ix86, reenable ix86
- Add build requirement for graphviz
- Make doc a noarch package
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Tue May 26 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-4
- Move documentation into doc package
* Thu May 21 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-3
- Exclude arch ix86, because the unit tests fail
* Thu Apr 30 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-2
- Clean up documentation (remove kdl.tag, install html doc)
- Split python bindings into separate SPEC file
* Thu Mar 26 2015 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.3.0-1
- Update to 1.3.0
- Remove libsuffix and version patches (included upstream)
- Enable tests
- Include python subpackage using bootstrapping
* Fri Apr 11 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.2.2-1
- Update to 1.2.2
* Fri Mar 14 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.1.102-2
- Include libsuffix patch
* Fri Feb 14 2014 Till Hofmann <hofmann@kbsg.rwth-aachen.de> - 1.1.102-1
- Initial package

## This release does not compile because of current unsupported GCC version (4.8.5) on rhel7
## during compilation of bundled 'jsoncpp'.
## Error "unsupported GCC version - see https://github.com/nlohmann/json#supported-compilers"

# Use devtoolset 8
%if 0%{?rhel} && 0%{?rhel} == 7
%global dts devtoolset-8-
%endif

# Qt6 builds for testing
%bcond_with qt6

Name:           avogadro2-libs
Version:        1.97.0
Release:        4%{?dist}
Summary:        Avogadro2 libraries

# BSD is main license
# BSD is the license of avogenerators scripts
License: BSD and MIT
URL:     http://avogadro.openmolecules.net/
Source0: https://github.com/OpenChemistry/avogadrolibs/archive/%{version}/avogadrolibs-%{version}.tar.gz
Source1: https://github.com/OpenChemistry/avogenerators/archive/%{version}/avogenerators-%{version}.tar.gz

# External sources for data files
Source2: https://github.com/OpenChemistry/molecules/archive/refs/heads/master.zip#/avogadro2-libs-molecules-master.zip
Source3: https://github.com/OpenChemistry/crystals/archive/1.0.1/crystals-1.0.1.tar.gz#/avogadro2-libs-crystals-1.0.1.tar.gz

# Set installation path of Python files
Patch0: %{name}-set_pythonpath.patch
Patch1: %{name}-1.94.0-do_not_download_external_files.patch
Patch2: %{name}-bug1185.patch

BuildRequires:  boost-devel
BuildRequires:  python%{python3_pkgversion}-devel
%if 0%{?rhel}
BuildRequires:  epel-rpm-macros
%endif
BuildRequires:  cmake3
BuildRequires:  chrpath
BuildRequires:  %{?dts}gcc
BuildRequires:  %{?dts}gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(openbabel-3)
BuildRequires:  mesa-libGLU-devel
BuildRequires:  hdf5-devel
BuildRequires:  mmtf-cpp-devel, jsoncpp-devel
BuildRequires:  spglib-devel
%if %{with qt6}
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtsvg-devel
%else
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
%endif
%if 0%{?fedora}
BuildRequires:  libarchive-devel >= 3.4.0
%endif
Provides: %{name}-static = 0:%{version}-%{release}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}

%description
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular modeling,
bioinformatics, materials science, and related areas.

%package  devel
Summary:  Development files of %{name}
%if %{with qt6}
Requires: qt6-qtbase-devel%{?_isa}
%else
Requires: qt5-qtbase-devel%{?_isa}
%endif
Requires: glew-devel%{?_isa}
Requires: libGL-devel%{?_isa}
Requires: mesa-libGLU-devel%{?_isa}
Requires: spglib-devel%{?_isa}
Requires: %{name}%{?_isa} = %{version}-%{release}

Provides: libgwavi-static

%description devel
This package contains libraries and header files for developing
applications that use %{name}.

%package doc
Summary: HTML documentation of %{name}
BuildArch: noarch
BuildRequires: doxygen, graphviz
BuildRequires: make
%description doc
HTML documentation of %{name}.

%prep
%autosetup -a 1 -N -n avogadrolibs-%{version}

unzip -qq %{SOURCE2} && mv molecules-master molecules
tar -xf %{SOURCE3} && mv crystals-1.0.1 crystals
# Rename LICENSE file
mv molecules/LICENSE molecules/LICENSE-molecules

%patch0 -p0 -b .backup
%patch1 -p0 -b .backup
%patch2 -p1 -b .backup

# Make avogadro generators source code available for CMake
mv avogenerators-%{version} avogadrogenerators
mv avogadrogenerators/README.md avogadrogenerators/README-avogenerators.md
sed -e 's|../avogadrogenerators|avogadrogenerators|g' -i avogadro/qtplugins/quantuminput/CMakeLists.txt
#

mv thirdparty/libgwavi/README.md thirdparty/libgwavi/README-libgwavi.md

%build
%if 0%{?el7}
%{?dts:source /opt/rh/devtoolset-8/enable}
%endif
mkdir -p build
export CXXFLAGS="%{optflags} -DH5_USE_110_API"
# RHBZ #1996330
%ifarch %{power64}
export CXXFLAGS="%{optflags} -DEIGEN_ALTIVEC_DISABLE_MMA"
%endif
%cmake3 -B build -DCMAKE_BUILD_TYPE:STRING=Release \
 -DINSTALL_INCLUDE_DIR:PATH=include/avogadro2 -DINSTALL_LIBRARY_DIR:PATH=%{_lib} \
 -Wno-dev \
 -DENABLE_GLSL:BOOL=ON \
 -DENABLE_PYTHON:BOOL=ON  \
 -DPYTHON_EXECUTABLE:FILEPATH=%{__python3} \
 -DPYTHON_VERSION:STRING=%{python3_version} \
%if 0%{?fedora}
 -DUSE_BOOST_PYTHON:BOOL=ON \
 -DUSE_LIBARCHIVE:BOOL=ON \
%else
 -DUSE_BOOST_PYTHON:BOOL=OFF \
 -DUSE_LIBARCHIVE:BOOL=OFF \
%endif
 -DENABLE_RPATH:BOOL=OFF \
 -DENABLE_TESTING:BOOL=OFF \
 -DUSE_MMTF:BOOL=ON \
 -DUSE_QT:BOOL=ON \
 -DUSE_MOLEQUEUE:BOOL=ON \
 -DUSE_VTK:BOOL=OFF \
 -DUSE_HDF5:BOOL=ON \
 -DUSE_SPGLIB:BOOL=ON \
 -DSPGLIB_LIBRARY:FILEPATH=%{_libdir}/libsymspg.so -DSPGLIB_INCLUDE_DIR:PATH=%{_includedir}/spglib \
 -DBUILD_GPL_PLUGINS:BOOL=ON \
 -DBUILD_STATIC_PLUGINS:BOOL=ON \
 -DBUILD_DOCUMENTATION:BOOL=ON \
 -DUSE_LIBMSYM:BOOL=OFF

%make_build -C build

pushd build/docs
doxygen
popd

%install
%make_install -C build

# Move scale.py* files into %%{python3_sitearch}/avogadro2
cp -a %{buildroot}%{_libdir}/avogadro2/scripts %{buildroot}%{python3_sitearch}/avogadro2/
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{python3_sitearch}/avogadro2/scripts/*/*.py
ln -sf %{python3_sitearch}/avogadro2/scripts %{buildroot}%{_libdir}/avogadro2/scripts

chrpath -d %{buildroot}%{_libdir}/lib*.so
rm -rf %{buildroot}%{_datadir}/doc

%files
%doc README.md thirdparty/libgwavi/README-libgwavi.md avogadrogenerators/README-avogenerators.md
%license LICENSE molecules/LICENSE-molecules
%{_libdir}/libAvogadro*.so.1
%{_libdir}/libAvogadro*.so.%{version}
%dir %{_libdir}/avogadro2
%{_libdir}/avogadro2/scripts/
%{_libdir}/avogadro2/libgwavi.a
%{_libdir}/avogadro2/staticplugins/
%{python3_sitearch}/avogadro2/
%{_datadir}/avogadro2/

%files devel
%{_includedir}/avogadro2/
%{_libdir}/libAvogadro*.so
%{_libdir}/cmake/avogadrolibs/

%files doc
%doc README.md build/docs/html
%license LICENSE

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.97.0-4
- Rebuilt for Python 3.12

* Sat Jan 28 2023 Antonio Trande <sagitter@fedoraproject.org> - 1.97.0-3
- Fix upstream bug #1185

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.97.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.97.0-1
- Release 1.97.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.96.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 24 2022 Jonathan Wakely <jwakely@redhat.com> - 1.96.0-3
- Remove obsolete boost-python3-devel build dependency (#2100748)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.96.0-2
- Rebuilt for Python 3.11

* Sun Jun 05 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.96.0-1
- Release 1.96.0

* Tue Mar 01 2022 Antonio Trande <sagitter@fedoraproject.org> - 1.95.1-8
- Fix rhbz#2003342

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 1.95.1-7
- Rebuild for glew 2.2

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.95.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 12 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.95.1-5
- Disable libarchive on EPEL

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 1.95.1-4
- Rebuild for hdf5 1.12.1

* Sun Nov 21 2021 Orion Poplawski <orion@nwra.com> - 1.95.1-3
- Skipped build release

* Sat Nov 06 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.95.1-2
- Prepare Qt6 builds for testing
- Rebuilt against openbabel3

* Tue Aug 31 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.95.1-1
- Release 1.95.1
- Upgrade avogenerators

* Tue Aug 10 2021 Orion Poplawski <orion@nwra.com> - 1.94.0-4
- Rebuild for hdf5 1.10.7

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.94.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 08 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.94.0-2
- Release 1.94.0

* Fri Jun 04 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.94.0-1
- Release 1.94.0
- Update avogenerators code

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.93.1-2
- Rebuilt for Python 3.10

* Mon May 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.93.1-1
- Release 1.93.1
- Remove obsolete patches

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.93.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.93.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.93.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Orion Poplawski <orion@nwra.com> - 1.93.0-5
- Rebuild for hdf5 1.10.6

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.93.0-4
- Rebuilt for Python 3.9

* Sat Feb 29 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-3
- Reorganize scripts directory

* Fri Feb 28 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-2
- Set USE_SYSTEM_LIBARCHIVE CMake option
- Set libarchive's minimal version for building
- Explicit Obsoletes tag

* Thu Feb 06 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.93.0-1
- Release 1.93.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.92.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Antonio Trande <sagitter@fedoraproject.org> - 1.92.1-1
- Release 1.92.1
- Rebuild for spglib-1.14.1
- Use devtools-8 on EPEL7
- Use CMake3

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.91.0-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.91.0-5
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.91.0-3
- Rebuild for hdf5 1.10.5

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.91.0-1
- Release 1.91.0
- Include 'avogenerators' source code

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.91.0-0.3.20180612gitda6ebb9
- Rebuilt for glew-2.1.0

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.91.0-0.2.20180612gitda6ebb9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.91.0-0.1.20180612gitda6ebb9
- Update to commit #da6ebb9 (1.91.0 pre-release)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.90.0-16
- Rebuilt for Python 3.7

* Tue Feb 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-15
- Add explicit dependencies to -devel sub-package (bz#1544510)

* Tue Feb 13 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-14
- Fix AvogadroLibsConfig.cmake relative paths (bz#1544510)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-12
- Rebuild for moloqueue-0.9.0
- Use %%ldconfig_scriptlets

* Thu Dec 14 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-11
- Rebuild for spglib-1.10.2

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 1.90.0-10
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 22 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-7
- Modified for epel builds

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.90.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon Mar 13 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-5
- Add ld scriptlets

* Sun Mar 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-4
- Set python3 installation directory

* Sun Mar 12 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-3
- Move jsoncpp.a into the private lib directory

* Sat Mar 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-2
- Use default paths

* Sat Mar 11 2017 Antonio Trande <sagitter@fedoraproject.org> - 1.90.0-1
- Initial package

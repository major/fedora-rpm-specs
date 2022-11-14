%global osg_ver 3.6.5

%global with_docs 1

Name:          osgearth
Version:       3.2
Release:       11%{?dist}
Summary:       Dynamic map generation toolkit for OpenSceneGraph

License:       LGPLv3 with exceptions
URL:           http://osgearth.org/
Source0:       https://github.com/gwaldron/osgearth/archive/%{name}-%{version}.tar.gz
# Fix mingw build failure due to header case mismatch
Patch0:        osgearth_mingw.patch
# Support option to disable fastdxt build
Patch1:        osgearth_fastdxt.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gdal-devel
BuildRequires: geos-devel
BuildRequires: glew-devel
BuildRequires: libcurl-devel
BuildRequires: libzip-devel
BuildRequires: libzip-tools
BuildRequires: make
BuildRequires: OpenSceneGraph = %{osg_ver}
BuildRequires: OpenSceneGraph-devel
BuildRequires: protobuf-devel
BuildRequires: sqlite-devel
%if 0%{?with_docs}
BuildRequires: python3-recommonmark
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-markdown-tables
%endif

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-OpenSceneGraph = %{osg_ver}
BuildRequires: mingw32-curl
BuildRequires: mingw32-gdal
BuildRequires: mingw32-protobuf

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-OpenSceneGraph = %{osg_ver}
BuildRequires: mingw64-curl
BuildRequires: mingw64-gdal
BuildRequires: mingw64-protobuf

Provides:      bundled(tinyxml)

Requires:      OpenSceneGraph = %{osg_ver}

%description
osgEarth is a C++ terrain rendering SDK. Just create a simple XML file, point
it at your imagery, elevation, and vector data, load it into your favorite
OpenSceneGraph application, and go! osgEarth supports all kinds of data and
comes with lots of examples to help you get up and running quickly and easily.


%package       devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      OpenSceneGraph-devel

%description   devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package       tools
Summary:       %{name} viewers and tools
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description   tools
The %{name}-tools contains viewers and data manipulation tools for %{name}.


%package       examples
Summary:       %{name} example applications
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-examples-data = %{version}-%{release}

%description   examples
The %{name}-examples contains %{name} example applications.


%package       examples-data
Summary:       Data for %{name} example applications
BuildArch:     noarch
Requires:      %{name}-examples = %{version}-%{release}

%description   examples-data
The %{name}-examples-data contains data for the %{name} example
applications.


%if 0%{?with_docs}
%package doc
Summary:       Documentation files for %{name}
Provides:      bundled(jquery)
BuildArch:     noarch

%description doc
The %{name}-doc package contains documentation files for developing
applications that use %{name}.
%endif


%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw32-%{name}
MinGW Windows %{name} library.


%package -n mingw32-%{name}-tools
Summary:       MinGW Windows %{name} tools
BuildArch:     noarch

%description -n mingw32-%{name}-tools
MinGW Windows %{name} tools.


%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch

%description -n mingw64-%{name}
MinGW Windows %{name} library.


%package -n mingw64-%{name}-tools
Summary:       MinGW Windows %{name} tools
BuildArch:     noarch

%description -n mingw64-%{name}-tools
MinGW Windows %{name} tools.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{name}-%{name}-%{version}

# Remove non-free content
rm -rf data/loopix


%build
# Native build
# Disable fastdxt driver on non x86 arches, requires x86 intrinsics
%ifnarch i686 x86_64
%cmake -DDISABLE_FASTDXT=ON
%else
%cmake
%endif
%cmake_build
%if 0%{?with_docs}
make -C docs html
rm -f docs/build/html/.buildinfo
%endif

# MinGW build
%mingw_cmake
%mingw_make_build


%install
%cmake_install
%mingw_make_install

install -Dd %{buildroot}%{_datadir}/%{name}
cp -a data %{buildroot}%{_datadir}/%{name}/data
cp -a tests %{buildroot}%{_datadir}/%{name}/tests


%mingw_debug_install_post


%files
%license LICENSE.txt
%{_libdir}/libosgEarth*.so.3.2.0
%{_libdir}/libosgEarth*.so.113
%{_libdir}/osgPlugins-%{osg_ver}/osgdb_*.so

%files devel
%{_includedir}/osgEarth/
%{_includedir}/osgEarthDrivers/
%{_libdir}/libosgEarth.so

%files tools
%{_bindir}/osgearth_atlas
%{_bindir}/osgearth_boundarygen
%{_bindir}/osgearth_conv
%{_bindir}/osgearth_shadergen
%{_bindir}/osgearth_tfs
%{_bindir}/osgearth_version
%{_bindir}/osgearth_viewer

%files examples
%{_bindir}/osgearth_3pv
%{_bindir}/osgearth_annotation
%{_bindir}/osgearth_bindless
%{_bindir}/osgearth_city
%{_bindir}/osgearth_clamp
%{_bindir}/osgearth_cluster
%{_bindir}/osgearth_collecttriangles
%{_bindir}/osgearth_computerangecallback
%{_bindir}/osgearth_controls
%{_bindir}/osgearth_createtile
%{_bindir}/osgearth_decal
%{_bindir}/osgearth_drawables
%{_bindir}/osgearth_eci
%{_bindir}/osgearth_elevation
%{_bindir}/osgearth_ephemeris
%{_bindir}/osgearth_featurefilter
%{_bindir}/osgearth_featurequery
%{_bindir}/osgearth_features
%{_bindir}/osgearth_geodetic_graticule
%{_bindir}/osgearth_graticule
%{_bindir}/osgearth_heatmap
%{_bindir}/osgearth_horizon
%{_bindir}/osgearth_imgui
%{_bindir}/osgearth_infinitescroll
%{_bindir}/osgearth_lights
%{_bindir}/osgearth_los
%{_bindir}/osgearth_magnify
%{_bindir}/osgearth_manip
%{_bindir}/osgearth_map
%{_bindir}/osgearth_measure
%{_bindir}/osgearth_minimap
%{_bindir}/osgearth_mrt
%{_bindir}/osgearth_mvtindex
%{_bindir}/osgearth_occlusionculling
%{_bindir}/osgearth_overlayviewer
%{_bindir}/osgearth_pick
%{_bindir}/osgearth_scenegraphcallbacks
%{_bindir}/osgearth_sequencecontrol
%{_bindir}/osgearth_shadercomp
%{_bindir}/osgearth_skyview
%{_bindir}/osgearth_terrainprofile
%{_bindir}/osgEarth_tests
%{_bindir}/osgearth_toc
%{_bindir}/osgearth_tracks
%{_bindir}/osgearth_transform
%{_bindir}/osgearth_video
%{_bindir}/osgearth_wfs
%{_bindir}/osgearth_windows

%files examples-data
%{_datadir}/%{name}

%if 0%{?with_docs}
%files doc
%license LICENSE.txt
%doc docs/build/html
%endif

%files -n mingw32-%{name}
%license LICENSE.txt
%{mingw32_bindir}/libosgEarth*.dll
%{mingw32_bindir}/osgPlugins-%{osg_ver}/*.dll
%{mingw32_libdir}/libosgEarth*.dll.a
%{mingw32_includedir}/osgEarth*/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe


%files -n mingw64-%{name}
%license LICENSE.txt
%{mingw64_bindir}/libosgEarth*.dll
%{mingw64_bindir}/osgPlugins-%{osg_ver}/*.dll
%{mingw64_libdir}/libosgEarth*.dll.a
%{mingw64_includedir}/osgEarth*/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe


%changelog
* Sat Nov 12 2022 Sandro Mani <manisandro@gmail.com> - 3.2-11
- Rebuild (gdal)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 3.2-9
- Rebuild for gdal-3.5.0 and/or openjpeg-2.5.0

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.2-8
- Rebuild with mingw-gcc-12

* Thu Feb 24 2022 Sandro Mani <manisandro@gmail.com> - 3.2-7
- Make mingw subpackages noarch

* Tue Feb 22 2022 Sandro Mani <manisandro@gmail.com> - 3.2-6
- Add mingw subpackage

* Thu Feb 10 2022 Orion Poplawski <orion@nwra.com> - 3.2-5
- Rebuild for glew 2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Sandro Mani <manisandro@gmail.com> - 3.2-3
- Revert accidental -O0 CFLAGS override

* Tue Nov 16 2021 Sandro Mani <manisandro@gmail.com> - 3.2-2
- Enable docs

* Sun Nov 14 2021 Sandro Mani <manisandro@gmail.com> - 3.2-1
- Update to 3.2

* Thu Nov 11 2021 Sandro Mani <manisandro@gmail.com> - 2.7-37
- Rebuild (gdal)

* Mon Nov 08 2021 Sandro Mani <manisandro@gmail.com> - 2.7-36
- Rebuild (geos)

* Thu Oct 21 2021 Sandro Mani <manisandro@gmail.com> - 2.7-35
- Rebuild (geos)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 2.7-33
- Rebuild (gdal)

* Fri May 07 2021 Sandro Mani <manisandro@gmail.com> - 2.7-32
- Rebuild (gdal)

* Sat Feb 13 2021 Sandro Mani <manisandro@gmail.com> - 2.7-31
- Rebuild (geos)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 12:39:13 CET 2020 Sandro Mani <manisandro@gmail.com> - 2.7-29
- Rebuild (geos)

* Wed Nov 11 12:50:28 CET 2020 Sandro Mani <manisandro@gmail.com> - 2.7-28
- Rebuild (proj, gdal)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 21 2020 Sandro Mani <manisandro@gmail.com> - 2.7-26
- Rebuild (gdal)

* Wed May 06 2020 Sandro Mani <manisandro@gmail.com> - 2.7-25
- Rebuild (geos)

* Mon Mar 09 2020 Sandro Mani <manisandro@gmail.com> - 2.7-24
- Update geos patch

* Tue Mar 03 2020 Sandro Mani <manisandro@gmail.com> - 2.7-23
- Rebuild (gdal)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 20 2019 Sandro Mani <manisandro@gmail.com> - 2.7-20
- Fix build against GEOS-3.7

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.coM> - 2.7-17
- Add missing BR: gcc-c++, make

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Ralf Corsepius <corsepiu@fedoraproject.org> - 2.7-15
- Rebuild for OSG-3.4.1.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 02 2017 Sandro Mani <manisandro@gmail.com> - 2.7-11
- Rebuild (geos)

* Thu Jun 23 2016 Sandro Mani <manisandro@gmail.com> - 2.7-10
- Add osgearth_gdalperformance.patch

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 14 2015 Sandro Mani <manisandro@gmail.com> - 2.7-8
- Rebuild (GEOS)

* Tue Oct 13 2015 Sandro Mani <manisandro@gmail.com> - 2.7-7
- osgearth-devel: Requires: OpenSceneGraph-devel, OpenSceneGraph-qt-devel

* Fri Sep 11 2015 Ralf Corsepius <corsepiu@fedoraproject.org> - 2.7-6
- Rebuild for OSG-3.4.0.

* Fri Aug 28 2015 Sandro Mani <manisandro@gmail.com> - 2.7-5
- Rebuild (gdal)

* Mon Aug 17 2015 Sandro Mani <manisandro@gmail.com> - 2.7-4
- Rebuild (OpenSceneGraph)

* Sun Aug 09 2015 Ralf Corsepius <corsepiu@fedoraproject.org> - 2.7-3
- Rebuild for OSG-3.2.2.

* Mon Jul 27 2015 Sandro Mani <manisandro@gmail.com> - 2.7-2
- Rebuild (gdal)

* Fri Jul 24 2015 Sandro Mani <manisandro@gmail.com> - 2.7-1
- Update to 2.7

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 18 2015 Sandro Mani <manisandro@gmail.com> - 2.6-4
- Add patch to fix FTBFS (#1213049)

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 2.6-3
- Parallel build for docs
- Noarch data subpackage

* Fri Dec 12 2014 Sandro Mani <manisandro@gmail.com> - 2.6-2
- Add explicit Requires: OpenSceneGraph = %%{osg_ver}
- Add Provides: bundled(jquery) to -doc
- Use %%license for license
- Use system tinyxml, remove bundled sources
- Remove non-free loopix data
- Remove html/.buildinfo
- Add -Wl,--as-needed
- Improve descriptions
- Rename package data -> examples, put example binaries in that package

* Thu Nov 20 2014 Sandro Mani <manisandro@gmail.com> - 2.6-1
- Initial package

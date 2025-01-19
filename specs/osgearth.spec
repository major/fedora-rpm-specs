%global osg_ver 3.6.5

%global with_docs 1

Name:          osgearth
Version:       3.7
Release:       3%{?dist}
Summary:       Dynamic map generation toolkit for OpenSceneGraph

License:       LGPL-3.0-only
URL:           http://osgearth.org/
Source0:       https://github.com/gwaldron/osgearth/archive/%{name}-%{version}.tar.gz
# Fix mingw build failure due to header case mismatch
# Don't use _dupenv_s
Patch0:        osgearth_mingw.patch
# Support option to disable fastdxt build
Patch1:        osgearth_fastdxt.patch
# Unbundle liblerc, rapidjson
Patch2:        osgearth_unbundle.patch
# Link against liblerct
Patch3:        osgearth_link-lerc.patch
# Fix installation paths of plugins and cmake modules
Patch4:        osgearth_cmake-install-paths.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: gdal-devel
BuildRequires: geos-devel
BuildRequires: glew-devel
BuildRequires: libcurl-devel
BuildRequires: liblerc-devel
BuildRequires: libzip-devel
BuildRequires: libzip-tools
BuildRequires: make
BuildRequires: OpenSceneGraph = %{osg_ver}
BuildRequires: OpenSceneGraph-devel
BuildRequires: protobuf-devel
BuildRequires: rapidjson-devel
BuildRequires: sqlite-devel
%if 0%{?with_docs}
BuildRequires: python3-recommonmark
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx-markdown-tables
BuildRequires: python3-myst-parser
%endif

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-curl
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-gdal
BuildRequires: mingw32-glew
BuildRequires: mingw32-glew-static
BuildRequires: mingw32-liblerc
BuildRequires: mingw32-OpenSceneGraph
BuildRequires: mingw32-protobuf

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-curl
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-gdal
BuildRequires: mingw64-glew
BuildRequires: mingw64-glew-static
BuildRequires: mingw64-liblerc
BuildRequires: mingw64-OpenSceneGraph
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
export CXXFLAGS="%{optflags} -Wno-error=format-security"
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
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2 -Wno-error=format-security -fpermissive"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2 -Wno-error=format-security -fpermissive"
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
%{_libdir}/libosgEarth*.so.3.7.0
%{_libdir}/libosgEarth*.so.163
%{_libdir}/osgPlugins-%{osg_ver}/osgdb_*.so

%files devel
%{_includedir}/osgEarth/
%{_includedir}/osgEarthDrivers/
%{_includedir}/osgEarthImGui/
%{_libdir}/libosgEarth.so
%{_libdir}/libosgEarthImGui.so
%{_libdir}/cmake/osgearth/

%files tools
%{_bindir}/osgearth_atlas
%{_bindir}/osgearth_bakefeaturetiles
%{_bindir}/osgearth_boundarygen
%{_bindir}/osgearth_conv
%{_bindir}/osgearth_imgui
%{_bindir}/osgearth_tfs
%{_bindir}/osgearth_version
%{_bindir}/osgearth_viewer

%files examples
%{_bindir}/osgearth_3pv
%{_bindir}/osgearth_annotation
%{_bindir}/osgearth_clamp
%{_bindir}/osgearth_featurefilter
%{_bindir}/osgearth_features
%{_bindir}/osgearth_heatmap
%{_bindir}/osgearth_infinitescroll
%{_bindir}/osgearth_los
%{_bindir}/osgearth_map
%{_bindir}/osgearth_minimap
%{_bindir}/osgearth_mrt
%{_bindir}/osgearth_occlusionculling
%{_bindir}/osgearth_simple
%{_bindir}/osgearth_skyview
%{_bindir}/osgearth_terrainprofile
%{_bindir}/osgearth_video

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
%{mingw32_libdir}/cmake/osgearth/
%{mingw32_includedir}/osgEarth*/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe


%files -n mingw64-%{name}
%license LICENSE.txt
%{mingw64_bindir}/libosgEarth*.dll
%{mingw64_bindir}/osgPlugins-%{osg_ver}/*.dll
%{mingw64_libdir}/libosgEarth*.dll.a
%{mingw64_libdir}/cmake/osgearth/
%{mingw64_includedir}/osgEarth*/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 09 2024 Sandro Mani <manisandro@gmail.com> - 3.7-2
- Rebuild (GDAL)

* Mon Oct 07 2024 Sandro Mani <manisandro@gmail.com> - 3.7-1
- Update to 3.7

* Thu Jul 25 2024 Sandro Mani <manisandro@gmail.com> - 3.6.1-1
- Update to 3.6.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 14 2024 Sandro Mani <manisandro@gmail.com> - 3.5-5
- Rebuild (gdal)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 15 2023 Sandro Mani <manisandro@gmail.com> - 3.5-2
- Rebuild (gdal)

* Tue Oct 24 2023 Sandro Mani <manisandro@gmail.com> - 3.5-1
- Update to 3.5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Sandro Mani <manisandro@gmail.com> - 3.4-2
- Rebuild (geos)

* Fri May 19 2023 Sandro Mani <manisandro@gmail.com> - 3.4-1
- Update to 3.4

* Thu May 11 2023 Sandro Mani <manisandro@gmail.com> - 3.3-4
- Rebuild (gdal)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 15 2022 Sandro Mani <manisandro@gmail.com> - 3.3-2
- Rebuild (geos)

* Mon Nov 14 2022 Sandro Mani <manisandro@gmail.com> - 3.3-1
- Update to 3.3

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

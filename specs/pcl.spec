%global apiversion 1.15
%global soversion 1.15

Name:           pcl
Version:        1.15.0
Release:        %autorelease
Summary:        Library for point cloud processing
# PCL is BSD-3-Clause
# lzf.h/cpp in io are BSD-2-Clause
# outofcore/include/pcl/outofcore/cJSON.h is MIT
# recognition/include/pcl/recognition/3rdparty/metslib is BSD-2-Clause
License:        BSD-3-Clause and BSD-2-Clause and MIT
URL:            http://pointclouds.org/

Source0:        https://github.com/PointCloudLibrary/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

# System metslib doesn't build under c++17
# Included version contains fixes.
Provides: bundled(metslib)

# Only enable sse2, and only on x86_64
Patch0:         %{name}-1.15.0-sse2.patch
# Patch for PCLConfig.cmake to find pcl
Patch2:         %{name}-1.12.0-fedora.patch
# Exclude the "build" directory from doxygen processing.
Patch3:         %{name}-1.11.0-doxyfix.patch
# Use a built-in sphinx documentation theme and disable doxylink plugin
Patch5:         %{name}-1.15.0-sphinx.patch
# For plain building
BuildRequires:  cmake, gcc-c++, boost-devel
# Documentation
BuildRequires:  doxygen, graphviz, /usr/bin/sphinx-build

# mandatory
BuildRequires:  eigen3-static, flann-devel, vtk-devel, gl2ps-devel, hdf5-devel, libxml2-devel, netcdf-cxx-devel, jsoncpp-devel, libXext-devel, libatomic
# To fix Imported target "VTK::Java" includes non-existent path "/usr/lib/jvm/java/include" in its INTERFACE_INCLUDE_DIRECTORIES
%ifarch %{java_arches}
BuildRequires:  java-devel
%endif

# optional
BuildRequires:  cjson-devel, libpcap-devel, qhull-devel, libusbx-devel, gtest-devel
%ifarch x86_64
BuildRequires:  openni-devel
%endif

# Testing
BuildRequires:  gtest-devel

%description
The Point Cloud Library (or PCL) is a large scale, open project for point
cloud processing.

The PCL framework contains numerous state-of-the art algorithms including
filtering, feature estimation, surface reconstruction, registration, model
fitting and segmentation. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       eigen3-devel, qhull-devel, flann-devel, vtk-devel
%ifarch x86_64
Requires:       openni-devel
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        tools
Summary:        Point cloud tools and viewers
Requires:       %{name} = %{version}-%{release}

%description    tools
This package contains tools for point cloud file processing and viewers
for point cloud files and live Kinect data.


%package        doc
Summary:        PCL API documentation
BuildArch:      noarch

%description    doc
The %{name}-doc package contains API documentation for the Point Cloud
Library.


%prep
%setup -qn %{name}-%{name}-%{version}
%patch -P0 -p1 -b .sse2
%patch -P2 -p0 -b .fedora
%patch -P3 -p0 -b .doxyfix
%patch -P5 -p1 -b .sphinx

# Just to make it obvious we're not using any of these
rm -fr surface/src/3rdparty/opennurbs
rm -rf surface/include/pcl/surface/3rdparty/opennurbs

# Exclude build directory from doxygen generation
sed -i 's|@PCL_SOURCE_DIR@/build|@PCL_SOURCE_DIR@/%{_vpath_builddir}|' doc/doxygen/doxyfile.in

%build
# try to reduce memory usage of compile process (can cause OOM errors
# esp. on ARM builders)
#%global optflags %(echo %{optflags} | sed -e 's/-g /-g1 /' -e 's/-pipe //' -e's/-ffat-lto-objects/-fno-fat-lto-objects/')

%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DWITH_DOCS=ON \
  -DWITH_CUDA=OFF \
  -DWITH_TUTORIALS=ON \
  -DBUILD_apps=ON \
  -DBUILD_global_tests=OFF \
  -DOPENNI_INCLUDE_DIR:PATH=/usr/include/ni \
  -DLIB_INSTALL_DIR=%{_lib} \
  -DPCL_WARNINGS_ARE_ERRORS=OFF \
%ifarch x86_64
  -DPCL_ENABLE_SSE=ON \
%else
  -DPCL_ENABLE_SSE=OFF \
%endif
  -DPCL_PKGCONFIG_SUFFIX:STRING="" \
  -DBUILD_documentation=ON \
  -DCMAKE_SKIP_RPATH=ON

%cmake_build

%install
%cmake_install

# Remove libtool archives
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# Just a dummy test
rm -f $RPM_BUILD_ROOT%{_bindir}/timed_trigger_test

# Remove installed documentation (will use %doc)
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

pushd %{_vpath_builddir}
# Rename the documentation folders from "html"
mv doc/doxygen/html doc/doxygen/api
mv doc/tutorials/html doc/tutorials/tutorials
mv doc/advanced/html doc/advanced/advanced

cp -fr ../doc/advanced/content/files/* doc/advanced/advanced
cp -fr ../doc/tutorials/content/sources doc/tutorials/tutorials

rm -f doc/doxygen/api/_form*
popd

for f in $RPM_BUILD_ROOT%{_bindir}/{openni_image,pcd_grabber_viewer,pcd_viewer,openni_viewer,oni_viewer}; do
	if [ -f $f ]; then
		mv $f $RPM_BUILD_ROOT%{_bindir}/pcl_$(basename $f)
	fi
done
rm $RPM_BUILD_ROOT%{_bindir}/{openni_fast_mesh,openni_ii_normal_estimation,openni_voxel_grid} ||:

mkdir -p $RPM_BUILD_ROOT%{_libdir}/cmake/pcl
mv $RPM_BUILD_ROOT%{_datadir}/%{name}-*/*.cmake $RPM_BUILD_ROOT%{_libdir}/cmake/pcl/
mv $RPM_BUILD_ROOT%{_datadir}/%{name}-*/Modules $RPM_BUILD_ROOT%{_libdir}/cmake/pcl/

%check
%ctest || true


%files
%license LICENSE.txt
%doc AUTHORS.txt
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}
%{_datadir}/%{name}-%{apiversion}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/pcl

%files tools
%{_bindir}/pcl_*
# There are no .desktop files because the GUI tools are rather examples
# to understand a particular feature of PCL.

%files doc
%doc %{_vpath_builddir}/doc/doxygen/api
%doc %{_vpath_builddir}/doc/tutorials/tutorials
%doc %{_vpath_builddir}/doc/advanced/advanced

%changelog
%autochangelog

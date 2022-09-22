%undefine __cmake_in_source_build

Name:      mrpt
Version:   1.4.0
Release:   33%{?dist}
License:   BSD
Summary:   Libraries and programs for mobile robot SLAM and navigation
URL:       http://www.mrpt.org

# Source downloaded and processed by create_tarball_mrpt.sh
# Usage: ./create_tarball_mrpt.sh 1.3.0
Source0: %{name}-%{version}-fedora.tar.xz
Source1: create_tarball_%{name}.sh

# Get rid of -GNUCXX_PARALLEL flag when building with openmp
Patch1: mrpt-1.3.0-openmp.patch
# Run gcc -dumpfullversion if -dumpversion doesn't return the whole version string
Patch2: mrpt-1.4.0-gcc7.patch

# Fix detection of system-wide libfreenect
Patch8: mrpt-1.3.0-freenect.patch
# Use system octomap instead of bundled version
Patch9: mrpt-1.3.0-octomap.patch
# Fix to access member variable properly
Patch10: mrpt-1.4.0-cpp11.patch
# Update deprecated function calls removed in octomap-1.8
# Not submitted upstream
Patch12: mrpt-1.3.2-octomap18.patch
# Fix inclusion of boost mutex
Patch13: mrpt-1.4.0-boost173.patch
# Fix for gcc-11
Patch14: mrpt-gcc11.patch
# Fix for deprecated pcl_isfinite function, removed for pcl-1.12
Patch15: mrpt-1.4.0-pcl1.12.patch
# Patch for eigen 3.4.0 type mismatch
Patch16: mrpt-1.4.0-eigen340-type-mismatch.patch
# Workaround for eigen 3.4.0 / X11 header conflicts
Patch17: mrpt-1.4.0-eigen340-X11-conflict.patch
Patch18: mrpt-1.4.0-glut.patch
Patch19: mrpt-1.4.0-gcc12.patch

BuildRequires: assimp-devel
BuildRequires: cmake
BuildRequires: wxGTK-devel
BuildRequires: freeglut-devel
BuildRequires: lib3ds-devel
BuildRequires: boost-devel
BuildRequires: eigen3-static
BuildRequires: doxygen, ghostscript, graphviz
BuildRequires: tex(latex), tex(dvips)
BuildRequires: octomap-devel
%ifnarch s390 s390x
BuildRequires: libdc1394-devel
%endif
BuildRequires: pcl-devel
BuildRequires: tbb-devel
BuildRequires: libfreenect-devel
BuildRequires: libftdi-devel
BuildRequires: libjpeg-turbo-devel
BuildRequires: libusbx-devel
%if !(0%{?fedora} >= 32)
# Doesn't build with OpenCV4
# See rhbz#1697254#c35
BuildRequires: opencv-devel
%endif
BuildRequires: desktop-file-utils
BuildRequires: suitesparse-devel
BuildRequires: libphidget22-devel
BuildRequires: perl-podlators
BuildRequires: libappstream-glib
Provides: bundled(freeglut) = 2.4.0
%description
The Mobile Robot Programming Toolkit (MRPT) is an extensive, cross-platform,
and open source C++ library aimed to help robotics researchers to design and
implement algorithms in the fields of Simultaneous Localization and Mapping 
(SLAM), computer vision, and motion planning (obstacle avoidance).

The libraries include classes for easily managing 3D(6D) geometry, 
probability density functions (pdfs) over many predefined variables (points 
and poses, landmarks, maps), Bayesian inference (Kalman filters, particle 
filters), image processing, path planning and obstacle avoidance, 3D 
visualization of all kind of maps (points, occupancy grids, landmarks,...), 
etc.
Gathering, manipulating and inspecting very large robotic datasets (Rawlogs)
efficiently is another goal of MRPT, supported by several classes and 
applications.

The MRPT is free software and is released under the GPL. 

%package base
Summary: Mobile Robot Programming Toolkit - mrpt-base

%description base
The Mobile Robot Programming Toolkit (MRPT) library mrpt-base

%package libs
Summary: Mobile Robot Programming Toolkit - All the libraries
Requires: %{name}-base%{?_isa} = %{version}-%{release}

# Removed library packages
Provides: %{name}-base = %{version}-%{release}
Provides: %{name}-detectors = %{version}-%{release}
Provides: %{name}-gui = %{version}-%{release}
Provides: %{name}-hmtslam = %{version}-%{release}
Provides: %{name}-hwdrivers = %{version}-%{release}
Provides: %{name}-kinematics = %{version}-%{release}
Provides: %{name}-maps = %{version}-%{release}
Provides: %{name}-obs = %{version}-%{release}
Provides: %{name}-opengl = %{version}-%{release}
Provides: %{name}-pbmap = %{version}-%{release}
Provides: %{name}-reactivenav = %{version}-%{release}
Provides: %{name}-scanmatching = %{version}-%{release}
Provides: %{name}-slam = %{version}-%{release}
Provides: %{name}-topography = %{version}-%{release}
Provides: %{name}-vision = %{version}-%{release}
# Removed app packages
Provides: %{name}-prrt-navigation = %{version}-%{release}

# Removed library packages
Obsoletes: %{name}-base < 1.3.0
Obsoletes: %{name}-detectors < 1.3.0
Obsoletes: %{name}-gui < 1.3.0
Obsoletes: %{name}-hmtslam < 1.3.0
Obsoletes: %{name}-hwdrivers < 1.3.0
Obsoletes: %{name}-kinematics < 1.3.0
Obsoletes: %{name}-maps < 1.3.0
Obsoletes: %{name}-obs < 1.3.0
Obsoletes: %{name}-opengl < 1.3.0
Obsoletes: %{name}-pbmap < 1.3.0
Obsoletes: %{name}-reactivenav < 1.3.0
Obsoletes: %{name}-scanmatching < 1.3.0
Obsoletes: %{name}-slam < 1.3.0
Obsoletes: %{name}-topography < 1.3.0
Obsoletes: %{name}-vision < 1.3.0
# Removed app packages
Obsoletes: %{name}-prrt-navigation < 1.3.0

%description libs
The Mobile Robot Programming Toolkit (MRPT) is an extensive, cross-platform,
and open source C++ library aimed to help robotics researchers to design and
implement algorithms in the fields of Simultaneous Localization and Mapping 
(SLAM), computer vision, and motion planning (obstacle avoidance).

This virtual package depends on all MRPT libraries.

%package apps
Summary: Mobile Robot Programming Toolkit - Console and GUI applications
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-2d-slam%{?_isa} = %{version}-%{release}
Requires: %{name}-camera-calibration%{?_isa} = %{version}-%{release}
Requires: %{name}-gridmap-navigation%{?_isa} = %{version}-%{release}
Requires: %{name}-navlog-viewer%{?_isa} = %{version}-%{release}
Requires: %{name}-rawlog-viewer%{?_isa} = %{version}-%{release}
Requires: %{name}-reactive-navigation%{?_isa} = %{version}-%{release}
Requires: %{name}-robotic-arm-kinematics%{?_isa} = %{version}-%{release}
Requires: %{name}-scene-viewer%{?_isa} = %{version}-%{release}
Requires: %{name}-stereo-camera-calibration%{?_isa} = %{version}-%{release}

%description apps
The Mobile Robot Programming Toolkit (MRPT) is an extensive, cross-platform,
and open source C++ library aimed to help robotics researchers to design and
implement algorithms in the fields of Simultaneous Localization and Mapping 
(SLAM), computer vision, and motion planning (obstacle avoidance).

This package provides a set of console and GUI applications for manipulating 
datasets, particle filtering localization and SLAM, grabbing data from 
robotic sensors, etc.

# MRPT Apps
%package 2d-slam
Summary: Mobile Robot Progamming Toolkit 2D SLAM demo

%description 2d-slam
2d-slam-demo is a GUI application which allows the user to run a
Extended Kalman Filter (EKF) implementation of range-bearing 2D SLAM in
step-by-step or continuous mode. Graphs are shown for the observations,
data association, etc.

%package camera-calibration
Summary: Mobile Robot Programming Toolkit Camera Calibration

%description camera-calibration
camera-calib-gui is a graphical application which allows the user to
select a sequence of images where a checkerboad (calibration pattern)
appears, then it computes the intrinsic and distortion parameters of
the camera, using the OpenCV implementation of Zhang's algorithm.

The sequence of images can be grabbed directly from a webcam, firewire
camera or any other video source.

%package gridmap-navigation
Summary: Mobile Robot Programming Toolkit Camera Calibration

%description gridmap-navigation
A GUI application for simulation of robot motion within a simulated
environment defined by an occupancy grid map. The program simulates
noisy odometry and laser measurements and generates a rawlog which can
then be used as the input of SLAM algorithms. A ground truth file is
also generated.

The robot is controlled with a joystick or the cursor arrow keys.

%package navlog-viewer
Summary: Mobile Robot Programming Toolkit Navigation Log Viewer

%description navlog-viewer
A GUI application for playing back the logs generated by MRPT programs such
as GridmapNavSimul. Navigaton logs are useful to debug the internal workings of
robot navigation algorithms, their internal decisions, etc.

%package rawlog-viewer
Summary: Mobile Robot Programming Toolkit Raw Log Viewer

%description rawlog-viewer
A GUI viewer and editor of robotic datasets stored in the MRPT
rawlog format.

%package reactive-navigation
Summary: Mobile Robot Programming Toolkit Reactive Navigation

%description reactive-navigation
A program to demonstrate the usage of the mrpt reactivenav library. It
allow the user to set an arbitrary target and then simulate the robot
actions to try to reach the target.

The movements take into account the arbitrary shape of the robot, and a
set of kinematically-constrained trajectories.  

%package robotic-arm-kinematics
Summary: Mobile Robot Programming Toolkit Robotic Arm Kinematics

%description robotic-arm-kinematics
A GUI to practice and learn the Denavit-Hartenberg (DH) parameters
of robotic arm manipulators

%package scene-viewer
Summary: Mobile Robot Programming Toolkit Scene Viewer

%description scene-viewer
A viewer for 3D scenes generated by MRPT applications in the
MRPT 3Dscene format: a (possibly gz-compressed) file where a
mrpt::opengl::COpenGLScene has been serialized.

%package stereo-camera-calibration
Summary: Mobile Robot Programming Toolkit Stereo Camera Calibration

%description stereo-camera-calibration
A GUI application for calibration of stereo and RGBD cameras.

%package devel
Summary: Mobile Robot Programming Toolkit - Development package

Requires: pkgconfig
Requires: suitesparse-devel

%description devel
The Mobile Robot Programming Toolkit (MRPT) is an extensive, cross-platform,
and open source C++ library aimed to help robotics researchers to design and
implement algorithms in the fields of Simultaneous Localization and Mapping 
(SLAM), computer vision, and motion planning (obstacle avoidance).

This package provides the headers and required files to build third-party 
applications that use MRPT libraries.


%package doc
Summary: Mobile Robot Programming Toolkit - Documentation
%description doc
The Mobile Robot Programming Toolkit (MRPT) is an extensive, cross-platform,
and open source C++ library aimed to help robotics researchers to design and
implement algorithms in the fields of Simultaneous Localization and Mapping 
(SLAM), computer vision, and motion planning (obstacle avoidance).

This package contains documentation, examples and the reference generated
with Doxygen.


%prep
%setup -q
%patch1 -p0 -b .openmp
%patch2 -p0 -b .gcc7
%patch8 -p0 -b .freenect
%patch9 -p0 -b .octomap
%patch10 -p0 -b .cpp11
%patch12 -p0 -b .octomap18
%patch13 -p0 -b .boost173
%patch14 -p1 -b .gcc11
%patch15 -p1 -b .pcl1.12
%patch16 -p1 -b .eigen_type
%patch17 -p1 -b .eigen_X11
%patch18 -p1 -b .glut
%patch19 -p1 -b .gcc12
rm -rf libs/opengl/src/{glew,glext,lib3ds}
rm -rf libs/base/src/math/CSparse
rm -rf libs/base/include/mrpt/otherlibs/CSparse
rm -rf libs/base/src/utils/jpeglib
rm -rf libs/base/src/compress/zlib/
rm -rf otherlibs/assimp
rm -rf otherlibs/octomap
rm -rf libs/hwdrivers/src/rplidar
rm -rf libs/maps/include/mrpt/otherlibs/octomap

%build
# The flag CMAKE_MRPT_IS_RPM_PACKAGE disables global "-mtune=native"
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DCMAKE_INSTALL_LIBDIR=%{_lib} \
  -DCSPARSE_LIBRARY=%{_libdir}/libcxsparse.so \
  -DCMAKE_MRPT_IS_RPM_PACKAGE=1 \
  -DMRPT_ENABLE_LIBSTD_PARALLEL_MODE=ON \
  -DMRPT_ENABLE_PRECOMPILED_HDRS=OFF \
  -DMRPT_HAS_PHIDGET=ON \
  -DPHIDGET_ROOT_DIR=/usr \
  -DPHIDGET_LIB_DIR=%{_libdir} \
  -DMRPT_HAS_TBB=ON \
  -DTBB_LIB_DIR=%{_libdir} \
  -DMRPT_AUTODETECT_SSE=OFF \
  -DDISABLE_SSE4=ON \
  -DDISABLE_SSE4_1=ON \
  -DDISABLE_SSE4_2=ON \
  -DDISABLE_SSE4_A=ON \
  -DDISABLE_SSE3=ON \
%ifnarch x86_64
  -DDISABLE_SSE2=ON \
%endif
  -DBOOST_ROOT=/usr \
  -DBOOST_LIBRARYDIR=%{_libdir} \
  -DMRPT_OPTIMIZE_NATIVE=OFF \
  -DCMAKE_BUILD_TYPE=None \
  -DEIGEN_USE_EMBEDDED_VERSION=OFF \
  -DBUILD_KINECT_USE_FREENECT=ON \
  -DBUILD_ARIA=OFF \
  -DBUILD_XSENS_MT3=OFF \
  -DBUILD_XSENS_MT4=OFF \
  -DDISABLE_SIFT_HESS=ON \
  -DPCL_FIND_QUIETLY=OFF \
  -DBUILD_TESTING=OFF \
  -DBUILD_ROBOPEAK_LIDAR=OFF \
%if 0%{?fedora} >= 32
  -DDISABLE_OPENCV=ON \
%endif
  -DDISABLE_FFMPEG=ON \

%cmake_build
%cmake_build --target documentation_html
%cmake_build --target  man_pages_all

%check
export LD_LIBRARY_PATH=$(pwd)/lib
%ctest --verbose || echo "**Warning**: unit tests failed, check whether it was only due to SSE* stuff" 

%install
%cmake_install
# Validate .g files:
find ${RPM_BUILD_ROOT}%{_datadir}/applications/ -name "*.desktop" | xargs -I FIL desktop-file-validate FIL
# Validate appdata files
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

rm -fr $RPM_BUILD_ROOT/%{_datadir}/mrpt-doc
rm -fr $RPM_BUILD_ROOT/%{_datadir}/doc/mrpt-doc
rm -fr $RPM_BUILD_ROOT/%{_usr}/lib/python*

%files base
%doc README.md doc/COPYING
%{_libdir}/libmrpt-base.so.*
# This directory is empty here but contains files in other sub-packages 
#  depending on mrpt-base:
%dir %{_datadir}/mrpt
%{_datadir}/mime/packages/*.xml

%files apps
%doc README.md doc/COPYING
%exclude %{_bindir}/2d-slam-demo
%exclude %{_bindir}/camera-calib
%exclude %{_bindir}/GridmapNavSimul
%exclude %{_bindir}/kinect-stereo-calib
%exclude %{_bindir}/navlog-viewer
%exclude %{_bindir}/RawLogViewer
%exclude %{_bindir}/ReactiveNavigationDemo
%exclude %{_bindir}/robotic-arm-kinematics
%exclude %{_bindir}/SceneViewer3D
%{_bindir}/*
%{_datadir}/pixmaps/*.ico
%{_datadir}/mrpt/config_files/
%{_datadir}/mrpt/datasets/
%exclude %{_mandir}/man1/2d-slam-demo.1.*
%exclude %{_mandir}/man1/camera-calib.1.*
%exclude %{_mandir}/man1/GridmapNavSimul.1.*
%exclude %{_mandir}/man1/kinect-stereo-calib.1.*
%exclude %{_mandir}/man1/navlog-viewer.1.*
%exclude %{_mandir}/man1/RawLogViewer.1.*
%exclude %{_mandir}/man1/ReactiveNavigationDemo.1.*
%exclude %{_mandir}/man1/SceneViewer3D.1.*
%exclude %{_mandir}/man1/robotic-arm-kinematics.1.*
%{_mandir}/man1/*

%files 2d-slam
%{_datadir}/applications/2dslamdemo.desktop
%{_datadir}/appdata/2dslamdemo.appdata.xml
%{_datadir}/pixmaps/2d-slam-demo.png
%{_bindir}/2d-slam-demo
%{_mandir}/man1/2d-slam-demo.1.*

%files camera-calibration
%{_datadir}/applications/cameracalib.desktop
%{_datadir}/appdata/cameracalib.appdata.xml
%{_datadir}/pixmaps/cameracalibgui.png
%{_bindir}/camera-calib
%{_mandir}/man1/camera-calib.1.*

%files gridmap-navigation
%{_datadir}/applications/gridmapnavsimul.desktop
%{_datadir}/appdata/gridmapnavsimul.appdata.xml
%{_datadir}/pixmaps/gridmapsimul.png
%{_bindir}/GridmapNavSimul
%{_mandir}/man1/GridmapNavSimul.1.*

%files navlog-viewer
%{_datadir}/applications/navlog-viewer.desktop
%{_datadir}/appdata/navlog-viewer.appdata.xml
%{_datadir}/pixmaps/navlog-viewer.png
%{_bindir}/navlog-viewer
%{_mandir}/man1/navlog-viewer.1.*

%files rawlog-viewer
%{_datadir}/applications/rawlogviewer.desktop
%{_datadir}/appdata/rawlogviewer.appdata.xml
%{_datadir}/pixmaps/rawlogviewer.png
%{_bindir}/RawLogViewer
%{_mandir}/man1/RawLogViewer.1.*

%files reactive-navigation
%{_datadir}/applications/reactivenavdemo.desktop
%{_datadir}/appdata/reactivenavdemo.appdata.xml
%{_datadir}/pixmaps/reactivenav.png
%{_bindir}/ReactiveNavigationDemo
%{_mandir}/man1/ReactiveNavigationDemo.1.*

%files robotic-arm-kinematics
%{_datadir}/applications/robotic-arm-kinematics.desktop
%{_datadir}/appdata/robotic-arm-kinematics.appdata.xml
%{_datadir}/pixmaps/robotic-arm-kinematics.png
%{_bindir}/robotic-arm-kinematics
%{_mandir}/man1/robotic-arm-kinematics.1.*

%files scene-viewer
%{_datadir}/applications/sceneviewer.desktop
%{_datadir}/appdata/sceneviewer.appdata.xml
%{_datadir}/pixmaps/sceneviewer.png
%{_bindir}/SceneViewer3D
%{_mandir}/man1/SceneViewer3D.1.*

%files stereo-camera-calibration
%{_datadir}/applications/kinect-stereo-camera-calib-gui.desktop
%{_datadir}/appdata/kinect-stereo-camera-calib-gui.appdata.xml
%{_datadir}/pixmaps/cameracalibgui.png
%{_bindir}/kinect-stereo-calib
%{_mandir}/man1/kinect-stereo-calib.1.*

%files devel
%doc README.md doc/COPYING
%{_libdir}/*.so
%{_includedir}/mrpt
%{_libdir}/pkgconfig/*.pc
# _datadir/mrpt is owned by mrpt-core:
%{_datadir}/mrpt/MRPTConfig.cmake
%{_datadir}/mrpt/MRPTConfig-version.cmake

%files doc
%doc README.md doc/COPYING
%doc doc/html
#%doc doc/mrpt-book.ps.gz
%doc samples

%files libs
%doc README.md doc/COPYING
%{_libdir}/*.so.*

%changelog
* Mon Sep 12 2022 Scott Talbert <swt@techie.net> - 1.4.0-33
- Rebuild with wxWidgets 3.2

* Mon Aug 29 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.0-32
- Rebuild for new libphidget and change BR to libphidget renaming

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.0-29
- Patch to build for eigen 3.4.0

* Fri Aug 20 2021 Björn Esser <besser82@fedoraproject.org> - 1.4.0-28
- Rebuild (pcl)

* Sun Aug 01 2021 Rich Mattes <richmattes@gmail.com> - 1.4.0-27
- Rebuild for assimp-5.0.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jan 31 2021 Orion Poplawski <orion@nwra.com> - 1.4.0-25
- Rebuild for VTK 9

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 15 2020 Jeff Law <law@redhat.com> - 1.4.0-23
- Fix missing #includes for gcc-11

* Mon Aug 31 2020 Jeff Law <law@redhat.com> - 1.4.0-22
- Re-enable LTO

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-21
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4.0-19
- Rebuilt for OpenCV 4.3

* Sun Apr 19 2020 Rich Mattes <richmattes@gmail.com> - 1.4.0-18
- Rebuild for octomap-1.9.5

* Tue Mar 03 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.4.0-17
- Rebuilt for libfreenect

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rich Mattes <richmattes@gmail.com> - 1.4.0-15
- Rebuild with wxWidgets GTK3 build (PR#2)

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.4.0-14
- Disable opencv4

* Tue Sep 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.4.0-1
- Revert to bundled freeglut.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 27 2018 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-11
- Rebuild for VTK 8.1

* Sat Sep 08 2018 Scott Talbert <swt@techie.net> - 1.4.0-10
- Rebuild with wxWidgets 3.0 (GTK+ 2 build)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 1.4.0-8
- Rebuild for opencv soname bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 26 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.0-6
- Rebuilt for jsoncpp.so.20

* Fri Sep 01 2017 Björn Esser <besser82@fedoraproject.org> - 1.4.0-5
- Rebuilt for jsoncpp-1.8.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 21 2017 Kalev Lember <klember@redhat.com> - 1.4.0-2
- Rebuilt for Boost 1.64

* Sun Mar 12 2017 Rich Mattes <richmattes@gmail.com> - 1.4.0-1
- Update to release 1.4.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Rich Mattes <richmattes@gmail.com> - 1.3.2-11
- Rebuild for eigen3-3.3.1

* Wed Dec 7 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-10
- Rebuild for vtk 7.1

* Mon Oct 03 2016 Björn Esser <fedora@besser82.io> - 1.3.2-9
- Rebuilt for libjsoncpp.so.11

* Sun Aug 14 2016 Rich Mattes <richmattes@gmail.com> - 1.3.2-8
- Rebuild for octomap-1.8.0

* Wed May 25 2016 Rich Mattes <richmattes@gmail.com> - 1.3.2-7
- Rebuild for assimp-3.2.0

* Sun May 22 2016 Rich Mattes <richmattes@gmail.com> - 1.3.2-6
- Add work-around for OpenCV API change

* Thu May 19 2016 Till Maas <opensource@till.name> - 1.3.2-6
- Fix typo in provides

* Tue May 03 2016 Rich Mattes <richmattes@gmail.com> - 1.3.2-5
- Rebuild for opencv-3.1.0

* Fri Mar 25 2016 Björn Esser <fedora@besser82.io> - 1.3.2-4
- Rebuilt for libjsoncpp.so.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.2-2
- Rebuild for hdf5 1.8.16

* Fri Jan 01 2016 Rich Mattes <richmattes@gmail.com> - 1.3.2-1
- Update to release 1.3.2

* Thu Oct 29 2015 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-2
- Rebuild for vtk 6.3.0

* Sat Sep 12 2015 Rich Mattes <richmattes@gmail.com> - 1.3.0-1
- Update to release 1.3.0 (rhbz#1196299)
- Removed individual library sub-packages in favor of libs subpackage

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.0.2-19
- Rebuilt for Boost 1.59

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-18
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.0.2-17
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Nils Philippsen <nils@redhat.com> - 1.0.2-15
- rebuild for suitesparse-4.4.4

* Mon May 18 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.2-14
- Rebuild for hdf5 1.8.15

* Thu Mar 19 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.2-13
- Rebuild for vtk 6.2.0

* Wed Jan 28 2015 Petr Machata <pmachata@redhat.com> - 1.0.2-12
- Rebuild for boost 1.57.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.0.2-11
- update mime scriptlet

* Wed Sep 10 2014 Jiri Kastner <jkastner /at/ redhat /dot/ com> - 1.0.2-10
- rebuild for suitesparse 4.3.1

* Mon Sep 01 2014 Rich Mattes <richmattes@gmail.com> - 1.0.2-9
- Split apps into separate packages for appstream

* Fri Aug 22 2014 Jiri Kastner <jkastner /at/ redhat /dot/ com> - 1.0.2-8
- Rebuild for libreenect 0.5.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Petr Machata <pmachata@redhat.com> - 1.0.2-5
- Rebuild for boost 1.55.0

* Fri May 23 2014 David Tardon <dtardon@redhat.com> - 1.0.2-4
- rebuild for boost 1.55.0

* Sat May 03 2014 Rich Mattes <richmattes@gmail.com> - 1.0.2-3
- Rebuild for libfreenect

* Fri Dec 06 2013 Nils Philippsen <nils@redhat.com> - 1.0.2-2
- rebuild (suitesparse)

* Sun Sep 08 2013 Rich Mattes <richmattes@gmail.com> - 1.0.2-1
- Update to release 1.0.2
- Re-enable tbb on ARM

* Sun Aug  4 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.1-5
- Modernise SPEC
- exclude tbb build dep on ARM (not currently available)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 28 2013 Petr Machata <pmachata@redhat.com> - 1.0.1-3
- Rebuild for boost 1.54.0

* Sat Jun 29 2013 Rich Mattes <richmattes@gmail.com> - 1.0.1-2
- Compress tarball using xz (rhbz#979191)
- Change to require eigen3-static instead of -devel
- Rebuild for new eigen3 (rhbz#978971)

* Sun Jun 02 2013 Rich Mattes <richmattes@gmail.com> - 1.0.1-1
- Update to release 1.0.1

* Fri May 24 2013 Petr Machata <pmachata@redhat.com> - 1.0.0-3
- Rebuild for TBB memory barrier bug

* Tue Apr 16 2013 Rich Mattes <richmattes@gmail.com> - 1.0.0-2
- License changed to BSD for 1.0.0, updated spec license field to match

* Mon Apr 15 2013 Rich Mattes <richmattes@gmail.com> - 1.0.0-1
- Update to release 1.0.0

* Sat Feb 23 2013 Rich Mattes <richmattes@gmail.com> - 0.9.6-6
- Fixed doxygen layout file to work with new doxygen version
- Fixed bogus changelog dates
- Made doc subpackage noarch

* Sat Feb 09 2013 Denis Arnaud <denis.arnaud_fedora@m4x.org> - 0.9.6-6
- Rebuild for Boost-1.53.0

* Mon Jan 21 2013 Adam Tkac <atkac redhat com> - 0.9.6-5
- rebuild due to "jpeg8-ABI" feature drop

* Thu Jan 03 2013 Dan Horák <dan[at]danny.cz> - 0.9.6-4
- update BRs for s390(x)

* Sat Dec 22 2012 Rich Mattes <richmattes@gmail.com> - 0.9.6-3
- Rebuild for new flann

* Sat Nov 10 2012 Rich Mattes <richmattes@gmail.com> - 0.9.6-2
- Rebuild for new OpenCV

* Sun Aug 26 2012 Rich Mattes <richmattes@gmail.com> - 0.9.6-1
- Added dependency on suitesparse
- Fixed resolution of libphidget and tbb

* Sat Aug 25 2012 Rich Mattes <richmattes@gmail.com> - 0.9.6-1
- Updated to 0.9.6

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-0.6.20110917svn2662
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Rich Mattes <richmattes@gmail.com> - 0.9.5-0.5.20110917svn2662
- Rebuild for new OpenCV
- Fix for zlib 1.2.7
- Fix for gcc 4.7

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-0.4.20110917svn2662
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-0.3.20110917svn2662
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 16 2011 Dan Horák <dan[at]danny.cz> - 0.9.5-0.2.20110917svn2662
- no FireWire on s390(x)

* Mon Sep 19 2011 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.5-0.1.20110917svn2662
- New 0.9.5 svn snapshot.

* Fri Sep 16 2011 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.5-0.1.20110916svn2655
- New 0.9.5 svn snapshot.

* Tue Aug 23 2011 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.5-0.1.20110823svn2634
- New 0.9.5 svn snapshot.

* Mon Jan 10 2011 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.4-0.1.20110110svn2383
- New 0.9.4 svn snapshot, with more secure unit tests for autobuilders.

* Mon Jan 10 2011 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.4-0.1.20110110svn2382
- Packaging of new upstream version 0.9.4 (svn snapshot)

* Mon Jan 10 2011 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.4-0.1.20110110svn2380
- Packaging of new upstream version 0.9.4 (svn snapshot)

* Sat Dec 25 2010 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.4-0.1.20101225svn2354
- Packaging of new upstream version 0.9.4 (svn snapshot)

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 0.9.0-0.5
- rebuilt against wxGTK-2.8.11-2

* Sun Jul 4 2010 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.0-0.4
- Rebuild needed by new opencv.

* Sun Jun 6 2010 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.0-0.3
- Changed source tarball name numbering.

* Sat Jun 5 2010 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.0-0.2
- Fixed build against OpenCV.

* Fri Jun 4 2010 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.9.0-0.1
- Packaging of new upstream version 0.9.0.

* Sat Mar  6 2010 - Thomas Spura <tomspur@fedoraproject.org> 0.8.0-0.3.20100102svn1398
- rebuild as requested in
  http://lists.fedoraproject.org/pipermail/devel/2010-March/132519.html

* Fri Jan 22 2010 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.8.0-0.2.20100102svn1398
- Fixed dependencies in spec file.

* Thu Jan 21 2010 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.8.0-0.1.20100102svn1398
- Packaging of new upstream version 0.8.0.

* Tue Aug 18 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.7.1-0.1.20090818svn1148
- Packaging of new upstream version 0.7.1, patched.

* Mon Aug 17 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.7.1-0.1.20090817svn1147
- Packaging of new upstream version 0.7.1.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-0.2.20090529svn1047
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.7.0-0.1.20090529svn1047
- Packaging of new upstream version 0.7.0.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-0.4.20090213svn807
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 19 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.6.5-0.3.20090213svn807
- Fixed ownship of datadir/mrpt/config_files/ by two sub-packages.

* Fri Feb 13 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.6.5-0.2.20090213svn807
- All applications are now in mrpt-apps.

* Fri Feb 13 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.6.5-0.1.20090213
- New upstream sources.
- Individual packages created for each MRPT application.
- Removed unneeded dependencies from -devel package.
- Fixed "doc" package should own the mrpt-doc directory.
- Mime types moved to mrpt-core package.

* Sun Jan 18 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.6.5-0.1.20090118svn746
- New upstream sources.
- Fixed license tag to "GPLv3+".
- Added "export LD_LIBRARY_PATH..." at "check" to allow the tests to work.
- Comments added explaining the split in subpackages.
- devel package depends on wxGTK-devel instead of wxGTK due to needed headers.
- datadir/mrpt is now owned by mrpt-core to avoid duplicated ownership.
- Several fixes to libmrpt.pc
- Added calls to "update-desktop-database" and "update-mime-database" in post/postun of mrpt-apps.
- Corrected texlive-latex dependency to enable compilation of doxygen formulas.

* Thu Jan 8 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.6.4-2
- More verbose output in 'make test', and possibly fixed wrong compiler flag.
- Fixed ownership of the same file MRPTConfig.cmake in two subpackages.

* Sun Jan 4 2009 - Jose Luis Blanco <joseluisblancoc@gmail.com> 0.6.4-1
- Initial packaging for Fedora.


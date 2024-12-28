%global abiver 2.56
Name:           librealsense
Version:        2.56.3
Release:        %autorelease
Summary:        Cross-platform camera capture for Intel RealSense

License:        Apache-2.0
URL:            https://github.com/IntelRealSense/librealsense
Source0:        https://github.com/IntelRealSense/librealsense/archive/v%{version}.tar.gz#/librealsense-%{version}.tar.gz
# Remove custom CFLAGS that override ours.
# This was discussed with upstream, but upstream wants to keep those flags.
# https://github.com/morxa/librealsense/tree/remove-cflags
Patch0:         librealsense.remove-cflags.patch
# https://github.com/morxa/librealsense/tree/realsense-file-shared-library
Patch1:         librealsense.realsense-file-shared-library.patch
#  https://github.com/morxa/librealsense/tree/use-system-pybind11
Patch2:         librealsense.use-system-pybind11.patch
# https://github.com/morxa/librealsense/tree/remove-invalid-unused-code
Patch3:         librealsense.remove-invalid-unused-code.patch
# https://github.com/morxa/librealsense/tree/rsutils-shared-library
Patch4:         librealsense.rsutils-shared-library.patch
# https://github.com/morxa/librealsense/tree/use-system-pybind11
Patch5:         librealsense.use-system-json.patch

BuildRequires:  cmake
BuildRequires:  cmake(glfw3)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gdb-headless
BuildRequires:  glfw-devel
BuildRequires:  libGL-devel
BuildRequires:  libcurl-devel
BuildRequires:  libusb1-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Provides:       librealsense2 = %{version}-%{release}

%description
The Intel RealSense SDK is a cross-platform library (Linux, OSX, Windows) for
capturing data from the Intel RealSense D400 and SR 300 depth cameras.

For older devices (F200, R200, LR200, ZR300), please use librealsense1.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       librealsense2-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package -n     python3-%{name}
Summary:        Python bindings for %{name}
%{?python_provide:%python_provide python3-%{name}}
Provides:       python3-librealsense2 = %{version}-%{release}

%description -n python3-%{name}
The python3-%{name} package contains python bindings for %{name}.


%package -n     python3-%{name}-devel
Summary:        Python development files for %{name}
Requires:       python3-%{name}%{?_isa} = %{version}-%{release}
Provides:       python3-librealsense2-devel = %{version}-%{release}

%description -n python3-%{name}-devel
The python3-%{name}-devel package contains libraries and header files for
developing python applications that use %{name}.


%package        doc
BuildArch:      noarch
Summary:        Documentation for %{name}
Provides:       librealsense2-doc = %{version}-%{release}

%description    doc
The %{name}-doc package contains documentation for developing applications
with %{name}.

# enable PIE, we need -fPIC anyway
%global _hardened_build 1

%prep
%autosetup -p1


%build
%cmake \
  -DBUILD_UNIT_TESTS=NO \
  -DCHECK_FOR_UPDATES=NO \
  -DCMAKE_INSTALL_BINDIR=%{_bindir} \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
  -DBUILD_PYTHON_BINDINGS:bool=true \
  -DPYTHON_EXECUTABLE=%{python3}
%cmake_build

sed -i "s:/usr/local/bin:%{_datadir}/realsense:" config/*
sed -i "s/plugdev/users/g" config/*rules

pushd doc/doxygen
# Do not generate Windows help files
sed -i \
  -e "s/GENERATE_HTMLHELP[[:space:]]*=[[:space:]]*YES/GENERATE_HTMLHELP = NO/" \
  doxyfile
doxygen
popd


%install
%cmake_install

mkdir -p %{buildroot}/%{_udevrulesdir}
install -p -m644 config/99-realsense-libusb.rules %{buildroot}/%{_udevrulesdir}
mkdir -p %{buildroot}/%{_datadir}/realsense
install -p -m755 config/usb-R200-in{,_udev} %{buildroot}/%{_datadir}/realsense
mv %{buildroot}/builddir/Documents/librealsense2/presets %{buildroot}/%{_datadir}/realsense

%files
%license LICENSE
%doc readme.md
%{_libdir}/librealsense-file.so.%{abiver}*
%{_libdir}/librealsense2-gl.so.%{abiver}*
%{_libdir}/librealsense2.so.%{abiver}*
%{_libdir}/librsutils.so.%{abiver}*
%{_datadir}/realsense
%{_bindir}/realsense-viewer
%{_bindir}/rs-align
%{_bindir}/rs-align-advanced
%{_bindir}/rs-align-gl
%{_bindir}/rs-benchmark
%{_bindir}/rs-callback
%{_bindir}/rs-capture
%{_bindir}/rs-color
%{_bindir}/rs-convert
%{_bindir}/rs-data-collect
%{_bindir}/rs-depth
%{_bindir}/rs-depth-quality
%{_bindir}/rs-distance
%{_bindir}/rs-embed
%{_bindir}/rs-enumerate-devices
%{_bindir}/rs-fw-logger
%{_bindir}/rs-fw-update
%{_bindir}/rs-gl
%{_bindir}/rs-hdr
%{_bindir}/rs-hello-realsense
%{_bindir}/rs-measure
%{_bindir}/rs-motion
%{_bindir}/rs-multicam
%{_bindir}/rs-pointcloud
%{_bindir}/rs-post-processing
%{_bindir}/rs-record
%{_bindir}/rs-record-playback
%{_bindir}/rs-rosbag-inspector
%{_bindir}/rs-save-to-disk
%{_bindir}/rs-sensor-control
%{_bindir}/rs-software-device
%{_bindir}/rs-terminal
%{_udevrulesdir}/99-realsense-libusb.rules

%files devel
%{_includedir}/librealsense2
%{_includedir}/librealsense2-gl
%{_libdir}/librsutils.so
%{_libdir}/cmake/realsense2
%{_libdir}/cmake/realsense2-gl
%{_libdir}/librealsense-file.so
%{_libdir}/librealsense2-gl.so
%{_libdir}/librealsense2.so
%{_libdir}/pkgconfig/realsense2-gl.pc
%{_libdir}/pkgconfig/realsense2.pc

%files -n python3-%{name}
%dir %{python3_sitearch}/pyrealsense2/
%{python3_sitearch}/pyrealsense2/__init__.py
%{python3_sitearch}/pyrealsense2/__pycache__/
%{python3_sitearch}/pyrealsense2/pyrealsense2*.so.%{abiver}*
%{python3_sitearch}/pyrealsense2/pyrsutils*.so.%{abiver}*

%files -n python3-%{name}-devel
%{_libdir}/cmake/pyrealsense2
%{python3_sitearch}/pyrealsense2/pyrealsense2*.so
%{python3_sitearch}/pyrealsense2/pyrsutils*.so

%files doc
%license LICENSE
%doc doc/doxygen/html/*


%changelog
%autochangelog

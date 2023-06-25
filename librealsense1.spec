%global commit 24ddaecfc6e1099f96330757181174e7054d6cd6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           librealsense1
Version:        1.12.4
Release:        %autorelease -s %{shortcommit}
Summary:        Cross-platform camera capture for Intel RealSense

License:        Apache-2.0
URL:            https://github.com/IntelRealSense/librealsense
Source0:        https://github.com/IntelRealSense/librealsense/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# Remove custom CFLAGS that override ours.
# This was discussed with upstream, but upstream wants to keep those flags.
# See https://github.com/IntelRealSense/librealsense/pull/422 for the
# discussion.
Patch0:         librealsense.remove-cflags.patch
Patch1:         librealsense.v1-paths.patch
Patch2:         librealsense.do-not-throw-on-usberror.patch
Patch3:         librealsense1-cmake-c99.patch

Obsoletes:      librealsense < 1.12.1-11

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libusb1-devel
BuildRequires:  systemd

%description
This project is a cross-platform library (Linux, OSX, Windows) for capturing
data from the Intel RealSense F200, SR300 and R200 cameras. This is a legacy
package to provide support for older camera hardware. For newer hardware, use
librealsense.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

Obsoletes:      librealsense-devel < 1.12.1-11

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
BuildArch:      noarch
Summary:        Documentation for %{name}

Obsoletes:      librealsense-doc < 1.12.1-11

%description    doc
The %{name}-doc package contains documentation for developing applications
with %{name}.


%prep
%autosetup -p1 -n librealsense-%{commit}


%build
%cmake \
  -DBUILD_UNIT_TESTS=NO \
  -DCMAKE_INSTALL_BINDIR=%{_bindir} \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}
%cmake_build

sed -i "s:/usr/local/bin:%{_datadir}/realsense1:" config/*
sed -i "s/plugdev/users/g" config/*rules

pushd doc/Doxygen_API
# Do not generate Windows help files
sed -i \
  -e "s/GENERATE_HTMLHELP[[:space:]]*=[[:space:]]*YES/GENERATE_HTMLHELP = NO/" \
  Doxyfile
doxygen
popd


%install
%cmake_install

mkdir -p %{buildroot}/%{_udevrulesdir}
install -p -m644 config/99-realsense-libusb.rules \
  %{buildroot}/%{_udevrulesdir}/99-realsense1-libusb.rules
mkdir -p %{buildroot}/%{_datadir}/realsense1
install -p -m755 config/usb-R200-in{,_udev} %{buildroot}/%{_datadir}/realsense1


%files
%license LICENSE
%doc readme.md
%{_libdir}/librealsense1.so.*
%{_datadir}/realsense1
%{_udevrulesdir}/*

%files devel
%{_includedir}/librealsense1
%{_libdir}/librealsense1.so
%{_libdir}/cmake/realsense1

%files doc
%license LICENSE
%doc doc/Doxygen_API/html/*


%changelog
%autochangelog

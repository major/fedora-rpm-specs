# The examples fail to build with OpenCV 4.x and aren't terribly useful, so
# disable them by default (https://github.com/libuvc/libuvc/issues/233)
%bcond_with examples

%global forgeurl https://github.com/libuvc/libuvc

Name:           libuvc
Version:        0.0.7
Release:        %autorelease
Summary:        Cross-platform library for USB video devices

# include/utlist.h is BSD-1-Clause, the rest is BSD-3-Clause
License:        BSD-3-Clause AND BSD-1-Clause
URL:            https://libuvc.github.io
Source:         %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc

BuildRequires:  libjpeg-devel
BuildRequires:  libusb1-devel
%if %{with examples}
BuildRequires:  opencv-devel
%endif

%description
libuvc is a cross-platform library for USB video devices, built atop libusb. It
enables fine-grained control over USB video devices exporting the standard USB
Video Class (UVC) interface, enabling developers to write drivers for
previously unsupported devices, or just access UVC devices in a generic
fashion.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Suggests:       %{name}-doc = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains developer documentation for %{name}.

%if %{with examples}
%package        examples
Summary:        Examples for %{name}

%description    examples
This package contains examples making use of %{name}.
%endif

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_BUILD_TARGET=Shared \
%if %{with examples}
  -DBUILD_TEST=ON \
  -DBUILD_EXAMPLE=ON
%else
  -DBUILD_TEST=OFF \
  -DBUILD_EXAMPLE=OFF
%endif
%cmake_build

# Build documentation
doxygen doxygen.conf

%install
%cmake_install

%if %{with examples}
install -Dpm0755 %{_vpath_builddir}/example %{buildroot}%{_bindir}/uvc_example
install -Dpm0755 -t %{buildroot}%{_bindir} %{_vpath_builddir}/uvc_test
%endif

%check
%ctest

%files
%license LICENSE.txt
%doc README.md changelog.txt
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license LICENSE.txt
%doc cameras standard-units.yaml
%doc doc

%if %{with examples}
%files examples
%{_bindir}/uvc_example
%{_bindir}/uvc_test
%endif

%changelog
%autochangelog

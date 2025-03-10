%global date 20250307
%global commit 9d8ec46f02da5120a035663c2f329b4bba0e6206
%global shortcommit %(c=%{commit}; echo ${c:0:7})

# These libraries are statically linked into libsurvive, are only used by this
# project and come from the same upstream
%global cnkalman_commit 6b350314225e28d2e4e8daad7d2971d22386f76f
%global cnkalman_url https://github.com/collabora/cnkalman
%global cnmatrix_commit 5936c62511305227fbd59b2d5a43aaf89ec3a0b6
%global cnmatrix_url https://github.com/collabora/cnmatrix
# These are artifacts used by the unit tests
%global extras_data_commit 3476af66c488b029e04c74fbb1b57f3b7acb9eb7
%global extras_data_url https://github.com/jdavidberger/libsurvive-extras-data

Name:           libsurvive
Version:        1.01^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Open Source Lighthouse Tracking System

# libsurvive is MIT, the rest comes from bundled libraries
License:        MIT AND (MIT AND BSD-2-Clause) AND Minpack AND LicenseRef-Fedora-UltraPermissive AND HIDAPI AND ((MIT OR X11) OR BSD-3-Clause OR GPL-1.0-or-later) AND (MIT AND (MIT OR X11) OR BSD-3-Clause) AND (MIT AND (MIT OR X11)) AND Zlib
URL:            https://github.com/collabora/libsurvive
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        %{cnkalman_url}/archive/%{cnkalman_commit}/cnkalman-%{cnkalman_commit}.tar.gz
Source2:        %{cnmatrix_url}/archive/%{cnmatrix_commit}/cnmatrix-%{cnmatrix_commit}.tar.gz
Source3:        %{extras_data_url}/archive/%{extras_data_commit}/libsurvive-extras-data-%{extras_data_commit}.tar.gz
# Do not attempt to get the test artifacts from the Internet
Patch:          libsurvive-no-external-project.patch

# Build fails on i686 due to incompatible pointer types
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  systemd-rpm-macros

BuildRequires:  blas-devel
BuildRequires:  eigen3-devel
# Excluded as it currently breaks the build
# BuildRequires:  gattlib-devel
BuildRequires:  lapack-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb1-devel
BuildRequires:  libX11-devel
BuildRequires:  openblas-devel
BuildRequires:  opencv-devel
# Excluded as it currently breaks the build
# BuildRequires:  sciplot-devel
BuildRequires:  zlib-devel

# Imported under libs/cnkalman/
# License: MIT
Provides:       bundled(cnkalman) = 0.1
# Imported under libs/cnmatrix/ by cnkalman
# License: MIT AND BSD-2-Clause
Provides:       bundled(cnmatrix) = 0.0
# Imported under src/test_cases/libsurvive-extras-data/
# License: MIT (assumed, see https://github.com/jdavidberger/libsurvive-extras-data/issues/1)
# Vendored under redist/mpfit/
# License: Minpack
Provides:       bundled(mpfit) = 1.24
# Vendored under redist/crc32.{c,h}
# License: LicenseRef-Fedora-UltraPermissive
Provides:       bundled(crc32)
# Vendored under redist/hid*.{c,h}
# License: HIDAPI
Provides:       bundled(hidapi)
# Vendored under redist/CNFG3D.{c,h}
# License: (MIT OR X11) OR BSD 3-Clause OR GPL-1.0-or-later
Provides:       bundled(CNFG3D)
# Vendored under redist/CNFG*.{c,h}
# License: MIT AND (MIT OR X11) OR BSD 3-Clause
Provides:       bundled(CNFG)
# Vendored under redist/jsmn*.{c,h}
# License: MIT
Provides:       bundled(jsmn)
# Vendored under redist/lin*.{c,h}
# License: MIT AND (MIT OR X11)
Provides:       bundled(linmath)
# Vendored under redist/puff.{c,h}
# License: Zlib
Provides:       bundled(zlib)

Requires:       systemd-udev

%description
Libsurvive is a set of tools and libraries that enable 6 dof tracking on
Lighthouse and Vive based systems that is completely Open Source and can run on
any device. It currently supports both SteamVR 1.0 and SteamVR 2.0 generation
of devices and should support any tracked object commercially available.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{commit} -p1

# Drop bundled libraries for non-Linux platforms
rm redist/*.m redist/dirent.windows.h

# Extract libraries and test artifacts in the right places
tar -xf %SOURCE1 --strip-components 1 -C libs/cnkalman/
tar -xf %SOURCE2 --strip-components 1 -C libs/cnkalman/libs/cnmatrix/
mkdir -p %{_vpath_builddir}/src/test_cases/libsurvive-extras-data/
tar -xf %SOURCE3 --strip-components 1 -C %{_vpath_builddir}/src/test_cases/libsurvive-extras-data/

%build
%cmake \
  -DLIB_INSTALL_DIR="%{_lib}/" \
  -DENABLE_TESTS=ON \
  -DUSE_OPENBLAS=ON \
  -DUSE_OPENCV=ON
%cmake_build

%install
%cmake_install

rm %{buildroot}%{_prefix}/lib/*.a

# Install udev rules
install -Dpm0644 -t %{buildroot}%{_udevrulesdir} useful_files/81-vive.rules

%if %{with tests}
%check
%ctest
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/sensors-readout
%{_bindir}/survive-buttons
%{_bindir}/survive-cli
%{_bindir}/survive-solver
%{_bindir}/survive-websocketd
%{_libdir}/%{name}.so.0*
%{_libdir}/%{name}/
%{_udevrulesdir}/81-vive.rules

%files devel
%doc docs/*.md
%{_bindir}/api_example
%{_includedir}/cnkalman/
%{_includedir}/cnmatrix/
%{_includedir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/cnkalman.pc
%{_libdir}/pkgconfig/cnmatrix.pc
%{_libdir}/pkgconfig/survive.pc

%changelog
%autochangelog

%global date 20250328
%global commit 440518bb7b0015a235f2e209b3fb454b2cf13ea2
%global shortcommit %{sub %{commit} 1 7}

# These are artifacts used by the unit tests
%global extras_data_commit 1d5bdc744743daa3cf15a96489b1e6a7785767e2
%global extras_data_shortcommit %{sub %{extras_data_commit} 1 7}
%global extras_data_url https://github.com/jdavidberger/libsurvive-extras-data

Name:           libsurvive
Version:        1.01^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Open Source Lighthouse Tracking System
URL:            https://github.com/collabora/libsurvive

# libsurvive is MIT, the rest comes from bundled libraries
License:        MIT AND (MIT AND BSD-2-Clause) AND Minpack AND LicenseRef-Fedora-UltraPermissive AND HIDAPI AND ((MIT OR X11) OR BSD-3-Clause OR GPL-1.0-or-later) AND (MIT AND (MIT OR X11) OR BSD-3-Clause) AND (MIT AND (MIT OR X11)) AND Zlib
# License breakdown:
# ./src/test_cases/libsurvive-extras-data/
# ./libs/cnkalman/
# ./redist/jsmn*.{c,h}
# License: MIT
# ./libs/cnmatrix/
# License: MIT AND BSD-2-Clause
# ./redist/mpfit/
# License: Minpack
# ./redist/crc32.{c,h}
# License: LicenseRef-Fedora-UltraPermissive
# ./redist/hid*.{c,h}
# License: HIDAPI
# ./redist/CNFG3D.{c,h}
# License: (MIT OR X11) OR BSD 3-Clause OR GPL-1.0-or-later
# ./redist/CNFG*.{c,h}
# License: MIT AND (MIT OR X11) OR BSD 3-Clause
# ./redist/lin*.{c,h}
# License: MIT AND (MIT OR X11)
# ./redist/puff.{c,h}
# License: Zlib

Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz
Source1:        %{extras_data_url}/archive/%{extras_data_commit}/%{name}-extras-data-%{extras_data_commit}.tar.gz#/%{name}-extras-data-%{extras_data_shortcommit}.tar.gz

# Do not attempt to get the test artifacts from the Internet
Patch:          %{name}-no-external-project.patch
# Adapt eigen version detection for eigen3-5.0.0
Patch:          %{name}-eigen3.patch

# Build fails on i686 due to incompatible pointer types
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  blas-devel
BuildRequires:  eigen3-devel
BuildRequires:  gattlib-devel
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  libpcap-devel
BuildRequires:  libusb1-devel
BuildRequires:  libX11-devel
BuildRequires:  openblas-devel
BuildRequires:  opencv-devel
BuildRequires:  python3-devel
BuildRequires:  sciplot-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel

Provides:       bundled(CNFG3D)
Provides:       bundled(CNFG)
Provides:       bundled(crc32)
Provides:       bundled(hidapi)
Provides:       bundled(jsmn)
Provides:       bundled(linmath)
Provides:       bundled(mpfit) = 1.24
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

# Extract test artifacts in the right places
mkdir -p %{_vpath_builddir}/src/test_cases/libsurvive-extras-data/
tar -xf %{SOURCE1} --strip-components 1 -C %{_vpath_builddir}/src/test_cases/%{name}-extras-data/

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

%check
%ctest

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

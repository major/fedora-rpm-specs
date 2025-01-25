%global date 20240930
%global commit 8cc40f73e62adbb8351a0180aa779cdd546170cb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global forgeurl https://github.com/thp/psmoveapi

%global common_description %{expand:
The PS Move API is an open source library to access the Sony Move Motion
Controller via Bluetooth and USB directly from your PC without the need for a
PS3. Tracking in 3D space is possible using a PS Eye or any other suitable
camera source.}

Name:           psmoveapi
Version:        4.0.12^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Library for 6DoF tracking of the PS Move Motion Controller

# psmoveapi is BSD-2-Clause, src/utils/sixpair.c is BSD-3-Clause. Additionally:
# - the upstream tarball includes vendored dependencies under external/ that
#   are removed in prep and not used in this package
# - the upstream tarball includes a couple of sources for OSX under GPLv3;
#   these are also removed in prep and not used
License:        BSD-2-Clause AND BSD-3-Clause
URL:            https://thp.io/2010/psmove
Source:         %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz
# Add missing include
Patch:          %{forgeurl}/pull/499.patch
# Fedora downstream changes
# * Use system libraries
# * Set soversion
# * Fix udev rules path
# * Drop installed cruft
Patch:          psmoveapi-fedora-changes.patch
# Drop libusb-compat-0.1 dependency
Patch:          psmoveapi-no-libusb-compat.patch

BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  python3-sphinx
BuildRequires:  sed

BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-devel
BuildRequires:  glm-devel
BuildRequires:  hidapi-devel
BuildRequires:  libusb1-devel
BuildRequires:  libv4l-devel
BuildRequires:  opencv-devel
BuildRequires:  SDL2-devel
BuildRequires:  systemd-devel

# Per docs/navcon.rst, src/utils/sixpair.c is adapted from sixad
# License: BSD-3-Clause
Provides:       bundled(sixad) = 1.6.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       systemd-udev

%description    %{common_description}

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconf-pkg-config

%description    devel %{common_description}

This package contains development headers and libraries for %{name}.

%package        doc
Summary:        Additional documentation for %{name}
BuildArch:      noarch

%description    doc %{common_description}

This package contains additional documentation for %{name}.

%package        examples
Summary:        Sample and test programs for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    examples %{common_description}

This package contains a number of example and test programs for %{name}.

%package        libs
Summary:        Shared libraries for %{name}

%description    libs %{common_description}

This package contains shared libraries for %{name}.

%prep
%autosetup -p1 -n %{name}-%{commit}

# Strip bundled libraries
rm -r external

# Remove unused OSX sources
rm src/daemon/*.mm

%build
# sixpair is disabled because it uses the deprecated libusb 0.1 API
# https://github.com/thp/psmoveapi/issues/494
%cmake -DPSMOVE_USE_SIXPAIR=OFF
%cmake_build

sphinx-build-3 docs html
rm -rf html/{.buildinfo,.doctrees}

%install
%cmake_install

# Strip rpath, install and rename examples
for f in example example_new_api multiple test_navcon; do
  chrpath -d "%{_vpath_builddir}/${f}"
  install -Dpm0755 "%{_vpath_builddir}/${f}" "%{buildroot}%{_bindir}/%{name}-${f}"
done

%check
%ctest

%files
%doc CHANGELOG.md README.md
%{_bindir}/psmove
%{_udevrulesdir}/99-psmove.rules

%files devel
%{_includedir}/%{name}/
%{_libdir}/libpsmoveapi.so
%{_libdir}/libpsmoveapi_tracker.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%license COPYING
%doc html

%files examples
%{_bindir}/%{name}-example
%{_bindir}/%{name}-example_new_api
%{_bindir}/%{name}-multiple
%{_bindir}/%{name}-test_navcon

%files libs
%license COPYING
%{_libdir}/libpsmoveapi.so.4{,.*}
%{_libdir}/libpsmoveapi_tracker.so.4{,.*}

%changelog
%autochangelog

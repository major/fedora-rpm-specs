Name: bctoolbox
Version: 5.2.45
Release: 2%{?dist}
Summary: Utility library for software from Belledonne Communications and others
License: GPL-3.0-or-later AND GPL-2.0-or-later
URL: https://gitlab.linphone.org/BC/public/bctoolbox/

Source: https://gitlab.linphone.org/BC/public/bctoolbox/-/archive/%{version}/%{name}-%{version}.tar.bz2

# Patches.
# Set real version numberf for maintenance purposes  - philip.wyett@kathenas.org.
Patch00: 0001_bctoolbox_set_current_version.patch
# Set cmake file installation to default location on fedora/rhel - philip.wyett@kathenas.org.
Patch01: 0002_bctoolbox_change_cmake_files_default_install_location.patch

BuildRequires: cmake >= 3.2
BuildRequires: gcc-c++
BuildRequires: mbedtls-devel
BuildRequires: pkgconfig(bcunit)
BuildRequires: pkgconfig(ncurses)

%description
bctoolbox utilities library for software from Belledonne Communications and
others.

This package contains the bctoolbox shared library.

%package devel
Summary: Development files for bctoolbox utility library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-tester%{?_isa} = %{version}-%{release}

%description devel
bctoolbox utilities library for software from Belledonne Communications and
others.

This package contains the libraries, headers and other files required to develop
software with bctoolbox.

%package tester
Summary: Testing binary, library and files for bctoolbox utility library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tester
bctoolbox utilities library for software from Belledonne Communications and
others.

This package contains the bctoolbox testing binary and shared library for
the testing component.

%prep
%autosetup -p1

%build
# Do not error/break compilation for -Werror=unused-parameter, just warn.
%set_build_flags
CFLAGS="$CFLAGS -Wno-error=unused-parameter -Wunused-parameter"
CXXFLAGS="$CXXFLAGS -Wno-error=unused-parameter -Wunused-parameter"

%cmake \
  -DENABLE_DECAF=OFF \
  -DENABLE_POLARSSL=OFF \
  -DCMAKE_SKIP_INSTALL_RPATH=ON \
  -DENABLE_SHARED=ON \
  -DENABLE_MBEDTLS=ON \
  -DENABLE_PACKAGE_SOURCE=OFF \
  -DENABLE_DEFAULT_LOG_HANDLER=ON \
  -DENABLE_STATIC=OFF \
  -DENABLE_TESTS_COMPONENT=ON \
  -DENABLE_TESTS=ON
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%{_libdir}/libbctoolbox.so.1*

%files tester
%{_bindir}/bctoolbox_tester
%{_libdir}/libbctoolbox-tester.so.1*

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/bctoolbox/
# Note: cmake files location. We have moved location, see Patch03.
%{_libdir}/cmake/bctoolbox/
%{_libdir}/pkgconfig/bctoolbox.pc
%{_libdir}/libbctoolbox.so
%{_libdir}/pkgconfig/bctoolbox-tester.pc
%{_libdir}/libbctoolbox-tester.so

%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.45-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 31 2023 Phil Wyett <philip.wyett@kathenas.org> - 5.2.45-1
- Initial package.

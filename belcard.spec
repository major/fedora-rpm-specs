Name: belcard
Version: 5.2.45
Release: 1%{?dist}
Summary: C++ library to manipulate vCard standard format files
License: GPL-3.0-or-later AND GPL-2.0-or-later

URL: https://gitlab.linphone.org/BC/public/belcard/

Source: https://gitlab.linphone.org/BC/public/belcard/-/archive/%{version}/%{name}-%{version}.tar.bz2

# Patches.
Patch00: 0001_belcard_set_current_version_and_change_name.patch
Patch01: 0002_belcard_install_pkgconfig_file.patch
Patch02: 0003_belcard_change_cmake_files_default_install_location.patch

BuildRequires: cmake >= 3.2
BuildRequires: gcc-c++
BuildRequires: libudev-devel
BuildRequires: pkgconfig(bctoolbox) >= 5.2.45
BuildRequires: pkgconfig(belr) >= 5.2.45

%description
Belcard is a C++ library to manipulate the vCard standard format files.

%package data
Summary: Belcard data files
BuildArch: noarch
Recommends: %{name}-devel = %{version}-%{release}

%description data
Belcard is a C++ library to manipulate the vCard standard format files.

This package contains data files for belcard such as belr grammar.

%package devel
Summary: Headers and libraries for the belcard library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-data = %{version}-%{release}
Recommends: %{name}-tools%{?_isa} = %{version}-%{release}

%description devel
Belcard is a C++ library to manipulate the vCard standard format files.

This package contains header files and development libraries needed
to develop applications using the belcard library.

%package tools
Summary: Tools for the belcard library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description tools
Belcard is a C++ library to manipulate the vCard standard format files.

This package contains tools required by the belcard library.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_SHARED=ON \
  -DENABLE_STATIC=OFF \
  -DENABLE_STRICT=ON \
  -DENABLE_TOOLS=ON \
  -DENABLE_UNIT_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%{_libdir}/libbelcard.so.1

%files data
%dir %{_datadir}/belr/
%{_datadir}/belr/grammars/

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/belcard/
%{_libdir}/libbelcard.so
%{_libdir}/cmake/belcard/
%{_libdir}/pkgconfig/belcard.pc

%files tools
%{_bindir}/belcard-folder
%{_bindir}/belcard-parser
%{_bindir}/belcard-unfolder

%changelog
* Thu Jun 01 2023 Phil Wyett <philip.wyett@kathenas.org> - 5.2.45-1
- Initial package.
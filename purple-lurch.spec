%global plugin_name lurch

Name: purple-%{plugin_name}
Version: 0.7.0
Release: 1%{?dist}

License: GPL-3.0-or-later
Summary: OMEMO Encryption plugin for libpurple
URL: https://github.com/gkdr/%{plugin_name}
Source0: %{url}/archive/v%{version}/%{plugin_name}-%{version}.tar.gz

# https://github.com/gkdr/lurch/pull/177
Patch100: %{name}-cmake-build.patch

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(purple)
BuildRequires: pkgconfig(libomemo)
BuildRequires: pkgconfig(libaxc)
BuildRequires: pkgconfig(libsignal-protocol-c)
BuildRequires: pkgconfig(libxml-2.0)

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: ninja-build

%description
This plugin brings Axolotl, by now renamed to double ratchet, to libpurple
applications such as Pidgin by implementing the XEP-0384: OMEMO Encryption.

%prep
%autosetup -n %{plugin_name}-%{version} -p1

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DLURCH_INSTALL:BOOL=ON \
    -DLURCH_WITH_SYSTEM_AXC:BOOL=ON \
    -DLURCH_WITH_SYSTEM_OMEMO:BOOL=ON \
    -DLURCH_WITH_TESTS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_libdir}/purple-2/%{plugin_name}.so

%changelog
* Mon Feb 06 2023 Vitaly Zaitsev <vitaly@easycoding.org> - 0.7.0-1
- Initial SPEC release.

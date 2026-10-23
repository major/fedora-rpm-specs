Name:           hyprmag
Version:        2.2.0
Release:        %autorelease
Summary:        A wlroots-compatible Wayland screen magnifier with basic customization options
License:        BSD-3-Clause AND HPND-sell-variant
URL:            https://github.com/SIMULATAN/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/SIMULATAN/hyprmag/pull/5
Patch0001:      0001-Add-include-GNUInstallDirs-to-CMakeLists.txt.patch

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  wayland-devel
BuildRequires:  wlroots-devel
BuildRequires:  pango-devel
BuildRequires:  cairo-devel
BuildRequires:  libjpeg-devel

%description
A wlroots-compatible Wayland screen magnifier with basic customization options.

%prep
%autosetup

%conf
%cmake

%build
%cmake_build

%check
%ctest
./redhat-linux-build/%{name} --help >/dev/null

%install
%cmake_install

%files
%{_bindir}/hyprmag
%{_mandir}/man1/hyprmag.1.*
%doc README.md
%license LICENSE

%changelog
%autochangelog

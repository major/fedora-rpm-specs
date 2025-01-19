%global forgeurl https://github.com/PixlOne/ipcgull
%global proj_epoc 0

Name:    ipcgull
Version: 0.1
Release: 5%{?dist}
Summary: A GDBus-based IPC library for modern C++
%forgemeta

License: GPL-3.0-or-later
URL:     %{forgeurl}

Source: %{forgesource}

# Change from static to dynamic lib
Patch0:         ipcgull-shared-lib.patch
Patch1:         ipcgull-include-stdexcept.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libstdc++-devel

%description
Ipcgull is a C++ IPC library that takes advantage of modern C++17 
features to provide a simple interface for developers to handle IPC.

Currently, Ipcgull only supports a D-Bus backend (via GDBus), but this 
is abstracted by the library and can theoretically be replaced. 
However, that is out of scope for this project.

%package devel
Summary: A GDBus-based IPC library for modern C++
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains header files and other files needed to develop
with ipcgull.

%prep
%autosetup -p1

%build
%{cmake} -DPROJECT_EPOCH=%{proj_epoc}
%{cmake_build}

%install
%{cmake_install}
install -D -pm 755 redhat-linux-build/libipcgull_shared.so.%{version} %{buildroot}%{_libdir}/libipcgull_shared.so.%{version}
install -D -pm 755 redhat-linux-build/libipcgull_shared.so.%{proj_epoc} %{buildroot}%{_libdir}/libipcgull_shared.so.%{proj_epoc}

%files
%{_libdir}/*.so.*

%license LICENSE
%doc README.md

%files devel
%{_libdir}/*.so
%{_includedir}/ipcgull/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Nicolas De Amicis <deamicis@bluewin.ch> - 0.1-1
- Initial packaging

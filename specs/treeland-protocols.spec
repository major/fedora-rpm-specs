Name:           treeland-protocols
Version:        0.5.1
Release:        %autorelease
Summary:        Wayland protocol extensions for treeland
License:        Apache-2.0 OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL:            https://github.com/linuxdeepin/treeland-protocols
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Wayland protocol extensions for treeland.

%package        devel
Summary:        Development files for %{name}

%description    devel
Wayland protocol extensions for treeland.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license LICENSES/
%doc README.md
%{_datadir}/cmake/TreelandProtocols/
%{_datadir}/pkgconfig/treeland-protocols.pc
%dir %{_datadir}/treeland-protocols
%{_datadir}/treeland-protocols/*.xml

%changelog
%autochangelog

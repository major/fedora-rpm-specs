# This package contains files under %%_libdir but no binary files
%global debug_package %{nil}

Name:           dtkcommon
Version:        5.6.21
Release:        %autorelease
Summary:        DTK common files

# migrated to SPDX
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/dtkcommon
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
This package contains common configuration files for DTK.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains common build configuration files for DTK.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_datadir}/dsg/configs/org.deepin.dtk.preference.json

%files devel
%{_libdir}/cmake/Dtk/
%{_libdir}/cmake/Dtk6/
%{_libdir}/cmake/DtkBuildHelper/

%changelog
%autochangelog

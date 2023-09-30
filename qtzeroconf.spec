%bcond_without check

%global forgeurl https://github.com/jbagg/QtZeroConf
%global commit 38083c612603c1634017838b449c63781d05e7ae

Name:			qtzeroconf
Version:		0.1.0

%forgemeta

Release:		%{autorelease}
Summary:		A Qt wrapper class for ZeroConf libraries across various platforms

# LGPL-3.0-or-later: this project
# LGPL-2.1-or-later: headers derived from avahi
License:		LGPL-3.0-or-later AND LGPL-2.1-or-later
URL:			%{forgeurl}
Source0:		%{forgesource}

BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)

BuildRequires:	avahi-devel

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++

%description
QZeroConf is a Qt wrapper class for ZeroConf libraries across various platforms.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and development files for %{name}.

%prep
%forgesetup


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libQtZeroConf.so.0*

%files devel
%{_includedir}/QtZeroConf/
%{_libdir}/libQtZeroConf.so
%{_libdir}/cmake/QtZeroConf/

%changelog
%{autochangelog}


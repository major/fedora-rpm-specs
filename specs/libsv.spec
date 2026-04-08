Name:           libsv
Version:        1.2

%global forgeurl https://github.com/uael/sv
%forgemeta

Release:        %autorelease
Summary:        Semantic versioning for the C language

License:        Unlicense
URL:            %{forgeurl}
Source:         %{forgesource}

Patch:          https://github.com/uael/sv/commit/b0c92e1be2badd67b2eb3c3baebed43b6f1962ce.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Public domain cross-platform semantic versioning in c99

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains headers and development files for %{name}.

%prep
%forgeautosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license UNLICENSE
%doc     README.md
%{_libdir}/libsv.so.1.0.0
%{_libdir}/libsv.so.1

%files devel
%{_includedir}/semver.h
%{_libdir}/libsv.so
%{_libdir}/pkgconfig/libsv.pc

%changelog
%autochangelog

Version:        7
%global forgeurl https://github.com/neocturne/libuecc
%forgemeta

Name:           libuecc
Release:        %autorelease
Summary:        Very small Elliptic Curve Cryptography library

License:        BSD-2-Clause
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc
BuildRequires:  cmake

%description
Very small Elliptic Curve Cryptography library that is well suited for embedded
software.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%forgeautosetup


%build
%cmake
%cmake_build


%install
%cmake_install
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%files
%doc CHANGELOG README
%license COPYRIGHT
%{_libdir}/%{name}.so.*

%files devel
%doc CHANGELOG README
%license COPYRIGHT
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
%autochangelog

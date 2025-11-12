%global upstream_version        1.0.1

Name:                   redisx
Version:                1.0.1
Release:                %autorelease
Summary:                An independent C/C++ Redis/Valkey client library and toolkit
License:                Unlicense
URL:                    https://smithsonian.github.io/redisx
Source0:                https://github.com/Smithsonian/redisx/archive/refs/tags/v%{upstream_version}.tar.gz
BuildRequires:          doxygen >= 1.13.0
BuildRequires:          gcc
BuildRequires:          libbsd-devel
BuildRequires:          libomp-devel
BuildRequires:          libxchange-devel >= 1.0.1
BuildRequires:          openssl-devel
BuildRequires:          popt-devel
BuildRequires:          readline-devel
BuildRequires:          sed

%description

RedisX is a free, light-weight Redis / Valkey client library for C/C++. It 
supports both interactive and batch Redis queries, managing and processing 
subscriptions, atomic execution blocks, and LUA script loading. It can be used 
with multiple Redis servers simultaneously also. RedisX is free to use, in any 
way you like, without licensing restrictions.

%package devel
Summary:                C development files for the RedisX C/C++ library
Requires:               %{name}%{_isa} = %{version}-%{release}
Requires:               libbsd-devel%{_isa}
Requires:               libomp-devel%{_isa}
Requires:               libxchange-devel%{_isa} >= 1.0.1
Requires:               openssl-devel%{_isa}
Requires:               popt-devel%{_isa}
Requires:               readline-devel%{_isa}


%description devel
This sub-package provides C headers and non-versioned shared library symbolic 
links for the RedisX C/C++ library.

%package doc
Summary:                Documentation for the RedisX C/C++ library
BuildArch:              noarch

%description doc
This package provides HTML documentation and examples for the RedisX C/C++ 
library. The HTML API documentation can also be used with the Eclipse IDE.

%prep
%autosetup

%build

%make_build

%install

%make_install libdir=%{_libdir}

%check

export LD_LIBRARY_PATH=$(pwd)/lib
make test

%files
%license LICENSE
%doc CHANGELOG.md
%{_libdir}/libredisx.so.1{,.*}
%{_bindir}/redisx-cli
%{_mandir}/man1/redisx-cli.1*

%files devel
%doc CONTRIBUTING.md
%doc examples/*
%{_includedir}/*.h
%{_libdir}/libredisx.so

%files doc
%license LICENSE
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/redisx.tag
%doc %{_docdir}/%{name}/html

%changelog
%autochangelog

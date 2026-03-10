%global srcname CxxUrl

%global commit_date     20260214
%global commit_long     e81b86e8779dcd393ed791c1928690e57a83c544
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})

Name:              cxxurl
Version:           0.3^%{commit_date}git%{commit_short}
Release:           1%{dist}
Summary:           A simple C++ URL class
License:           MIT
URL:               https://github.com/chmike/CxxUrl
Source0:           %{url}/archive/%{commit_long}/%{name}-%{commit_long}.tar.gz

# Per i686 leaf package policy 
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:     gcc-c++
BuildRequires:     cmake

%description
The cxxurl library provides a C++ URL handling class with a very simple API.
Its use is straightforward. URIs that don't follow the URL standard defined
in RFC3986 might not be correctly parsed in all cases.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p 1 -n %{srcname}-%{commit_long}

%build
%cmake \
       -DENABLE_INSTALL=ON \
       -DCxxUrl_BUILD_STATIC_LIBS=OFF \
       -DCxxUrl_BUILD_TESTS=ON

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/lib%{srcname}.so.1{,.*}

%files devel
%{_libdir}/lib%{srcname}.so

%dir %{_libdir}/cmake/%{srcname}
%{_libdir}/cmake/%{srcname}/*.cmake

%dir %{_includedir}/%{srcname}
%{_includedir}/%{srcname}/url.hpp
%{_includedir}/%{srcname}/string.hpp

%changelog
* Sat Feb 14 2026 Andrew Bauer <zonexpertconsulting@outlook.com> - 0.3^20260214gite81b86e-1
- initial specfile


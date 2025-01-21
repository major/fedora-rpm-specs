Summary:        An enterprise-level RPC system
Name:           srpc
License:        Apache-2.0

Version:        0.10.3
Release:        2%{?dist}

URL:            https://github.com/sogou/srpc
Source0:        %{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(liblz4)
# Using pkgconfig for openssl gives a fedora-review warning
# that openssl1.1 is deprecated and should not be used
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  workflow-devel

%global _description %{expand:
SRPC is an enterprise-level RPC system used by almost all online services
in Sogou. It handles tens of billions of requests every day, covering
searches, recommendations, advertising system, and other types of services.}

%description
%_description

%package devel
Summary:        Development files for SRPC
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%_description

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
# Do not package static library
rm %{buildroot}/%{_libdir}/libsrpc.a
# README is packaged later
rm %{buildroot}/%{_docdir}/%{name}-%{version}/README.md

%check
# change build directory
sed -i "s/DEFAULT_BUILD_DIR := build.cmake/DEFAULT_BUILD_DIR := %__cmake_builddir/g"  GNUmakefile
make check

%files 
%license LICENSE
%doc README.md
%{_bindir}/%{name}_generator
%{_libdir}/libsrpc.so.0*

%files devel
%{_libdir}/libsrpc.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_includedir}/%name/*.inl
%dir %{_libdir}/cmake/%{name}
%{_libdir}/cmake/%{name}/*.cmake

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep 29 2024 Benson Muite <benson_muite@emailplus.org> - 0.10.3-1
- Upgrade to release 0.10.3

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Bensob Muite <benson_muite@emailplus.org> - 0.10.1-1
- Upgrade to release 0.10.1

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 05 2023 Benson Muite <benson_muite@emailplus.org> - 0.10.0-1
- Initial package

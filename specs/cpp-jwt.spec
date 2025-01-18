%global debug_package %{nil}
# header only lib

Name:           cpp-jwt
Version:        1.4
Release:        9%{?dist}
Summary:        JSON Web Token library for C++

License:        MIT
URL:            https://github.com/arun11299/cpp-jwt
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:          cmake-project-version.patch
Patch1:          side-channel-fix.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  openssl-devel
BuildRequires:  gtest-devel

%global _description %{expand:
JSON Web Token(JWT) is a JSON based standard (RFC-
7519) for creating assertions or access tokens that consists of some
claims (encoded within the assertion). This assertion can be used in some
kind of bearer authentication mechanism that the server will provide to
clients, and the clients can make use of the provided assertion for
accessing resources.}

%description %{_description}

%package devel
Summary:        %{summary}
Recommends:     cmake
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{_description}


%prep
%autosetup -p1


%build
%cmake # -DCPP_JWT_BUILD_EXAMPLES=OFF
%cmake_build


%check
%ctest


%install
%cmake_install


%files devel
%license LICENSE
%doc README.md
%{_includedir}/jwt/
# empty dir
%exclude %{_includedir}/jwt/test
# not needed
%exclude %{_includedir}/jwt/json/test_json.cc
%{_libdir}/cmake/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jonathan Wright <jonathan@almalinux.org> - 1.4-7
- Fix side channel vulnerability rhbz#2263329

* Thu Feb 01 2024 Teoh Han Hui <teohhanhui@gmail.com> - 1.4-6
- Provide cmake config

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 20 2022 Jonathan Wright <jonathan@almalinux.org> - 1.4-1
- Initial package build
- rhbz#2120012

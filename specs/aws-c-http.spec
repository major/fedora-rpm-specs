%global _description %{expand:
C99 implementation of the HTTP/1.1 and HTTP/2 specifications.}

Name:           aws-c-http
Version:        0.9.2
Release:        2%{?dist}
Summary:        C99 implementation of the HTTP/1.1 and HTTP/2 specifications

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-http-cmake.patch
Patch1:         0001-disable-tests-that-require-internet-connectivity.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  numactl-devel
BuildRequires:  aws-c-compression-devel
BuildRequires:  aws-c-io-devel

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# Dependencies like aws-c-common don't support and build on s390x
# Upstream issue: https://github.com/awslabs/aws-c-common/issues/1111
# Fedora bugzilla ticket to be created after package review
ExcludeArch: s390x

%description %{_description}


%package libs
Summary:        %{summary}

%description libs %{_description}


%package devel
Summary:        %{summary}
Requires:       openssl-devel
Requires:       aws-c-compression-devel
Requires:       aws-c-io-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE NOTICE
%doc README.md bin/elasticurl/README.md
%{_bindir}/elasticurl


%files libs
%{_libdir}/libaws-c-http.so.1{,.*}


%files devel
%{_libdir}/libaws-c-http.so
%dir %{_includedir}/aws/http
%{_includedir}/aws/http/*.h
%dir %{_libdir}/cmake/aws-c-http
%dir %{_libdir}/cmake/aws-c-http/shared
%{_libdir}/cmake/aws-c-http/aws-c-http-config.cmake
%{_libdir}/cmake/aws-c-http/shared/aws-c-http-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-http/shared/aws-c-http-targets.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Packit <hello@packit.dev> - 0.9.2-1
- Update to version 0.9.2
- Resolves: rhbz#2321727

* Fri Sep 27 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.8.10-2
- '0001-disable-tests-that-require-internet-connectivity.patch' updated to work with new release.

* Tue Sep 17 2024 Packit <hello@packit.dev> - 0.8.10-1
- Update to version 0.8.10
- Resolves: rhbz#2306011

* Mon Aug 12 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.8.7-2
- '0001-disable-tests-that-require-internet-connectivity.patch' updated to work with new release.

* Thu Aug 08 2024 Packit <hello@packit.dev> - 0.8.7-1
- Update to version 0.8.7
- Resolves: rhbz#2301775

* Thu Jun 06 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.8.2-1
- update to 0.8.2

* Fri Feb 04 2022 David <davdunc@amazon.com> - 0.6.8-4
- Update and verify spec file for review

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.8-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.6.8-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.8-1
- Initial package development

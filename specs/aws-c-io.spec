%global _description %{expand:
IO package for AWS SDK for C. It handles all IO and TLS work
for application protocols.}

Name:           aws-c-io
Version:        0.15.3
Release:        3%{?dist}
Summary:        IO package for AWS SDK for C

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Install cmake files in 'libdir/cmake/aws-c-io' rather than 'libdir/aws-c-io/cmake'
Patch0:         aws-c-io-cmake.patch
# All tests disabled that require internet connectivity
Patch1:         0001-disable-tests-that-require-internet-connectivity.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-c-cal-devel
BuildRequires:  s2n-tls-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# Dependencies like aws-c-common don't support and build on s390x
# Upstream issue: https://github.com/awslabs/aws-c-common/issues/1111
# Fedora bugzilla ticket to be created after package review
ExcludeArch: s390x

%description %{_description}


%package devel
Summary:        IO package for AWS SDK for C
Requires:       openssl-devel%{?_isa}
Requires:       aws-c-common-devel%{?_isa}
Requires:       aws-c-cal-devel%{?_isa}
Requires:       s2n-tls-devel%{?_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

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
%doc README.md
%{_libdir}/libaws-c-io.so.1{,.*}


%files devel
%{_libdir}/libaws-c-io.so
%{_includedir}/aws/io/
%{_includedir}/aws/testing/
%{_libdir}/cmake/aws-c-io/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.15.3-2
- Patch '0001-disable-tests-that-require-internet-connectivity.patch' updated to work with 0.15.3

* Thu Nov 14 2024 Packit <hello@packit.dev> - 0.15.3-1
- Update to version 0.15.3
- Resolves: rhbz#2318007

* Mon Aug 12 2024 Packit <hello@packit.dev> - 0.14.18-1
- Update to version 0.14.18
- Resolves: rhbz#2302713

* Fri Aug 02 2024 Packit <hello@packit.dev> - 0.14.17-1
- Update to version 0.14.17
- Resolves: rhbz#2302547

* Fri Aug 02 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.14.16-2
- Patch '0001-disable-tests-that-require-internet-connectivity.patch' updated to work with 0.14.16

* Thu Aug 01 2024 Packit <hello@packit.dev> - 0.14.16-1
- Update to version 0.14.16
- Resolves: rhbz#2297806

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 11 2024 Packit <hello@packit.dev> - 0.14.10-1
- Update to version 0.14.10
- Resolves: rhbz#2297250

* Wed Jun 05 2024 Packit <hello@packit.dev> - 0.14.9-1
- Update to version 0.14.9
- Resolves: rhbz#2290498

* Wed May 15 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.14.8-1
- update to 0.14.8

* Fri Feb 04 2022 David <davdunc@amazon.com> - 0.10.12-4
- Update and verify spec file for review

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.10.12-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.10.12-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.10.12-1
- Initial package development 

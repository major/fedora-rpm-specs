%global _description %{expand:
AWS Crypto Abstraction Layer: Cross-Platform, C99 wrapper for
cryptography primitives}

Name:           aws-c-cal
Version:        0.8.1
Release:        3%{?dist}
Summary:        AWS Crypto Abstraction Layer

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Install cmake files in 'libdir/cmake/<pkgname>' rather than 'libdir/<pkgname>/cmake'
Patch0:         aws-c-cal-cmake.patch
# Upstream introduced SHA1 related code and tests in v0.8.1
# Fedora 41 and RHEL 9 distrust SHA1 signatures
# Disabling tests of additional functionality to unblock package build
Patch0001:      0001-patch-Disable-SHA1-related-tests.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-common-devel

# Dependency aws-c-common doesn't build on s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2279275
ExcludeArch: s390x

%description %{_description}


%package libs
Summary:        AWS Crypto Abstraction Layer
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs %{_description}


%package devel
Summary:        AWS Crypto Abstraction Layer
Requires:       openssl-devel
Requires:       aws-c-common-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON -DUSE_OPENSSL=ON
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE NOTICE
%doc README.md


%files libs
%{_libdir}/libaws-c-cal.so.1{,.*}


%files devel
%{_libdir}/libaws-c-cal.so
%dir %{_includedir}/aws/cal
%{_includedir}/aws/cal/*.h
%dir %{_libdir}/cmake/aws-c-cal
%dir %{_libdir}/cmake/aws-c-cal/modules
%dir %{_libdir}/cmake/aws-c-cal/shared
%{_libdir}/cmake/aws-c-cal/aws-c-cal-config.cmake
%{_libdir}/cmake/aws-c-cal/modules/Findcrypto.cmake
%{_libdir}/cmake/aws-c-cal/shared/aws-c-cal-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-cal/shared/aws-c-cal-targets.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.8.1-2
- Patch added to disable SHA1 related tests.

* Mon Nov 18 2024 Packit <hello@packit.dev> - 0.8.1-1
- Update to version 0.8.1
- Resolves: rhbz#2321724

* Sun Aug 25 2024 Packit <hello@packit.dev> - 0.7.4-1
- Update to version 0.7.4
- Resolves: rhbz#2304748

* Thu Jul 18 2024 Packit <hello@packit.dev> - 0.7.2-1
- Update to version 0.7.2
- Resolves: rhbz#2298632

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Packit <hello@packit.dev> - 0.7.1-1
- Update to version 0.7.1
- Resolves: rhbz#2293738

* Sun Jun 02 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.6.15-1
- Update to version 0.6.15
- Resolves: rhbz#2281445

* Sun Jun 02 2024 Packit <hello@packit.dev> - 0.6.14-1
- Update to version 0.6.14

* Mon May 06 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.6.12-2
- Exclude from Arch s390x build (rhbz#2279275)

* Tue Apr 30 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.6.12-1
- update to 0.6.12

* Thu Feb 24 2022 David Duncan <davdunc@amazon.com> - 0.5.12-7
- Include check and ctest section in spec

* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.5.12-6
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-5
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-4
- Move sha256_profile executable to standard package

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.5.12-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.5.12-1
- Initial package development

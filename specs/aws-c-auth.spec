%global _description %{expand:
C99 library implementation of AWS client-side authentication}

Name:           aws-c-auth
Version:        0.8.0
Release:        2%{?dist}
Summary:        C99 library implementation of AWS client-side authentication

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-auth-cmake.patch
Patch1:         0001-disable-tests-that-require-internet-connectivity.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-sdkutils-devel
BuildRequires:  aws-c-cal-devel
BuildRequires:  aws-c-http-devel
BuildRequires:  aws-c-io-devel
BuildRequires:  aws-c-compression-devel

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# Dependencies like aws-c-common don't support and build on s390x
# Upstream issue: https://github.com/awslabs/aws-c-common/issues/1111
# Fedora bugzilla ticket to be created after package review
ExcludeArch: s390x

%description %{_description}


%package devel
Summary:        %{summary}
Requires:       openssl-devel
Requires:       aws-c-sdkutils-devel
Requires:       aws-c-cal-devel
Requires:       aws-c-http-devel
Requires:       aws-c-io-devel
Requires:       aws-c-compression-devel
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
%{_libdir}/libaws-c-auth.so.1{,.*}


%files devel
%{_libdir}/libaws-c-auth.so
%dir %{_includedir}/aws/auth
%{_includedir}/aws/auth/*.h
%dir %{_libdir}/cmake/aws-c-auth
%dir %{_libdir}/cmake/aws-c-auth/shared
%{_libdir}/cmake/aws-c-auth/aws-c-auth-config.cmake
%{_libdir}/cmake/aws-c-auth/shared/aws-c-auth-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-auth/shared/aws-c-auth-targets.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Packit <hello@packit.dev> - 0.8.0-1
- Update to version 0.8.0
- Resolves: rhbz#2321728

* Thu Sep 26 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.7.31-1
- update to 0.7.31

* Mon Aug 12 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.7.25-1
- update to 0.7.25

* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.6.5-6
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5-5
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5-4
- Add patch to set CMake configs to correct path

* Thu Feb 03 2022 David Duncan <davdunc@amazon.com> - 0.6.5-3
- Fix CMake targets and move files to lib

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.6.5-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.5.1
- Initial package development

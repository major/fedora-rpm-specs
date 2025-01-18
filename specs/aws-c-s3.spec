%global _description %{expand:
The AWS-C-S3 library is an asynchronous AWS S3 client
focused on maximizing throughput and network utilization.}

Name:           aws-c-s3
Version:        0.7.7
Release:        3%{?dist}
Summary:        C99 library implementation for communicating with the S3 service

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-s3-cmake.patch
Patch1:         0001-disable-tests-that-require-internet-connectivity.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-auth-devel
BuildRequires:  aws-c-http-devel
BuildRequires:  aws-checksums-devel
BuildRequires:  aws-c-sdkutils-devel

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
Requires:       aws-c-auth-devel
Requires:       aws-c-http-devel
Requires:       aws-checksums-devel
Requires:       aws-c-sdkutils-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}


%package doc
Summary:        %{summary}
BuildArch:      noarch

%description doc %{_description}


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build


%install
%cmake_install
# install documentation
mkdir -p %{buildroot}/%{_docdir}/aws-c-s3/docs
mkdir -p %{buildroot}/%{_docdir}/aws-c-s3/docs/images
install -p -m 644 docs/*.md %{buildroot}/%{_docdir}/aws-c-s3/docs/
install -p -m 644 docs/images/*.svg %{buildroot}/%{_docdir}/aws-c-s3/docs/images/


%check
%ctest


%files
%license LICENSE NOTICE
%doc README.md
%{_bindir}/s3


%files libs
%{_libdir}/libaws-c-s3.so.1{,.*}
%{_libdir}/libaws-c-s3.so.0unstable


%files devel
%{_libdir}/libaws-c-s3.so
%dir %{_includedir}/aws/s3
%{_includedir}/aws/s3/*.h
%dir %{_libdir}/cmake/aws-c-s3
%dir %{_libdir}/cmake/aws-c-s3/shared
%{_libdir}/cmake/aws-c-s3/aws-c-s3-config.cmake
%{_libdir}/cmake/aws-c-s3/shared/aws-c-s3-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-s3/shared/aws-c-s3-targets.cmake


%files doc
%license LICENSE NOTICE
%dir %{_docdir}/aws-c-s3/docs/
%dir %{_docdir}/aws-c-s3/docs/images/
%{_docdir}/aws-c-s3/docs/*.md
%{_docdir}/aws-c-s3/docs/images/*.svg


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 21 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.7.7-2
- Patch '0001-disable-tests-that-require-internet-connectivity.patch' updated to work with current release.

* Fri Dec 13 2024 Packit <hello@packit.dev> - 0.7.7-1
- Update to version 0.7.7
- Resolves: rhbz#2331911

* Mon Dec 09 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.7.5-1
- update to 0.7.5

* Mon Nov 25 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.7.1-1
- update to 0.7.1
- doc sub-package 'BuildArch: noarch'

* Mon Sep 30 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.6.6-1
- update to 0.6.6
- minor spec file changes

* Fri May 03 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.5.7-1
- update to 0.5.7

* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.1.27-5
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.27-4
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.27-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.1.27-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.27-1
- Initial package development

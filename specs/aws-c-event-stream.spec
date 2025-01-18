%global _description %{expand:
C99 implementation of the vnd.amazon.eventstream content-type.}

Name:           aws-c-event-stream
Version:        0.5.0
Release:        2%{?dist}
Summary:        C99 implementation of the vnd.amazon.eventstream content-type

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-event-stream-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  aws-c-common-devel
BuildRequires:  aws-checksums-devel
BuildRequires:  aws-c-io-devel

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
Requires:       aws-c-common-devel
Requires:       aws-checksums-devel
Requires:       aws-c-io-devel
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
%{_libdir}/libaws-c-event-stream.so.1{,.*}


%files devel
%{_libdir}/libaws-c-event-stream.so
%dir %{_includedir}/aws/event-stream
%{_includedir}/aws/event-stream/*.h
%dir %{_libdir}/cmake/aws-c-event-stream
%dir %{_libdir}/cmake/aws-c-event-stream/shared
%{_libdir}/cmake/aws-c-event-stream/aws-c-event-stream-config.cmake
%{_libdir}/cmake/aws-c-event-stream/shared/aws-c-event-stream-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-event-stream/shared/aws-c-event-stream-targets.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Packit <hello@packit.dev> - 0.5.0-1
- Update to version 0.5.0
- Resolves: rhbz#2321726

* Tue Aug 20 2024 Packit <hello@packit.dev> - 0.4.3-1
- Update to version 0.4.3
- Resolves: rhbz#2306010

* Thu Jun 06 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.4.2-1
- update to 0.4.2

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.2.7-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.2.7-1
- Build and create package for aws-c-event-stream

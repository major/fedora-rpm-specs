%global _description %{expand:
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.}

Name:           aws-c-common
Version:        0.10.6
Release:        2%{?dist}
Summary:        Core c99 package for AWS SDK for C

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-common-cmake.patch

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
BuildRequires:  cmake

# Bug: Three tests fail when building on s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2279089
ExcludeArch: s390x

%description %{_description}


%package libs
Summary:        Core c99 package for AWS SDK for C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs %{_description}


%package devel
Summary:        Core c99 package for AWS SDK for C
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
%doc README.md


%files libs
%{_libdir}/libaws-c-common.so.1{,.*}


%files devel
%{_libdir}/libaws-c-common.so
%dir %{_includedir}/aws/common
%dir %{_includedir}/aws/common/posix
%dir %{_includedir}/aws/common/external
%dir %{_includedir}/aws/testing
%{_includedir}/aws/common/*.h
%{_includedir}/aws/common/*.inl
%{_includedir}/aws/common/posix/common.inl
%{_includedir}/aws/common/external/*.h
%{_includedir}/aws/testing/aws_test_harness.h
%dir %{_libdir}/cmake/aws-c-common
%dir %{_libdir}/cmake/aws-c-common/shared
%{_libdir}/cmake/aws-c-common/aws-c-common-config.cmake
%{_libdir}/cmake/aws-c-common/shared/aws-c-common-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-common/shared/aws-c-common-targets.cmake
%{_libdir}/cmake/AwsCFlags.cmake
%{_libdir}/cmake/AwsCheckHeaders.cmake
%{_libdir}/cmake/AwsFeatureTests.cmake
%{_libdir}/cmake/AwsFindPackage.cmake
%{_libdir}/cmake/AwsLibFuzzer.cmake
%{_libdir}/cmake/AwsSIMD.cmake
%{_libdir}/cmake/AwsSanitizers.cmake
%{_libdir}/cmake/AwsSharedLibSetup.cmake
%{_libdir}/cmake/AwsTestHarness.cmake
%{_libdir}/cmake/AwsCRuntime.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Dec 11 2024 Packit <hello@packit.dev> - 0.10.6-1
- Update to version 0.10.6
- Resolves: rhbz#2329252

* Thu Nov 14 2024 Packit <hello@packit.dev> - 0.10.3-1
- Update to version 0.10.3
- Resolves: rhbz#2318418

* Fri Sep 06 2024 Packit <hello@packit.dev> - 0.9.28-1
- Update to version 0.9.28
- Resolves: rhbz#2304749

* Mon Aug 12 2024 Packit <hello@packit.dev> - 0.9.25-1
- Update to version 0.9.25
- Resolves: rhbz#2299849

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jul 12 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.9.23-2
- Patch 'upstream_pr_1110_remove_aws_promise.patch' removed, included since 0.9.18.

* Fri Jun 21 2024 Packit <hello@packit.dev> - 0.9.23-1
- Update to version 0.9.23
- Resolves: rhbz#2290497

* Mon May 06 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.9.17-6
- [PATCH] remove aws_promise, test promise_test_multiple_waiters was flaky

* Sun May 05 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.9.17-5
- Packit config update, no package code change

* Sat May 04 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.9.17-4
- ExcludeArch s390x, upstream bug, tests fail

* Sat May 04 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.9.17-3
- Run cmake tests during package build
- Include missing file and directories because of version bump

* Sat May 04 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.9.17-2
- Packit config update, no package code change

* Sat May 04 2024 Packit <hello@packit.dev> - 0.9.17-1
- Update to version 0.9.17
- Resolves: rhbz#2246663

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.6.14-6
- Updated for package review

* Wed Feb 16 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.14-5
- Include missing devel directories

* Thu Feb 03 2022 David Duncan <davdunc@amazon.com> - 0.6.14-4
- rebuilt for fedora review

* Wed Feb 02 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.14-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.6.14-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.6.14.1
- Initial Package development 

Name:           aws-c-common
Version:        0.6.14 
Release:        9%{?dist}
Summary:        Core c99 package for AWS SDK for C

License:        ASL 2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-common-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake

%description
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.


%package libs
Summary:        Core c99 package for AWS SDK for C

%description libs
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.


%package devel
Summary:        Core c99 package for AWS SDK for C
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Core c99 package for AWS SDK for C. Includes cross-platform primitives,
configuration, data structures, and error handling.


%prep
%autosetup -p1


%build
%cmake -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install


%files libs
%license LICENSE
%doc README.md
%{_libdir}/libaws-c-common.so.1{,.*}

%files devel
%dir %{_includedir}/aws/common
%dir %{_includedir}/aws/common/posix
%dir %{_includedir}/aws/testing
%{_includedir}/aws/common/*.h
%{_includedir}/aws/common/*.inl
%{_includedir}/aws/common/posix/common.inl
%{_includedir}/aws/testing/aws_test_harness.h

%dir %{_libdir}/cmake/aws-c-common
%dir %{_libdir}/cmake/aws-c-common/shared
%{_libdir}/libaws-c-common.so
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


%changelog
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

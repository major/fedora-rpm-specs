Name:           aws-c-sdkutils
Version:        0.2.2
Release:        2%{?dist}
Summary:        Utility package for AWS SDK for C

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         aws-c-sdkutils-cmake.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  aws-c-common-devel

Requires:       aws-c-common-libs

# Dependency aws-c-common doesn't build on s390x
# To-do: Create related Bug
ExcludeArch: s390x

%description
Utility package for AWS SDK for C


%package libs
Summary:        Utility package for AWS SDK for C
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs
Utility package for AWS SDK for C


%package devel
Summary:        Utility package for AWS SDK for C
Requires:       aws-c-common-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Utility package for AWS SDK for C


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
%{_libdir}/libaws-c-sdkutils.so.1{,.*}


%files devel
%{_libdir}/libaws-c-sdkutils.so
%dir %{_includedir}/aws/sdkutils
%{_includedir}/aws/sdkutils/*.h
%dir %{_libdir}/cmake/aws-c-sdkutils
%dir %{_libdir}/cmake/aws-c-sdkutils/shared
%{_libdir}/cmake/aws-c-sdkutils/aws-c-sdkutils-config.cmake
%{_libdir}/cmake/aws-c-sdkutils/shared/aws-c-sdkutils-targets-noconfig.cmake
%{_libdir}/cmake/aws-c-sdkutils/shared/aws-c-sdkutils-targets.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 08 2025 Packit <hello@packit.dev> - 0.2.2-1
- Update to version 0.2.2
- Resolves: rhbz#2336445

* Sat Nov 09 2024 Packit <hello@packit.dev> - 0.2.1-1
- Update to version 0.2.1
- Resolves: rhbz#2321722

* Thu Sep 05 2024 Packit <hello@packit.dev> - 0.1.19-1
- Update to version 0.1.19
- Resolves: rhbz#2302714

* Fri Aug 02 2024 Packit <hello@packit.dev> - 0.1.17-1
- Update to version 0.1.17
- Resolves: rhbz#2302548

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 1 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.1.16-1
- update to 0.1.16

* Tue Feb 22 2022 David Duncan <davdunc@amazon.com> - 0.1.1-5
- Updated for package review

* Tue Feb 22 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.1-4
- Include missing devel directories

* Thu Feb 03 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.1-3
- Update specfile based on review feedback

* Wed Feb 02 2022 David Duncan <davdunc@amazon.com> - 0.1.1-2
- Prepare for package review

* Tue Jan 18 2022 Kyle Knapp <kyleknap@amazon.com> - 0.1.1-1
- Initial package development

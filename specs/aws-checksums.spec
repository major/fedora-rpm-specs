Name:           aws-checksums
Version:        0.2.2
Release:        2%{?dist}
Summary:        Efficient CRC32c and CRC32 implementations

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          aws-checksums-cmake.patch

BuildRequires:  aws-c-common-devel
BuildRequires:  cmake
BuildRequires:  gcc

Requires:       aws-c-common-libs

# Dependency aws-c-common doesn't build on s390x
# To-do: Create related Bug
ExcludeArch: s390x

%description
Cross-Platform HW accelerated CRC32c and CRC32 with 
fallback to efficient SW implementations. C interface
with language bindings for each of our SDKs


%package libs
Summary:        Efficient CRC32c and CRC32 implementations
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs
Cross-Platform HW accelerated CRC32c and CRC32 with
fallback to efficient SW implementations. C interface
with language bindings for each of our SDKs


%package devel
Summary:        Efficient CRC32c and CRC32 implementations
Requires:       aws-c-common-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Cross-Platform HW accelerated CRC32c and CRC32 with
fallback to efficient SW implementations. C interface
with language bindings for each of our SDKs


%prep
%autosetup -p1


%build
%cmake
%cmake_build


%install
%cmake_install


%check
%ctest


%files
%license LICENSE
%doc README.md
%{_bindir}/checksum-profile


%files libs
%{_libdir}/libaws-checksums.so.1{,.*}


%files devel
%{_libdir}/libaws-checksums.so
%dir %{_includedir}/aws
%dir %{_includedir}/aws/checksums
%{_includedir}/aws/checksums/*.h
%dir %{_libdir}/cmake/aws-checksums
%dir %{_libdir}/cmake/aws-checksums/shared
%{_libdir}/cmake/aws-checksums/*.cmake
%{_libdir}/cmake/aws-checksums/shared/*.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 13 2024 Packit <hello@packit.dev> - 0.2.2-1
- Update to version 0.2.2
- Resolves: rhbz#2321725

* Thu Sep 26 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.1.20-2
- Update to version 0.1.20, add new binary 'checksum-profile'
- Resolves: rhbz#2310537

* Sun Sep 15 2024 Packit <hello@packit.dev> - 0.1.20-1
- Update to version 0.1.20
- Resolves: rhbz#2310537

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 02 2024 Dominik Wombacher <dominik@wombacher.cc> - 0.1.18-1
- update to 0.1.18

* Tue Sep 26 2023 Benson Muite <benson_muite@emailplus.org> - 0.1.12-1
- Initial import

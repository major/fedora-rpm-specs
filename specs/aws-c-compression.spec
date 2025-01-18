Name:           aws-c-compression
Version:        0.3.0
Release:        2%{?dist}
Summary:        C99 implementation of huffman encoding/decoding

License:        Apache-2.0
URL:            https://github.com/awslabs/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          aws-c-compression-cmake.patch

BuildRequires:  aws-c-common-devel
BuildRequires:  cmake
BuildRequires:  gcc

Requires:       aws-c-common-libs

# Dependency aws-c-common doesn't build on s390x
# To-do: Create related Bug
ExcludeArch: s390x

%description
This is a cross-platform C99 implementation of compression
algorithms such as gzip, and huffman encoding/decoding.
Currently only huffman is implemented.


%package libs
Summary:        C99 implementation of huffman encoding/decoding
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description libs
This is a cross-platform C99 implementation of compression
algorithms such as gzip, and huffman encoding/decoding.
Currently only huffman is implemented.


%package devel
Summary:        C99 implementation of huffman encoding/decoding
Requires:       aws-c-common-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This is a cross-platform C99 implementation of compression
algorithms such as gzip, and huffman encoding/decoding.
Currently only huffman is implemented.


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
%license LICENSE NOTICE
%doc README.md


%files libs
%{_libdir}/libaws-c-compression.so.1{,.*}


%files devel
%{_libdir}/libaws-c-compression.so
%dir %{_includedir}/aws
%dir %{_includedir}/aws/compression
%{_includedir}/aws/compression/*.h
%dir %{_libdir}/cmake/aws-c-compression
%dir %{_libdir}/cmake/aws-c-compression/shared
%{_libdir}/cmake/aws-c-compression/*.cmake
%{_libdir}/cmake/aws-c-compression/shared/*.cmake


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Packit <hello@packit.dev> - 0.3.0-1
- Update to version 0.3.0
- Resolves: rhbz#2321723

* Wed Aug 21 2024 Packit <hello@packit.dev> - 0.2.19-1
- Update to version 0.2.19
- Resolves: rhbz#2307057

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 1 2024 Dominik Wombacher <dominik@wombacher.cc> 0.2.18-1
- update to 0.2.18

* Tue Sep 26 2023 Benson Muite <benson_muite@emailplus.org> 0.2.17-1
- Initial packaging

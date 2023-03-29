Name:           nativefiledialog-extended
Version:        1.0.2
Release:        1%{?dist}
Summary:        Native file dialog library with C and C++ bindings

License:        Zlib
URL:            https://github.com/btzy/nativefiledialog-extended
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel

%global _description %{expand:
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.

This library is based on Michael Labbe's Native File Dialog (
mlabbe/nativefiledialog).}


%description
%{_description}


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}


%description devel
%{_description}


%prep
%autosetup


%build
%cmake \
  -D NFD_BUILD_TESTS=OFF \
  -D BUILD_SHARED_LIBRARY=ON
%cmake_build


%check
# all tests will fail because they require a display


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%{_libdir}/libnfd.so.*


%files devel
%license LICENSE
%{_includedir}/nfd.h*
%{_libdir}/libnfd.so


%changelog
* Mon Mar 27 2023 Jonathan Wright <jonathan@almalinux.org> - 1.0.2-1
- Update to 1.0.2 rhbz#2181792

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Jonathan Wright <jonathan@almalinux.org> - 1.0.1-1
- Update to 1.0.1 rhbz#2148493

* Sat Aug 13 2022 Jonathan Wright <jonathan@almalinux.org> - 1.0.0-1
- Initial package build

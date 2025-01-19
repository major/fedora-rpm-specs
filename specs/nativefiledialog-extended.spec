Name:           nativefiledialog-extended
Version:        1.2.1
Release:        2%{?dist}
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
%{_includedir}/nfd_glfw3.h
%{_includedir}/nfd_sdl2.h
%{_libdir}/libnfd.so
%{_exec_prefix}/lib/cmake/nfd/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Jonathan Wright <jonathan@almalinux.org> - 1.2.1-1
- update to 1.2.1 rhbz#2302640

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 24 2024 Jonathan Wright <jonathan@almalinux.org> - 1.2.0-1
- update to 1.2.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Jonathan Wright <jonathan@almalinux.org> - 1.1.1-1
- Update to 1.1.1 rhbz#2250919
- Fix changelog version cited for 1.1.0-1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Jonathan Wright <jonathan@almalinux.org> - 1.1.0-1
- Update to 1.1.0 rhbz#2219052

* Tue May 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.0.3-1
- Update to 1.0.3 rhbz#2192332

* Mon Mar 27 2023 Jonathan Wright <jonathan@almalinux.org> - 1.0.2-1
- Update to 1.0.2 rhbz#2181792

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Jonathan Wright <jonathan@almalinux.org> - 1.0.1-1
- Update to 1.0.1 rhbz#2148493

* Sat Aug 13 2022 Jonathan Wright <jonathan@almalinux.org> - 1.0.0-1
- Initial package build

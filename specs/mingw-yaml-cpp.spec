%{?mingw_package_header}

%global pkgname yaml-cpp

Name:           mingw-%{pkgname}
Version:        0.6.2
Release:        16%{?dist}
Summary:        A YAML parser and emitter for C++
License:        MIT
URL:            https://github.com/jbeder/yaml-cpp
Source0:        https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-%{version}.tar.gz

# https://github.com/jbeder/yaml-cpp/pull/489
Patch0:         CVE-2017-5950.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++


%description
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.


%package -n mingw32-%{pkgname}
Summary:        A YAML parser and emitter for C++

%description -n mingw32-%{pkgname}
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.


%package -n mingw64-%{pkgname}
Summary:        A YAML parser and emitter for C++

%description -n mingw64-%{pkgname}
yaml-cpp is a YAML parser and emitter in C++ written around the YAML 1.2 spec.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n yaml-cpp-%{pkgname}-%{version}


%build
%mingw_cmake -DYAML_CPP_BUILD_TESTS=OFF -DYAML_CPP_BUILD_TOOLS=OFF
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/yaml-cpp.dll
%{mingw32_libdir}/yaml-cpp.dll.a
%{mingw32_includedir}/yaml-cpp/
%{mingw32_prefix}/CMake/yaml-cpp-config-version.cmake
%{mingw32_prefix}/CMake/yaml-cpp-config.cmake
%{mingw32_prefix}/CMake/yaml-cpp-targets-release.cmake
%{mingw32_prefix}/CMake/yaml-cpp-targets.cmake

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/yaml-cpp.dll
%{mingw64_libdir}/yaml-cpp.dll.a
%{mingw64_includedir}/yaml-cpp/
%{mingw64_prefix}/CMake/yaml-cpp-config-version.cmake
%{mingw64_prefix}/CMake/yaml-cpp-config.cmake
%{mingw64_prefix}/CMake/yaml-cpp-targets-release.cmake
%{mingw64_prefix}/CMake/yaml-cpp-targets.cmake

# See https://fedoraproject.org/wiki/Packaging:MinGW

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.6.2-9
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 0.6.2-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 04 2019 Michał Janiszewski <janisozaur+yamlcppfedoramingw@gmail.com> - 0.6.2-1
- Initial MinGW packaging

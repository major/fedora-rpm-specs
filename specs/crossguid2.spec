%global commit ca1bf4b810e2d188d04cb6286f957008ee1b7681
%global short_commit %(c=%{commit}; echo ${c:0:7})	
%global date 20190529

Name: crossguid2
Version: 0.2.2
Release: 20.%{date}git%{short_commit}%{?dist}
Summary: Lightweight cross platform C++ GUID/UUID library
License: MIT
URL: https://github.com/graeme-hill/crossguid/
Source0: %{url}/archive/%{commit}/crossguid-%{commit}.tar.gz

# Fix library and directory names
Patch0: %{name}-fix_name.patch
Patch1: %{name}-fix_GCC13.patch

BuildRequires: gcc-c++, cmake
BuildRequires: libuuid-devel
BuildRequires: make
BuildRequires: marshalparser

%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and has a generic class for
parsing, stringifying, and comparing IDs.


%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libuuid-devel%{?_isa}
Requires: cmake%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%autosetup -n crossguid-%{commit} -N

%patch -P 0 -p0 -b .fix_name
%patch -P 1 -p1 -b .fix_name


%build
%cmake -DCROSSGUID_SOVERSION_STRING:STRING=0 -DCROSSGUID_VERSION_STRING:STRING=0.0 \
 -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/%{name}
%cmake_build

%install
%cmake_install

%check
%__cmake_builddir/%{name}-test

%files
%doc README.md
%license LICENSE
%{_libdir}/libcrossguid2.so.0
%{_libdir}/libcrossguid2.so.0.2.3

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcrossguid2.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-20.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-19.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 25 2024 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-18.20190529gitca1bf4b
- Fix patch commands

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-17.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-16.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-15.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 28 2023 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-14.20190529gitca1bf4b
- Fix build with GCC-13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-13.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jul 26 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-10.20190529gitca1bf4b
- Change build directory

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 18 2021 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-8.20190529gitca1bf4b
- Fix CMake commands

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-6.20190529gitca1bf4b
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-4.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3.20190529gitca1bf4b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-2.20190529gitca1bf4b
- New commit
- Fix rhbz#1721342
- Add pkgconfig file

* Sat Mar 23 2019 Antonio Trande <sagitter@fedoraproject.org> - 0.2.2-1.20190126gitb151b7d
- Renamed crossguid2 to avoid conflict with older crossguid-0.1
- Post release 0.2.2
- Use CMake method

%{?mingw_package_header}

%global pkgname jansson

Name:           mingw-%{pkgname}
Version:        2.12
Release:        16%{?dist}
Summary:        C library for encoding, decoding and manipulating JSON data
License:        MIT 
URL:            http://www.digip.org/jansson/
Source0:        http://www.digip.org/jansson/releases/jansson-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires: make
BuildRequires:  cmake

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-dlfcn

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-dlfcn


%description
Small library for parsing and writing JSON documents.

%package -n mingw32-%{pkgname}
Summary:        C library for encoding, decoding and manipulating JSON data

%description -n mingw32-%{pkgname}
Small library for parsing and writing JSON documents.

%package -n mingw64-%{pkgname}
Summary:        C library for encoding, decoding and manipulating JSON data

%description -n mingw64-%{pkgname}
Small library for parsing and writing JSON documents.

%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake -DJANSSON_BUILD_SHARED_LIBS=ON -DJANSSON_EXAMPLES=OFF -DJANSSON_WITHOUT_TESTS=ON -DJANSSON_BUILD_DOCS=OFF -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libjansson.dll
%{mingw32_libdir}/libjansson.dll.a
%{mingw32_libdir}/pkgconfig/jansson.pc
%{mingw32_includedir}/jansson.h
%{mingw32_includedir}/jansson_config.h
%{mingw32_prefix}/cmake/janssonConfig.cmake
%{mingw32_prefix}/cmake/janssonConfigVersion.cmake
%{mingw32_prefix}/cmake/janssonTargets-relwithdebinfo.cmake
%{mingw32_prefix}/cmake/janssonTargets.cmake

%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libjansson.dll
%{mingw64_libdir}/libjansson.dll.a
%{mingw64_libdir}/pkgconfig/jansson.pc
%{mingw64_includedir}/jansson.h
%{mingw64_includedir}/jansson_config.h
%{mingw64_prefix}/cmake/janssonConfig.cmake
%{mingw64_prefix}/cmake/janssonConfigVersion.cmake
%{mingw64_prefix}/cmake/janssonTargets-relwithdebinfo.cmake
%{mingw64_prefix}/cmake/janssonTargets.cmake

# See https://fedoraproject.org/wiki/Packaging:MinGW

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.12-9
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.12-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Michał Janiszewski <janisozaur+janssonfedoramingw@gmail.com> - 2.12-1
- Initial MinGW packaging

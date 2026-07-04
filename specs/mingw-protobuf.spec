%{?mingw_package_header}

%global pkgname protobuf

Name:          mingw-%{pkgname}
Version:       33.5
Release:       3%{?dist}
Summary:       MinGW Windows protobuf library

BuildArch:     noarch
License:       BSD-3-Clause
URL:           https://github.com/protocolbuffers/protobuf
Source0:       https://github.com/protocolbuffers/protobuf/archive/v%{version}/%{pkgname}-%{version}-all.tar.gz
# Add version suffix to dlls
Patch0:        protobuf_dllver.patch

BuildRequires: cmake
BuildRequires: ninja-build

BuildRequires: mingw32-abseil-cpp
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-zlib

BuildRequires: mingw64-abseil-cpp
BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-zlib



%description
MinGW Windows protobuf library.


%package -n mingw32-%{pkgname}
Summary:        MinGW Windows protobuf library
BuildArch:      noarch
Obsoletes:      mingw32-%{pkgname}-static < 33.5-1
Provides:       mingw32-%{pkgname}-static = %{version}-%{release}
Obsoletes:      mingw32-%{pkgname}-tools < 33.5-1
Provides:       mingw32-%{pkgname}-tools = %{version}-%{release}

%description -n mingw32-%{pkgname}
MinGW Windows protobuf library.


%package -n mingw64-%{pkgname}
Summary:        MinGW Windows protobuf library
BuildArch:      noarch
Obsoletes:      mingw64-%{pkgname}-static < 33.5-1
Provides:       mingw64-%{pkgname}-static = %{version}-%{release}
Obsoletes:      mingw64-%{pkgname}-tools < 33.5-1
Provides:       mingw64-%{pkgname}-tools = %{version}-%{release}

%description -n mingw64-%{pkgname}
MinGW Windows protobuf library.

%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
%mingw_cmake -Dprotobuf_ABSL_PROVIDER=package \
    -Dprotobuf_BUILD_TESTS:BOOL=OFF \
    -GNinja
%mingw_ninja


%install
%mingw_ninja_install
%mingw_debug_install_post


%files -n mingw32-%{pkgname}
%license LICENSE
%{mingw32_bindir}/libprotobuf-33.5.0.dll
%{mingw32_bindir}/libprotobuf-lite-33.5.0.dll
%{mingw32_bindir}/libprotoc-33.5.0.dll
%{mingw32_bindir}/libutf8_range-33.5.0.dll
%{mingw32_bindir}/libutf8_validity-33.5.0.dll
%{mingw32_bindir}/protoc-gen-upb.exe
%{mingw32_bindir}/protoc-gen-upb.exe-%{version}.0
%{mingw32_bindir}/protoc-gen-upb_minitable.exe
%{mingw32_bindir}/protoc-gen-upb_minitable.exe-%{version}.0
%{mingw32_bindir}/protoc-gen-upbdefs.exe
%{mingw32_bindir}/protoc-gen-upbdefs.exe-%{version}.0
%{mingw32_bindir}/protoc.exe
%{mingw32_bindir}/protoc.exe-%{version}.0
%dir %{mingw32_includedir}/google
%{mingw32_includedir}/google/protobuf/
%{mingw32_includedir}/upb/
%{mingw32_includedir}/utf8_range.h
%{mingw32_includedir}/utf8_validity.h
%{mingw32_libdir}/cmake/protobuf/
%{mingw32_libdir}/cmake/utf8_range/
%{mingw32_libdir}/libprotobuf-lite.dll.a
%{mingw32_libdir}/libprotobuf.dll.a
%{mingw32_libdir}/libprotoc.dll.a
%{mingw32_libdir}/libupb.a
%{mingw32_libdir}/libutf8_range.dll.a
%{mingw32_libdir}/libutf8_validity.dll.a
%{mingw32_libdir}/pkgconfig/protobuf-lite.pc
%{mingw32_libdir}/pkgconfig/protobuf.pc
%{mingw32_libdir}/pkgconfig/upb.pc
%{mingw32_libdir}/pkgconfig/utf8_range.pc


%files -n mingw64-%{pkgname}
%license LICENSE
%{mingw64_bindir}/libprotobuf-33.5.0.dll
%{mingw64_bindir}/libprotobuf-lite-33.5.0.dll
%{mingw64_bindir}/libprotoc-33.5.0.dll
%{mingw64_bindir}/libutf8_range-33.5.0.dll
%{mingw64_bindir}/libutf8_validity-33.5.0.dll
%{mingw64_bindir}/protoc-gen-upb.exe
%{mingw64_bindir}/protoc-gen-upb.exe-%{version}.0
%{mingw64_bindir}/protoc-gen-upb_minitable.exe
%{mingw64_bindir}/protoc-gen-upb_minitable.exe-%{version}.0
%{mingw64_bindir}/protoc-gen-upbdefs.exe
%{mingw64_bindir}/protoc-gen-upbdefs.exe-%{version}.0
%{mingw64_bindir}/protoc.exe
%{mingw64_bindir}/protoc.exe-%{version}.0
%dir %{mingw64_includedir}/google
%{mingw64_includedir}/google/protobuf/
%{mingw64_includedir}/upb/
%{mingw64_includedir}/utf8_range.h
%{mingw64_includedir}/utf8_validity.h
%{mingw64_libdir}/cmake/protobuf/
%{mingw64_libdir}/cmake/utf8_range/
%{mingw64_libdir}/libprotobuf-lite.dll.a
%{mingw64_libdir}/libprotobuf.dll.a
%{mingw64_libdir}/libprotoc.dll.a
%{mingw64_libdir}/libupb.a
%{mingw64_libdir}/libutf8_range.dll.a
%{mingw64_libdir}/libutf8_validity.dll.a
%{mingw64_libdir}/pkgconfig/protobuf-lite.pc
%{mingw64_libdir}/pkgconfig/protobuf.pc
%{mingw64_libdir}/pkgconfig/upb.pc
%{mingw64_libdir}/pkgconfig/utf8_range.pc


%changelog
* Thu Jul 02 2026 Sandro Mani <manisandro@gmail.com> - 33.5-3
- Drop separate protobuf-compiler subpackage

* Thu Jul 02 2026 Sandro Mani <manisandro@gmail.com> - 33.5-2
- Drop separate protobuf-lite subpackage

* Fri Jan 16 2026 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sat Mar 22 2025 Sandro Mani <manisandro@gmail.com> - 3.19.6-9
- Rebuild

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.19.6-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Sandro Mani <manisandro@gmail.com> - 3.19.6-1
- Update to 3.19.6

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 3.19.4-2
- Rebuild with mingw-gcc-12

* Wed Feb 16 2022 Sandro Mani <manisandro@gmail.com> - 3.19.4-1
- Update to 3.19.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 08 2021 Sandro Mani <manisandro@gmail.com> - 3.19.0-1
- Update to 3.19.0

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 3.18.1-2
- Rebuilt for protobuf 3.19.0

* Wed Oct 27 2021 Sandro Mani <manisandro@gmail.com> - 3.18.1-1
- Update to 3.18.1

* Tue Oct 26 2021 Adrian Reber <adrian@lisas.de> - 3.14.0-4
- Rebuilt for protobuf 3.18.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Sandro Mani <manisandro@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Thu Jan 14 08:33:00 CET 2021 Adrian Reber <adrian@lisas.de> - 3.13.0-3
- Rebuilt for protobuf 3.14

* Mon Sep 28 2020 Sandro Mani <manisandro@gmail.com> - 3.13.0-2
- Correctly require protobuf-compiler

* Sun Sep 27 2020 Sandro Mani <manisandro@gmail.com> - 3.13.0-1
- Update to 3.13.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Sandro Mani <manisandro@gmail.com> - 3.12.3-1
- Update to 3.12.3

* Fri May 22 2020 Sandro Mani <manisandro@gmail.com> - 3.11.4-1
- Update to 3.11.4

* Wed Feb 05 2020 Sandro Mani <manisandro@gmail.com> - 3.11.2-1
- Update to 3.11.2

* Mon Oct 28 2019 Sandro Mani <manisandro@gmail.com> - 3.6.1-1
- Initial package

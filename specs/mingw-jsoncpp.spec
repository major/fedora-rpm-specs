%{?mingw_package_header}

%global pkgname jsoncpp

%global jsondir json

%global common_desc \
%{pkgname} is an implementation of a JSON (http://json.org) reader and writer in \
C++. JSON (JavaScript Object Notation) is a lightweight data-interchange format. \
It is easy for humans to read and write. It is easy for machines to parse and \
generate. \
%{nil}

Name:           mingw-%{pkgname}
Version:        1.8.4
Release:        19%{?dist}
Summary:        JSON library implemented in C++

# Automatically converted from old format: Public Domain or MIT - review is highly recommended.
License:        LicenseRef-Callaway-Public-Domain OR LicenseRef-Callaway-MIT
URL:            https://github.com/open-source-parsers/%{pkgname}
Source0:        %{url}/archive/%{version}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake >= 3.1

# Win32 BRs
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-headers

# Win64 BRs
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-headers


%description %{common_desc}


# Win32
%package -n mingw32-%{pkgname}
Summary:        JSON library implemented in C++ for Win32 target

%description -n mingw32-%{pkgname} %{common_desc}
This package provides the library for the Win32 target.

# Win64
%package -n mingw64-%{pkgname}
Summary:        JSON library implemented in C++ for Win64 target

%description -n mingw64-%{pkgname} %{common_desc}
This package provides the library for the Win64 target.


%{?mingw_debug_package}


%prep
%autosetup -n %{pkgname}-%{version} -p1


%build
%mingw_cmake -DBUILD_STATIC_LIBS=OFF                \
             -DJSONCPP_WITH_WARNING_AS_ERROR=OFF    \
             -DJSONCPP_WITH_PKGCONFIG_SUPPORT=ON    \
             -DJSONCPP_WITH_CMAKE_PACKAGE=ON        \
             -DJSONCPP_WITH_POST_BUILD_UNITTEST=OFF \
             .

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=%{buildroot}



%files -n mingw32-%{pkgname}
%license AUTHORS LICENSE
%doc README.md
%{mingw32_bindir}/lib%{pkgname}*.dll
%{mingw32_libdir}/lib%{pkgname}.dll.a
%{mingw32_includedir}/%{jsondir}
%{mingw32_libdir}/cmake/*
%{mingw32_libdir}/pkgconfig/%{pkgname}.pc

%files -n mingw64-%{pkgname}
%license AUTHORS LICENSE
%doc README.md
%{mingw64_bindir}/lib%{pkgname}*.dll
%{mingw64_libdir}/lib%{pkgname}.dll.a
%{mingw64_includedir}/%{jsondir}
%{mingw64_libdir}/cmake/*
%{mingw64_libdir}/pkgconfig/%{pkgname}.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.8.4-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.8.4-11
- Rebuild for mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.8.4-5
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 04 2018 Neal Gompa <ngompa13@gmail.com> - 1.8.4-1
- Initial packaging based on native Fedora version

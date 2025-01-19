%{?mingw_package_header}

%global win32_shared_dir %{_builddir}/mingw32-%{name}-%{version}-%{release}
%global win32_static_dir %{_builddir}/mingw32-%{name}-static-%{version}-%{release}
%global win64_shared_dir %{_builddir}/mingw64-%{name}-%{version}-%{release}
%global win64_static_dir %{_builddir}/mingw64-%{name}-static-%{version}-%{release}

%global pkgname glew

Name:          mingw-%{pkgname}
Version:       2.2.0
Release:       10%{?dist}
Summary:       MinGW Windows GLEW library
# Automatically converted from old format: BSD and MIT - review is highly recommended.
License:       LicenseRef-Callaway-BSD AND LicenseRef-Callaway-MIT

BuildArch:     noarch
URL:           https://github.com/nigels-com/glew
Source0:       https://github.com/nigels-com/glew/releases/download/%{pkgname}-%{version}/%{pkgname}-%{version}.tgz
# - Install both static and shared libraries
# - Remove glu requirement in pkgconfig file
Patch0:        glew_cmake.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc


%description
MinGW Windows GLEW library.


%package -n mingw32-%{pkgname}
Summary:       MinGW Windows GLEW library

%description -n mingw32-%{pkgname}
MinGW Windows GLEW library.


%package -n mingw32-%{pkgname}-static
Summary:       Static version of MinGW Windows GLEW library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
Static version of MinGW Windows GLEW library.


%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows GLEW library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
Tools for the MinGW Windows GLEW library.


%package -n mingw64-%{pkgname}
Summary:       MinGW Windows GLEW library

%description -n mingw64-%{pkgname}
MinGW Windows GLEW library.


%package -n mingw64-%{pkgname}-static
Summary:       Static version of MinGW Windows GLEW library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
Static version of MinGW Windows GLEW library.


%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows GLEW library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
Tools for the MinGW Windows GLEW library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n %{pkgname}-%{version}


%build
# ../ because %%mingw_cmake and %%mingw_make work in build_winXX subfolders
%mingw_cmake ../build/cmake
%mingw_make_build


%install
%mingw_make_install


%files -n mingw32-%{pkgname}
%license LICENSE.txt
%{mingw32_bindir}/glew32.dll
%{mingw32_libdir}/pkgconfig/glew.pc
%{mingw32_includedir}/GL/glew.h
%{mingw32_includedir}/GL/glxew.h
%{mingw32_includedir}/GL/wglew.h
%{mingw32_libdir}/libglew32.dll.a
%{mingw32_libdir}/cmake/glew/

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libglew32.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/glewinfo.exe
%{mingw32_bindir}/visualinfo.exe

%files -n mingw64-%{pkgname}
%doc LICENSE.txt
%{mingw64_bindir}/glew32.dll
%{mingw64_libdir}/pkgconfig/glew.pc
%{mingw64_includedir}/GL/glew.h
%{mingw64_includedir}/GL/glxew.h
%{mingw64_includedir}/GL/wglew.h
%{mingw64_libdir}/libglew32.dll.a
%{mingw64_libdir}/cmake/glew/

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libglew32.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/glewinfo.exe
%{mingw64_bindir}/visualinfo.exe


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.2.0-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.2.0-2
- Rebuild with mingw-gcc-12

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Sandro Mani <manisandro@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 07 2017 Sandro Mani <manisandro@gmail.com> - 2.0.0-4
- Rebuild for ppc64le binutils bug

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 08 2017 Sandro Mani <manisandro@gmail.com> - 2.0.0-1
- Update to 2.0.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Sandro Mani <manisandro@gmail.com> - 1.13.0-2
- Fix glu requirement in pkg-config file
- Don't strip on install

* Sun Jan 17 2016 Sandro Mani <manisandro@gmail.com> - 1.13.0-1
- Update to 1.13.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 19 2013 Sandro Mani <manisandro@gmail.com> - 1.10.0-2
- Remove glu requirement in pkgconfig file

* Thu Aug 08 2013 Sandro Mani <manisandro@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 30 2013 Sandro Mani <manisandro@gmail.com> - 1.9.0-5
- Don't strip glew.exe visualinfo.exe on install

* Fri May 17 2013 Sandro Mani <manisandro@gmail.com> - 1.9.0-4
- Pass correct CFLAGS

* Thu May 09 2013 Sandro Mani <manisandro@gmail.com> - 1.9.0-3
- Remove mingw_build_win32/64 macros
- Properly version mingw32-filesystem BuildRequires
- Reword win32/64_dynamic_dir to win32/64_shared_dir

* Thu May 09 2013 Sandro Mani <manisandro@gmail.com> - 1.9.0-2
- Spec updates

* Thu Feb 28 2013 Sandro Mani <manisandro@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Sat Aug 18 2012 Sandro Mani <manisandro@gmail.com> - 1.7.0-1
- Update to 1.7.0
- Enable Win64 build

* Mon May 28 2012 Sandro Mani <manisandro@gmail.com> - 1.6.0-4
- Packaging fixes

* Thu May 24 2012 Sandro Mani <manisandro@gmail.com> - 1.6.0-3
- Packaging fixes

* Thu May 24 2012 Sandro Mani <manisandro@gmail.com> - 1.6.0-2
- Packaging fixes

* Thu May 24 2012 Sandro Mani <manisandro@gmail.com> - 1.6.0-1
- Initial build

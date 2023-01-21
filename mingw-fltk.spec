%{?mingw_package_header}

Name:           mingw-fltk
Version:        1.3.8
Release:        4%{?dist}
Summary:        C++ user interface toolkit

# See https://www.fltk.org/COPYING.php for exceptions 
License:        LGPLv2+ with exceptions
URL:            http://www.fltk.org
Source0:        https://fltk.org/pub/fltk/%{version}/fltk-%{version}-source.tar.gz

Patch0:         mingw-fltk-cmake.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  fltk-fluid
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
# Libraries
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
# Libraries
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg


%global _description \
FLTK (pronounced "fulltick") is a cross-platform C++ GUI toolkit. \
It provides modern GUI functionality without the bloat, and supports \
3D graphics via OpenGL and its built-in GLUT emulation.


%description
%{_description}

%package -n mingw32-fltk
Summary:       %{summary}

%description -n mingw32-fltk
%{_description}

# Win64
%package -n mingw64-fltk
Summary:       MinGW compiled fltk for the Win64 target

%description -n mingw64-fltk
%{_description}

%package -n mingw32-fltk-static
Summary:       %{summary}

%description -n mingw32-fltk-static
%{_description}

# Win64
%package -n mingw64-fltk-static
Summary:       MinGW compiled fltk for the Win64 target

%description -n mingw64-fltk-static
%{_description}


%{?mingw_debug_package}


%prep
%autosetup -p1 -n fltk-%{version}


%build
%mingw_cmake -DOPTION_BUILD_SHARED_LIBS=TRUE
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=%{buildroot}


%files -n mingw32-fltk
%license COPYING src/xutf8/COPYING
%{mingw32_bindir}/fltk-config
%{mingw32_bindir}/libfltk.dll
%{mingw32_libdir}/libfltk.dll.a
%{mingw32_bindir}/libfltk_forms.dll
%{mingw32_libdir}/libfltk_forms.dll.a
%{mingw32_bindir}/libfltk_images.dll
%{mingw32_libdir}/libfltk_images.dll.a
%{mingw32_bindir}/libfltk_gl.dll
%{mingw32_libdir}/libfltk_gl.dll.a
%{mingw32_includedir}/FL/
%{mingw32_datadir}/cmake/fltk/
%exclude %{mingw32_datadir}/man/*

%files -n mingw64-fltk
%license COPYING src/xutf8/COPYING
%{mingw64_bindir}/fltk-config
%{mingw64_bindir}/libfltk.dll
%{mingw64_libdir}/libfltk.dll.a
%{mingw64_bindir}/libfltk_forms.dll
%{mingw64_libdir}/libfltk_forms.dll.a
%{mingw64_bindir}/libfltk_images.dll
%{mingw64_libdir}/libfltk_images.dll.a
%{mingw64_bindir}/libfltk_gl.dll
%{mingw64_libdir}/libfltk_gl.dll.a
%{mingw64_includedir}/FL/
%{mingw64_datadir}/cmake/fltk/
%exclude %{mingw64_datadir}/man/*

%files -n mingw32-fltk-static
%{mingw32_libdir}/libfltk.a
%{mingw32_libdir}/libfltk_forms.a
%{mingw32_libdir}/libfltk_images.a
%{mingw32_libdir}/libfltk_gl.a

%files -n mingw64-fltk-static
%{mingw64_libdir}/libfltk.a
%{mingw64_libdir}/libfltk_forms.a
%{mingw64_libdir}/libfltk_images.a
%{mingw64_libdir}/libfltk_gl.a


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.3.8-2
- Rebuild with mingw-gcc-12

* Mon Feb 21 2022 Richard Shaw <hobbes1069@gmail.com> - 1.3.8-1
- Update to 1.3.8.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.5-2
- Revise per reviewer feedback.

* Sun May 10 2020 Richard Shaw <hobbes1069@gmail.com> - 1.3.5-1
- Initial packaging.

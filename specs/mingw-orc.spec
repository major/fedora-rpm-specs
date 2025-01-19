%{?mingw_package_header}

Name:           mingw-orc
Version:        0.4.40
Release:        2%{?dist}
Summary:        Cross compiled Oil Run-time Compiler

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://code.entropywave.com/projects/orc/
Source0:        http://gstreamer.freedesktop.org/src/orc/orc-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc

%description
Orc is a library and set of tools for compiling and executing
very simple programs that operate on arrays of data.  The "language"
is a generic assembly language that represents many of the features
available in SIMD architectures, including saturated addition and
subtraction, and many arithmetic operations.


# Mingw32
%package -n mingw32-orc
Summary: %{summary}

%description -n mingw32-orc
Cross compiled Oil Run-time Compiler.

%package -n mingw32-orc-compiler
Summary:        Orc compiler
Requires:       mingw32-orc = %{version}-%{release}
Requires:       pkgconfig

%description -n mingw32-orc-compiler
The Orc compiler, to produce optimized code.

# Mingw64
%package -n mingw64-orc
Summary: %{summary}

%description -n mingw64-orc
Cross compiled Oil Run-time Compiler.

%package -n mingw64-orc-compiler
Summary:        Orc compiler
Requires:       mingw64-orc = %{version}-%{release}
Requires:       pkgconfig

%description -n mingw64-orc-compiler
The Orc compiler, to produce optimized code.

%{?mingw_debug_package}


%prep
%setup -q -n orc-%{version}


%build
%mingw_meson -Dgtk_doc=disabled
%mingw_ninja


%install
%mingw_ninja_install


# Mingw32
%files -n mingw32-orc
%license COPYING
%doc README
%{mingw32_bindir}/liborc-0.4-0.dll
%{mingw32_bindir}/liborc-test-0.4-0.dll
%{mingw32_bindir}/orc-bugreport.exe
%{mingw32_includedir}/orc-0.4/
%{mingw32_libdir}/liborc-0.4.dll.a
%{mingw32_libdir}/liborc-test-0.4.dll.a
%{mingw32_libdir}/pkgconfig/orc-0.4.pc
%{mingw32_libdir}/pkgconfig/orc-test-0.4.pc

%files -n mingw32-orc-compiler
%{mingw32_bindir}/orcc.exe

# Mingw64
%files -n mingw64-orc
%license COPYING
%doc README
%{mingw64_bindir}/liborc-0.4-0.dll
%{mingw64_bindir}/liborc-test-0.4-0.dll
%{mingw64_bindir}/orc-bugreport.exe
%{mingw64_includedir}/orc-0.4/
%{mingw64_libdir}/liborc-0.4.dll.a
%{mingw64_libdir}/liborc-test-0.4.dll.a
%{mingw64_libdir}/pkgconfig/orc-0.4.pc
%{mingw64_libdir}/pkgconfig/orc-test-0.4.pc

%files -n mingw64-orc-compiler
%{mingw64_bindir}/orcc.exe


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4.40-1
- new version

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.38-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 01 2024 Sandro Mani <manisandro@gmail.com> - 0.4.38-2
- Rebuild

* Thu Mar 07 2024 Sandro Mani <manisandro@gmail.com> - 0.4.38-1
- Update to 0.4.38

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 0.4.27-11
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 15 2017 Kalev Lember <klember@redhat.com> - 0.4.27-1
- Update to 0.4.27

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 05 2016 Kalev Lember <klember@redhat.com> - 0.4.26-1
- Update to 0.4.26
- Don't set group tags

* Thu May 12 2016 Kalev Lember <klember@redhat.com> - 0.4.25-1
- Update to 0.4.25

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 26 2015 Kalev Lember <klember@redhat.com> - 0.4.24-1
- Update to 0.4.24
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Nov 28 2014 Michael Cronenworth <mike@cchtml.com> - 0.4.22-1
- Updated to 0.4.22

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May  3 2012 Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4.16-1
- Updated to 0.4.16

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul  4 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.4.14-2
- The package wasn't installable due to broken Requires tags. Fixed

* Fri May 13 2011 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4.14-1
- Updated to 0.4.14
- Updated to newer mingw instructions (with mingw64 support)

* Wed Dec 29 2010 - Marc-André Lureau <marcandre.lureau@redhat.com> - 0.4.11-1
- Initial mingw32-orc 0.4.11
- Based upon previous package in Fedora by Fabian Deutsch

%{?mingw_package_header}

%global _pkg_name clucene

Summary:	MinGW build of a C++ port of Lucene
Name:		mingw-%{_pkg_name}
Version:	2.3.3.4
Release:	30%{?dist}
License:	LGPLv2+ or ASL 2.0
URL:		http://www.sourceforge.net/projects/clucene
Source0:	http://downloads.sourceforge.net/clucene/clucene-core-%{version}.tar.gz
BuildRequires: make
BuildRequires:	gawk cmake
BuildRequires:	mingw32-zlib mingw64-zlib
BuildRequires:	mingw32-boost mingw64-boost
BuildRequires:	mingw32-gcc-c++ mingw64-gcc-c++
BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw64-filesystem >= 95

BuildArch:	noarch

## upstreamable patches
# include LUCENE_SYS_INCLUDES in pkgconfig --cflags output
# https://bugzilla.redhat.com/748196
# and
# https://sourceforge.net/tracker/?func=detail&aid=3461512&group_id=80013&atid=558446
# pkgconfig file is missing clucene-shared
Patch50: clucene-core-2.3.3.4-pkgconfig.patch
# https://bugzilla.redhat.com/794795
# https://sourceforge.net/tracker/index.php?func=detail&aid=3392466&group_id=80013&atid=558446
# contribs-lib is not built and installed even with config
Patch51: clucene-core-2.3.3.4-install_contribs_lib.patch
Patch52: mingw-clucene-core-2.3.3.4-fix-threads.patch

# Don't try to use pthreads on win32 even when it is available
# Fixes FTBFS against mingw-winpthreads
Patch53: mingw-clucene-dont-use-pthreads-on-win32.patch

# Don't try to declare beginthread as it is already part of the mingw-w64 headers
Patch54: clucene-remove-beginthread-declaration.patch

# Add support for GCC > 5.x
Patch55: mingw-clucene-gcc-version.patch

# Fix errors about unsigned/signed narrowing precision loss
Patch56: mingw-clucene-narrowing.patch


%description
CLucene is a C++ port of the popular Apache Lucene search engine
(http://lucene.apache.org/java).
CLucene aims to be a high-speed alternative to Java Lucene, its API is very
similar to that of the Java version. CLucene has recently been brought up to
date with Lucene 2.3.2. It contains most of the same functionality as the
Java version.

%package -n mingw32-%{_pkg_name}
Summary:	%{summary}

%description -n mingw32-%{_pkg_name}
CLucene is a C++ port of the popular Apache Lucene search engine
(http://lucene.apache.org/java).
CLucene aims to be a high-speed alternative to Java Lucene, its API is very
similar to that of the Java version. CLucene has recently been brought up to
date with Lucene 2.3.2. It contains most of the same functionality as the
Java version.

%package -n mingw64-%{_pkg_name}
Summary:	%{summary}

%description -n mingw64-%{_pkg_name}
CLucene is a C++ port of the popular Apache Lucene search engine
(http://lucene.apache.org/java).
CLucene aims to be a high-speed alternative to Java Lucene, its API is very
similar to that of the Java version. CLucene has recently been brought up to
date with Lucene 2.3.2. It contains most of the same functionality as the
Java version.


%{?mingw_debug_package}


%prep
%setup -qn %{_pkg_name}-core-%{version}

%patch50 -p1 -b .pkgconfig
%patch51 -p1 -b .install_contribs_lib
%patch52 -p1 -b .threads
%patch53 -p0 -b .pthread
%patch54 -p0 -b .beginthread
%patch55 -p1 -b .gcc7
%patch56 -p1 -b .narrowing

rm -rf src/ext/{boost,zlib}

%build
# Also for 64-bit
MINGW32_CMAKE_ARGS="
	-DLIB_DESTINATION:PATH=%{mingw32_libdir}"

MINGW64_CMAKE_ARGS="
	-DLIB_DESTINATION:PATH=%{mingw64_libdir}
	-DDISABLE_MULTITHREADING:BOOL=ON"

%mingw_cmake -DBUILD_STATIC_LIBRARIES:BOOLEAN=FALSE \
	-D_CL_HAVE_GCC_ATOMIC_FUNCTIONS_EXITCODE=0 \
	-D_CL_HAVE_GCC_ATOMIC_FUNCTIONS_EXITCODE__TRYRUN_OUTPUT= \
	-D_CL_HAVE_TRY_BLOCKS_EXITCODE=0 \
	-D_CL_HAVE_TRY_BLOCKS_EXITCODE__TRYRUN_OUTPUT= \
	-D_CL_HAVE_NAMESPACES_EXITCODE=0 \
	-D_CL_HAVE_NAMESPACES_EXITCODE__TRYRUN_OUTPUT= \
	-D_CL_HAVE_NO_SNWPRINTF_BUG_EXITCODE=0 \
	-D_CL_HAVE_NO_SNWPRINTF_BUG_EXITCODE__TRYRUN_OUTPUT= \
	-DLUCENE_STATIC_CONSTANT_SYNTAX_EXITCODE=1 \
	-DLUCENE_STATIC_CONSTANT_SYNTAX_EXITCODE__TRYRUN_OUTPUT= \
	-D_CL_HAVE_GCCVISIBILITYPATCH=0 \
	-D_CL_HAVE_FUNCTION_SNPRINTF:INTERNAL=0

%mingw_make %{?_smp_mflags}


%install
%mingw_make install/fast DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{mingw32_libdir}/CLuceneConfig.cmake
rm -rf $RPM_BUILD_ROOT%{mingw64_libdir}/CLuceneConfig.cmake

mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
mv $RPM_BUILD_ROOT%{mingw32_libdir}/libclucene-core.dll \
   $RPM_BUILD_ROOT%{mingw32_libdir}/libclucene-shared.dll \
   $RPM_BUILD_ROOT%{mingw32_bindir}

mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
mv $RPM_BUILD_ROOT%{mingw64_libdir}/libclucene-core.dll \
   $RPM_BUILD_ROOT%{mingw64_libdir}/libclucene-shared.dll \
   $RPM_BUILD_ROOT%{mingw64_bindir}

%files -n mingw32-%{_pkg_name}
%doc APACHE.license AUTHORS ChangeLog COPYING LGPL.license README
%{mingw32_libdir}/libclucene-core.dll.a
%{mingw32_bindir}/libclucene-core.dll
%{mingw32_libdir}/libclucene-shared.dll.a
%{mingw32_bindir}/libclucene-shared.dll
%{mingw32_includedir}/CLucene/
%{mingw32_includedir}/CLucene.h

%files -n mingw64-%{_pkg_name}
%doc APACHE.license AUTHORS ChangeLog COPYING LGPL.license README
%{mingw64_libdir}/libclucene-core.dll.a
%{mingw64_bindir}/libclucene-core.dll
%{mingw64_libdir}/libclucene-shared.dll.a
%{mingw64_bindir}/libclucene-shared.dll
%{mingw64_includedir}/CLucene/
%{mingw64_includedir}/CLucene.h

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 2.3.3.4-28
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 2.3.3.4-22
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 22 2018 Greg Hellings <greg.hellings@gmail.com> - 2.3.3.4-19
- Increased gcc detection patch for compiler versions above 7
- Added patch to fix errors about unsigned/signed type narrowing
- Cleaned up spurious trailing whitespace characters

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Apr 11 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.3.4-12
- Rebuild against latest mingw-gcc

* Fri Jan 30 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.3.3.4-11
- Fix FTBFS against recent mingw-w64 (conflicting _beginthread declaration)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Oct 07 2013 Greg Hellings <greg.hellings@gmail.com> 2.3.3.4-9
- Forced rebuild for library compatibility

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 31 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.3.3.4-7
- Don't use pthreads on win32 even when it is available
  (clucene uses the win32 threading API directly)

* Sun Jan 27 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 2.3.3.4-6
- Rebuild against mingw-gcc 4.8 (win64 uses SEH exceptions now)

* Fri Nov 16 2012 Greg Hellings <greg.hellings@gmail.com> 2.3.3.4-5
- Fixed remaining Summary values

* Fri Nov 16 2012 Greg Hellings <greg.hellings@gmail.com> 2.3.3.4-4
- Added back boost dependency
- Removed bundled library copies
- Removed extraneous Provides lines
- Eliminated length warnings on descriptions from rpmlint
- Eliminated "setup not quiet" warning from rpmlint
- Removed unused "Group:" directives

* Wed Nov 14 2012 Greg Hellings <greg.hellings@gmail.com> 2.3.3.4-3
- Renamed packages to avoid unnecessary confusion
- Removed unused BuildRequires
- Removed conflicting dependency on pthreads in favor of native Win32 threading
- Removed duplicate configure flags
- Eliminated unsupported configure flags

* Wed Aug 08 2012 Greg Hellings <greg.hellings@gmail.com> 2.3.3.4-2
- Bumped version as requested
- Updated file lists from review request feedback

* Fri Jul 06 2012 Greg Hellings <greg.hellings@gmail.com> 2.3.3.4-1
- Removed redundant files
- Removed extra files yielding warnings
- Removed clean section which is superfluous.

* Fri May 25 2012 Greg Hellings <greg.hellings@gmail.com> 2.3.3.4-0
- Initial package for MinGW

%{?mingw_package_header}

%global _pkg_name sword

Summary:	MinGW build of a cross-platform scripture text library
Name:		mingw-%{_pkg_name}
Version:	1.9.0
Release:	12%{?dist}
License:	GPLv2
URL:		http://www.crosswire.org/sword
Source0:	http://crosswire.org/ftpmirror/pub/sword/source/v1.9/sword-%{version}.tar.gz
BuildRequires: make
BuildRequires:	cmake
BuildRequires:  mingw32-gcc-c++ mingw64-gcc-c++
BuildRequires:	mingw32-zlib mingw64-zlib
BuildRequires:	mingw32-clucene mingw64-clucene
BuildRequires:	mingw32-glib2 mingw64-glib2
BuildRequires:	mingw32-curl mingw64-curl
BuildRequires:	mingw32-icu mingw64-icu
BuildRequires:	mingw32-libgnurx mingw64-libgnurx
BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw64-filesystem >= 95
%if 0%{?fedora} >= 20
BuildRequires:  mingw32-winpthreads mingw64-winpthreads
%endif

BuildArch:	noarch

%description
SWORD is a cross-platform C++ library for storage, retrieval, conversion, and
search of texts with an emphasis on Biblical texts, commentaries, and related
works.

%package -n mingw32-%{_pkg_name}
Summary:	%{summary}

%description -n mingw32-%{_pkg_name}
SWORD is a cross-platform C++ library for storage, retrieval, conversion, and
search of texts with an emphasis on Biblical texts, commentaries, and related
works.

%package -n mingw64-%{_pkg_name}
Summary:	%{summary}

%description -n mingw64-%{_pkg_name}
SWORD is a cross-platform C++ library for storage, retrieval, conversion, and
search of texts with an emphasis on Biblical texts, commentaries, and related
works.

%{?mingw_debug_package}


%prep
%setup -qn %{_pkg_name}-%{version}

%build
MINGW64_CXXFLAGS="${MINGW64_CXXFLAGS} -fpermissive -Wint-to-pointer-cast -D_ICUSWORD_"
MINGW32_CXXFLAGS="${MINGW32_CXXFLAGS} -D_ICUSWORD_"
export MINGW64_CXXFLAGS MINGW32_CXXFLAGS

MINGW32_CMAKE_ARGS=-DICU_CONFIG_BIN_PATH=%{mingw32_bindir}

MINGW64_CMAKE_ARGS=-DICU_CONFIG_BIN_PATH=%{mingw64_bindir}

%mingw_cmake -DLIBSWORD_LIBRARY_TYPE=Shared \
	-DSWORD_BUILD_EXAMPLES="Yes" \
	-DCMAKE_BUILD_TYPE="Debug" \
	-DICU_CONFIG_OPTS="--noverify" \
	-DCROSS_COMPILE_MINGW32=TRUE

%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

%files -n mingw32-%{_pkg_name}
%doc AUTHORS ChangeLog COPYING LICENSE
%{mingw32_libdir}/libsword.dll.a
%{mingw32_bindir}/libsword.dll
%{mingw32_bindir}/addld.exe
%{mingw32_bindir}/diatheke.exe
%{mingw32_bindir}/imp2gbs.exe
%{mingw32_bindir}/imp2ld.exe
%{mingw32_bindir}/imp2vs.exe
%{mingw32_bindir}/installmgr.exe
%{mingw32_bindir}/mkfastmod.exe
%{mingw32_bindir}/mod2imp.exe
%{mingw32_bindir}/mod2osis.exe
%{mingw32_bindir}/mod2vpl.exe
%{mingw32_bindir}/mod2zmod.exe
%{mingw32_bindir}/osis2mod.exe
%{mingw32_bindir}/tei2mod.exe
%{mingw32_bindir}/vpl2mod.exe
%{mingw32_bindir}/vs2osisref.exe
%{mingw32_bindir}/vs2osisreftxt.exe
%{mingw32_bindir}/xml2gbs.exe
%{mingw32_bindir}/emptyvss.exe
%{mingw32_libdir}/pkgconfig/sword.pc
%{mingw32_includedir}/sword/
%{mingw32_datadir}/sword/
%{mingw32_sysconfdir}/sword.conf

%files -n mingw64-%{_pkg_name}
%doc AUTHORS ChangeLog COPYING LICENSE
%{mingw64_libdir}/libsword.dll.a
%{mingw64_bindir}/libsword.dll
%{mingw64_bindir}/addld.exe
%{mingw64_bindir}/diatheke.exe
%{mingw64_bindir}/imp2gbs.exe
%{mingw64_bindir}/imp2ld.exe
%{mingw64_bindir}/imp2vs.exe
%{mingw64_bindir}/installmgr.exe
%{mingw64_bindir}/mkfastmod.exe
%{mingw64_bindir}/mod2imp.exe
%{mingw64_bindir}/mod2osis.exe
%{mingw64_bindir}/mod2vpl.exe
%{mingw64_bindir}/mod2zmod.exe
%{mingw64_bindir}/osis2mod.exe
%{mingw64_bindir}/tei2mod.exe
%{mingw64_bindir}/vpl2mod.exe
%{mingw64_bindir}/vs2osisref.exe
%{mingw64_bindir}/vs2osisreftxt.exe
%{mingw64_bindir}/xml2gbs.exe
%{mingw64_bindir}/emptyvss.exe
%{mingw64_libdir}/pkgconfig/sword.pc
%{mingw64_includedir}/sword/
%{mingw64_datadir}/sword/
%{mingw64_sysconfdir}/sword.conf

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Sandro Mani <manisandro@gmail.com> - 1.9.0-10
- Rebuild (mingw-icu)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Sandro Mani <manisandro@gmail.com> - 1.9.0-8
- Rebuild (mingw-icu)

* Fri Aug 05 2022 Sandro Mani <manisandro@gmail.com> - 1.9.0-7
- Rebuild (icu)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Sandro Mani <manisandro@gmail.com> - 1.9.0-3
- Rebuild (icu)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Greg Hellings <greg.hellings@gmail.com> - 1.9.0-1
- Upstream 1.9.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 19 2020 Sandro Mani <manisandro@gmail.com> - 1.8.1-11
- Rebuild (icu)

* Sun Apr 26 2020 Greg Hellings <greg.hellings@gmail.com> - 1.8.1-10
- Actually apply patch from -9. Ugh.

* Sun Apr 26 2020 Greg Hellings <greg.hellings@gmail.com> - 1.8.1-9
- Add upstream patch

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Sandro Mani <manisandro@gmail.com> - 1.8.1-7
- Rebuild (icu)

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.8.1-6
- Rebuild (Changes/Mingw32GccDwarf2)

* Tue Aug 13 2019 Sandro Mani <manisandro@gmail.com> - 1.8.1-5
- Rebuild (icu)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Greg Hellings <greg.hellings@gmail.com> - 1.8.1-1
- Upstream version 1.8.1

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Oct 24 2016 Kalev Lember <klember@redhat.com> - 1.7.4-4
- Rebuilt for mingw-icu 57

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Greg Hellings <greg.hellings@gmail.com> 1.7.4-1
- New upstream version
- Update Xiphos patch
- Take ownership of share dir
- Add emptyvss.exe and sword.conf to installed files

* Sun Nov 23 2014 Greg Hellings <greg.hellings@gmail.com> 1.7.3-2
- Added some improved rendering through a patch to osisxhtml.cpp

* Tue May 06 2014 Greg Hellings <greg.hellings@gmail.com> 1.7.3-1
- Final upstream 1.7.3 release
- Removed Xiphos patch because of breakages

* Wed Apr 30 2014 Greg Hellings <greg.hellings@gmail.com> 1.7.3-0.1
- Upstream alpha2 release

* Mon Jan 13 2014 Greg Hellings <greg.hellings@gmail.com> 1.7.2-1
- New upstream release

* Tue Dec 31 2013 Greg Hellings <greg.hellings@gmail.com> 1.7.1-1
- New upstream release

* Sat Dec 14 2013 Greg Hellings <greg.hellings@gmail.com> 1.7.0-2
- New upstream release

* Wed Jul 17 2013 Greg Hellings <greg.hellings@gmail.com> 1.6.2+svn2908
- Update to latest upstream commits

* Sat Jan 26 2013 Greg Hellings <greg.hellings@gmail.com> 1.6.2+svn2778
- Updated to latest upstream commits

* Fri Nov 16 2012 Greg Hellings <greg.hellings@gmail.com> 1.6.2+sv2746
- New upstream release
- Add glib build dependency
- Remove pthread build dependency
- Added locales directory, pkg-config file, and application .exe files

* Tue Oct 23 2012 Greg Hellings <greg.hellings@gmail.com> 1.6.2+svn2741
- Initial package for MinGW.

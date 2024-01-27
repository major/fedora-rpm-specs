%?mingw_package_header

%global _pkg_name libgsf

Summary:	MinGW build of structured file editing library
Name:		mingw-%{_pkg_name}
Version:	1.14.48
Release:	7%{?dist}
License:	LGPLv2+
URL:		http://www.gnome.org/
Source:		http://ftp.gnome.org/pub/gnome/sources/libgsf/1.14/libgsf-%{version}.tar.xz

BuildArch:	noarch

BuildRequires: make
BuildRequires:	mingw32-zlib
BuildRequires:	mingw32-glib2
BuildRequires:	mingw32-libxml2
BuildRequires:	mingw32-gettext
BuildRequires:	mingw32-bzip2
BuildRequires:	mingw32-filesystem >= 95
BuildRequires:	mingw32-gcc
BuildRequires:	mingw32-gcc-c++
BuildRequires:	mingw32-binutils

BuildRequires:	mingw64-zlib
BuildRequires:	mingw64-glib2
BuildRequires:	mingw64-libxml2
BuildRequires:	mingw64-gettext
BuildRequires:	mingw64-bzip2
BuildRequires:	mingw64-filesystem >= 95
BuildRequires:	mingw64-gcc
BuildRequires:	mingw64-gcc-c++
BuildRequires:	mingw64-binutils

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	intltool
BuildRequires:	gtk-doc


%description
MinGW Windows port of the library for reading and writing structured files.


# Win32
%package -n mingw32-%{_pkg_name}
Summary:	%{summary}

%description -n mingw32-%{_pkg_name}
MinGW Windows port of the library for reading and writing structured files.

%package -n mingw32-%{_pkg_name}-static
Summary:	%{summary}
Requires:	mingw32-%{_pkg_name} = %{version}-%{release}

%description -n mingw32-%{_pkg_name}-static
Static version of the MinGW Windows libgsf library.

# Win64
%package -n mingw64-%{_pkg_name}
Summary:	%{summary}

%description -n mingw64-%{_pkg_name}
MinGW Windows port of the library for reading and writing structured files.

%package -n mingw64-%{_pkg_name}-static
Summary:	%{summary}
Requires:	mingw64-%{_pkg_name} = %{version}-%{release}

%description -n mingw64-%{_pkg_name}-static
Static version of the MinGW Windows libgsf library.


%{?mingw_debug_package}


%prep
%setup -q -n %{_pkg_name}-%{version}

autoreconf

%build
%mingw_configure --enable-static --enable-shared \
	--without-python --disable-gtk-doc
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

rm -r ${RPM_BUILD_ROOT}%{mingw32_mandir}/man1/
rm -r ${RPM_BUILD_ROOT}%{mingw64_mandir}/man1/

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%mingw_find_lang %{_pkg_name}

# Win32
%files -n mingw32-%{_pkg_name} -f mingw32-%{_pkg_name}.lang
%doc COPYING.LIB README ChangeLog
%{mingw32_bindir}/libgsf-1-114.dll
%{mingw32_bindir}/libgsf-win32-1-114.dll
%{mingw32_bindir}/gsf.exe
%{mingw32_bindir}/gsf-office-thumbnailer.exe
%{mingw32_bindir}/gsf-vba-dump.exe
%{mingw32_libdir}/libgsf-1.dll.a
%{mingw32_libdir}/libgsf-win32-1.dll.a
%{mingw32_libdir}/pkgconfig/libgsf-1.pc
%{mingw32_libdir}/pkgconfig/libgsf-win32-1.pc
%{mingw32_includedir}/libgsf-1/gsf
%{mingw32_includedir}/libgsf-1/gsf-win32
%{mingw32_datadir}/thumbnailers/gsf-office.thumbnailer

%files -n mingw32-%{_pkg_name}-static
%{mingw32_libdir}/libgsf-win32-1.a
%{mingw32_libdir}/libgsf-1.a

# Win64
%files -n mingw64-%{_pkg_name} -f mingw64-%{_pkg_name}.lang
%doc COPYING.LIB README ChangeLog
%{mingw64_bindir}/libgsf-1-114.dll
%{mingw64_bindir}/libgsf-win32-1-114.dll
%{mingw64_bindir}/gsf.exe
%{mingw64_bindir}/gsf-office-thumbnailer.exe
%{mingw64_bindir}/gsf-vba-dump.exe
%{mingw64_libdir}/libgsf-1.dll.a
%{mingw64_libdir}/libgsf-win32-1.dll.a
%{mingw64_libdir}/pkgconfig/libgsf-1.pc
%{mingw64_libdir}/pkgconfig/libgsf-win32-1.pc
%{mingw64_includedir}/libgsf-1/gsf
%{mingw64_includedir}/libgsf-1/gsf-win32
%{mingw64_datadir}/thumbnailers/gsf-office.thumbnailer

%files -n mingw64-%{_pkg_name}-static
%{mingw64_libdir}/libgsf-win32-1.a
%{mingw64_libdir}/libgsf-1.a


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.48-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.48-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.48-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.14.48-2
- Rebuild with mingw-gcc-12

* Fri Mar 18 2022 Greg Hellings <greg.hellings@gmail.com> - 1.14.48-1
- New upstream version 1.14.48
- Dropped export-symbols patch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.47-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.47-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:42:26 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.14.47-3
- Rebuild (mingw-gettext)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 22 2020 Greg Hellings <greg.hellings@gmail.com> - 1.14.47-1
- New upstream version 1.14.47

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.14.46-5
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.46-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 1.14.46-3
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Greg Hellings <greg.hellings@gmail.com> - 1.14.46-1
- New upstream version 1.14.46
- Drop included patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 23 2018 Greg Hellings <greg.hellings@gmail.com> - 1.14.44-1
- Upstream version 1.14.44
- Add patch for misplaced sys/stat.h header in MinGW

* Wed Jul 25 2018 Greg Hellings <greg.hellings@gmail.com> - 1.14.43-1
- Upstream version 1.14.43

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.42-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Greg Hellings <greg.hellings@gmail.com> - 1.14.42-1
- Upstream version 1.14.42

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 05 2017 Greg Hellings <greg.hellings@gmail.com> - 1.14.41-1
- New upstream version 1.14.41

* Tue Nov 01 2016 Greg Hellings <greg.hellings@gmail.com> - 1.14.40-1
- New upstream version 1.14.40

* Wed Jun 01 2016 Greg Hellings <greg.hellings@gmail.com> - 1.14.37-1
- New upstream version 1.14.37

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 01 2015 Greg Hellings <greg.hellings@gmail.com> - 1.14.34-1
- New upstream version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 11 2015 Greg Hellings <greg.hellings@gmail.com> - 1.14.31-1
- New upstream version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Greg Hellings <greg.hellings@gmail.com> - 1.14.30-1
- Updated to new upstream version

* Mon Jan 06 2014 Greg Hellings <greg.hellings@gmail.com> - 1.14.29-1
- Updated to new upstream version

* Tue Sep 03 2013 Greg Hellings <greg.hellings@gmail.com> - 1.14.28-1
- Updated to new upstream version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Greg Hellings <greg.hellings@gmail.com> - 1.14.27-1
- Updated to new upstream version

* Sun Jun 16 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.14.26-2
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Mon May 6 2013 Greg Hellings <greg.hellings@gmail.com> - 1.14.26-1
- Updated to new upstream version

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Greg Hellings <greg.hellings@gmail.com> - 1.14.25-1
- Updated to reflect better Fedora/MinGW packaging adherence
- Updated to new upstream version
- Migrated to mingw_find_lang instead of explicit file inclusion

* Thu Aug 23 2012 Greg Hellings <greg.hellings@gmail.com> - 1.14.23-1
- Initial import

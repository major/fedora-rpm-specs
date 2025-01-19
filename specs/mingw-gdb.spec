%{?mingw_package_header}

Name:           mingw-gdb
Version:        15.2
Release:        2%{?dist}
Summary:        MinGW Windows port of the GDB debugger

# Same License tag as the native gdb package has:
License:        GPL-3.0-or-later AND BSD-3-Clause AND FSFAP AND LGPL-2.1-or-later AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LicenseRef-Fedora-Public-Domain AND GFDL-1.3-or-later AND LGPL-2.0-or-later WITH GCC-exception-2.0 AND GPL-3.0-or-later WITH GCC-exception-3.1 AND GPL-2.0-or-later WITH GNU-compiler-exception
URL:            http://gnu.org/software/gdb/
Source0:        https://ftp.gnu.org/gnu/gdb/gdb-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  automake autoconf libtool
BuildRequires:  make
BuildRequires:  gcc

BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gmp
BuildRequires:  mingw32-mpfr
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gmp
BuildRequires:  mingw64-mpfr
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib

BuildRequires:  texinfo

Provides: bundled(libiberty)

%description
This is the MinGW Windows port of the GDB, the GNU debugger.


# Win32
%package -n mingw32-gdb
Summary:        MinGW Windows port of the GDB debugger
# Provide upgrade path for the gdb packages distributed at
# http://mingw-cross.sourceforge.net
Obsoletes:      mingw32-gdb-gdbserver < 6.8.50.20090302-2

%description -n mingw32-gdb
This is the MinGW Windows port of the GDB, the GNU debugger.

# Win64
%package -n mingw64-gdb
Summary:        MinGW Windows port of the GDB debugger

%description -n mingw64-gdb
This is the MinGW Windows port of the GDB, the GNU debugger.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n gdb-%{version}


%build
%mingw_configure
%mingw_make_build


%install
%mingw_make_install

# Remove bfd and opcodes libraries
rm -rf %{buildroot}%{mingw32_datadir}/locale/
rm -rf %{buildroot}%{mingw32_includedir}/
rm -rf %{buildroot}%{mingw32_libdir}/

rm -rf %{buildroot}%{mingw64_datadir}/locale/
rm -rf %{buildroot}%{mingw64_includedir}/
rm -rf %{buildroot}%{mingw64_libdir}/

# Remove documentation which is duplicate with native gdb package
rm -rf %{buildroot}%{mingw32_datadir}/info/
rm -rf %{buildroot}%{mingw32_mandir}/

rm -rf %{buildroot}%{mingw64_datadir}/info/
rm -rf %{buildroot}%{mingw64_mandir}/

# Remove unusefull gdb-add-index script
rm %{buildroot}%{mingw64_bindir}/gdb-add-index
rm %{buildroot}%{mingw32_bindir}/gdb-add-index


%files -n mingw32-gdb
%license COPYING3 COPYING COPYING.LIB
%{mingw32_bindir}/gdb.exe
%{mingw32_bindir}/gdbserver.exe
%{mingw32_datadir}/gdb/

%files -n mingw64-gdb
%license COPYING3 COPYING COPYING.LIB
%{mingw64_bindir}/gdb.exe
%{mingw64_bindir}/gdbserver.exe
%{mingw64_datadir}/gdb/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 15 2024 Sandro Mani <manisandro@gmail.com> - 15.2-1
- Update to 15.2

* Thu Aug 08 2024 Sandro Mani <manisandro@gmail.com> - 15.1-1
- Update to 15.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 08 2024 Sandro Mani <manisandro@gmail.com> - 14.2-1
- Update to 14.2

* Sun Feb 18 2024 Sandro Mani <manisandro@gmail.com> - 14.0.1-1
- Update to 14.0.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 30 2023 Sandro Mani <manisandro@gmail.com> - 13.2-1
- Update to 13.2

* Sun Mar 12 2023 Sandro Mani <manisandro@gmail.com> - 13.1-1
- Update to 13.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri May 20 2022 Sandro Mani <manisandro@gmail.com> - 12.1-1
- Update to 12.1

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 11.2-2
- Rebuild with mingw-gcc-12

* Thu Feb 10 2022 Sandro Mani <manisandro@gmail.com> - 11.2-1
- Update to 11.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Oct 18 2021 Sandro Mani <manisandro@gmail.com> - 11.1-1
- Update to 11.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Sandro Mani <manisandro@gmail.com> - 10.2-1
- Update to 10.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 19 2021 Sandro Mani <manisandro@gmail.com> - 10.1-1
- Update to 10.1

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 07:40:55 GMT 2020 Sandro Mani <manisandro@gmail.com> - 9.2-2
- Drop explicit -fstack-protector, it's in global ldflags now

* Sat Jun 20 2020 Sandro Mani <manisandro@gmail.com> - 9.2-1
- Update to 9.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 08 2019 Sandro Mani <manisandro@gmail.com> - 8.0-7
- Rebuild (Changes/Mingw32GccDwarf2)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 20 2017 Kalev Lember <klember@redhat.com> - 8.0-1
- Update to 8.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Oct 14 2016 Kalev Lember <klember@redhat.com> - 7.12-1
- Update to 7.12

* Tue Sep 27 2016 Kalev Lember <klember@redhat.com> - 7.11.1-1
- Update to 7.11.1
- Use license macro for COPYING files
- Don't set group tags

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 7.8.1-1
- Update to 7.8.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 07 2014 Kalev Lember <kalevlember@gmail.com> - 7.7-1
- Update to 7.7

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May  4 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 7.6-1
- Update to 7.6

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Kalev Lember <kalevlember@gmail.com> - 7.5.1-1
- Update to 7.5.1

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 7.5.0.20120926-1
- Update to 7.5.0.20120926

* Mon Oct 15 2012 Jon Ciesla <limburgher@gmail.com> - 7.5-2
- Provides: bundled(libiberty)

* Sun Sep  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 7.5-1
- Update to 7.5

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.4.50.20120603-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 7.4.50.20120603-1
- Update to 7.4.50 20120603 snapshot
- Applied patch from Jan Kratochvil to fix compile failure

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 7.4-1
- Update to 7.4
- Added win64 support
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 7.3-3
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 30 2011 Kalev Lember <kalevlember@gmail.com> - 7.3-1
- Update to 7.3
- Use automatic mingw dep extraction

* Wed Jul 06 2011 Erik van Pienbroek <epienbro@fedoraproject.org> - 7.2-3
- Rebuild against win-iconv

* Fri Jun 03 2011 Kalev Lember <kalev@smartlink.ee> - 7.2-2
- Renamed the source package to mingw-gdb (#702846)

* Mon Apr 25 2011 Kalev Lember <kalev@smartlink.ee> - 7.2-1
- Update to 7.2
- Removed documentation which is duplicate with the native gcc
- Don't install the bfd and opcodes libraries
- Provide upgrade path from the mingw32-gdb packages from mingw-cross.sf.net
- Include license files in the rpm

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 6.8-4
- Rebuild for mingw32-gcc 4.4

* Wed Sep 24 2008 Richard W.M. Jones <rjones@redhat.com> - 6.8-3
- Rename mingw -> mingw32.

* Fri Sep 12 2008 Richard W.M. Jones <rjones@redhat.com> - 6.8-2
- Initial RPM release.

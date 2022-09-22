%{?mingw_package_header}

Name:           mingw-gdbm
Version:        1.11
Release:        19%{?dist}
Summary:        MinGW port of GNU database routines

License:        GPLv3+
URL:            http://www.gnu.org/software/gdbm/
Source0:        ftp://ftp.gnu.org/gnu/gdbm/gdbm-%{version}.tar.gz

# Prevent gdbm from storing uninitialized memory content
# to database files.
# The change allows Valgrind users to debug their packages without
# dealing with gdbm-related noise. It also improves security, as
# the uninitialized memory might contain sensitive informations
# from other applications. The patch is taken from Debian.
# See https://bugzilla.redhat.com/show_bug.cgi?id=4457
# See http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=208927
Patch0:         gdbm-1.10-zeroheaders.patch
# Fix GCC10 FTBFS: multiple definition of parseopt_program_doc/parseopt_program_args
Patch1:         gdbm_gcc_10.patch

# Win32 compatibility
Patch1000:      gdbm-win32-support.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext

BuildRequires:  autoconf automake libtool
BuildRequires:  gettext-devel
BuildRequires:  texinfo


%description
Gdbm is a GNU database indexing library, including routines which use
extensible hashing.  Gdbm works in a similar way to standard UNIX dbm
routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

This is the MinGW Windows port of the libraries and development tools.


# Win32
%package -n mingw32-gdbm
Summary:        MinGW port of GNU database routines

%description -n mingw32-gdbm
Gdbm is a GNU database indexing library, including routines which use
extensible hashing.  Gdbm works in a similar way to standard UNIX dbm
routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

This is the MinGW Windows port of the libraries and development tools.

%package -n mingw32-gdbm-static
Summary:        Static version of the MinGW Windows GDBM library
Requires:       mingw32-gdbm = %{version}-%{release}

%description -n mingw32-gdbm-static
Static version of the MinGW Windows GDBM library.

# Win64
%package -n mingw64-gdbm
Summary:        MinGW port of GNU database routines

%description -n mingw64-gdbm
Gdbm is a GNU database indexing library, including routines which use
extensible hashing.  Gdbm works in a similar way to standard UNIX dbm
routines.  Gdbm is useful for developers who write C applications and
need access to a simple and efficient database or who are building C
applications which will use such a database.

This is the MinGW Windows port of the libraries and development tools.

%package -n mingw64-gdbm-static
Summary:        Static version of the MinGW Windows GDBM library
Requires:       mingw64-gdbm = %{version}-%{release}

%description -n mingw64-gdbm-static
Static version of the MinGW Windows GDBM library.


%?mingw_debug_package


%prep
%setup -q -n gdbm-%{version}
%patch0 -p1 -b .zeroheaders
%patch1 -p1 -b .gcc10

%patch1000 -p0 -b .windows

autoreconf --install --force


%build
%mingw_configure
%mingw_make %{?_smp_mflags} V=1


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Native Fedora package seems to fluff this, but as far as I
# can tell they are trying to create <gdbm/gdbm.h> which
# links to <gdbm.h>.
pushd $RPM_BUILD_ROOT%{mingw32_includedir}
mkdir gdbm
cd gdbm
ln -s ../gdbm.h
popd

pushd $RPM_BUILD_ROOT%{mingw64_includedir}
mkdir gdbm
cd gdbm
ln -s ../gdbm.h
popd

# Remove man page and info file which duplicate what is in native package.
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}
rm -r $RPM_BUILD_ROOT%{mingw32_infodir}
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}
rm -r $RPM_BUILD_ROOT%{mingw64_infodir}

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%mingw_find_lang gdbm


%files -n mingw32-gdbm -f mingw32-gdbm.lang
%{mingw32_bindir}/libgdbm-4.dll
%{mingw32_bindir}/gdbm_dump.exe
%{mingw32_bindir}/gdbm_load.exe
%{mingw32_bindir}/gdbmtool.exe
%{mingw32_includedir}/gdbm.h
%{mingw32_includedir}/gdbm/
%{mingw32_libdir}/libgdbm.dll.a

%files -n mingw32-gdbm-static
%{mingw32_libdir}/libgdbm.a

%files -n mingw64-gdbm -f mingw64-gdbm.lang
%{mingw64_bindir}/libgdbm-4.dll
%{mingw64_bindir}/gdbm_dump.exe
%{mingw64_bindir}/gdbm_load.exe
%{mingw64_bindir}/gdbmtool.exe
%{mingw64_includedir}/gdbm.h
%{mingw64_includedir}/gdbm/
%{mingw64_libdir}/libgdbm.dll.a

%files -n mingw64-gdbm-static
%{mingw64_libdir}/libgdbm.a


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 Sandro Mani <manisandro@gmail.com> - 1.11-18
- Rebuild with mingw-gcc-12

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 12 13:36:29 GMT 2020 Sandro Mani <manisandro@gmail.com> - 1.11-14
- Rebuild (mingw-gettext)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Sandro Mani <manisandro@gmail.com> - 1.11-11
- Rebuild (gettext)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan  1 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.11-1
- Update to 1.11

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10-2
- Added BR: texinfo

* Wed Nov 21 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.10-1
- Update to 1.10
- Upstream changed license to GPLv3+
- Ported the package to the new mingw packaging guidelines
- Added win64 support
- Added static subpackages

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.0-9
- Renamed the source package to mingw-gdbm (RHBZ #800874)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags
- Dropped all .la files

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.8.0-8
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-3
- Rebuild for mingw32-gcc 4.4

* Sat Jan 17 2009 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-2
- Update config.sub and config.guess.
- Patch to use libtool-2-style commands.

* Fri Oct  3 2008 Richard W.M. Jones <rjones@redhat.com> - 1.8.0-1
- Initial RPM release.

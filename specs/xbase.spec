Name:		xbase
Summary:	XBase compatible database library
Version:	4.3.0
Release:	%autorelease
License:	LGPL-3.0-or-later
URL:		http://linux.techass.com/projects/xdb/
Source0:	http://downloads.sourceforge.net/xdb/%{name}64-%{version}.tar.gz
Patch0:		xbase-4.3.0-fix-sover.patch
Patch1:		xbase-4.3.0-fix-parent-dir.patch
Patch2:		xbase-4.2.7-no-local-no-namespace.patch
Patch3:		xbase-4.2.7-fix-mandir.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	gcc-c++
BuildRequires:	libtool
BuildRequires:	make
Provides:	xbase64 = %{version}-%{release}

%description
XBase is an xbase (i.e. dBase, FoxPro, etc.) compatible C++ class library
originally by Gary Kunkel and others (see the AUTHORS file).

XBase is useful for accessing data in legacy dBase 3 and 4 database files as
well as a general light-weight database engine.  It includes support for
DBF (dBase version 3 and 4) data files, NDX and NTX indexes, and DBT
(dBase version 3 and 4).  It supports file and record locking under *nix
OS's.

%package devel
Summary:	XBase development libraries and headers
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	xbase64-devel = %{version}-%{release}

%description devel
Headers and libraries for compiling programs that use the XBase library.

%package utils
Summary:	XBase utilities / tools
License:	GPL-3.0-or-later
Provides:	xbase64-utils = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description utils
This package contains various utilities for working with X-Base files:
checkndx (check an NDX file), copydbf (copy a DBF file structure), deletall
(mark all records for deletion), dumphdr (print an X-Base file header),
dumprecs (dump records for an X-Base file), packdbf (pack a database file),
reindex (rebuild an index), undelall (undeletes all deleted records in a file),
zap (remove all records from a DBF file).

%prep
%autosetup -n %{name}64-%{version} -p1

chmod -x NEWS README docs/html/*

%build
%cmake -S build/linux64
%cmake_build

%install
%cmake_install

# Fix files for multilib
touch -r COPYING docs/html/*.html

pushd $RPM_BUILD_ROOT%{_libdir}
ln -s libxbase64.so.%{version} libxbase.so.%{version}
ln -s libxbase64.so.4 libxbase.so.4
ln -s libxbase64.so libxbase.so
popd

pushd $RPM_BUILD_ROOT%{_includedir}
ln -s Xbase64 xbase
popd

%check
export TZ=UTC
%ctest -j1

%files
%license COPYING
%doc NEWS README
%{_libdir}/libxbase*.so.*

%files devel
%doc docs/html
%{_includedir}/xbase*
%{_includedir}/Xbase64
%{_libdir}/libxbase*.so

%files utils
%{_bindir}/xb_cfg_check
%{_bindir}/xb_clearix
%{_bindir}/xb_copydbf
%{_bindir}/xb_dbfutil
%{_bindir}/xb_deletall
%{_bindir}/xb_dumpdbt
%{_bindir}/xb_dumprecs
%{_bindir}/xb_dumptag
%{_bindir}/xb_execsql
%{_bindir}/xb_import
%{_bindir}/xb_pack
%{_bindir}/xb_reindex
%{_bindir}/xb_tblinfo
%{_bindir}/xb_undelall
%{_mandir}/man1/xb_*.1*

%changelog
%autochangelog

Name:           log4cpp
Version:        1.1.3
Release:        %autorelease
Summary:        C++ logging library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://sourceforge.net/projects/log4cpp/
Source0:        http://downloads.sourceforge.net/log4cpp/%{name}-%{version}.tar.gz
# Fix errors when compiling with gcc >= 4.3
Patch0:         log4cpp-1.0-gcc43.patch
# Don't put build cflags in .pc
Patch1:         log4cpp-1.0-remove-pc-cflags.patch
# Install docs into DESTDIR
Patch2:         log4cpp-1.0-fix-doc-dest.patch
# Don't try to build snprintf.c
Patch3:         log4cpp-1.0-no-snprintf.patch
# Version is actually 1.1.3
Patch4:         log4cpp-version-1.1.3.patch
Patch5:         03_aclocal_automake.diff
Patch6:         log4cpp-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  automake, autoconf, libtool
BuildRequires: make

%description
A library of C++ classes for flexible logging to files, syslog, IDSA and
other destinations. It is modeled after the Log for Java library
(http://www.log4j.org), staying as close to their API as is reasonable.

%package devel
Summary:        Header files, libraries and development man pages  %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if 0%{?el4}%{?el5}
Requires:       pkgconfig
%endif

%description devel
This package contains the header files, static libraries and development
man pages for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary:        Development documentation for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description doc
This package contains the development documentation for %{name}.
If you like to documentation to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n log4cpp
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1 -b .no-snprintf
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
# Delete non-free (but freely distributable) file under Artistic 1.0
# just to be sure we're not using it.
rm -rf src/snprintf.c
#Convert line endings.
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/share/doc/log4cpp-%{version} rpmdocs
rm -f %{buildroot}%{_libdir}/*.a
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%{_libdir}/liblog4cpp.so.5*
%doc ChangeLog COPYING

%files devel
%{_bindir}/log4cpp-config
%{_includedir}/log4cpp/
%{_libdir}/liblog4cpp.so
%{_libdir}/pkgconfig/log4cpp.pc
%{_datadir}/aclocal/log4cpp.m4
%{_mandir}/man3/log4cpp*

%files doc
%doc rpmdocs/*

%changelog
%autochangelog

# License
# ===========
#
# The GNUstep libraries and library resources are covered under the GNU
# Lesser Public License.  This means you can use these libraries in any
# program (even non-free programs).

# GNUstep tools, test programs, and other files are covered under the
# GNU Public License.

Name: gnustep-base
Version: 1.31.0
Release: %autorelease
License: GPL-3.0-or-later AND LGPL-2.0-or-later
Summary: GNUstep Base library package
URL:     https://www.gnustep.org/
Source0: https://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz

# https://bugzilla.redhat.com/show_bug.cgi?id=1179297
Patch0: %{name}-use_system-wide_crypto-policies.patch

Patch1: %{name}-fix_GCC15.patch

Patch2: %{name}-fix_ending_tag_mismatch.patch

Patch3: %{name}-1.31.0-fix_s390x.patch

BuildRequires: gcc
BuildRequires: gcc-objc
BuildRequires: libffi-devel >= 3.0.9
BuildRequires: gnutls-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel
BuildRequires: pkgconfig
BuildRequires: gnustep-make >= 2.9.2
BuildRequires: avahi-compat-libdns_sd-devel
BuildRequires: gmp-devel
BuildRequires: texi2html texinfo-tex
BuildRequires: libicu-devel
BuildRequires: libcurl-devel
BuildRequires: texi2html

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: make

Conflicts: libFoundation

%description
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.


%package libs
Summary: GNUStep Base Libraries
Requires: gnustep-make%{?_isa} >= 2.9.2

%description libs
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.
This packages contains the run-time libraries for %{name}.


%package devel
Summary: Header of the GNUstep Base library packes
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files of the gnustep-base package.


%package doc
Summary: Documentation for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnustep-filesystem

%description doc
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.
This package contains the documentation for %{name}

%prep
%autosetup -N

%patch -P 0 -p1 -b .backup
%patch -P 1 -p1 -b .backup
%patch -P 2 -p1 -b .backup
%ifarch s390x
%patch -P 3 -p1 -b .backup
%endif

iconv -f iso-8859-1 -t utf-8 ChangeLog.2 -o ChangeLog.2.utf8
mv ChangeLog.2.utf8 ChangeLog.2

%build
ffi_include=$(pkg-config --cflags-only-I libffi | sed -e 's/^\-\I//')
export LDFLAGS="%{__global_ldflags}"
%gnustep_configure --disable-ffcall --with-ffi-include="$ffi_include"

%gnustep_make -n

%install
%gnustep_install -n

# Rename pl to pllist to fix naming conflict
mv ${RPM_BUILD_ROOT}%{_bindir}/pl ${RPM_BUILD_ROOT}%{_bindir}/pllist

rm -f Examples/.cvsignore
rm -f Examples/.gdbinit

# We need a modified GNUstep.conf, because the DTDs are install not
# on there real destination

sed -e "s|GNUSTEP_SYSTEM_LIBRARY=|GNUSTEP_SYSTEM_LIBRARY=$RPM_BUILD_ROOT|" \
    -e "s|GNUSTEP_SYSTEM_HEADERS=|GNUSTEP_SYSTEM_HEADERS=$RPM_BUILD_ROOT|" \
    %{_sysconfdir}/GNUstep/GNUstep.conf >GNUstep.conf

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
export GNUSTEP_CONFIG_FILE=$(pwd)/GNUstep.conf

%gnustep_makedoc
%gnustep_installdoc

%files
%{_bindir}/HTMLLinker
%{_bindir}/autogsdoc
%{_bindir}/cvtenc
%{_bindir}/classes
%{_bindir}/defaults
%{_bindir}/gdnc
%{_bindir}/gdomap
%{_bindir}/gspath
%{_bindir}/make_strings
%{_bindir}/pl2link
%{_bindir}/pldes
%{_bindir}/plget
%{_bindir}/pllist
%{_bindir}/plmerge
%{_bindir}/plparse
%{_bindir}/plser
%{_bindir}/plutil
%{_bindir}/sfparse
%{_bindir}/xmlparse
%{_mandir}/man1/*
%{_mandir}/man8/*
%{gnustep_dtddir}/

%files libs
%doc ANNOUNCE ChangeLog* NEWS README*
%license COPYING.LIB COPYINGv3
%{gnustep_libraries}/
%{_libdir}/libgnustep-base.so.1.31
%{_libdir}/libgnustep-base.so.%{version}
%dir %{_libdir}/GNUstep/Tools
%dir %{_libdir}/GNUstep/Tools/Resources
%dir %{_libdir}/GNUstep/Tools/Resources/autogsdoc
%{_libdir}/GNUstep/Tools/Resources/autogsdoc/default-styles.css

%files devel
%{_includedir}/Foundation/
%{_includedir}/CoreFoundation/
%{_includedir}/GNUstepBase/
%{_libdir}/libgnustep-base.so
%{_libdir}/pkgconfig/gnustep-base.pc
%{gnustep_additional}/base.make
%doc Examples

%files doc
%{_infodir}/*
%dir %{_datadir}/GNUstep/Documentation
%{_datadir}/GNUstep/Documentation/*

%changelog
%autochangelog

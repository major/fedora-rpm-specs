Summary:	Automated text file generator
Name:		autogen
Version:	5.18.16
Release:	%autorelease
# Some files are licensed under GPLv2+.
# We redistribute them under GPLv3+.
License:	GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND GPL-1.0-or-later AND (LGPL-3.0-or-later OR BSD-3-Clause) AND GFDL-1.2-or-later
URL:		http://www.gnu.org/software/autogen/
Source0:	ftp://ftp.gnu.org/gnu/autogen/rel%{version}/%{name}-%{version}.tar.xz

# Fix multilib conflicts
Patch0:		autogen-multilib.patch
# Fix gcc error on overlapping strings
Patch1:		autogen-overlap.patch
Patch2:		autogen-configure-c99.patch
# https://sourceforge.net/p/autogen/bugs/212/
Patch3:		autogen-fortify.patch

Requires:	%{name}-libopts%{?_isa} = %{version}-%{release}

BuildRequires:	gcc
BuildRequires:	guile22-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl(Carp)
BuildRequires:	perl(constant)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(lib)
BuildRequires:	perl(List::Util)
BuildRequires:	perl(strict)
BuildRequires:	perl(Text::ParseWords)
BuildRequires:	perl(warnings)
BuildRequires:	chrpath
BuildRequires:	sed
BuildRequires:	automake autoconf

%description
AutoGen is a tool designed to simplify the creation and maintenance of
programs that contain large amounts of repetitious text. It is especially
valuable in programs that have several blocks of text that must be kept
synchronised.

%package libopts
Summary:	Automated option processing library based on %{name}
# Although sources are dual licensed with BSD, some autogen generated files
# are only under LGPLv3+. We drop BSD to avoid multiple licensing scenario.
License:	LGPL-3.0-or-later

%description libopts
Libopts is very powerful command line option parser consisting of a set of
AutoGen templates and a run time library that nearly eliminates the hassle of
parsing and documenting command line options.

%package libopts-devel
Summary:	Development files for libopts
# Although sources are dual licensed with BSD, some autogen generated files
# are only under LGPLv3+. We drop BSD to avoid multiple licensing scenario.
License:	LGPL-3.0-or-later

Requires:	automake
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-libopts%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description libopts-devel
This package contains development files for libopts.

%prep
%autosetup -p1

# Disable failing test
sed -i 's|errors.test||' autoopts/test/Makefile.in

%build
# Static libraries are needed to run test-suite.
export CFLAGS="$RPM_OPT_FLAGS -Wno-implicit-fallthrough -Wno-format-overflow \
		-Wno-format-truncation"
autoreconf -fiv
%configure

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' ./libtool

make %{?_smp_mflags}

%check
make check

%install
make install INSTALL="%{__install} -p" DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -delete
find $RPM_BUILD_ROOT -type f -name "*.a" -delete

# Remove time stamps from generated devel man pages to avoid multilib conflicts
sed -i 's|\(It has been AutoGen-ed\).*.\(by AutoGen\)|\1 \2|' \
	$RPM_BUILD_ROOT%{_mandir}/man3/*.3

# Remove rpath.
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/{columns,getdefs,%{name},xml2ag}
chrpath --delete $RPM_BUILD_ROOT%{_libdir}/lib*.so.*

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%ldconfig_scriptlets libopts

%files
%doc AUTHORS
%doc ChangeLog
%doc COPYING
%doc NEWS
%doc README
%doc THANKS
%doc TODO
%doc pkg/libopts/COPYING.gplv3
%{_bindir}/columns
%{_bindir}/getdefs
%{_bindir}/%{name}
%{_bindir}/xml2ag
%{_infodir}/%{name}.info*.gz
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/columns.1.gz
%{_mandir}/man1/getdefs.1.gz
%{_mandir}/man1/xml2ag.1.gz
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*

%files libopts
%doc pkg/libopts/COPYING.mbsd
%doc pkg/libopts/COPYING.lgplv3
%{_libdir}/libopts.so.25*

%files libopts-devel
%{_bindir}/autoopts-config
%{_datadir}/aclocal/autoopts.m4
%{_libdir}/libopts.so
%{_libdir}/pkgconfig/autoopts.pc
%{_mandir}/man1/autoopts-config.1.gz
%{_mandir}/man3/*

%dir %{_includedir}/autoopts
%{_includedir}/autoopts/options.h
%{_includedir}/autoopts/usage-txt.h

%changelog
%autochangelog

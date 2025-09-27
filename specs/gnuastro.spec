Name: gnuastro
Version: 0.23
Release: %autorelease
Summary: GNU Astronomy Utilities

License: GPL-3.0-or-later AND FSFAP AND GFDL-1.3-or-later
# Config files are FSFAP
# Docs are GFDL-1.3-or-later
# Code is GPL-3.0-or-later
URL: https://www.gnu.org/software/gnuastro/
Source0: https://ftp.gnu.org/gnu/gnuastro/%{name}-%{version}.tar.gz
Source1: https://ftp.gnu.org/gnu/gnuastro/%{name}-%{version}.tar.gz.sig
Source2: https://akhlaghi.org/public-pgp-key.txt
# https://savannah.gnu.org/bugs/?67289
Patch0: gnuastro-dont-override-cflags.patch
# https://savannah.gnu.org/bugs/?67289
Patch1: gnuastro-skip-test.patch
# https://savannah.gnu.org/bugs/?67232
Patch2: gnuastro-i686.patch

ExcludeArch: %{ix86}

BuildRequires: gpgverify

BuildRequires: gcc
#
BuildRequires: gsl-devel
BuildRequires: cfitsio-devel
BuildRequires: wcslib-devel
BuildRequires: make-devel
BuildRequires: gnulib-devel
#
BuildRequires: ghostscript
BuildRequires: libtool
BuildRequires: libjpeg-devel
BuildRequires: libtiff-devel 
BuildRequires: libgit2-devel
BuildRequires: lzip  
BuildRequires: curl 

BuildRequires: desktop-file-utils

Provides: bundled(gnulib)

%description
GNU Astronomy Utilities (Gnuastro) is an official GNU package consisting 
of various programs and library functions for the manipulation and 
analysis of astronomical data. All the programs share the same basic 
command-line user interface for the comfort of both the users and developers. 

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
License: GFDL-1.3-or-later
Summary: Documentation files for %{name}
BuildArch: noarch

%description doc
This %{name}-doc package contains the full documentation for %{name}.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
export CPATH="/usr/include/cfitsio"
%configure --disable-static --disable-rpath
%make_build

%install
export CPATH="/usr/include/cfitsio"
%make_install 
test -f %{buildroot}/%{_infodir}/dir && rm %{buildroot}/%{_infodir}/dir

%check
desktop-file-validate %{buildroot}/%{_datadir}/%{name}/astscript-fits-view.desktop

export CPATH="/usr/include/cfitsio"
make check

%ldconfig_scriptlets

%files
%doc README NEWS THANKS
%license COPYING COPYING.FDL
%{_libdir}/libgnuastro.so.21*
%{_libdir}/libgnuastro_make.so.21*
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/ast*.conf
%config(noreplace) %{_sysconfdir}/%{name}/gnuastro.conf
%{_bindir}/astarithmetic
%{_bindir}/astbuildprog
%{_bindir}/astconvertt
%{_bindir}/astconvolve
%{_bindir}/astcosmiccal
%{_bindir}/astcrop
%{_bindir}/astfits
%{_bindir}/astmatch
%{_bindir}/astmkcatalog
%{_bindir}/astmkprof
%{_bindir}/astnoisechisel
%{_bindir}/astquery
%{_bindir}/astscript-color-faint-gray
%{_bindir}/astscript-ds9-region
%{_bindir}/astscript-fits-view
%{_bindir}/astscript-pointing-simulate
%{_bindir}/astscript-psf-scale-factor
%{_bindir}/astscript-psf-select-stars
%{_bindir}/astscript-psf-stamp
%{_bindir}/astscript-psf-subtract
%{_bindir}/astscript-psf-unite
%{_bindir}/astscript-radial-profile
%{_bindir}/astscript-sort-by-night
%{_bindir}/astscript-zeropoint
%{_bindir}/astsegment
%{_bindir}/aststatistics
%{_bindir}/asttable
%{_bindir}/astwarp
%{_datadir}/%{name}/
%{_mandir}/man1/ast*.1.*

%files devel
%{_libdir}/libgnuastro.so
%{_libdir}/libgnuastro_make.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/gnuastro.pc

%files doc
%license COPYING.FDL
%{_infodir}/gnuastro.info.*
%{_infodir}/gnuastro.info-*.gz
%{_infodir}/gnuastro-figures/

%changelog
%autochangelog

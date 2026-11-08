Name:		psftools
Version:	1.0.14
Release:	%autorelease
Summary:	Conversion tools for .PSF fonts

License:	GPL-2.0-or-later
URL:		https://www.seasip.info/Unix/PSF/
Source0:	https://www.seasip.info/Unix/PSF/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

%description
The PSFTOOLS are designed to manipulate fixed-width bitmap fonts, such as DOS
or Linux console fonts. Both the PSF1 (8 pixels wide) and PSF2 (any width)
formats are supported; the default output format is PSF2.

%package devel
Summary: Development files for %{name}
Requires: gcc
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains the libpsf static library and the header
files needed to develop programs that use %{name}.

%prep
%autosetup

%build
# libpsf is a static internal library; shared library not useful to consumers
%configure --disable-shared
%make_build

%install
%make_install

%files
%license COPYING
%doc NEWS AUTHORS
%doc doc/*.txt
%{_bindir}/ams2psf
%{_bindir}/bbc2psf
%{_bindir}/cpi2psf
%{_bindir}/cpicomp
%{_bindir}/cpidcomp
%{_bindir}/fnt2psf
%{_bindir}/fon2fnts
%{_bindir}/fnts2fon
%{_bindir}/mda2psf
%{_bindir}/page2cp2
%{_bindir}/psf2ams
%{_bindir}/psf2bdf
%{_bindir}/psf2bbc
%{_bindir}/psf2bsd
%{_bindir}/psf2fnt
%{_bindir}/psf2inc
%{_bindir}/psf2pbms
%{_bindir}/psf2raw
%{_bindir}/psf2txt
%{_bindir}/psf2wof
%{_bindir}/psf2wyse
%{_bindir}/psf2xbm
%{_bindir}/psf2zx
%{_bindir}/psfjoin
%{_bindir}/psfmerge
%{_bindir}/psfpages
%{_bindir}/psfs2cpi
%{_bindir}/psfs2mda
%{_bindir}/psfxform
%{_bindir}/raw2psf
%{_bindir}/txt2psf
%{_bindir}/wof2psf
%{_bindir}/wyse2psf
%{_bindir}/zx2psf
%{_mandir}/man1/ams2psf.1*
%{_mandir}/man1/cpi2psf.1*
%{_mandir}/man1/cpicomp.1*
%{_mandir}/man1/cpidcomp.1*
%{_mandir}/man1/fnt2psf.1*
%{_mandir}/man1/fnts2fon.1*
%{_mandir}/man1/fon2fnts.1*
%{_mandir}/man1/mda2psf.1*
%{_mandir}/man1/psf2ams.1*
%{_mandir}/man1/psf2bdf.1*
%{_mandir}/man1/psf2bsd.1*
%{_mandir}/man1/psf2fnt.1*
%{_mandir}/man1/psf2inc.1*
%{_mandir}/man1/psf2pbms.1*
%{_mandir}/man1/psf2raw.1*
%{_mandir}/man1/psf2txt.1*
%{_mandir}/man1/psf2wof.1*
%{_mandir}/man1/psf2wyse.1*
%{_mandir}/man1/psf2xbm.1*
%{_mandir}/man1/psf2zx.1*
%{_mandir}/man1/psfjoin.1*
%{_mandir}/man1/psfmerge.1*
%{_mandir}/man1/psfpages.1*
%{_mandir}/man1/psfs2cpi.1*
%{_mandir}/man1/psfs2mda.1*
%{_mandir}/man1/psfxform.1*
%{_mandir}/man1/raw2psf.1*
%{_mandir}/man1/txt2psf.1*
%{_mandir}/man1/wof2psf.1*
%{_mandir}/man1/wyse2psf.1*
%{_mandir}/man1/zx2psf.1*

%files devel
%{_includedir}/psflib.h
%{_includedir}/psfutils.h
%{_libdir}/libpsf.a

%changelog
%autochangelog

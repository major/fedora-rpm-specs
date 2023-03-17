%global _hardened_build 1

%global upstream_version 2.0b4

# don't build libppd-tools until CUPS 3.x drops them
%bcond_with tools

Name:           libppd
Epoch:          1
Version:        2.0~b4
Release:        2%{?dist}
Summary:        Library for retro-fitting legacy printer drivers

# the CUPS exception text is the same as LLVM exception, so using that name with
# agreement from legal team
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/message/A7GFSD6M3GYGSI32L2FC5KB22DUAEQI3/
License:        Apache-2.0 WITH LLVM-exception
URL:            https://github.com/OpenPrinting/libppd
Source0:        %{URL}/releases/download/%{upstream_version}/%{name}-%{upstream_version}.tar.gz


# Patches
# https://github.com/OpenPrinting/libppd/pull/15
Patch0001: 0001-ppd-filter.c-Generate-media-col-if-media-col-default.patch


# for autogen.sh
BuildRequires: autoconf
# for autogen.sh
BuildRequires: automake
# mostly written in C
BuildRequires: gcc
# PPD compiler support written in C++
BuildRequires: gcc-c++
# for autogen.sh
BuildRequires: gettext-devel
# ghostscript is needed during build due configure check
BuildRequires: ghostscript >= 10.0.0
# for autosetup
BuildRequires: git-core
# for autogen.sh
BuildRequires: libtool
# uses make
BuildRequires: make
# for pkg-config in SPEC file and in configure
BuildRequires: pkgconf-pkg-config
# for CUPS API functions
BuildRequires: pkgconfig(cups) >= 2.2.2
# for filter functions
BuildRequires: pkgconfig(libcupsfilters) >= 2.0b3
# for rastertops
BuildRequires: pkgconfig(zlib)
# pdftops has to be in buildroot due configure check
BuildRequires: poppler-utils

%if %{without tools}
# libppd exports symbols for compiling PPD compilers, which needs charset
# definitions and header files during runtime to generate a PPD file - those
# are provided by cups right now - once cups drops them, require libppd-tools
Requires: cups
%else
Requires: %{name}-tools%{?_isa} = %{epoch}:%{version}-%{release}
%endif

# needded for hybrid pdftops filter function - for all legacy printers
# except for Brother and Minolta/Konica Minolta, which firmware bugs
# doesn't work with pdftops from GS
Requires: ghostscript >= 10.0.0
# needed for hybrid pdftops filter function - for Brother and Minolta/
# Konica Minolta printers
Requires: poppler-utils


%description
Libppd provides all PPD related function/API which is going
to be removed from CUPS 3.X, but are still required for retro-fitting
support of legacy printers. The library is meant only for retro-fitting
printer applications, any new printer drivers have to be written as
native printer application without libppd.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       cups-devel
Requires:       libcupsfilters-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing retro-fitting printer applications.

%if %{with tools}
%package tools
Summary: PPD compiler tools and definition files
Requires: %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description tools
The package contains PPD compiler and definition files needed for generating
PPD files from *.drv files.
%endif

%prep
%autosetup -n %{name}-%{upstream_version} -S git


%build
# generate configuration/compilation files
./autogen.sh

# disable PPD compiler tools for now (until CUPS 3.x drops PPD support) to prevent
# conflicts with cups 2.x package
%configure\
  --disable-acroread\
  --disable-mutool\
  --disable-rpath\
  --disable-silent-rules\
  --disable-static\
%if %{with tools}
  --enable-ppdc-utils\
%else
  --disable-ppdc-utils\
%endif
  --with-pdftops=hybrid

# fix rpmlint error about linking to libraries, but not actually using their functions
# it happens when the required libraries uses pkgconfig - pkgconfig file doesn't know
# which specific functions our binary calls, so it tells us to link against every
# possibilities
# https://fedoraproject.org/wiki/Common_Rpmlint_issues#unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%check
make check


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# remove the license files from doc dir, since we ship them in /usr/share/licenses
rm -f %{buildroot}%{_pkgdocdir}/{LICENSE,NOTICE,COPYING}

# remove INSTALL since it is unnecessary
rm -f %{buildroot}%{_pkgdocdir}/INSTALL

# 1.x was the release were all cups-filters components were together
# let only libcupsfilters to carry it
rm -f %{buildroot}%{_pkgdocdir}/CHANGES-1.x.md

# charsets and header files needed for PPD compilation in runtime
# are for now shipped by cups - libppd will ship them once cups
# drops them
%if %{without tools}
rm -rf %{buildroot}%{_datadir}/ppdc
%endif

%{?ldconfig_scriptlets}


%files
%license LICENSE NOTICE COPYING
%doc ABOUT-NLS AUTHORS CHANGES.md README.md
%{_libdir}/libppd.so.2*

%files devel
%{_docdir}/%{name}/CONTRIBUTING.md
%{_docdir}/%{name}/DEVELOPING.md
%dir %{_includedir}/ppd
%{_includedir}/ppd/ppd-filter.h
%{_includedir}/ppd/ppdc.h
%{_includedir}/ppd/ppd.h
%{_libdir}/libppd.so
%{_libdir}/pkgconfig/libppd.pc

%if %{with tools}
%files tools
%{_bindir}/ppdc
%{_bindir}/ppdhtml
%{_bindir}/ppdi
%{_bindir}/ppdmerge
%{_bindir}/ppdpo
%dir %{_datadir}/ppdc/
%{_datadir}/ppdc/epson.h
%{_datadir}/ppdc/font.defs
%{_datadir}/ppdc/hp.h
%{_datadir}/ppdc/label.h
%{_datadir}/ppdc/media.defs
%{_datadir}/ppdc/raster.defs
%endif

%changelog
* Wed Mar 15 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1:2.0~b4-2
- fix printing images to Postscript printers

* Wed Mar 01 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1:2.0~b4-1
- 2.0b4
- introduce Epoch because I didn't read FPG carefully...

* Mon Feb 20 2023 Zdenek Dohnal <zdohnal@redhat.com> - 2.0b3-4
- rebuilt with required cups

* Thu Feb 16 2023 Zdenek Dohnal <zdohnal@redhat.com> - 2.0b3-3
- don't use bootstrap for now - koji doesn't seem to see it...

* Thu Feb 16 2023 Zdenek Dohnal <zdohnal@redhat.com> - 2.0b3-2
- bootstrap cups to prevent conflicts for now

* Wed Feb 01 2023 Zdenek Dohnal <zdohnal@redhat.com> - 2.0b3-1
- Initial import

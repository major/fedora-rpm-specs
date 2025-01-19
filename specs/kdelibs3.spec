# kdelibs3 review: http://bugzilla.redhat.com/248899

%define _default_patch_fuzz 2

%define arts_ev 8:1.5.10
%define qt3 qt3
%define qt3_version 3.3.8b
%define qt3_ev %{?qt3_epoch}%{qt3_version} 
%define qt3_docdir %{_docdir}/qt-devel-%{qt3_version}

%define kde_major_version 3

%define apidocs 0

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Summary: KDE 3 Libraries
Name:    kdelibs3
Version: 3.5.10
Release: 131%{?dist}

License: LGPL-2.0-only
Url: http://www.kde.org/

Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdelibs-%{version}.tar.bz2
Source3: devices.protocol

Patch1: kdelibs-3.5.1-xdg-menu.patch
Patch2: kdelibs-3.0.0-ndebug.patch
Patch4: kdelibs-3.0.4-ksyscoca.patch
Patch5: kdelibs-3.5.10-openssl.patch
Patch15: kdelibs-3.4.91-buildroot.patch
Patch32: kdelibs-3.2.3-cups.patch
Patch33: kdelibs-3.3.2-ppc.patch
Patch34: kdelibs-3.4.0-qtdoc.patch
Patch35: kdelibs-3.4.92-inttype.patch
Patch37: kdelibs-3.5.2-kdebug-kmail-quiet.patch
Patch38: kdelibs-3.5.2-cupsdconf2-group.patch
Patch39: kdelibs-3.5.4-kabc-make.patch
Patch40: kdelibs-3.5.4-kdeprint-utf8.patch
Patch41: kdelibs-3.5.6-utempter.patch
Patch43: kdelibs-3.5.6-lang.patch
Patch45: kdelibs-3.5.7-autostart.patch
Patch46: kdelibs-3.5.8-kate-vhdl.patch
Patch48: kdelibs-3.5.8-kspell-hunspell.patch
Patch49: kdelibs-3.5.8-kspell2-enchant.patch
Patch50: kdelibs-3.5.8-kspell2-no-ispell.patch
Patch51: kdelibs-3.5.9-cupsserverbin.patch
# initial support for (Only|Not)ShowIn=KDE3
Patch52: kdelibs-3.5.9-KDE3.patch
# use newer/plasma drkonqi in KCrash (#453243)
Patch53: kdelibs-3.5.10-drkonqi-plasma5.patch
# use inotify_* functions which are defined in glibc-header
Patch54: kdelibs-3.5.10-inotify.patch
# update the KatePart latex.xml syntax definition to the version from Kile 2.0.3
Patch55: kdelibs-3.5.10-latex-syntax-kile-2.0.3.patch
# fix ftbfs (#631195)
Patch56: kdelibs-3.5.10-qcolor_gcc_ftbfs.patch
# fix FTBFS (cups-util.c must include stdio.h, #714133)
Patch57: kdelibs-3.5.10-cups-util-missing-header.patch
# fix FTBFS with CUPS 2.0 due to bad CUPS_VERSION_MAJOR checks
Patch58: kdelibs-3.5.10-cups20.patch
Patch59: kdelibs-3.5.10-gcc6.patch
# fix endless loop in svgicon
Patch60: kdelibs-3.5.10-svgicon-endlessloop.patch
# fix FTBFS with gcc7
Patch61: kdelibs-3.5.10-gcc7.patch

# libidn2 support for > f26
Patch62:  kdelibs-3-libidn2.patch

# use /etc/kde in addition to /usr/share/config, borrowed from debian
Patch100: kdelibs-3.5.5-kstandarddirs.patch
# http://bugs.kde.org/93359, alternative to export libltdl_cv_shlibext=".so" hack.
Patch101: kde-3.5-libtool-shlibext.patch
# kget ignores simultaneous download limit (kde #101956)
Patch103: kdelibs-3.5.0-101956.patch
Patch104: kdelibs-3.5.10-gcc44.patch
Patch105: kdelibs-3.5.10-ossl-1.x.patch
Patch106: kdelibs-3.5.10-kio.patch
Patch107: kdelibs-3.5.10-assert.patch
Patch108: kdelibs-3.5.10-dtoa.patch
Patch109: kdelibs-3.5.10-kabc.patch
# kde4.4 backport
Patch111: kdelibs-3.5.10-kde-config_kde-version.patch
# ftbfs
Patch112: kdelibs-3.5.10-dup-ftbfs.patch

## Trinity backports
# build fix for CUPS 1.6 by Timothy Pearson, backported by Kevin Kofler
# http://git.trinitydesktop.org/cgit/tdelibs/commit?id=9bc0d2cd9d38750658770e69bf0445dc5162beb7
# http://git.trinitydesktop.org/cgit/tdelibs/commit?id=91bf63b43bf4cc9ff640bd3c11549644cef05e6e
Patch150: kdelibs-3.5.10-cups16.patch
# build fix for CUPS 2.2 by Slávek Banko, backported by Kevin Kofler
# http://git.trinitydesktop.org/cgit/tdelibs/commit/?id=52a1b55368ec53b14347996851aca7eb29374397
Patch151: kdelibs-3.5.10-cups22.patch
# OpenSSL 1.1 support by Slávek Banko (with prerequisite patch by Timothy
# Pearson), backported by Kevin Kofler
# http://git.trinitydesktop.org/cgit/tdelibs/commit/?id=e757d3d6ae93cf967d54c566e9c003b0f9cc3a9c
# http://git.trinitydesktop.org/cgit/tdelibs/commit/?id=e1861cb6811f7bac405ece204407ca46c000a453
Patch152: kdelibs-3.5.10-openssl-1.1.patch
# native support for xdg-user-dirs, without shelling out to xdg-user-dir from
# the config file (by Timothy Pearson), needed after the CVE-2019-14744 fix,
# backported by Kevin Kofler
# http://mirror.git.trinitydesktop.org/cgit/tdelibs/commit/kdecore/kglobalsettings.cpp?id=865f314dd5ed55508f45a32973b709b79a541e36
# http://mirror.git.trinitydesktop.org/cgit/tdelibs/commit/?id=ae5384b4bdea0c9ab28322bb53183bef569c77c5
Patch153: kdelibs-3.5.10-kglobalsettings-xdg-user-dirs.patch
# fix accidental double-free in KJS garbage collector, by Timothy Pearson
# backported by Wolfgang Bauer from OpenSUSE
# http://mirror.git.trinitydesktop.org/cgit/tdelibs/commit/?id=36a7df39b0f89c467fc6d9c957a7a30f20d96994
# https://bugs.trinitydesktop.org/show_bug.cgi?id=2116
Patch154: kdelibs-3.5.10-fix-accidental-double-free-in-kjs-garbage-collector.patch
# Process the new (libice 1.0.10) location of the ICEauthority file (#1768193)
# patch by Slávek Banko, backported by Kevin Kofler
# http://mirror.git.trinitydesktop.org/cgit/tdelibs/commit/?id=38b2b0be7840d868c21093a406ab98a646212de1
# https://bugs.trinitydesktop.org/show_bug.cgi?id=3027
Patch155: kdelibs-3.5.10-libice-1.0.10.patch

## security fixes
# fix CVE-2009-2537 - select length DoS
Patch200: kdelibs-3.5.10-cve-2009-2537-select-length.patch
# fix CVE-2009-1725 - crash, possible ACE in numeric character references
Patch201: kdelibs-3.5.10-cve-2009-1725.patch
# fix CVE-2009-1690 - crash, possible ACE in KHTML (<head> use-after-free)
Patch202: kdelibs-3.5.4-CVE-2009-1687.patch
# fix CVE-2009-1687 - possible ACE in KJS (FIXME: still crashes?)
Patch203: kdelibs-3.5.4-CVE-2009-1690.patch
# fix CVE-2009-1698 - crash, possible ACE in CSS style attribute handling
Patch204: kdelibs-3.5.10-cve-2009-1698.patch
# fix CVE-2009-2702 - ssl incorrect verification of SSL certificate with NUL in subjectAltName
Patch205: kdelibs-3.5.10-CVE-2009-2702.patch
# fix oCERT-2009-015 - unrestricted XMLHttpRequest access to local URLs
Patch206: kdelibs-3.5.10-oCERT-2009-015-xmlhttprequest.patch
# CVE-2009-3736, libltdl may load and execute code from a library in the current directory
Patch207: libltdl-CVE-2009-3736.patch
# CVE-2011-3365, input validation failure in KSSL
Patch208: kdelibs-3.5.x-CVE-2011-3365.patch
# CVE-2013-2074, prints passwords contained in HTTP URLs in error messages
Patch209: kdelibs-3.5.10-CVE-2013-2074.patch
# CVE-2015-7543 arts,kdelibs3: Use of mktemp(3) allows attacker to hijack the IPC
# backport upstream fix (the lnusertemp.c change) from kdelibs 4:
# http://commits.kde.org/kdelibs/cc5515ed7ce8884c9b18169158ba29ab2f7a3db7
# upstream fix by Joseph Wenninger, rediffed for kdelibs 3.5.10 by Kevin Kofler
Patch210: kdelibs-3.5.10-CVE-2015-7543.patch
# CVE-2016-6232 - directory traversal vulnerability in KArchive
# patch from Trinity (Slávek Banko), based on KF5 fix (Andreas Cord-Landwehr)
Patch211: kdelibs-3.5.10-CVE-2016-6232.patch
# CVE-2017-6410 - info leak when accessing https when using a malicious PAC file
# backport upstream fix (by Albert Astals Cid) from kdelibs 4:
# http://commits.kde.org/kdelibs/1804c2fde7bf4e432c6cf5bb8cce5701c7010559
Patch212: kdelibs-3.5.10-CVE-2017-6410.patch
# CVE-2019-14744 - kconfig: malicious .desktop files (and others) would execute code
# backport upstream fix (by David Faure, backported to kdelibs 4 by Kai Uwe
# Broulik) from kdelibs 4 (backported by Kevin Kofler):
# http://commits.kde.org/kdelibs/2c3762feddf7e66cf6b64d9058f625a715694a00
Patch213: kdelibs-3.5.10-CVE-2019-14744.patch

## fixes to common KDE 3 autotools machinery
# tweak autoconfigury so that it builds with autoconf 2.64 or 2.65
Patch300: kde3-acinclude.patch
# remove flawed and obsolete automake version check in admin/cvs.sh
Patch301: kde3-automake-version.patch
# fix build failure with automake 1.13: add the --add-missing --copy flags
# also add --force-missing to get aarch64 support (#925029/#925627)
Patch302: kde3-automake-add-missing.patch
# fix aarch64 FTBFS due to libtool not liking the file output on *.so files
Patch303: kde3-libtool-aarch64.patch
# Fix configure bits compromised by LTO optimizations
Patch304: kdelibs-3.5.10-configure.patch
# autoconf 2.7x
Patch305: kde3-autoconf-version.patch
Patch306: kdelibs3-c99.patch
# Fix compilation with libxml2 2.12.0
Patch307: kdelibs-3.5.10-libxml2-2_12_0.patch
Patch308: kdelibs3-c99-2.patch
# tweak autoconfigury so that it builds with autoconf 2.72
# https://src.fedoraproject.org/rpms/kdebase3/c/91233a5b909d09775930236bd21556faa993176f?branch=rawhide
Patch309: kde3-autoconf-2.72.patch

Requires: ca-certificates
Requires: hicolor-icon-theme
Requires: kde-settings >= 3.5
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
Requires: kde3-filesystem
%else
Requires: kde-filesystem
%endif
Requires: kdelibs-common
Requires: redhat-menus
Requires: shadow-utils
#Requires: sudo
BuildRequires: sudo

%if 0%{?fedora}
%define libkdnssd libkdnssd
%endif
BuildRequires: xorg-x11-proto-devel libX11-devel
%define _with_rgbfile --with-rgbfile=%{_datadir}/X11/rgb.txt
Requires: iceauth

Requires(pre): coreutils
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires: hunspell

BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: pcre-devel
BuildRequires: cups-devel cups
BuildRequires: %{qt3}-devel %{qt3}-devel-docs
BuildRequires: arts-devel >= %{arts_ev}
BuildRequires: flex >= 2.5.4a-13
BuildRequires: doxygen
BuildRequires: libxslt-devel
BuildRequires: sgml-common
BuildRequires: openjade
BuildRequires: jadetex
BuildRequires: docbook-dtd31-sgml
BuildRequires: docbook-style-dsssl
BuildRequires: perl-generators
BuildRequires: perl-SGMLSpm
BuildRequires: docbook-utils
BuildRequires: zlib-devel
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
BuildRequires: libidn2-devel
%else
BuildRequires: libidn-devel
%endif
BuildRequires: audiofile-devel
BuildRequires: openssl-devel
BuildRequires: perl-interpreter
BuildRequires: gawk
BuildRequires: byacc
BuildRequires: libart_lgpl-devel
BuildRequires: bzip2-devel
BuildRequires: libtiff-devel
BuildRequires: libacl-devel libattr-devel
BuildRequires: enchant-devel
BuildRequires: krb5-devel
BuildRequires: openldap-devel
BuildRequires: alsa-lib-devel
%if 0%{?fedora} > 25 || 0%{?rhel} > 7
BuildRequires: pkgconf-pkg-config
%else
BuildRequires: pkgconfig
%endif
BuildRequires: glibc-kernheaders
BuildRequires: libutempter-devel
BuildRequires: findutils
BuildRequires: jasper-devel
BuildRequires: OpenEXR-devel
BuildRequires: automake libtool
BuildRequires: chrpath
BuildRequires: make

%if "%{name}" != "kdelibs" && "%{?apidocs}" != "1"
Obsoletes: kdelibs-apidocs < 6:%{version}-%{release}
%endif

Provides: crystalsvg-icon-theme = 1:%{version}-%{release}
Obsoletes: crystalsvg-icon-theme < 1:%{version}-%{release}


%description
Libraries for KDE 3:
KDE Libraries included: kdecore (KDE core library), kdeui (user interface),
kfm (file manager), khtmlw (HTML widget), kio (Input/Output, networking),
kspell (spelling checker), jscript (javascript), kab (addressbook),
kimgio (image manipulation).

%package devel
Summary: Header files and documentation for compiling KDE 3 applications.
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{qt3}-devel
Requires: openssl-devel
Requires: arts-devel
Requires: gcc-c++
%{?libkdnssd:Requires: libkdnssd-devel}
%description devel
This package includes the header files you will need to compile
applications for KDE 3.

%package apidocs
Summary: KDE 3 API documentation.
Requires: kde-filesystem
BuildArch: noarch
%description apidocs
This package includes the KDE 3 API documentation in HTML
format for easy browsing

%package tools
Summary: KDE 3 tools.
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description tools
This package includes tools kgrantpty and kpac_dhcp_helper.

%prep
%setup -q -n kdelibs-%{version}

%patch -P1 -p1 -b .xdg-menu
%patch -P2 -p1 -b .debug
%patch -P4 -p1 -b .ksyscoca
%patch -P5 -p1 -b .openssl
%patch -P15 -p1 -b .buildroot
%patch -P32 -p1 -b .cups
%patch -P33 -p1 -b .ppc
%patch -P34 -p1 -b .qtdoc
%patch -P35 -p1 -b .inttype
%patch -P37 -p1 -b .kdebug-kmail-quiet
%patch -P38 -p1 -b .cupsdconf2-group
%patch -P39 -p1 -b .kabc-make
%patch -P40 -p1 -b .kdeprint-utf8
%patch -P41 -p1 -b .utempter
%patch -P43 -p1 -b .lang
%patch -P45 -p1 -b .xdg-autostart
%patch -P46 -p1 -b .kate-vhdl
%patch -P48 -p1 -b .kspell
%patch -P49 -p1 -b .kspell2
%patch -P50 -p1 -b .no-ispell
%patch -P51 -p1 -b .cupsserverbin
%patch -P52 -p1 -b .KDE3
%patch -P53 -p1 -b .drkonqi-plasma5
%patch -P54 -p1 -b .inotify
%patch -P55 -p1 -b .latex-syntax
%patch -P56 -p1 -b .qcolor_gcc_ftbfs
%patch -P57 -p1 -b .cups-util
%patch -P58 -p1 -b .cups20
%patch -P59 -p1 -b .gcc6
%patch -P60 -p1 -b .endless-loop
%patch -P61 -p1 -b .gcc7
%if 0%{?fedora} > 26 || 0%{?rhel} > 7
%patch -P62 -p1 -b .libidn2
%endif
%patch -P100 -p1 -b .kstandarddirs
%patch -P101 -p1 -b .libtool-shlibext
%patch -P104 -p1 -b .gcc44
%patch -P105 -p1 -b .ossl-1.x
%patch -P106 -p1 -b .kio
%patch -P107 -p1 -b .assert
%patch -P108 -p1 -b .alias
%patch -P109 -p1 -b .kabc
%patch -P111 -p1 -b .kde-config_kde-version
%patch -P112 -p1 -b .dup

%patch -P150 -p1 -b .cups16
%patch -P151 -p1 -b .cups22
%patch -P155 -p1 -b .libice-1.0.10

# security fixes
%patch -P200 -p1 -b .cve-2009-2537
%patch -P201 -p0 -b .cve-2009-1725
%patch -P202 -p1 -b .cve-2009-1687
%patch -P203 -p1 -b .cve-2009-1690
%patch -P204 -p1 -b .cve-2009-1698
%patch -P205 -p1 -b .cve-2009-2702
%patch -P206 -p0 -b .oCERT-2009-015-xmlhttprequest
%patch -P207 -p1 -b .CVE-2009-3736
%patch -P208 -p1 -b .CVE-2011-3365
%patch -P209 -p1 -b .CVE-2013-2074
%patch -P210 -p1 -b .CVE-2015-7543
%patch -P211 -p1 -b .CVE-2016-6232
%patch -P212 -p1 -b .CVE-2017-6410
%patch -P213 -p1 -b .CVE-2019-14744

# must be applied after the ossl-1.x patch (105) and the CVE-2009-2702 fix (205)
%patch -P152 -p1 -b .openssl-1.1
# goes along with the CVE-2019-14744 fix (ordering not strictly required)
%patch -P153 -p1 -b .xdg-user-dirs
# must be applied after the CVE-2009-1687 fix
%patch -P154 -p1 -b .kjs-double-free

%patch -P300 -p1 -b .acinclude
%patch -P301 -p1 -b .automake-version
%patch -P302 -p1 -b .automake-add-missing
%patch -P303 -p1 -b .libtool-aarch64
%patch -P304 -p1 -b .configure
%patch -P305 -p1 -b .autoconf2.7x
%patch -P306 -p1
%patch -P307 -p1 -b .libxml2_2_12_0
%patch -P 308 -p1
%patch -P 309 -p1

make -f admin/Makefile.common cvs


%build
unset QTDIR && . /etc/profile.d/qt.sh

export QTDOC=%{qt3_docdir}

if [ -x /etc/profile.d/krb5.sh ]; then
  . /etc/profile.d/krb5.sh
elif ! echo ${PATH} | grep -q /usr/kerberos/bin ; then
  export PATH=/usr/kerberos/bin:${PATH}
fi

%if "%{name}" != "kdelibs"
export DO_NOT_COMPILE="libkscreensaver"
%endif

# drop the extra -Werror= flags for C, they break the configure script
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags} -Wno-deprecated-declarations -Wno-narrowing -std=gnu++98"

%configure \
   --includedir=%{_includedir}/kde \
   --disable-rpath \
   --disable-new-ldflags \
   --disable-debug --disable-warnings \
   --disable-final \
   --disable-fast-malloc \
%if "%{_lib}" == "lib64"
  --enable-libsuffix="64" \
%endif
   --enable-cups \
   --enable-mitshm \
   --enable-pie \
   --enable-sendfile \
   --with-distribution="$(cat /etc/redhat-release 2>/dev/null)" \
   --with-alsa \
   --without-aspell \
   --without-hspell \
   --disable-libfam \
   --enable-dnotify \
   --enable-inotify \
   --with-utempter \
   %{?_with_rgbfile} \
   --with-jasper \
   --with-openexr \
   --with-xinerama

# kill rpath harder, inspired by https://fedoraproject.org/wiki/Packaging:Guidelines?rd=Packaging/Guidelines#Removing_Rpath
# other more standard variants didnt work or caused other problems
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' libtool

%if 0%{?apidocs}
  doxygen -s -u admin/Doxyfile.global
  %make_build apidox
%endif

# https://koji.fedoraproject.org/koji/taskinfo?taskID=82799269
# agent.cpp:21:10: warning: addressee.h is shorter than expected
# disable parallel make for now
%make_build -j1


%install
%make_install

# create/own, see http://bugzilla.redhat.com/483318
mkdir -p %{buildroot}%{_libdir}/kconf_update_bin

chmod a+x %{buildroot}%{_libdir}/*
install -p -m 644 %{SOURCE3} %{buildroot}%{_datadir}/services/devices.protocol

%if 0%{?apidocs}
pushd %{buildroot}%{_docdir}
ln -sf HTML/en/kdelibs-apidocs %{name}-devel-%{kde_major_version}
popd
%endif

# Make symlinks relative
pushd %{buildroot}%{_docdir}/HTML/en
for i in *; do
   if [ -d $i -a -L $i/common ]; then
      rm -f $i/common
      ln -sf ../common $i
   fi
done
popd

# Use hicolor-icon-theme rpm/pkg instead (#178319)
rm -rf $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/

# ghost'd files
touch $RPM_BUILD_ROOT%{_datadir}/services/ksycoca

# remove references to extraneous/optional libraries in .la files (#170602)
# fam, libart_lgpl, pcre, libidn, libpng, libjpeg, libdns_sd, libacl/libattr, alsa-lib/asound
find $RPM_BUILD_ROOT%{_libdir} -name "*.la" | xargs \
 sed -i \
 -e "s@-lfam@@g" \
 -e "s@%{_libdir}/libfam.la@@g" \
 -e "s@-lart_lgpl_2@@g" \
 -e "s@%{_libdir}/libpcreposix.la@@g" \
 -e "s@-lpcreposix@@g" \
 -e "s@-lpcre@@g" \
 -e "s@-lidn2\?@@g" \
 -e "s@%{_libdir}/libidn2\?.la@@g" \
 -e "s@-lpng@@g" \
 -e "s@-ljpeg@@g" \
 -e "s@%{_libdir}/libjpeg.la@@g" \
 -e "s@-ldns_sd@@g" \
 -e "s@-lacl@@g" \
 -e "s@%{_libdir}/libacl.la@@g" \
 -e "s@/%{_lib}/libacl.la@@g" \
 -e "s@-lattr@@g" \
 -e "s@%{_libdir}/libattr.la@@g" \
 -e "s@/%{_lib}/libattr.la@@g" \
 -e "s@-lasound@@g"  \
 -e "s@-lutempter@@g"

# libkdnssd bits
rm -f %{buildroot}%{_libdir}/libkdnssd.la
%{?libkdnssd:rm -rf %{buildroot}{%{_libdir}/libkdnssd.*,%{_includedir}/kde/dnssd}}

# remove conflicts with kdelibs-4
rm -f %{buildroot}%{_bindir}/checkXML
rm -fv %{buildroot}%{_bindir}/kmailservice
rm -fv %{buildroot}%{_bindir}/ksvgtopng
rm -fv %{buildroot}%{_bindir}/ktelnetservice
rm -f %{buildroot}%{_bindir}/kunittestmodrunner
rm -f %{buildroot}%{_datadir}/config/kdebug.areas
rm -f %{buildroot}%{_datadir}/config/kdebugrc
rm -f %{buildroot}%{_datadir}/config/ui/ui_standards.rc
rm -f %{buildroot}%{_docdir}/HTML/en/common/1.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/10.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/2.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/3.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/4.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/5.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/6.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/7.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/8.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/9.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/artistic-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-left.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-middle.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bottom-right.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/bsd-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/doxygen.css
rm -f %{buildroot}%{_docdir}/HTML/en/common/favicon.ico
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/fdl-notice.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/footer.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/gpl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/gpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/header.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/kde-default.css
rm -f %{buildroot}%{_docdir}/HTML/en/common/kde_logo_bg.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/lgpl-license
rm -f %{buildroot}%{_docdir}/HTML/en/common/lgpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/mainfooter.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/mainheader.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/qpl-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-left.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-middle.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-right-konqueror.png
rm -f %{buildroot}%{_docdir}/HTML/en/common/top-right.jpg
rm -f %{buildroot}%{_docdir}/HTML/en/common/x11-license.html
rm -f %{buildroot}%{_docdir}/HTML/en/common/xml.dcl
rm -rf %{buildroot}%{_datadir}/locale/all_languages
rm -rf %{buildroot}%{_sysconfdir}/xdg/menus/
rm -rf %{buildroot}%{_datadir}/autostart/
rm -f %{buildroot}%{_datadir}/config/colors/40.colors
rm -f %{buildroot}%{_datadir}/config/colors/Rainbow.colors
rm -f %{buildroot}%{_datadir}/config/colors/Royal.colors
rm -f %{buildroot}%{_datadir}/config/colors/Web.colors
rm -f %{buildroot}%{_datadir}/config/ksslcalist
rm -f %{buildroot}%{_bindir}/preparetips
# remove conflicts with kate-4.9.80+
rm -fv %{buildroot}%{_datadir}/config/katesyntaxhighlightingrc

# fix file conflict with leptonica-tools (#2156905)
mv -f %{buildroot}%{_bindir}/imagetops %{buildroot}%{_bindir}/imagetops-kde3
sed -i -e 's!exec:/imagetops!exec:/imagetops-kde3!g' %{buildroot}%{_datadir}/apps/kdeprint/filters/imagetops.desktop
sed -i -e 's/imagetops /imagetops-kde3 /g' %{buildroot}%{_datadir}/apps/kdeprint/filters/imagetops.xml

# don't show kresources
sed -i -e "s,^OnlyShowIn=KDE;,OnlyShowIn=KDE3;," %{buildroot}%{_datadir}/applications/kde/kresources.desktop 

# use ca-certificates' ca-bundle.crt, symlink as what most other
# distros do these days (http://bugzilla.redhat.com/521902)
if [  -f %{buildroot}%{_datadir}/apps/kssl/ca-bundle.crt -a \
      -f /etc/pki/tls/certs/ca-bundle.crt ]; then
  ln -sf /etc/pki/tls/certs/ca-bundle.crt \
         %{buildroot}%{_datadir}/apps/kssl/ca-bundle.crt
fi


%check
ERROR=0
# verify rpath, or lack thereof
if [ ! -z "$(chrpath --list %{buildroot}%{_bindir}/kioexec 2>/dev/null | grep RPATH=)" ]; then
  echo "ERROR: the end is neigh, rpath has returned!"
  ERROR=1
fi
%if 0%{?apidocs}
if [ ! -f %{buildroot}%{_docdir}/HTML/en/kdelibs-apidocs/index.html ]; then
  echo "ERROR: %{_docdir}/HTML/en/kdelibs-apidocs/index.html not generated"
  ERROR=1
fi 
%endif
exit $ERROR


%if 0%{?fedora} > 25
%ldconfig_scriptlets

%filetriggerin -- %{_datadir}/icons/crystalsvg
touch %{_datadir}/icons/crystalsvg &> /dev/null || :

%transfiletriggerin -- %{_datadir}/icons/crystalsvg
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/crystalsvg
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &>/dev/null || :

%else
# classic scriptlets
%post
%{?ldconfig}
touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &> /dev/null || :

%postun
%{?ldconfig}
if [ $1 -eq 0 ] ; then
touch --no-create %{_datadir}/icons/crystalsvg &> /dev/null || :
gtk-update-icon-cache %{_datadir}/icons/crystalsvg &> /dev/null || :
fi
%endif


%files
%doc README
%license COPYING.LIB
%{_bindir}/artsmessage
%{_bindir}/cupsdconf
%{_bindir}/cupsdoprint
%{_bindir}/make_driver_db_cups
%{_bindir}/dcop
%{_bindir}/dcopclient
%{_bindir}/dcopfind
%{_bindir}/dcopobject
%{_bindir}/dcopquit
%{_bindir}/dcopref
%{_bindir}/dcopserver
%{_bindir}/dcopserver_shutdown
%{_bindir}/dcopstart
%{_bindir}/filesharelist
%{_bindir}/fileshareset
%{_bindir}/imagetops-kde3
%{_bindir}/kab2kabc
%{_bindir}/kaddprinterwizard
%{_bindir}/kbuildsycoca
%{_bindir}/kcmshell
%{_bindir}/kconf_update
%{_bindir}/kcookiejar
%{_bindir}/kde-config
%{_bindir}/kde-menu
%{_bindir}/kded
%{_bindir}/kdeinit
%{_bindir}/kdeinit_shutdown
%{_bindir}/kdeinit_wrapper
%{_bindir}/kdesu_stub
%{_bindir}/kdontchangethehostname
%{_bindir}/kdostartupconfig
%{_bindir}/kfile
%{_bindir}/kfmexec
%{_bindir}/khotnewstuff
%{_bindir}/kinstalltheme
%{_bindir}/kio_http_cache_cleaner
%{_bindir}/kio_uiserver
%{_bindir}/kioexec
%{_bindir}/kioslave
%{_bindir}/klauncher
%{_bindir}/ksendbugmail
%{_bindir}/kshell
%{_bindir}/kstartupconfig
%{_bindir}/ktradertest
%{_bindir}/kwrapper
%{_bindir}/lnusertemp
%{_bindir}/make_driver_db_lpr
%{_bindir}/meinproc
%{_bindir}/start_kdeinit
%{_bindir}/start_kdeinit_wrapper
%{_libdir}/lib*.so.*
%{_libdir}/libkdeinit_*.so
%{_libdir}/lib*.la
%{_libdir}/kconf_update_bin/
%{_libdir}/kde3/
%{_datadir}/applications/kde/*.desktop
%{_datadir}/apps/*
%exclude %{_datadir}/apps/ksgmltools2/
%config(noreplace) %{_datadir}/config/*
%{_datadir}/emoticons/*
%{_datadir}/icons/default.kde
%{_datadir}/mimelnk/magic
%{_datadir}/mimelnk/*/*.desktop
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%ghost %{_datadir}/services/ksycoca
%{_docdir}/HTML/en/kspell
%{_docdir}/HTML/en/common/*
# split out someday? -- rex
%{_datadir}/icons/crystalsvg/

%files devel
%{_bindir}/dcopidl*
%{_bindir}/kconfig_compiler
%{_bindir}/makekdewidgets
%{_datadir}/apps/ksgmltools2/
%{_includedir}/kde/
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%exclude %{_libdir}/libkdeinit_*.so

%if 0%{?apidocs}
%files apidocs
%{_docdir}/%{name}-devel-%{kde_major_version}
%{_docdir}/HTML/en/kdelibs*
%endif

%files tools
%attr(4755,root,root) %{_bindir}/kgrantpty
%attr(4755,root,root) %{_bindir}/kpac_dhcp_helper

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-131
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-130
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Apr 24 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 3.5.10-129
- Patch for autoconf 2.72 (fix RHBZ#2276884)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-128
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-127
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Florian Weimer <fweimer@redhat.com> - 3.5.10-126
- C compatibility fixes for CUPS support

* Tue Nov 28 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.51.10-125
- Fix build with libxml2 2.12.0

* Tue Nov 28 2023 Orion Poplawski <orion@nwra.com> - 3.5.10-124
- Rebuild for jasper 4.1

* Thu Sep 14 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 3.5.10-123
- Update filesystem dependency

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-122
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 21 2023 Than Ngo <than@redhat.com> - 3.5.10-121
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-120
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-119
- Fix file conflict with leptonica-tools (#2156905)

* Tue Dec 13 2022 Florian Weimer <fweimer@redhat.com> - 3.5.10-118
- Port to C99

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-117
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Feb 14 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.5.10-116
- Disable parallel make for now (build failed on ppc64le)

* Sun Feb 13 2022 Josef Ridky <jridky@redhat.com> - 3.5.10-115
- Rebuilt for libjasper.so.6

* Mon Jan 24 2022 Timm Bäder <tbaeder@redhat.com> - 3.5.10-114
- Disable automatic .la file removal
- https://fedoraproject.org/wiki/Changes/RemoveLaFiles

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-113
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Than Ngo <than@redhat.com> - 3.5.10-112
- Fixed bz#1999506, FTBFS with autoconf-2.7x

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-111
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-110
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 01 2021 Richard Shaw <hobbes1069@gmail.com> - 3.5.10-109
- Rebuild for OpenEXR 2.5.3.

* Tue Sep 15 2020 Than Ngo <than@redhat.com> - 3.5.10-108
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-107
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-106
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 18 2020 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-105
- Process the new (libice 1.0.10) location of the ICEauthority file (#1768193)

* Wed May 13 2020 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-104
- Remove obsolete BuildRequires: db4-devel

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-103
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Jeff Law <law@redhat.com> - 3.5.10-102
- Fix configure tests compromised by LTO

* Sat Aug 10 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-101
- Backport CVE-2019-14744 fix by David Faure and Kai Uwe Broulik from kdelibs 4
- Backport native xdg-user-dirs support by Timothy Pearson from Trinity (needed
  to fix the regression that would otherwise result from the above security fix)
- Backport KJS double-free fix by Timothy Pearson (backport by wbauer/OpenSUSE)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-100
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Richard Shaw <hobbes1069@gmail.com> - 3.5.10-99
- Rebuild for OpenEXR 2.3.0.

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-98
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-97
- Rebuild for the new hardcoded qt3 build key in Rawhide
- Fix aarch64 FTBFS due to libtool not liking the file output on *.so files

* Fri Jul 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-96
- BR: gcc-c++
- -devel: Requires: gcc-c++ (avoid churn in legacy kde3 pkgs)
- use %%make_build %%make_install %%ldconfig_scriptlets %%license
- update scriptlets (icon triggers)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-95
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.5.10-94
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-93
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.5.10-92
- Rebuilt for switch to libxcrypt

* Sat Jan 06 2018 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-91
- Build against OpenSSL 1.1, patch from Trinity, backported by Kevin Kofler

* Thu Dec 28 2017 Yaakov Selkowitz <yselkowi@redhat.com> - 3.5.10-90
- Fix loading of latest compat-openssl10 (#1529417)
- Use ca-certificates' ca-bundle.crt (#521902)

* Tue Aug 08 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-89
- fix libidn dependency removal from .la files (#1479146)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-88
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Than Ngo <than@redhat.com> - 3.5.10-86
- fix build with libidn2

* Wed May 10 2017 Than Ngo <than@redhat.com> - 3.5.10-85
- add support libidn2 for f27

* Sat Mar 04 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-84
- backport fix for CVE-2017-6410 from kdelibs 4 (itself backported from KF5)

* Mon Feb 27 2017 Than Ngo <than@redhat.com> - 3.5.10-83
- devel requires compat-openssl10-devel, fix kdebase3 FTBS

* Tue Feb 21 2017 Hans de Goede <hdegoede@redhat.com> - 3.5.10-82
- Fix gcc7 FTBFS (rhbz#1423808)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-80
- backport fix for CVE-2016-6232 from Trinity (itself backported from KF5)

* Sun Jan 22 2017 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-79
- use DrKonqi from Plasma 5 rather than from kde-runtime 4
- build against compat-openssl10 for now (F26+)
- BuildRequires: pkgconf-pkg-config instead of pkgconfig on F26+

* Sat Dec 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-78
- rebuild (jasper)
- drop the extra -Werror= flags for C, they break the configure script

* Wed Sep 28 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-77
- backport CUPS 2.2 build fix from Trinity / Slávek Banko

* Wed Sep 28 2016 Than Ngo <than@redhat.com> - 3.5.10-76
- fix bz#1376181, fix endless loop in svgicons

* Mon Jun 27 2016 Than Ngo <than@redhat.com> - 3.5.10-75
- move kpac_dhcp_helper, kpac_dhcp_helper into separate subpackage

* Tue Feb 16 2016 Than Ngo <than@redhat.com> - 3.5.10-74
- fix bz#1307685, FTBFS in rawhide 

* Sun Feb 14 2016 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-73
- Add -std=gnu++98 to the CXXFLAGS to fix FTBFS (#1307685)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.10-72
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-71
- Backport CVE-2015-7543 fix (Joseph Wenninger) from kdelibs 4 (#1289235)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-70
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-69
- drop hard Requires: sudo (kdesu can use it, but it's not default)

* Mon May 04 2015 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-68
- rebuild against qt3 with fixed build key (#1218091)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.5.10-67
- Rebuilt for GCC 5 C++11 ABI change

* Sun Apr 05 2015 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-66
- rebuild (gcc5)

* Tue Nov 25 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.10-65
- fix FTBFS with CUPS 2.0 due to bad CUPS_VERSION_MAJOR checks

* Tue Nov 25 2014 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-64
- rebuild (openexr)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-63
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-62
- kill rpath harder

* Tue Jul 22 2014 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-61
- drop bootstrap

* Wed Jul 02 2014 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-60.1.bootstrap
- bootstrap ppc64le

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-60
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Dec 01 2013 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-59
- trim %%changelog

* Sat Nov 30 2013 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-58
- --disable-new-ldflags, fix FTBFS on rawhide

* Wed Nov 27 2013 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-57
- rebuild (openexr)

* Sun Sep 08 2013 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-56
- rebuild (ilmbase/openexr)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 3.5.10-54
- Perl 5.18 rebuild

* Sat May 18 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-53
- fix CVE-2013-2074 (passwords in HTTP URLs in error messages, #962001)

* Mon Apr 01 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-52
- use automake --force-missing to get aarch64 support (#925029/#925627)
- also use automake --copy (the default is symlinking)

* Sun Mar 10 2013 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-51
- rebuild (OpenEXR)

* Sat Mar 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-50
- drop branding hack which breaks kde-config --kde-version

* Sat Mar 09 2013 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-49
- unify KDE 3 autotools fixes between packages

* Thu Mar 07 2013 Than Ngo <than@redhat.com> - 3.5.10-48
- fix build failture

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.5.10-46
- rebuild due to "jpeg8-ABI" feature drop

* Tue Dec 25 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.10-45
- drop CUPS conditionals, CUPS support must always be built
- backport CUPS 1.6 build fixes from Trinity / Timothy Pearson

* Fri Dec 21 2012 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-44
- disable cups support on f19+ (for now, needs lots 'o love)

* Fri Dec 21 2012 Adam Tkac <atkac redhat com> - 3.5.10-43
- rebuild against new libjpeg

* Thu Dec 20 2012 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-42
- omit ktelnetservice (in favor of kdelibs4's copy)

* Thu Dec 06 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.10-41
- omit cupsdconf (F19+), FTBFS with the latest CUPS and not worth fixing

* Tue Dec 04 2012 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-40
- kate has a file conflict with kdelibs3 (#883529)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jul 12 2012 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-38
- omit kmailservice (in favor of kdelibs4's copy (#773414)

* Mon Jun 11 2012 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-37
- rebuild for fixed GCC (#830618)
- remove flawed and obsolete automake version check in admin/cvs.sh

* Tue May 08 2012 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-36
- rebuild (libtiff)

* Wed Apr 04 2012 Than Ngo <than@redhat.com> - 3.5.10-35
- drop apidocs

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 3.5.10-34
- Rebuild against PCRE 8.30

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 3.5.10-32
- Rebuild for new libpng

* Thu Oct 13 2011 Than Ngo <than@redhat.com> - 3.5.10-31
- Resolves: bz#743074, CVE-2011-3365, input validation failure in KSSL

* Fri Jun 17 2011 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-30
- fix FTBFS (cups-util.c must include stdio.h, #714133)

* Thu Jun 16 2011 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-29
- rebuild

* Wed May 11 2011 Than Ngo <than@redhat.com> - 3.5.10-28
- use inotify_* functions which are defined in glibc-header 

* Tue Mar 15 2011 Than Ngo <than@redhat.com> - 3.5.10-27
- drop requiresflag hint, which isn't supported in new rpm

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 18 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-25
- FTBFS kdelibs3-3.5.10-24.fc14 (#631195)

* Thu Jun 10 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-24
- drop old Obsoletes/Provides: kdelibs(-devel/-apidocs)
- -apidocs: Requires: kde-filesystem

* Wed Jan 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-23
- patch for kde-config --kde-version option (kde#224540)

* Wed Dec 16 2009 Jaroslav Reznik <jreznik@redhat.com> - 3.5.10-22
- Repositioning the KDE Brand (#547361)

* Mon Dec 07 2009 Than Ngo <than@redhat.com> - 3.5.10-21
- fix security issues in libltdl bundle within kdelibs CVE-2009-3736
- backport upstream patches
- patch autoconfigury to build with autoconf >= 2.64 (Stepan Kasal)

* Mon Nov  2 2009 Lukáš Tinkl <ltinkl@redhat.com> - 3.5.10-20
- fix unrestricted XMLHttpRequest access to local URLs (oCERT-2009-015), #532428

* Mon Sep 28 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-19
- Conflicts with kde-settings (#526109)

* Mon Sep 28 2009 Than Ngo <than@redhat.com> - 3.5.10-18
- rhel cleanup

* Wed Sep 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-17 
- move /etc/profile.d/kde.(sh|csh) to kde-settings (F-12+)

* Fri Sep 04 2009 Than Ngo <than@redhat.com> - 3.5.10-16
- openssl-1.0 build fixes

* Fri Sep 04 2009 Than Ngo <than@redhat.com> - 3.5.10-15
- fix for CVE-2009-2702

* Thu Sep 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-14
- kde.(sh|csh): drop KDE_IS_PRELINKED (workaround bug #515539)

* Sun Jul 26 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.10-13
- fix CVE-2009-2537 - select length DoS
- fix CVE-2009-1725 - crash, possible ACE in numeric character references
- fix CVE-2009-1690 - crash, possible ACE in KHTML (<head> use-after-free)
- fix CVE-2009-1687 - possible ACE in KJS (FIXME: still crashes?)
- fix CVE-2009-1698 - crash, possible ACE in CSS style attribute handling

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-12 
- FTBFS kdelibs3-3.5.10-11.fc11 (#511571)
- -devel: Requires: %%{name}%%_isa ...

* Sun Apr 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-11
- update openssl patch (for 0.9.8k)

* Thu Apr 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-10
- move designer plugins to runtime (#487622)
- make -apidocs noarch

* Mon Mar 02 2009 Than Ngo <than@redhat.com> - 3.5.10-9
- enable -apidocs

* Fri Feb 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 3.5.10-8
- disable -apidocs (f11+, #487719)
- cleanup unused kdeui_symlink hack baggage

* Wed Feb 25 2009 Than Ngo <than@redhat.com> - 3.5.10-7
- fix files conflicts with 4.2.x
- fix build issue with gcc-4.4

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 6:3.5.10-5
- unowned dirs (#483318)

* Sat Jan 10 2009 Ville Skyttä <ville.skytta at iki.fi> - 6:3.5.10-4
- Slight speedup to profile.d/kde.sh (#465370).

* Mon Dec 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.10-3
- update the KatePart latex.xml syntax definition to the version from Kile 2.0.3

* Thu Dec 04 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-2
- omit libkscreensaver (F9+)

* Tue Aug 26 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.10-1
- kde-3.5.10

* Fri Aug 22 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-18
- fix build against Rawhide kernel headers (fix flock and flock64 redefinition)

* Fri Aug 22 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-17
- fix logic error in OnlyShowIn=KDE3 patch

* Wed Jul 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-16
- f9+: use drkonqi from KDE 4 kdebase-runtime in KCrash (#453243)

* Wed Jun 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.9-15
- set include_crystalsvg to 1 everywhere
- use Epoch 1 for crystalsvg-icon-theme, add Obsoletes

* Tue Jun 03 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-14
- revert kdeui symlink hack (there be dragons) 
- unbreak -apidocs, add %%check so this never ever happens again

* Sat May 24 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-13
- f9+: include kdeui symlink here + scriptlets to help rpm handle it

* Fri May 23 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-12
- f9+: omit %%{_datadir}/apps/kdeui, use version from kdelibs-common (rh#447965, kde#157850)

* Thu May 15 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-11
- (Only|Not)ShowIn=KDE3 patch (helps #446466)

* Thu May 15 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-10
- fix kresources.desktop: NoDisplay=true

* Mon Apr 14 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-8
- omit Requires: kdndsd-avahi (#441222)

* Wed Apr 02 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-7
- more qt->qt3 fixes

* Tue Mar 25 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-6
- s/qt-devel/qt3-devel/

* Mon Mar 10 2008 Than Ngo <than@redhat.com> 3.5.9-5
- apply upstream patch to fix regression in kate (bz#436384)

* Tue Mar 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-4
- hardcode qt_ver again because 3.3.8b reports itself as 3.3.8 (fixes apidocs)

* Tue Feb 26 2008 Lukáš Tinkl <ltinkl@redhat.com> - 3.5.9-3
- #230979: Writes ServerBin into cupsd.conf
- #416101: unable to print after configuring printing in KDE

* Sat Feb 16 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.9-2
- F9+: include %%{_docdir}/HTML/en/common files which are not in kdelibs-common

* Thu Feb 14 2008 Rex Dieter <rdieter@fedoraproject.org> 3.5.9-1
- kde-3.5.9

* Mon Feb 11 2008 Than Ngo <than@redhat.com> 3.5.8-24
- make kresources hidden on f9+

* Sat Feb 09 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-23
- rebuild for GCC 4.3

* Sat Dec 22 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.8-22
- BR enchant-devel instead of aspell-devel on F9+ (FeatureDictionary)
- Requires: hunspell on F9+ (FeatureDictionary)
- patch KSpell for hunspell support on F9+ (FeatureDictionary)
- add and build enchant backend for KSpell2 (backported from Sonnet) on F9+
  (FeatureDictionary)
- don't build aspell and ispell backends for KSpell2 on F9+ (FeatureDictionary)

* Fri Dec 21 2007 Lukáš Tinkl <ltinkl@redhat.com> - 3.5.8-21
- updated Flash patch

* Mon Dec 17 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.5.8-20
- Requires: kdelibs-common (F9+) (#417251)

* Thu Dec 13 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-19
- flash fix (#410651, kde#132138, kde#146784)
- simplify crystalsvg-icon-theme handling

* Tue Dec 11 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-18
- set include_crystalsvg to 0 on F9+ (it comes from kdeartwork now)

* Tue Dec 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-17
- update openssl patch

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-16
- install profile scripts as 644 instead of 755 (Ville Skyttä, #407521)
- don't rename profile scripts to kde3.(c)sh (not worth the breakage)

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-15
- separate include_crystalsvg conditional, set to 1 until we have kdeartwork 4
- don't run icon %%post/%%postun snippets for crystalsvg if we don't ship it
- add "3" in all summaries and descriptions

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-14
- fix inverted logic for Requires: crystalsvg-icon-theme

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> - 3.5.8-13
- don't hardcode %%fedora

* Wed Nov 21 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.5.8-12
- renew the list of file conflicts and removals

* Tue Nov 20 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.5.8-11
- preserve makekdewidgets and kconf_compiler for fedora > 9
- add Requires: crystalsvg-icon-theme (for kdelibs3)

* Sun Nov 18 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.5.8-10
- only include and provide crystalsvg-icon-theme for fedora < 9

* Sun Nov 18 2007 Sebastian Vahl <fedora@deadbabylon.de> 3.5.8-9
- add switch to force rpmbuild behavior for testing
- prepare %%files for non-conflicting kdelibs3

* Tue Oct 30 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-8
- Provides: crystalsvg-icon-theme

* Thu Oct 25 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 3.5.8-7
- fix application of custom zoom patch (rh#335461)

* Tue Oct 23 2007 Than Ngo <than@redhat.com> - 3.5.8-6
- Resolves: rh#335461, kpdf and kview lost custom zoom

* Thu Oct 18 2007 Than Ngo <than@redhat.com> - 3.5.8-5
- bz273681, add vhdl syntax for kate, thanks to Chitlesh GOORAH

* Wed Oct 17 2007 Than Ngo <than@redhat.com> 3.5.8-4
- apply upstream patch to fix http-regression

* Mon Oct 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.8-3
- respin (for openexr-1.6.0)

* Fri Oct 12 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.8-2
- kde-3.5.8

* Tue Sep 25 2007 Than Ngo <than@redhat.com> - 6:3.5.7-23
- fix rh#243611, autostart from XDG_CONFIG_DIRS

* Sun Sep 09 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 6:3.5.7-22
- Remove Conflicts: kdelibs4-devel, let kdelibs4 decide whether we conflict
  (allows using the old /opt/kde4 versions for now)

* Wed Aug 22 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-21
- vcard30 patch (kde#115219,rh#253496)
- -devel: restore awol Requires (< f8 only) (#253801)
- License: LGPLv2

* Wed Aug 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-20
- CVE-2007-3820, CVE-2007-4224, CVE-2007-4225
- clarify licensing

* Tue Aug 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 6:3.5.7-19
- ConsoleKit-related patch (#244065) 

* Sun Aug 12 2007 Florian La Roche <laroche@redhat.com> 6:3.5.7-18
- fix apidocs subpackage requires

* Mon Aug 06 2007 Than Ngo <than@redhat.com> - 6:3.5.7-17
- cleanup

* Fri Aug 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-16
- undo kdelibs3 rename (for now, anyway)
- move to -devel: checkXML, kconfig_compiler, (make)kdewidgets, ksgmltools2,
  ksvgtopng, kunittestmodrunner
- set KDE_IS_PRELINKED unconditionally (#244065)
- License: LGPLv2+

* Fri Jul 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-15
- Obsoletes/Provides: kdelibs-apidocs (kdelibs3)

* Fri Jul 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-14
- toggle kdelibs3 (f8+)

* Wed Jul 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-13
- build fails against cups-1.3 (#248717)
- incorporate kdelibs3 bits (not enabled... yet) 

* Wed Jul 18 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-10
- +Requires: kde-filesystem

* Mon Jul 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-9
- omit ICEauthority patch (kde#147454, rh#243560, rh#247455)

* Wed Jun 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-8
- rework previously botched openssl patch

* Wed Jun 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-7
- -devel: Provides: kdelibs3-devel = ...
- openssl patch update (portability)
- drop deprecated ssl-krb5 patch

* Sat Jun 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-6
- Provides: kdelibs3 = %%version-%%release

* Sat Jun 16 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-5
- -devel: +Requires: libutempter-devel

* Fri Jun 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-4
- omit lib_loader patch (doesn't apply cleanly)

* Fri Jun 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-3
- include experimental libtool patches

* Mon Jun 11 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.7-2
- kdesu: sudo support (kde bug #20914), Requires(hint): sudo

* Wed Jun 06 2007 Than Ngo <than@redhat.com> -  6:3.5.7-0.1.fc7
- 3.5.7

* Thu May 24 2007 Than Ngo <than@redhat.com> 6:3.5.6-10.fc7
- don't change permission .ICEauthority by sudo KDE programs
- apply patch to fix locale issue
- apply upstream patch to fix kde#146105

* Wed May 16 2007 Rex Dieter <rdieter[AT]fedorproject.org> - 6:3.5.6-9
- make qtdocdir handling robust
- kde_settings=1
- Req: -desktop-backgrounds-basic

* Wed May 16 2007 Than Ngo <than@redhat.com> - 3.5.6-8.fc7
- add correct qt-version to build kde apidocs ,bz#239947
- disable kde_settings

* Mon May 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-7
- BR: +keyutils-libs-devel (until krb5 is fixed, bug #240220)

* Mon May 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-6
- kde.sh: fix typo/thinko

* Mon May 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> - 6:3.5.6-5
- %%changelog: prune pre-kde3 entries
- %%ghost %%{_datadir}/services/ksycoca
- omit extraneous .la file references (#178733)
- BR: jasper-devel OpenEXR-devel
- xdg-menu compat symlinks (to help transition to using XDG_MENU_PREFIX)
- fix kde#126812.patch to be non-empty
- cleanup kde.(sh|csh)
- Requires: +kde-settings -redhat-artwork 
- make apidocs build optional (default on)
- use FHS-friendly /etc/kde (#238136)

* Mon Mar 26 2007 Than Ngo <than@redhat.com> - 6:3.5.6-3.fc7
- apply upstream patch to fix build issue with qt-3.3.8
- apply upstream patch to to fix crash on particular 404 url
  in embedded HTML viewer

* Tue Feb 27 2007 Than Ngo <than@redhat.com> - 6:3.5.6-2.fc7
- cleanup specfile

* Mon Feb 05 2007 Than Ngo <than@redhat.com> - 6:3.5.6-1.fc7
- 3.5.6
- apply patch to fix #225420, CVE-2007-0537 Konqueror improper
  HTML comment rendering, thanks to Dirk Müller, KDE security team

* Tue Nov 14 2006 Than Ngo <than@redhat.com> - 6:3.5.5-1.fc7
- rebuild

* Fri Oct 27 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.2
- add missing api docs

* Wed Oct 25 2006 Than Ngo <than@redhat.com> 6:3.5.5-0.1
- update to 3.5.5

* Sun Oct 01 2006 Than Ngo <than@redhat.com> 6:3.5.4-10
- fix utf8 issue in kdeprint
- fix #178320,#198828, follow menu-spec
- upstream patches,
   fix #106748, Evaluate scripts in <iframe src=javascript:..> in the right context
   fix #133071, Crash when characterSet was accessed on newly-created document

* Sat Sep 30 2006 Than Ngo <than@redhat.com> 6:3.5.4-9
- fix #178320,#198828, follow menu-spec
- fix #119167, page rendered incorrectly at larger font sizes

* Tue Sep 26 2006 <than@redhat.com> 6:3.5.4-8
- fix #115891/bz#208270, CUPS 1.2.x unix socket support
- apply upstream patches
   fix #123915, Page format display is 'overlaid'
   fix #100188, Fix incorrect 'endl' usage

* Thu Sep 14 2006 Than Ngo <than@redhat.com> 6:3.5.4-7
- apply upstream patches
   fix #132678, Google search encoding fix
   khtml rendering issue
   fix #134118, silent startup notification never going away
   fix #133401, crash when attempting to remove a standard shortcut that isn't actually in 
   the KStdAccel::ShortcutList
   fix #131979, unbreak "latest" and "most downloads" views

* Tue Sep 12 2006 Than Ngo <than@redhat.com> 6:3.5.4-6
- fix #205767, konsole no longer register itself to utmp
- fix #123941, qt xim plugin sometimes leads to crash

* Tue Sep 05 2006 Than Ngo <than@redhat.com> 6:3.5.4-5
- apply upstream patches
   fix #123413, kded crash when KDED modules make DCOP calls in their destructors
   fix #133529, konqueror's performance issue
   fix kdebug crash
   more icon contexts (Tango icontheme)
   fix #133677, file sharing doesn't work with 2-character long home directories

* Mon Sep 04 2006 Than Ngo <than@redhat.com> 6:3.5.4-4
- apply upstream patches
   fix kde#121528, konqueror crash

* Wed Aug 23 2006 Than Ngo <than@redhat.com> 6:3.5.4-3
- apply upstream patches
   fix kde#131366, Padding-bottom and padding-top not applied to inline elements
   fix kde#131933, crash when pressing enter inside a doxygen comment block
   fix kde#106812, text-align of tables should only be reset in quirk mode
   fix kde#90462, konqueror crash while rendering in khtml

* Tue Aug 08 2006 Than Ngo <than@redhat.com> 6:3.5.4-2
- add BR on gettext, cups

* Tue Aug 08 2006 Than Ngo <than@redhat.com> 6:3.5.4-1
- rebuilt

* Wed Jul 26 2006 Petr Rockai <prockai@redhat.com> - 6:3.5.4-0.pre2
- drop the gcc workaround, problem fixed in gcc/g++

* Mon Jul 24 2006 Petr Rockai <prockai@redhat.com> - 6:3.5.4-0.pre1
- prerelease of 3.5.4 (from the first-cut tag)
- disable --enable-final on s390x, seems to cause problems

* Thu Jul 20 2006 Than Ngo <than@redhat.com> 6:3.5.3-11
- apply upstream patches,
   fix kde#130831, remember when the last replacement string was the empty string

* Tue Jul 18 2006 Petr Rockai <prockai@redhat.com> - 6:3.5.3-10
- do not ship the dummy kdnssd implementation, depend on external one
  (there is one provided by kdnssd-avahi now)
- change the use of anonymous namespace in kedittoolbar.h, so that
  the KEditToolbar classes are exported again

* Mon Jul 17 2006 Petr Rockai <prockai@redhat.com>
- should have been 6:3.5.3-9 but accidentally built as 6:3.5.3-8.fc6
- --disable-libfam and --enable-inotify to get inotify support
  and to disable gamin/fam usage
- add %%{?dist} to Release:

* Tue Jul 11 2006 Than Ngo <than@redhat.com> 6:3.5.3-8
- upstream patches,
    kde#130605 - konqueror crash
    kde#129187 - konqueror crash when modifying address bar address

* Mon Jul 10 2006 Than Ngo <than@redhat.com> 6:3.5.3-7
- apply upstream patches,
    kde#123307 - Find previous does nothing sometimes
    kde#106795 - konqueror crash

* Tue Jul 04 2006 Than Ngo <than@redhat.com> 6:3.5.3-6
- apply upstream patches, fix #128940/#81806/#128760

* Sat Jun 24 2006 Than Ngo <than@redhat.com> 6:3.5.3-5
- fix #196013, mark kde.sh/kde.csh as config file
- fix #178323 #196225, typo in kde.sh
- apply upstream patches

* Thu Jun 08 2006 Than Ngo <than@redhat.com> 6:3.5.3-4
- enable --enable-new-ldflags again since ld bug fixed
- move only *.so symlinks to -devel subpackage

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 6:3.5.3-3
- move .so symlinks to -devel subpackage

* Thu Jun 01 2006 Than Ngo <than@redhat.com> 7:3.5.3-2
- drop --enable-new-ldflags, workaround for ld bug

* Wed May 31 2006 Than Ngo <than@redhat.com> 7:3.5.3-1
- update to 3.5.3

* Tue May 23 2006 Than Ngo <than@redhat.com> 7:3.5.2-7
- fix #189677, No longer possible to "copy & rename" file in same directory

* Mon May 22 2006 Than Ngo <than@redhat.com> 6:3.5.2-6
- fix #192585, kdeprint writes incorrect cupsd.conf

* Thu May 18 2006 Than Ngo <than@redhat.com> 6:3.5.2-5
- use a versioned Obsoletes for kdelibs-docs

* Tue May 16 2006 Than Ngo <than@redhat.com> 6:3.5.2-4 
- rebuild against new qt to fix multilib issue
- fix #178323, add KDE_IS_PRELINKED/KDE_NO_IPV60
 
* Wed May 03 2006 Than Ngo <than@redhat.com> 6:3.5.2-3
- fix #173235, disable kmail debug info #173235
- use XDG_CONFIG_DIRS for kde menu #178320
- don't use private API with newer CUPS >=1.2

* Fri Apr 21 2006 Than Ngo <than@redhat.com> 6:3.5.2-2
- apply patch to fix crash kdeprint

* Tue Mar 21 2006 Than Ngo <than@redhat.com> 6:3.5.2-1
- update to 3.5.2

* Tue Feb 21 2006 Than Ngo <than@redhat.com> 6:3.5.1-2.3
- apply patch to fix missing icons in KDE main menu
- requires redhat-artwork >= 0.239-2
- don't own /usr/share/icons/hicolor #178319
- remove broken links #154093 

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-2.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 6:3.5.1-2.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Thu Feb 02 2006 Than Ngo <than@redhat.com> 6:3.5.1-2 
- add Obsolete: kdelibs-docs

* Wed Feb 01 2006 Than Ngo <than@redhat.com> 6:3.5.1-1
- 3.5.1

* Thu Jan 19 2006 Than Ngo <than@redhat.com> 6:3.5.0-6
- rename subpackage to -apidocs

* Wed Jan 18 2006 Than Ngo <than@redhat.com> 6:3.5.0-5
- apply patch to fix a printing problem
- add subpackage kdelibs-docs
- enable --enable-new-ldflags #161074 

* Wed Dec 21 2005 Than Ngo <than@redhat.com> 6:3.5.0-4
- apply patch to fix crash in kicker on KDE logout

* Fri Dec 16 2005 Than Ngo <than@redhat.com> 6:3.5.0-3
- add requires on several devel subpackages

* Tue Dec 13 2005 Than Ngo <than@redhat.com> 6:3.5.0-2 
- apply patch to fix konqueror for working with new openssl #174541 

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
* - rebuilt

* Thu Dec 01 2005 Than Ngo <than@redhat.com> 6:3.5.0-1
- add fix for modular X, thanks to Ville Skyttä #174131
- probably fix #174541

* Mon Nov 28 2005 Than Ngo <than@redhat.com> 6:3.5.0-0.1.rc2
- 3.5 rc2

* Mon Nov 14 2005 Than Ngo <than@redhat.com> 6:3.5.0-0.1.rc1
- update 3.5.0 rc1
- remove unneeded lnusertemp workaround
- remove references to optional libraries in .la files #170602 

* Thu Nov 10 2005 Than Ngo <than@redhat.com> 6:3.4.92-4
- apply patch to fix gcc4 compilation

* Wed Nov 09 2005 Than Ngo <than@redhat.com> 6:3.4.92-3 
- rebuilt against new libcrypto, libssl
- requires iceauth
 
* Fri Nov 04 2005 Than Ngo <than@redhat.com> 6:3.4.92-2
- move lnusertemp in arts, workaround for #169631

* Mon Oct 24 2005 Than Ngo <than@redhat.com> 6:3.4.92-1
- update to 3.5 beta 2

* Wed Oct 12 2005 Than Ngo <than@redhat.com> 6:3.4.91-2
- add libacl-devel buildrequirement
- add openoffice mimelnk files #121769

* Tue Sep 27 2005 Than Ngo <than@redhat.com> 6:3.4.91-1
- update to KDE 3.5 Beta1

* Mon Aug 08 2005 Than Ngo <than@redhat.com> 6:3.4.2-2
- add requires xorg-x11 #165287

* Mon Aug 01 2005 Than Ngo <than@redhat.com> 6:3.4.2-1
- update to 3.4.2

* Tue Jun 21 2005 Than Ngo <than@redhat.com> 6:3.4.1-2
- add devices protocol #160927

* Wed May 25 2005 Than Ngo <than@redhat.com> 6:3.4.1-1
- 3.4.1

* Wed May 04 2005 Than Ngo <than@redhat.com> 6:3.4.0-6
- kimgio input validation vulnerabilities, CAN-2005-1046

* Wed Apr 13 2005 Than Ngo <than@redhat.com> 6:3.4.0-5
- more fixes from CVS stable branch
- fix kbuildsycoca crashes with signal 11 on kde startup #154246

* Tue Apr 12 2005 Than Ngo <than@redhat.com> 6:3.4.0-4
- add workaround for #154294

* Thu Apr 07 2005 Than Ngo <than@redhat.com> 3.4.0-3
- add missing kcontrol/khelp/home/find in main menu #151655 
- fix bad symlinks #154093

* Fri Apr 01 2005 Than Ngo <than@redhat.com> 6:3.4.0-2
- more patches from CVS stable branch
- add missing kde documents, workaround for rpm bug

* Thu Mar 17 2005 Than Ngo <than@redhat.com> 6:3.4.0-1
- 3.4.0 release

* Wed Mar 16 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.6
- new snapshot from KDE_3_4_BRANCH

* Mon Mar 14 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.5
- default font setting Sans/Monospace

* Fri Mar 04 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.4
- rebuilt against gcc-4.0.0-0.31

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.3
- fix dependency problem with openssl-0.9.7e

* Tue Mar 01 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.2
- rebuilt against gcc-4

* Sat Feb 26 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.1
- bump release

* Fri Feb 25 2005 Than Ngo <than@redhat.com> 6:3.4.0-0.rc1.0
- KDE 3.4.0 rc1

* Tue Feb 22 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.3
- respin KDE 3.4 beta2

* Thu Feb 17 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.2
- Add symlinks to crystal icons, thanks Peter Rockai, #121929
- fix export

* Mon Feb 14 2005 Than Ngo <than@redhat.com> 6:3.3.92-0.1
- KDE 3.4 Beta2

* Sat Feb 12 2005 Than Ngo <than@redhat.com> 6:3.3.2-0.7
- backport CVS patch, cleanup InputMethod

* Fri Feb 11 2005 Than Ngo <than@redhat.com> 6:3.3.2-0.6
- drop mktemp patch

* Thu Feb 10 2005 Than Ngo <than@redhat.com> 6:3.3.2-0.5
- use mkstemp instead of mktemp
- fix knotify crash after applying sound system change
- add steve cleanup patch

* Wed Dec 15 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.4
- get rid of broken AltiVec instructions on ppc

* Tue Dec 14 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.3
- apply the patch to fix Konqueror Window Injection Vulnerability #142510
  CAN-2004-1158,  Thanks to KDE security team
- Security Advisory: plain text password exposure, #142487
  thanks to KDE security team

* Wed Dec 08 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.2
- workaround for compiler bug on ia64 (-O0)

* Fri Dec 03 2004 Than Ngo <than@redhat.com> 6:3.3.2-0.1
- update to 3.3.2
- remove unneeded kdelibs-3.3.1-cvs.patch, kdelibs-3.3.1-xml.patch

* Tue Nov 02 2004 Than Ngo <than@redhat.com> 6:3.3.1-4
- backport CVS patches, fix konqueror crash #134758

* Fri Oct 29 2004 Than Ngo <than@redhat.com> 6:3.3.1-3
- add some fixes from CVS

* Sat Oct 16 2004 Than Ngo <than@redhat.com> 6:3.3.1-2
- rebuilt for rhel

* Wed Oct 13 2004 Than Ngo <than@redhat.com> 6:3.3.1-1
- update to KDE 3.3.1

* Wed Sep 29 2004 Than Ngo <than@redhat.com> 6:3.3.0-5
- add missing requires on libidn-devel

* Sun Sep 26 2004 Than Ngo <than@redhat.com> 6:3.3.0-4
- cleanup menu

* Mon Sep 20 2004 Than Ngo <than@redhat.com> 3.3.0-3
- fix a bug in ksslopen #114835

* Tue Sep 07 2004 Than Ngo <than@redhat.com> 6:3.3.0-2
- add patch to fix KDE trash always full #122988

* Thu Aug 19 2004 Than Ngo <than@redhat.com> 6:3.3.0-1
- update to 3.3.0 release

* Tue Aug 10 2004 Than Ngo <than@redhat.com> 6:3.3.0-0.1.rc2
- update to 3.3.0 rc1

* Sun Aug 08 2004 Than Ngo <than@redhat.com> 6:3.3.0-0.1.rc1
- update to 3.3 rc1

* Fri Jul 23 2004 Than Ngo <than@redhat.com> 3.2.92-2
- update to KDE 3.3 Beta 2
- remove some unneeded patch files
- enable libsuffix

* Mon Jul 19 2004 Than Ngo <than@redhat.com> 6:3.2.3-6
- add IM patch
- set kprinter default to cups

* Mon Jul 12 2004 Than Ngo <than@redhat.com> 6:3.2.3-5
- rebuild

* Mon Jul 05 2004 Than Ngo <than@redhat.com> 6:3.2.3-4
- built with libpcre support, it's needed for using regular expressions in Javascript code bug #125264

* Thu Jul 01 2004 Than Ngo <than@redhat.com> 6:3.2.3-3
- fix double entry in filelist
- add some devel packages in requires

* Thu Jun 17 2004 Than Ngo <than@redhat.com> 3.2.3-2
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon May 31 2004 Than Ngo <than@redhat.com> 3.2.3-1
- update to KDE 3.2.3
- remove some patch files, which are now included in 3.2.3

* Mon May 17 2004 Than Ngo <than@redhat.com> 6:3.2.2-7
- add patch to enable PIE

* Sun May 16 2004 Than Ngo <than@redhat.com> 6:3.2.2-6
- vulnerability in the mailto handler, CAN-2004-0411

* Fri May 14 2004 Than Ngo <than@redhat.com> 3.2.2-5
- KDE Telnet URI Handler File Vulnerability , CAN-2004-0411

* Wed Apr 21 2004 Than Ngo <than@redhat.com> 3.2.2-4
- Implements the FreeDesktop System Tray Protocol, thanks to Harald Hoyer

* Mon Apr 19 2004 Than Ngo <than@redhat.com> 3.2.2-3
- fix #120265 #119642

* Sun Apr 18 2004 Warren Togami <wtogami@redhat.com> 3.2.2-2
- #120265 #119642 -devel req alsa-lib-devel esound-devel fam-devel
                             glib2-devel libart_lgpl-devel
- #88853 BR autoconf automake libpng-devel libvorbis-devel
            glib2-devel libtiff-devel
- cups-libs explicit epoch, some cleanups

* Tue Apr 13 2004 Than Ngo <than@redhat.com> 3.2.2-1
- 3.2.2 release

* Fri Mar 12 2004 Than Ngo <than@redhat.com> 6:3.2.1-1.4
- rebuild

* Thu Mar 11 2004 Than Ngo <than@redhat.com> 6:3.2.1-1.3
- get rid of application.menu, it's added in redhat-menus

* Fri Mar 05 2004 Than Ngo <than@redhat.com> 6:3.2.1-1.2
- respin

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Than Ngo <than@redhat.com> 3.2.1-1
- update to 3.2.1 release

* Tue Feb 17 2004 Than Ngo <than@redhat.com> 6:3.2.0-1.5
- fix typo bug, _smp_mflags instead smp_mflags

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 09 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.4
- add new icon patch file 

* Thu Feb 05 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.3 
- build against qt 3.3.0
- fix a bug in ksslopen on x86_64, bug #114835

* Tue Feb 03 2004 Than Ngo <than@redhat.com> 6:3.2.0-0.2
- 3.2.0 release

* Fri Jan 23 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.4
- fixed #114114

* Wed Jan 21 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.3
- fixed file conflict with hicolor-icon-theme
- added requires: hicolor-icon-theme

* Tue Jan 20 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.2
- added kde.sh, kde.csh
- fixed build problem
- fixed rpm file list

* Mon Jan 19 2004 Than Ngo <than@redhat.com> 6:3.1.95-0.1
- KDE 3.2 RC1

* Tue Dec 02 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.2
- KDE 3.2 Beta2 respin

* Mon Dec 01 2003 Than Ngo <than@redhat.com> 6:3.1.94-0.1
- KDE 3.2 Beta2

* Wed Nov 26 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.4
- add missing cupsdconf, cupsdoprint and dcopquit

* Tue Nov 25 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.3
- enable alsa support

* Sat Nov 08 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.2
- cleanup several patch files

* Mon Nov 03 2003 Than Ngo <than@redhat.com> 6:3.1.93-0.1
- 3.2 Beta 1
- remove many patches, which are now in upstream
- adjust many redhat specific patch files
- cleanup rpm file list

* Fri Oct 17 2003 Than Ngo <than@redhat.com> 6:3.1.4-4
- fixed icon scale patch, thanks to Thomas Wörner

* Fri Oct 10 2003 Than Ngo <than@redhat.com> 6:3.1.4-3
- better icon scale patch

* Thu Oct 02 2003 Than Ngo <than@redhat.com> 6:3.1.4-2
- rebuild against new gcc-3.3.1-6, fixed miscompiled code on IA-32 

* Mon Sep 29 2003 Than Ngo <than@redhat.com> 6:3.1.4-1
- 3.1.4

* Thu Sep 04 2003 Than Ngo <than@redhat.com> 6:3.1.3a-1
- 3.1.3a

* Thu Aug 28 2003 Than Ngo <than@redhat.com> 6:3.1.3-8
- adopted a patch file from Mandrake, it fixes full screen problem

* Wed Aug 27 2003 Than Ngo <than@redhat.com> 6:3.1.3-7
- rebuilt

* Wed Aug 27 2003 Than Ngo <than@redhat.com> 6:3.1.3-6
- rebuilt

* Fri Aug 22 2003 Than Ngo <than@redhat.com> 6:3.1.3-5
- fix build problem with gcc 3.x

* Wed Aug 06 2003 Than Ngo <than@redhat.com> 6:3.1.3-4
- rebuilt

* Wed Aug 06 2003 Than Ngo <than@redhat.com> 6:3.1.3-3
- add patch file to fix horizontal scrollbar issue

* Thu Jul 31 2003 Than Ngo <than@redhat.com> 6:3.1.3-2
- rebuilt

* Tue Jul 29 2003 Than Ngo <than@redhat.com> 6:3.1.3-1
- 3.1.3
- add Prereq: dev

* Tue Jun 17 2003 Than Ngo <than@redhat.com> 6:3.1.2-7
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sun May 18 2003 Than Ngo <than@redhat.com> 6:3.1.2-5
- remove workaround for glibc bug

* Wed May 14 2003 Than Ngo <than@redhat.com> 6:3.1.2-3
- fix dependence bug

* Tue May 13 2003 Than Ngo <than@redhat.com> 6:3.1.2-2
- fix a bug in loading openssl library

* Mon May 12 2003 Than Ngo <than@redhat.com> 6:3.1.2-1
- 3.1.2

* Wed Apr 30 2003 Than Ngo <than@redhat.com> 6:3.1.1-7
- build with -fpic on ppc (ld bugs)

* Mon Apr 28 2003 Than Ngo <than@redhat.com> 6:3.1.1-6
- libjpeg-devel and bzip2-devel in buildrequires (#89635)

* Thu Apr 24 2003 Than Ngo <than@redhat.com> 6:3.1.1-5
- use pcre native API

* Mon Apr 14 2003 Than Ngo <than@redhat.com> 6:3.1.1-4
- add xrandr support

* Sun Apr 13 2003 Than Ngo <than@redhat.com> 6:3.1.1-3
- PS/PDF file handling vulnerability

* Thu Mar 20 2003 Than Ngo <than@redhat.com> 6:3.1.1-2
- add patch file from CVS to fix: https authentication through proxy fails
- add patch file from CVS to fix: KZip fails for some .zip archives

* Sun Mar 16 2003 Than Ngo <than@redhat.com> 6:3.1.1-1
- 3.1.1 stable release
- move desktop-create-kmenu to kdelibs

* Mon Mar  3 2003 Than Ngo <than@redhat.com> 6:3.1-12
- lan redirect

* Mon Feb 24 2003 Than Ngo <than@redhat.com> 6:3.1-11
- add Buildprereq libart_lgpl-devel

* Mon Feb 24 2003 Than Ngo <than@redhat.com> 6:3.1-10
- move API documentation into kdelibs-devel (#84976)

* Fri Feb 21 2003 Than Ngo <than@redhat.com> 6:3.1-9
- add fix from Thomas Wörner to watch /usr/share/applications
  for changes, (bug #71613)

* Thu Feb 20 2003 Than Ngo <than@redhat.com> 6:3.1-8
- rebuid against gcc 3.2.2 to fix dependency in la file

* Thu Feb 13 2003 Thomas Woerner <twoerner@redhat.com> 6:3.1-7
- fixed arts bug #82750, requires rebuild of kdelibs

* Tue Feb 11 2003 Than Ngo <than@redhat.com> 6:3.1-6
- fix Norway i18n issue, bug #73446

* Mon Feb 10 2003 Than Ngo <than@redhat.com> 6:3.1-5
- konqueror crashes on a double click, bug #81503

* Sun Feb  9 2003 Than Ngo <than@redhat.com> 6:3.1-4
- add patch to support the macromedia, bug #83808

* Thu Feb  6 2003 Than Ngo <than@redhat.com> 6:3.1-3
- add patch to set correct default encoding, bug #82539
- don't overwrite defaultstyle, bug #74795, #80103

* Fri Jan 31 2003 Than Ngo <than@redhat.com> 6:3.1-2
- Add better resize icon patch from Thomas Woerner

* Tue Jan 28 2003 Than Ngo <than@redhat.com> 6:3.1-1
- 3.1 final

* Sun Jan 26 2003 Than Ngo <than@redhat.com> 6:3.1-0.16
- use make apidox to create KDE api instead doxygen

* Fri Jan 24 2003 Than Ngo <than@redhat.com> 6:3.1-0.15
- use doxygen to create api docs
- clean up specfile

* Thu Jan 23 2003 Tim Powers <timp@redhat.com> 6:3.1-0.14
- rebuild

* Wed Jan 22 2003 Than Ngo <than@redhat.com> 3.1-0.13
- rc7

* Thu Jan 16 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.12
- added icon scale patch
- added ia64 again

* Mon Jan 13 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.11
- excluded ia64

* Sun Jan 12 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.10
- rebuild

* Fri Jan 10 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.9
- removed silly size_t check

* Fri Jan 10 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.8
- rc6

* Fri Jan 10 2003 Thomas Woerner <twoerner@redhat.com> 3.1-0.7
- ssl uses krb5

* Sat Dec 28 2002 Than Ngo <than@redhat.com> 3.1-0.6
- rebuild

* Mon Dec 16 2002 Than Ngo <than@redhat.com> 3.1-0.5
- rebuild

* Thu Dec 12 2002 Than Ngo <than@redhat.com> 3.1-0.4
- fix dependency bug
- use kdoc to create api docs

* Sat Nov 30 2002 Than Ngo <than@redhat.com> 3.1-0.3
- fix bug #78646
- set kde_major_version

* Fri Nov 22 2002 Than Ngo <than@redhat.com> 3.1-0.2
- use doxygen to create api docs

* Tue Nov 19 2002 Than Ngo <than@redhat.com> 3.1-0.1
- update rc4
- adjust many patch files for 3.1
- remove some patch files, which are now in 3.1

* Sun Nov 10 2002 Than Ngo <than@redhat.com> 3.0.5-1.1
- conform strict ANSI (bug #77603)

* Sat Nov  9 2002 Than Ngo <than@redhat.com> 3.0.5-1
- update to 3.0.5

* Wed Oct 16 2002 Than Ngo <than@redhat.com> 3.0.4-3
- rebuild to get rid of libstdc++.la on x86_64
- cleanup sepcfile
- dependency issue

* Sat Oct 12 2002 Than Ngo <than@redhat.com> 3.0.4-2
- better handling of desktop file renames (bug #74071)
- initLanguage issue

* Thu Oct 10 2002 Than Ngo <than@redhat.com> 3.0.4-1

- 3.0.4
- Added 2 patch files for built-in tests from AndreyPozdeev@rambler.ru (bug #75003)
- Added KDE Url (bug #54592)

* Tue Oct  8 2002 Than Ngo <than@redhat.com> 3.0.3-10
- Added fix to get correct Lib directory name on 64bit machine
- New fix to handle desktop file renames (bug #74071)

* Fri Sep 20 2002 Than Ngo <than@redhat.com> 3.0.3-8.1
- Konqueror Cross Site Scripting Vulnerability

* Sun Sep  1 2002 Than Ngo <than@redhat.com> 3.0.3-8
- remove merging share/applnk

* Sat Aug 31 2002 Than Ngo <than@redhat.com> 3.0.3-7
- put Red Hat in the version number
- desktop file issue

* Tue Aug 27 2002 Phil Knirsch <pknirsch@redhat.com> 3.0.3-6
- Removed gcc31 patch as it breaks the Netscape plugin in gcc32.

* Mon Aug 26 2002 Phil Knirsch <pknirsch@redhat.com> 3.0.3-5
- Use LANG env as default if available
- Fixed general language handling problems

* Sun Aug 25 2002 Than Ngo <than@redhat.com> 3.0.3-4
- revert about KDE, use preference

* Thu Aug 22 2002 Than Ngo <than@redhat.com> 3.0.3-3
- Added katetextbuffermultibyte patch from Leon Ho (bug #61464)
- build against new qt

* Tue Aug 13 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.3-2
- Update to 3.0.3 respin to fix SSL security bug

* Sun Aug 11 2002 Than Ngo <than@redhat.com> 3.0.3-1
- 3.0.3
- Added ksyscoca patch from Harald Hoyer

* Thu  Aug  8 2002 Than Ngo <than@redhat.com> 3.0.2-6
- Added better system tray dock patch from Harald Hoyer

* Fri Aug  2 2002 Than Ngo <than@redhat.com> 3.0.2-5
- Fixed a bug in ktip (bug #69627,70329)

* Fri Aug  2 2002 Than Ngo <than@redhat.com> 3.0.2-4
- Added system tray dock patch from Harald Hoyer
- Added Buildrequires audiofile-devel (bug #69983)
- Added Buildrequires openssl-devel (bug #64858)
- Rebuild against qt 3.0.5 (bug #70379)
- Added patch to remove "about KDE" menu item from help menu (bug #67287)
- Fixed dependencies bug by update (bug #69798)
- Added some bugfixes from 3.0.2 stable branches

* Fri Aug  2 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-3
- Add some bugfixes from CVS (mostly HTML rendering fixes)

* Mon Jul 22 2002 Tim Powers <timp@redhat.com> 3.0.2-2
- rebuild using gcc-3.2-0.1

* Tue Jul  2 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-1
- 3.0.2

* Tue Jun 25 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-0.cvs20020625.1
- Make KLocale respect the LANG setting when kpersonalizer wasn't run

* Mon Jun 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-0.cvs20020624.1
- Update, should be VERY close to 3.0.2 final now.

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Jun 20 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.2-0.cvs20020620.1
- Update
- Remove the malloc hack, it's no longer needed with glibc 2.2.90

* Tue May 28 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.1-3
- Add support for xdg-list icon theme spec

* Thu May  9 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.1-1
- 3.0.1

* Tue May  7 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-12
- Update to KDE_3_0_BRANCH
- Do away with the GCC296 define, it's handled automatically

* Thu May  2 2002 Than Ngo <than@redhat.com> 3.0.0-11
- add some fixes from KDE CVS
- build against gcc-3.1-0.26/qt-3.0.3-12

* Mon Apr 15 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-10
- Change sonames to something indicating the compiler version if a compiler
  < gcc 3.1 is used
- Add compat symlinks for binary compatibility with other distributions

* Thu Apr 11 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-9
- Fix Qt designer crash when loading KDE plugins

* Tue Apr  9 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-8
- Add build requirement on samba >= 2.2.3a-5 to make sure the correct
  smb ioslave can be built

* Mon Apr  8 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-7
- Merge the following fixes from KDE_3_0_BRANCH:
  - RFC 2818 compliance for KSSL
  - Detect premature loss of connection in http ioslave (this may have
    been the cause of the bugzilla CGI.pl:1444 issue)
  - Don't send SIGHUP to kdesu child applications
  - Fix KHTML form rendering problems

* Wed Apr  3 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-6
- Fix up timeout problems with form submissions (#62196)

* Wed Apr  3 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-5
- Merge kjs crash-on-invalid-input fix from KDE_3_0_BRANCH

* Thu Mar 28 2002 Than Ngo <than@redhat.com> 3.0.0-4
- fix kde version

* Thu Mar 28 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-3
- Add another khtml rendering fix

* Wed Mar 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-2
- Add a khtml fix from KDE_3_0_BRANCH, prevents form content from
  being submitted twice, which probably caused the CGI.pl:1444 bug
  some people have noted with Bugzilla.

* Wed Mar 27 2002 Bernhard Rosenkraenzer <bero@redhat.com> 3.0.0-1
- Update to final
- Add fixes from KDE_3_0_BRANCH

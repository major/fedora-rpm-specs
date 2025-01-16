%global prever pre1
%global ver %{version}-%{prever}

# change with every change of major or minor version number
#%%global majminver 5.3
%global majminver $(echo %{version} | sed -E 's/\.[0-9]+$//')

%if 0%{?rhel} <= 8 && 0%{?fedora} < 41
%bcond_without plugin
%else
%bcond_with plugin
%endif

%if 0%{?rhel} <= 9 || 0%{?fedora}
%bcond_without gtk2
%else
%bcond_with gtk2
%endif

# added in cups-1:2.4.7-3 - remove once F40 is EOL and C10S is released
# (that's the safe bet for versions where macros will be always available)
%{!?_cups_datadir:%global _cups_datadir %(/usr/bin/pkg-config --variable=cups_datadir cups)}
%{!?_cups_serverroot:%global _cups_serverroot %(/usr/bin/pkg-config --variable=cups_serverroot cups)}

Name: gutenprint
Summary: Printer Drivers Package
Version: 5.3.5
Release: 0.1%{prever}%{?dist}
URL: http://gimp-print.sourceforge.net/
Source0: http://downloads.sourceforge.net/gimp-print/%{name}-%{ver}.tar.xz
# Post-install script to update CUPS native PPDs.
Source1: cups-genppdupdate.py.in
# ported from old gimp-print package - fix for a menu in gimp gutenprint plugin
Patch0: gutenprint-menu.patch
Patch1: gutenprint-postscriptdriver.patch
Patch2: gutenprint-yyin.patch
Patch3: gutenprint-manpage.patch
Patch4: gutenprint-python36syntax.patch
# from upstream
Patch5: 0001-configure.ac-Fix-up-a-mistake-in-the-shared-library-.patch
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND GPL-3.0-or-later WITH Bison-exception-2.2


Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# autoreconf
BuildRequires: autoconf
BuildRequires: automake
# we remove rpath during %%install
BuildRequires: chrpath
# we use CUPS functions in CUPS driver
BuildRequires: cups
BuildRequires: cups-devel
BuildRequires: cups-libs
# gcc is no longer in buildroot by default
BuildRequires: gcc
# for language support
BuildRequires: gettext-devel
# glib-mkenums required for autogen.sh regardless of plugin
BuildRequires: glib2-devel
# for JPEG, PNG and TIFF file format support
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
# for autoreconf
BuildRequires: libtool
# uses make
BuildRequires: make
# we use pkgconfig in spec file to get correct devel packages
BuildRequires: pkgconfig
# for gutenprint usb backend gutenprintMAJMIN+usb
BuildRequires: pkgconfig(libusb-1.0)
# Make sure we get postscriptdriver tags - for automatic driver installation
# via PackageKit.
BuildRequires:  python3-cups
# needed for defining %%{__python3} macro for prep phase
BuildRequires: python3-devel
# we use sed in spec file to get majorver.minver string, which is used in directory
# structure
BuildRequires: sed

# the plugin is built only in Fedora, so
# no need gimp devel files for its ui
%if %{with plugin}
BuildRequires: gimp-devel
%endif

%if %{with gtk2}
# gutenprint library uses functions from GTK2 for gutenprint UI library
BuildRequires: pkgconfig(gtk+-2.0)
%endif

# escputil uses lp for sending raw print commands to the printer...
Requires:      cups-client%{?_isa}

## NOTE ##
# The README file in this package contains suggestions from upstream
# on how to package this software. I'd be inclined to follow those
# suggestions unless there's a good reason not to do so.

%description
Gutenprint is a package of high quality printer drivers for Linux, BSD,
Solaris, IRIX, and other UNIX-alike operating systems.
Gutenprint was formerly called Gimp-Print.

%package doc
Summary:        Documentation for gutenprint

%description doc
Documentation for gutenprint.

%package libs
Summary:       libgutenprint library

%description libs
This package includes libgutenprint library, necessary to run gutenprint.

%if %{with gtk2}
%package libs-ui
Summary:       libgutenprintui2 library
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
# function in the library tries to figure out local printing system by checking for lp binary
Requires:      cups-client%{?_isa}

%description libs-ui
This package includes libgutenprintui2 library, which contains
GTK+ widgets, which may be used for print dialogs etc.
%endif

%package devel
Summary:        Library development files for gutenprint
Requires:       %{name}%{?_isa} = %{version}-%{release}
%if %{with gtk2}
Requires:       gtk2-devel
%endif

%description devel
This package contains headers and libraries required to build applications that
uses gutenprint package.

%if %{with plugin}
%package plugin
Summary:        GIMP plug-in for gutenprint
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gimp

%description plugin
This package contains the gutenprint GIMP plug-in.

%package extras
Summary:        Sample test pattern generator for gutenprint-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description extras
This package contains test pattern generator and the sample test pattern
that is used by gutenprint-devel package.
%endif

%package cups
Summary:        CUPS drivers for Canon, Epson, HP and compatible printers
Requires:       cups
Requires:       %{name}%{?_isa} = %{version}-%{release}
# for cups-genppdupdate python script
Requires:       python3
Requires:       python3-charset-normalizer

%description cups
This package contains native CUPS support for a wide range of Canon,
Epson, HP and compatible printers.

%prep
%setup -q -n %{name}-%{ver}
# Fix menu placement of GIMP plugin.
%patch -P 0 -p1 -b .menu
# Allow the CUPS dynamic driver to run inside a build root.
%patch -P 1 -p1 -b .postscriptdriver
# Don't export yy* symbols (bug #882194).
%patch -P 2 -p1 -b .yyin
# Added some escputil options to the manpage (bug #979064).
%patch -P 3 -p1 -b .manpage

cp %{SOURCE1} src/cups/cups-genppdupdate.in

#shebang can change between releases - use %%{__python3} macro
sed -i -e 's,^#!/usr/bin/python3,#!%{__python3},' src/cups/cups-genppdupdate.in

# Python 3.6 invalid escape sequence deprecation fixes, COPYING as license (bug #1448303)
%patch -P 4 -p1 -b .python36syntax
%patch -P 5 -p1 -b .soname-ver


%build
# run after patch for configure.ac
./autogen.sh

# Don't run the weave test as it takes a very long time.
sed -i -e 's,^\(TESTS *=.*\) run-weavetest,\1,' test/Makefile.in

%configure --disable-dependency-tracking \
    --disable-static \
    --enable-samples \
    --enable-escputil \
    --enable-test \
    --disable-rpath \
    --enable-cups-1_2-enhancements \
    --disable-cups-ppds \
%if %{without gtk2}
    --disable-libgutenprintui2 \
%endif
    --enable-simplified-cups-ppds

%make_build

# Test suite disabled due to bug #1069274.
#%check
#make check
 
%install
%make_install

mkdir -p %{buildroot}%{_sbindir}

rm -rf %{buildroot}%{_datadir}/gutenprint/doc
rm -f %{buildroot}%{_datadir}/foomatic/kitload.log

rm -rf %{buildroot}%{_libdir}/gutenprint/%{majminver}/modules/*.la
rm -f %{buildroot}%{_cups_serverroot}/command.types

%find_lang %{name}
sed 's!%{_datadir}/locale/\([^/]*\)/LC_MESSAGES/gutenprint.mo!%{_datadir}/locale/\1/gutenprint_\1.po!g' %{name}.lang >%{name}-po.lang
rm -f %{name}.lang
%find_lang %{name} --all-name
cat %{name}-po.lang >>%{name}.lang

#echo .so man8/cups-genppd.8 > %{buildroot}%{_mandir}/man8/cups-genppd.5.3.3

# Fix up rpath.  If you can find a way to do this without resorting
# to chrpath, please let me know!
for file in \
  %{buildroot}%{_sbindir}/cups-genppd.%{majminver} \
  %{buildroot}%{_libdir}/*.so.* \
  %{buildroot}%{_cups_serverbin}/driver/* \
  %{buildroot}%{_cups_serverbin}/filter/* \
  %{buildroot}%{_bindir}/*
do
  chrpath --delete ${file}
done

%if %{with plugin}
  for file in %{buildroot}%{_libdir}/gimp/*/plug-ins/*
  do
    chrpath --delete ${file}
  done
%else
  %{_bindir}/rm -f %{buildroot}%{_bindir}/testpattern \
%endif

%ldconfig_scriptlets libs
%ldconfig_scriptlets libs-ui

%post cups
%{_sbindir}/cups-genppdupdate >/dev/null 2>&1 || :
%{_sbindir}/restorecon -vRF /etc/cups/printers.conf 2>&1 || :
%{_bindir}/systemctl restart cups >/dev/null 2>&1 || :
exit 0


%files -f %{name}.lang
%license COPYING
%{_bindir}/escputil
%{_mandir}/man1/escputil.1*
%{_datadir}/%{name}
%{_libdir}/%{name}

%files doc
%doc AUTHORS NEWS README doc/FAQ.html doc/gutenprint-users-manual.odt doc/gutenprint-users-manual.pdf
%license COPYING

%files libs
%{_libdir}/libgutenprint.so.9
%{_libdir}/libgutenprint.so.9.*

%if %{with gtk2}
%files libs-ui
%{_libdir}/libgutenprintui2.so.2
%{_libdir}/libgutenprintui2.so.2.*
%endif

%files devel
%doc ChangeLog doc/developer/reference-html doc/developer/gutenprint.pdf
%doc doc/gutenprint
%{_includedir}/gutenprint/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gutenprint.pc
%exclude %{_libdir}/*.la
%if %{with gtk2}
%doc doc/gutenprintui2
%{_includedir}/gutenprintui2/
%{_libdir}/pkgconfig/gutenprintui2.pc
%endif

%if %{with plugin}
%files plugin
%{_libdir}/gimp/*/plug-ins/gutenprint

%files extras
%doc
%{_bindir}/testpattern
%{_datadir}/gutenprint/samples/*
%endif

%files cups
%doc
%{_cups_datadir}/calibrate.ppm
%{_cups_datadir}/usb/net.sf.gimp-print.usb-quirks
%{_cups_serverbin}/filter/commandtocanon
%{_cups_serverbin}/filter/commandtodyesub
%{_cups_serverbin}/filter/commandtoepson
%{_cups_serverbin}/filter/rastertogutenprint.5.3
%{_cups_serverbin}/driver/gutenprint.5.3
%{_cups_serverbin}/backend/gutenprint53+usb
%{_bindir}/cups-calibrate
%{_sbindir}/cups-genppd.5.3
%{_sbindir}/cups-genppdupdate
%{_mandir}/man8/cups-calibrate.8*
%{_mandir}/man8/cups-genppd*8*.gz

%changelog
* Thu Dec 19 2024 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.5-0.1pre1
- 5.3.5pre1

* Tue Aug 20 2024 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.4-18
- 2305688 - disable gimp plugin for F41+ because it depends on GIMP 2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Florian Weimer <fweimer@redhat.com> - 5.3.4-14
- Backport upstream patch to fix C compatibility issue

* Thu Nov 16 2023 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.4-13
- make gutenprint and gutenprint-libs-ui dependant on cups-client - both checks for existence of lp

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 06 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 5.3.4-11
- Replace python3-chardet with python3-charset-normalizer

* Wed Apr 05 2023 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.4-11
- GTK2 is not in CentOS Stream 10, dont ship libs-ui subpackage there
- Add other licenses to License tag and use SPDX identifiers to comply with FPG

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 28 2022 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.4-8
- 2055504 - Set gutenprint53+usb backend to use the default USB context

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.4-6
- remove the static libraries which were shipped by mistake

* Mon Nov 22 2021 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.4-5
- 2025107 - cups-genppdupdate needs python3-chardet

* Wed Aug 11 2021 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.4-4
- fix xml errors reported by rpminspect

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 2021 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.4-1
- 5.3.4

* Fri Nov 06 2020 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.3-7
- 1773690 - cups-genppdupdate doesnt work for non-utf-8 PPDs

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.3-6
- make is no longer in buildroot by default

* Wed Sep 30 2020 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.3-5
- dont require the gimp package as build require, pkgconfig's gimpui-2.0 suffices

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 25 2020 Tom Stellard <tstellar@redhat.com> - 5.3.3-3
- Fix warning building with clang
- non-void function 'stp_paths_copy_with_prefix' should return a value [-Wreturn-type]

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 06 2019 Zdenek Dohnal <zdohnal@redhat.com> - 5.3.3-1
- 5.3.3

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 09 2019 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.14-6
- rebuilt again (because bodhi cannot release builds of unpushed updates)

* Mon Apr 08 2019 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.14-5
- rebuilt for gimp-2.10.10

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.14-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.14-2
- use %%{__python3} macro

* Thu Jun 28 2018 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.14-1
- 5.2.14

* Wed Feb 28 2018 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.14-0.4pre2
- name libraries explicitly 

* Tue Feb 20 2018 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.14-0.3pre2
- gcc is no longer in buildroot by default

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.14-0.2pre2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.14-0.1pre2
- Rebase to 5.2.14pre2

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 5.2.13-4
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.13-1
- rebase to 5.2.13

* Tue May 23 2017 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.13-0.1pre1
- rebase to 5.2.13-pre1

* Fri May 05 2017 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.12-4
- removing deprecated escape sequences because of Python-3.6, ship COPYING as license (patch provided by Ville Skyttä)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.12-2
- move back gutenprint folder to base package (bug #1412020)

* Fri Jan 13 2017 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.12-1
- rebase to 5.2.12 - removed foomatic and ghostscript/ijs support

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.2.12-0.5pre4
- Rebuild for Python 3.6

* Mon Oct 31 2016 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.12-0.4pre4
- rebase to 5.2.12-pre4

* Fri Oct 14 2016 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.12-0.4pre3
- rebase to 5.2.12-pre3, adding new share libraries to devel subpackage

* Tue Sep 20 2016 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.12-0.2pre2
- adding new sources

* Tue Sep 20 2016 Zdenek Dohnal <zdohnal@redhat.com> - 5.2.12-0.2pre2
- rebase to 5.2.12-pre2, GhostScript IJS driver and Foomatic data generator were removed from package

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 21 2016 Jiri Popelka <jpopelka@redhat.com> - 5.2.11-1
- 5.2.11

* Tue Oct 06 2015 Jiri Popelka <jpopelka@redhat.com> - 5.2.11-0.2pre2
- 5.2.11-pre2

* Tue Jun 30 2015 Jiri Popelka <jpopelka@redhat.com> - 5.2.11-0.1pre1
- 5.2.11-pre1

* Mon Jun 29 2015 Tim Waugh <twaugh@redhat.com> - 5.2.10-15
- Fix for PPD update script with more than one PPD (bug #1229619).

* Tue Jun 16 2015 Tim Waugh <twaugh@redhat.com> - 5.2.10-14
- Disable test suite again (bug #1069274).

* Mon Jun 01 2015 Jiri Popelka <jpopelka@redhat.com> - 5.2.10-13
- foomatic subpackage requires python3-cups (bug #1226871).

* Fri Apr 10 2015 Tim Waugh <twaugh@redhat.com> - 5.2.10-12
- Enable test suite again to see if bug #1069274 is still current.

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 5.2.10-11
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Thu Jan 15 2015 Tim Waugh <twaugh@redhat.com> - 5.2.10-10
- Require python3-cups to get postscriptdriver() tags.

* Mon Dec  8 2014 Tim Waugh <twaugh@redhat.com> - 5.2.10-9
- Fix tagging of language-specific files (bug #1157347).

* Fri Aug 29 2014 Tim Waugh <twaugh@redhat.com> - 5.2.10-8
- More Python 3 fixes for scripts (bug #1134092).

* Fri Aug 22 2014 Tim Waugh <twaugh@redhat.com> - 5.2.10-7
- Python 3 fixes for scripts (bug #1132924).

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Tomas Radej <tradej@redhat.com> - 5.2.10-5
- Ported scripts to Python 3

* Tue Aug  5 2014 Tim Waugh <twaugh@redhat.com> - 5.2.10-4
- Supply man page for gutenprint-foomaticupdate.
- Link to cups-genppd(8) man page from cups-genppd.5.2(8).

* Mon Aug  4 2014 Tim Waugh <twaugh@redhat.com> - 5.2.10-3
- Link to ijsgutenprint(1) man page from ijsgutenprint.5.2(1).

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Jiri Popelka <jpopelka@redhat.com> - 5.2.10-1
- 5.2.10

* Wed Apr 09 2014 Jiri Popelka <jpopelka@redhat.com> - 5.2.10-0.6.pre2
- Move libraries into separate subpackages (#1085599)
- Remove archaic Provides&Obsoletes

* Mon Mar 10 2014 Jaromír Končický <jkoncick@redhat.com> - 5.2.10-0.5.pre2
- 5.2.10-pre2.

* Mon Mar 10 2014 Jiri Popelka <jpopelka@redhat.com> - 5.2.10-0.4.pre1
- BuildRequires: pkgconfig(foo) instead of foo-devel

* Wed Feb 26 2014 Jaromír Končický <jkoncick@redhat.com> - 5.2.10-0.3.pre1
- Removing check phase because of strange and not reproducible segfault
  (bug #1069274)

* Fri Feb 21 2014 Jiri Popelka <jpopelka@redhat.com> - 5.2.10-0.2.pre1
- BuildRequires libusb1-devel

* Mon Feb 17 2014 Jaromír Končický <jkoncick@redhat.com> - 5.2.10-0.1.pre1
- 5.2.10-pre1.
- Removed: device-ids.patch ui2-libdeps.patch

* Thu Jan  2 2014 Tim Waugh <twaugh@redhat.com> - 5.2.9-15
- Fixed typo in cups-genppdupdate script (bug #1046073).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Tim Waugh <twaugh@redhat.com> - 5.2.9-13
- Run test suite.

* Thu Jun 27 2013 Tim Waugh <twaugh@redhat.com> - 5.2.9-12
- Fixed changelog dates.
- Added some escputil options to the manpage (bug #979064).

* Mon Mar 25 2013 Jiri Popelka <jpopelka@redhat.com> - 5.2.9-11
- Run autoreconf prior to running configure (#925535)

* Tue Feb 19 2013 Jiri Popelka <jpopelka@redhat.com> - 5.2.9-10
- Added IEEE 1284 Device ID for Canon PIXMA MP500 (bug #911727).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Jiri Popelka <jpopelka@redhat.com> 5.2.9-8
- Added IEEE 1284 Device ID for Kyocera FS-1118MFP (bug #782379).
- Use arch-specific dependency when requiring base package.

* Tue Dec 18 2012 Tim Waugh <twaugh@redhat.com> 5.2.9-7
- Don't export yy* symbols (bug #882194).

* Fri Dec 07 2012 Jiri Popelka <jpopelka@redhat.com> 5.2.9-6
- 5.2.9 has had wrong libgutenprintui2 dependencies

* Fri Oct 19 2012 Tim Waugh <twaugh@redhat.com> 5.2.9-5
- Added IEEE 1284 Device IDs for Samsung ML-1450 (bug #844687) and
  Canon ML280 series (bug #848093).

* Fri Sep 21 2012 Tim Waugh <twaugh@redhat.com> 5.2.9-4
- Updated source URL.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Jiri Popelka <jpopelka@redhat.com> 5.2.9-1
- 5.2.9

* Tue Jun 12 2012 Jiri Popelka <jpopelka@redhat.com> 5.2.8-2
- bumped release

* Tue Jun 12 2012 Jiri Popelka <jpopelka@redhat.com> 5.2.8-1
- 5.2.8

* Tue Apr 03 2012 Nils Philippsen <nils@redhat.com> - 5.2.7-11
- rebuild against gimp 2.8.0 release candidate

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Dec 16 2011 Nils Philippsen <nils@redhat.com> - 5.2.7-9
- rebuild for GIMP 2.7

* Mon Nov  7 2011 Tim Waugh <twaugh@redhat.com> 5.2.7-8
- Rebuild for new libpng.

* Tue Oct 11 2011 Tim Waugh <twaugh@redhat.com> 5.2.7-7
- Added IEEE 1284 Device ID for Canon PIXMA MP250 (bug #744087).

* Tue Sep 27 2011 Jiri Popelka <jpopelka@redhat.com> 5.2.7-6
- Use _cups_serverbin macro from cups-devel for where to put driver executables.
- Added IEEE 1284 Device ID for:
    Epson Stylus Photo R2400 (bug #720270)
    Epson Stylus C92 (bug #735400)
    Canon PIXMA iP1900 (bug #741329)
    Canon PIXMA iP4000 (bug #741006)

* Tue Aug 09 2011 Jiri Popelka <jpopelka@redhat.com> 5.2.7-5
- Improve the null-pointer.patch (bug #725447).
- Added IEEE 1284 Device ID for:
    Epson Stylus D78 (bug #245948).

* Tue Jun 28 2011 Tim Waugh <twaugh@redhat.com> 5.2.7-4
- Fixed use of find_lang macro (bug #716426).

* Wed Jun 15 2011 Tim Waugh <twaugh@redhat.com> 5.2.7-3
- Rebuilt against new python-cups package to fix postscriptdriver tags
  (bug #712074).

* Tue Jun  7 2011 Tim Waugh <twaugh@redhat.com> 5.2.7-2
- Fix build against newer versions of gcc.
- cups-genppdupdate: fixed multicat support (bug #711021).  It was
  writing an extra newline character after the URI, which caused the
  gutenprint.5.2 multicat process to exit.  This prevented some
  PPDs from being updated.

* Thu May 05 2011 Jiri Popelka <jpopelka@redhat.com> 5.2.7-1
- 5.2.7.

* Thu Dec 02 2010 Jiri Popelka <jpopelka@redhat.com> 5.2.6-3
- Added IEEE 1284 Device ID for:
    Canon PIXMA iP4200 (bug #626365).
    Canon PIXMA iP3000 (bug #652179).
    Epson Stylus Color 680 (bug #652228).
    Epson Stylus Photo 1270 (bug #638537).
    HP LaserJet 4050/4100/4350/5100/8000/M3027 MFP/M3035 MFP/P3005 (bug #659043).
    HP Color LaserJet 2500/4550 (bug #659044).
    Brother hl-2035 (bug #651603#c3).
- Avoid null pointer access in escputil (bug #659120).

* Fri Nov 26 2010 Tim Waugh <twaugh@redhat.com> 5.2.6-2
- The pycups requirement is now python-cups.

* Wed Aug 11 2010 Jiri Popelka <jpopelka@redhat.com> 5.2.6-1
- 5.2.6.

* Mon Jul 12 2010 Jiri Popelka <jpopelka@redhat.com> 5.2.5-10
- Added COPYING file to main package.

* Thu Jul  8 2010 Jiri Popelka <jpopelka@redhat.com> 5.2.5-9
- Don't ship kitload.log in foomatic sub-package (bug #594709).

* Fri Jun 11 2010 Tim Waugh <twaugh@redhat.com> 5.2.5-8
- Fixed Source0 URL.

* Wed May 12 2010 Jiri Popelka <jpopelka@redhat.com> 5.2.5-7
- Added IEEE 1284 Device ID for:
    Epson Stylus Photo 1400 (bug #577299).
    Epson Stylus Photo 830U (bug #577307).
    HP DeskJet 959C (bug #577291).

* Thu Mar 25 2010 Tim Waugh <twaugh@redhat.com> 5.2.5-6
- Added IEEE 1284 Device ID for Epson Stylus Photo R230 (from Ubuntu #520466).

* Mon Mar  8 2010 Tim Waugh <twaugh@redhat.com> 5.2.5-5
- Added IEEE 1284 Device ID for Epson Stylus D92 (bug #570888).

* Tue Mar  2 2010 Tim Waugh <twaugh@redhat.com> 5.2.5-4
- Better defattr use in file manifests.
- Fixed mixed spaces and tabs.
- Fixed main package summary.
- Added comments for all sources and patches.

* Mon Feb 15 2010 Tim Waugh <twaugh@redhat.com> 5.2.5-3
- The cups sub-package requires the exactly-matching main gutenprint
  package.

* Fri Feb 12 2010 Tim Waugh <twaugh@redhat.com> 5.2.5-2
- 5.2.5.

* Fri Feb  5 2010 Tim Waugh <twaugh@redhat.com> 5.2.4-11
- CUPS driver: if DESTDIR is set, use it when looking for XML files.
  Fixes postscriptdriver tags.

* Thu Feb  4 2010 Tim Waugh <twaugh@redhat.com> 5.2.4-10
- Rebuild for postscriptdriver tags.

* Wed Nov 25 2009 Tim Waugh <twaugh@redhat.com> 5.2.4-9
- The foomatic sub-package requires foomatic-db (for directories).

* Fri Nov 20 2009 Tim Waugh <twaugh@redhat.com> 5.2.4-8
- Don't ship command.types as CUPS defines its own.

* Thu Oct 29 2009 Tim Waugh <twaugh@redhat.com> 5.2.4-7
- Removed incorrect Device ID for Brother HL-2060 (bug #531370).

* Mon Sep 28 2009 Tim Waugh <twaugh@redhat.com> 5.2.4-6
- Reimplemented PPD upgrade script in Python to avoid perl
  dependency (bug #524978).

* Tue Sep  1 2009 Tim Waugh <twaugh@redhat.com> 5.2.4-5
- Provide IEEE 1284 Device IDs in CUPS model list.

* Tue Aug 18 2009 Tim Waugh <twaugh@redhat.com> 5.2.4-4
- Enabled simplified CUPS drivers (bug #518030).

* Mon Aug  3 2009 Tim Waugh <twaugh@redhat.com> 5.2.4-3
- Silence gutenprint-foomaticppdupdate on gutenprint-foomatic upgrade.

* Fri Jul 31 2009 Tim Waugh <twaugh@redhat.com> 5.2.4-2
- 5.2.4.  Re-enabled compiler optimization for ppc64.

* Thu Jul 30 2009 Tim Waugh <twaugh@redhat.com> 5.2.3-8
- Don't show output when upgrading cups sub-package (bug #507324).
- Split documentation into doc sub-package (bug #492452).

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Tim Waugh <twaugh@redhat.com> 5.2.3-6
- Don't build CUPS PPDs (instead build a CUPS driver that can
  generate them).  Fixes build (bug #511538).

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Tim Waugh <twaugh@redhat.com> 5.2.3-4
- When updating foomatic PPDs, don't give a traceback if some PPD is
  not strictly conformant (bug #481397).

* Sat Jan 10 2009 Tim Waugh <twaugh@redhat.com> 5.2.3-3
- Don't use popen2 in the foomatic PPD update script.

* Thu Jan  8 2009 Tim Waugh <twaugh@redhat.com> 5.2.3-2
- Only run the foomatic PPD update script on update, and make sure the
  script can deal with major version upgrades (bug #478328).

* Tue Dec 23 2008 Tim Waugh <twaugh@redhat.com> 5.2.3-1
- 5.2.3.

* Fri Dec  5 2008 Tim Waugh <twaugh@redhat.com> 5.2.2-2
- Fixed generation of globalized PPDs.

* Thu Nov 20 2008 Tim Waugh <twaugh@redhat.com> 5.2.2-1
- 5.2.2.
- Restore SELinux file contexts of modified PPDs.

* Mon Aug  4 2008 Tim Waugh <twaugh@redhat.com>
- Fixed summary for foomatic sub-package.

* Thu Jul 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> 5.0.2-3
- fix license tag

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 5.0.2-2
- Rebuild for GCC 4.3.

* Fri Jan 18 2008 Tim Waugh <twaugh@redhat.com> 5.0.2-1
- 5.0.2.  No longer need lpstat patch.

* Mon Jan  7 2008 Tim Waugh <twaugh@redhat.com>
- Own %%{_datadir}/gutenprint (bug #427801).

* Fri Oct  5 2007 Tim Waugh <twaugh@redhat.com> 5.0.1-5
- Don't ship samples in the main package.

* Fri Aug 31 2007 Tim Waugh <twaugh@redhat.com> 5.0.1-4
- Plug-in name is gutenprint, not print.

* Mon Jul  2 2007 Tim Waugh <twaugh@redhat.com> 5.0.1-3
- The foomatic package requires system-config-printer-libs for the
  update script (bug #246865).

* Mon Jul  2 2007 Tim Waugh <twaugh@redhat.com> 5.0.1-2
- Fix up foomatic PPD files after upgrade (bug #246448).

* Tue Jun 26 2007 Tim Waugh <twaugh@redhat.com> 5.0.1-1
- 5.0.1.

* Thu May 10 2007 Tim Waugh <twaugh@redhat.com> 5.0.0.99.1-3
- Try to work around GCC bug #239003.
- Don't add extra compiler flags.
- Moved gimp-print obsoletes/provides to the foomatic sub-package
  (bug #238890).

* Mon Mar  5 2007 Tim Waugh <twaugh@redhat.com> 5.0.0.99.1-2
- Slightly better obsoletes/provides to follow the naming guidelines.

* Mon Mar  5 2007 Tim Waugh <twaugh@redhat.com> 5.0.0.99.1-1
- 5.0.0.99.1.
- No longer need PPDs sub-packages: CUPS driver is included in the cups
  sub-package.
- Package the CUPS driver in sbindir and put a symlink in the CUPS ServerBin
  directory to work around bug #231015.
- Set POSIX locale when parsing lpstat output.

* Fri Mar  2 2007 Tim Waugh <twaugh@redhat.com> 5.0.0-7
- Fixed menu patch.
- Don't list rastertogutenprint twice.

* Wed Feb 28 2007 Tim Waugh <twaugh@redhat.com>
- Fixed typo in patch line.

* Wed Feb 28 2007 Tim Waugh <twaugh@redhat.com> 5.0.0-6
- Ported menu patch from gimp-print package.
- Fixed summary for plugin sub-package.

* Fri Feb  9 2007 Tim Waugh <twaugh@redhat.com> 5.0.0-5
- More obsoletes/provides for gimp-print sub-packages.

* Fri Jan 19 2007 Tim Waugh <twaugh@redhat.com> 5.0.0-4
- Disable libgutenprintui (GTK+ 1.2 library).  Build requires gtk2-devel,
  not gtk+-devel.

* Tue Jan 16 2007 Tim Waugh <twaugh@redhat.com> 5.0.0-3
- More obsoletes/provides fixing (bug #222546).

* Fri Jan 12 2007 Tim Waugh <twaugh@redhat.com> 5.0.0-2
- Make cups sub-package obsolete/provide gimp-print-cups.
- PPDs sub-packages require cups sub-package.
- Remove foomatic cache after foomatic sub-package is installed/removed.
- Obsoletes/Provides gimp-print-utils.

* Thu Jan 11 2007 Tim Waugh <twaugh@redhat.com> 5.0.0-1
- The cups subpackage no longer requires gimp-print-cups.
- Ship escputil, native CUPS backend/filters, and cups-calibrate.

* Thu Jan 11 2007 Parag Nemade <panemade@gmail.com>- 5.0.0-0.17
- Enabling -plugin subpackage as gimp-print dropped its -plugin subpackage.

* Tue Nov 14 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.16
- Added missing dependency of gimp-print-cups in gutenprint-cups

* Tue Oct 03 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.15
- Did some fix for tag issue

* Fri Sep 29 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.14
- Removed unwanted .la files and made following files owned by 
  main package.
  /usr/share/gutenprint/5.0.0
  /usr/share/gutenprint

* Fri Sep 29 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.13
- Fixed some missing file remove locations path

* Thu Sep 28 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.12
- Fixed rpm build for x86_64 arch

* Fri Sep 08 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.11
- Separated GIMP plugin under gutenprint-plugin package

* Thu Sep 07 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.10
- Added gimp as BR

* Thu Sep 07 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.9
- Removed Requires(post) and Requires(postun) lines in SPEC
- Removed mixed usage of macros

* Wed Aug 09 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.8
- Moved cups related files from main rpm to gutenprint-cups

* Wed Aug 09 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.7
- Moved /usr/share/gutenprint/doc to %%doc of main rpm and devel rpm 
- Additionally added API documents for gutenprint and gutenprintui2

* Tue Aug 08 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.6
- Added cups-genppdupdate.5.0 at post section
- Splitted gutenprint main rpm for separate languages

* Wed Aug 02 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.5
- New upstream release

* Wed Jul 19 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.4.rc3
- Removed Requires on perl-Curses and perl-perlmenu 
  as both are automatically added on binary RPM
- Commented Obsoletes and provides tag as Fedora Extras package can not
  Obsoletes Fedora Core Package.

* Tue Jul 18 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.3.rc3
- Added 3 more sub-packages-extras,cups,foomatic
- Added BuildRequires gtk+-devel
- Added correct options for %%configure
- Added Requires for perl-Curses, perl-perlmenu
- Added cups restart command at post section of SPEC

* Tue Jul 18 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.2.rc3
- Added Obsoletes and Provides tag

* Fri Jul 14 2006 Parag Nemade <panemade@gmail.com>- 5.0.0-0.1.rc3
- Initial Release


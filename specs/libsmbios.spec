# these are all substituted by autoconf
%define pot_file  libsmbios
%define lang_dom  libsmbios-2.4

Name: libsmbios
Version: 2.4.3
Release: 19%{?dist}
Summary: Libsmbios C/C++ shared libraries

License: GPL-2.0-or-later or OSL-2.1
URL: https://github.com/dell/libsmbios
Source0: https://github.com/dell/libsmbios/archive/v%{version}/libsmbios-%{version}.tar.gz

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cppunit-devel
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gettext-devel
BuildRequires: help2man
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: make
BuildRequires: pkgconfig
BuildRequires: python3-devel
BuildRequires: strace
BuildRequires: valgrind

# libsmbios only ever makes sense on intel compatible arches
# no DMI tables on ppc, s390, etc.
ExclusiveArch: x86_64 %{ix86}

%description
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package provides the C-based libsmbios library, with a C interface.

%package -n python3-smbios
Summary: Python interface to Libsmbios C library
Requires: libsmbios = %{version}-%{release}
Requires: python3
Obsoletes: python-smbios < 2.4.1

%description -n python3-smbios
This package provides a Python interface to libsmbios

%package -n smbios-utils
Summary: Meta-package that pulls in all smbios binaries and python scripts
Requires: smbios-utils-bin
Requires: smbios-utils-python

%description -n smbios-utils
This is a meta-package that pulls in the binary libsmbios executables as well
as the python executables.

%package -n smbios-utils-bin
Summary: Binary utilities that use libsmbios
Requires: libsmbios = %{version}-%{release}

%description -n smbios-utils-bin
Get BIOS information, such as System product name, product id, service tag and
asset tag.

%package -n smbios-utils-python
Summary: Python executables that use libsmbios
Requires: python3-smbios = %{version}-%{release}
BuildArch: noarch

%description -n smbios-utils-python
Get BIOS information, such as System product name, product id, service tag and
asset tag. Set service and asset tags on Dell machines. Manipulate wireless
cards/bluetooth on Dell laptops. Set BIOS password on select Dell systems.
Update BIOS on select Dell systems. Set LCD brightness on select Dell laptops.

# name the devel package libsmbios-devel regardless of package name, per suse/fedora convention
%package -n libsmbios-devel
Summary: Development headers and archives
Requires: libsmbios = %{version}-%{release}

%description -n libsmbios-devel
Libsmbios is a library and utilities that can be used by client programs to get
information from standard BIOS tables, such as the SMBIOS table.

This package contains the headers and .a files necessary to compile new client
programs against libsmbios.

%prep
%autosetup -p1

find . -type d -exec chmod -f 755 {} \;
find doc src -type f -exec chmod -f 644 {} \;
chmod 755 src/cppunit/*.sh

%build
# this line lets us build an RPM directly from a git tarball
# and retains any customized version information we might have
[ -e ./configure ] || PACKAGE_VERSION=%{version} ./autogen.sh --no-configure

mkdir _build
cd _build
echo '../configure "$@"' > configure
chmod +x ./configure

%configure

mkdir -p out/libsmbios_c
%make_build CFLAGS+="%{optflags} -Werror" 2>&1 | tee build-%{_arch}.log

%check
runtest() {
    mkdir _$1$2
    pushd _$1$2
    ../configure
    make -e $1 CFLAGS="$CFLAGS -DDEBUG_OUTPUT_ALL"
    touch -r ../configure.ac
    make -e $1
    popd
}

VALGRIND="strace -f" runtest check strace > /dev/null || echo FAILED strace check
runtest valgrind > /dev/null || echo FAILED valgrind check
runtest check > /dev/null || echo FAILED check

%install
cd _build
TOPDIR=..
%make_install
rm -f %{buildroot}/%{_libdir}/lib*.{la,a}
find %{buildroot}/%{_includedir} out/libsmbios_c -exec touch -r $TOPDIR/configure.ac {} \;

rename %{pot_file}.mo %{lang_dom}.mo $(find %{buildroot}/%{_datadir} -name %{pot_file}.mo)
%find_lang %{lang_dom}

%ldconfig_scriptlets

%files -f _build/%{lang_dom}.lang
# Only need to include license once here
%license COPYING-GPL COPYING-OSL
%{_libdir}/libsmbios_c.so.*

%files -n libsmbios-devel
%license src/bin/getopts_LICENSE.txt src/include/smbios_c/config/boost_LICENSE_1_0_txt
%doc _build/out/libsmbios_c
%{_includedir}/smbios_c
%{_libdir}/libsmbios_c.so
%{_libdir}/pkgconfig/*.pc

%files -n smbios-utils

%files -n smbios-utils-bin
%license src/bin/getopts_LICENSE.txt src/include/smbios_c/config/boost_LICENSE_1_0_txt
%{_sbindir}/smbios-state-byte-ctl
%{_mandir}/man?/smbios-state-byte-ctl.*
%{_sbindir}/smbios-get-ut-data
%{_mandir}/man?/smbios-get-ut-data.*
%{_sbindir}/smbios-upflag-ctl
%{_mandir}/man?/smbios-upflag-ctl.*
%{_sbindir}/smbios-sys-info-lite
%{_mandir}/man?/smbios-sys-info-lite.*

%files -n python3-smbios
%{python3_sitearch}/*

%files -n smbios-utils-python
%license src/bin/getopts_LICENSE.txt src/include/smbios_c/config/boost_LICENSE_1_0_txt
%dir %{_sysconfdir}/libsmbios
%config(noreplace) %{_sysconfdir}/libsmbios/*

# python utilities
%{_sbindir}/smbios-battery-ctl
%{_mandir}/man?/smbios-battery-ctl.*
%{_sbindir}/smbios-sys-info
%{_mandir}/man?/smbios-sys-info.*
%{_sbindir}/smbios-token-ctl
%{_mandir}/man?/smbios-token-ctl.*
%{_sbindir}/smbios-passwd
%{_mandir}/man?/smbios-passwd.*
%{_sbindir}/smbios-wakeup-ctl
%{_mandir}/man?/smbios-wakeup-ctl.*
%{_sbindir}/smbios-wireless-ctl
%{_mandir}/man?/smbios-wireless-ctl.*
%{_sbindir}/smbios-lcd-brightness
%{_mandir}/man?/smbios-lcd-brightness.*
%{_sbindir}/smbios-keyboard-ctl
%{_mandir}/man?/smbios-keyboard-ctl.*
%{_sbindir}/smbios-thermal-ctl
%{_mandir}/man?/smbios-thermal-ctl.*

# data files
%{_datadir}/smbios-utils

%changelog
* Thu Jul 24 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 02 2025 Python Maint <python-maint@redhat.com> - 2.4.3-18
- Rebuilt for Python 3.14

* Tue Feb 11 2025 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.4.3-17
- Drop build logs from package payload and make python subpackage noarch

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.4.3-14
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Sérgio Basto <sergio@serjux.com> - 2.4.3-11
- Use make macros https://src.fedoraproject.org/rpms/libsmbios/pull-request/5

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.4.3-9
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.4.3-6
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4.3-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 2.4.3-1
- Update to 2.4.3

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-8
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.4.2-5
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pete Walter <pwalter@fedoraproject.org> - 2.4.2-1
- Update to 2.4.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.4.1-3
- Rebuilt for Python 3.7

* Wed Apr 18 2018 Karsten Hopp <karsten@redhat.com> - 2.4.1-2
- rebuild with latest rpm build flags (rhbz#1540264)

* Wed Feb 14 2018 Peter Jones <pjones@redhat.com> - 2.4.1-1
- Update for libsmbios 2.4.1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Pete Walter <pwalter@fedoraproject.org> - 2.3.3-2
- Remove obsolete python-ctypes requires (#1399686)

* Tue Nov 14 2017 Pete Walter <pwalter@fedoraproject.org> - 2.3.3-1
- Update to 2.3.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Mar 09 2016 Peter Jones <pjones@redhat.com> - 2.3.0-2
- Once again, don't complain about compilers newer than tested with in the
  public headers.
- Fix up bad %%global vs %%define directives
- Fix up bad old changelog dates
- Note there's a missing changelog here from the 2.3.0 rebase

* Thu Feb 25 2016 Peter Jones <pjones@redhat.com> - 2.2.28-16
- Don't complain about compilers newer than tested with in the public
  headers.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.28-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Sep 1 2015 Srinivas G Gowda <srinivas_g_gowda@dell.com> - 2.2.28-14
- Fixes Bug 852719: Dell Open Manage falis to start when libsmbios in EPEL branch is used.
- Patch re-enables display of "OEM String" in smbios-sys-info-lite.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.28-12
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.28-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.28-6
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 30 2011 Praveen K Paladugu <praveen_paladugu@dell.com> 2.2.28-4
- Adding the right tar ball, coz files were missing from the previous version. 

* Thu Jun 30 2011 Praveen K Paladugu <praveen_paladugu@dell.com> - 2.2.28-3
- Fixing the build failure of version 2.2.26-4.
- The updated sources adds support for the compiler version available in F15 and other fixes.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 27 2010 Matt Domsch <mdomsch@fedoraproject.org> - 2.2.26-3
- build for Fedora 15

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.2.19-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 06 2010 Michael Brown <michael-e_brown at dell.com> - 2.2.26-1
- implement CSV export of token settings from smbios-token-ctl

* Tue Jul 06 2010 Michael Brown <michael-e_brown at dell.com> - 2.2.25-1
- Fix breakage resulting from improperly fixing up constructors for MemoryAccess/CmosAccess. Fixes CLI utilities.

* Fri Jun 11 2010 Michael Brown <michael-e_brown at dell.com> - 2.2.23-1
- Fixup ABI break where a couple functions that should have been exported were not marked.

* Thu Jun 10 2010 Michael Brown <michael-e_brown at dell.com> - 2.2.22-1
- Fixup bug in reading asset and service tag where it A) read checksum from wrong location and B) used wrong comparison check to validate it
- enable service tag SET for machines that still set service tag in CMOS
- ABI/API - change to -fvisibility=hidden for libsmbios_c.so.*, mark public api's. This removes all non-public symbols that were not formerly part of the ABI from the dynamic link table.

* Mon May 18 2009 Matt Domsch <Matt_Domsch@dell.com> - 2.2.16-3
- split yum plugin into yum-dellsysid package

* Tue Mar 24 2009 Michael E Brown <michael_e_brown at dell.com> - 2.2.16-1
- add gcc 4.4 support

* Tue Mar 24 2009 Michael E Brown <michael_e_brown at dell.com> - 2.2.15-1
- update to lastest upstream.
- fixes bug in bios update on systems with versions like x.y.z.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 3 2009 Michael E Brown <michael_e_brown at dell.com> - 2.2.12-1
- Add feature to turn on debugging printf()'s without recompiling by setting
  certain environment variables:
    LIBSMBIOS_C_DEBUG_OUTPUT_ALL    -- all debugging output
        or, per module:
    LIBSMBIOS_C_DEBUG_CONSTRUCTOR_C
    LIBSMBIOS_C_DEBUG_SYSINFO_C
    LIBSMBIOS_C_DEBUG_SMBIOS_C
    LIBSMBIOS_C_DEBUG_TOKEN_C
    LIBSMBIOS_C_DEBUG_MEMORY_C
    LIBSMBIOS_C_DEBUG_CMOS_C
    LIBSMBIOS_C_DEBUG_SMI_C

* Mon Feb 2 2009 Michael E Brown <michael_e_brown at dell.com> - 2.2.12-1
- Add pkgconfig files to -devel
- fixup yum plugin to not parse certain data that causes a crash on some machines (Optiplex 755, others may be affected)

* Thu Jan 15 2009 Michael E Brown <michael_e_brown at dell.com> - 2.2.8-1
- revert change in upstream renaming rpm to libsmbios2

* Thu Jan 15 2009 Michael E Brown <michael_e_brown at dell.com> - 2.2.7-1
- change source to bz2 format
- Update to latest upstream release. Many changes in the new release:
  - python interface
  - libsmbios_c interface almost fully implemented
  - libsmbios c++ interface deprecated

* Tue Oct 28 2008 Michael E Brown <michael_e_brown at dell.com> - 2.2.0-1
- Spec updates

* Mon Apr 21 2008 Michael E Brown <michael_e_brown at dell.com> - 2.0.1-2.1
- obsolete libsmbios-libs as well

* Mon Mar 3 2008 Michael E Brown <michael_e_brown at dell.com> - 2.0.1-2
- properly obsolete older versions

* Wed Feb 13 2008 Michael E Brown <michael_e_brown at dell.com> - 2.0.1
- Fixup GCC 4.3 compile issues.

* Wed Jan 9 2008 Michael E Brown <michael_e_brown at dell.com> - 2.0.0
- ABI incompatible, minor API changes
- sync up libsmbios soname with version #
- move binaries to /usr/sbin as they are only runnable by root
- drop libsmbiosxml lib as it was mostly unused.
- drop autotools generated files out of git and add autogen.sh
- drop tokenCtl binary-- pysmbios has a *much* improved version

* Wed Aug 22 2007 Michael E Brown <michael_e_brown at dell.com> - 0.13.9
- Fix a couple of failure-to-check-return on fopen. most were unit-test code
  only, but two or three were in regular code.
- Add hinting to the memory class, so that it can intelligently close /dev/mem
  file handle when it is not needed (which is most of the time). it only
  leaves it open when it is scanning, so speed is not impacted.

* Mon Aug 6 2007 Michael E Brown <michael_e_brown at dell.com> - 0.13.8
- new upstream

* Tue Apr 3 2007 Michael E Brown <michael_e_brown at dell.com> - 0.13.6
- critical bugfix for dellBiosUpdate utility for packet mode
- autoconf/automake support for automatically building docs
- more readable 'make' lines by splitting out env vars
- remove run_cppunit option... always run unit tests.
- update autoconf/automake utilities to latest version
- fix LDFLAGS to not overwrite user entered LDFLAGS
- add automatic doxygen build of docs
- fix urls of public repos
- remove yum repo page in favor of official page from docs
- split dmi table entry point from smbios table entry point
- support legacy _DMI_ tables
- fix support for EFI-based imacs without proper _SM_ anchor

* Tue Mar 20 2007 Michael E Brown <michael_e_brown at dell.com> - 0.13.5
- rpmlint cleanups
- Add dellLEDCtl binary
- update AUTHORS file to add credit for dellLEDCtl
- update doc/DellToken.txt to add a few more useful tokens.
- updated build system to create documentation
- skip cppunit dep on .elX builds (not in EPEL yet)

* Mon Mar 12 2007 Michael E Brown <michael_e_brown at dell.com> - 0.13.4-1
- Added dellWirelessCtl binary
- Added 'static' makefile target to build static binaries and clean them as well
- fix for signed/unsigned bug in probes binary. CPU temp misreported
- simplify interface for DELL_CALLING_INTERFACE_SMI, autodetect Port/Magic
- document all of the tokens for controlling wireless on dell notebooks
- enums for SMI args/res to make code match docs better (cbRES1 = res[0], which
  was confusing.
- helper functions isTokenActive() and activateToken() to simplify token API.
- Added missing windows .cpp files to the dist tarball for those who compile
  windows from dist tarball vs source control
- Add support for EFI based machines without backwards compatible smbios table
  entry point in 0xF0000 block.
- Added wirelessSwitchControl() and wirelessRadioControl() API for newer
  laptops.
- fixed bug in TokenDA activate() code where it wasnt properly using SMI
  (never worked, but apparently wasnt used until now.)

* Tue Oct 3 2006 Michael E Brown <Michael_E_Brown@Dell.com> - 0.13.0-1
- autotools conversion
- add Changelog

* Tue Sep 26 2006 Michael E Brown <michael_e_brown at dell.com> - 0.12.4-1
- Changes per Fedora Packaging Guidelines to prepare to submit to Extras.
- Add in a changelog entry per Fedora Packaging Guidelines...


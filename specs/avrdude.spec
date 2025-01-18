%global udev_rules_old 70-avrdude-devices.rules
%global udev_rules_gen 71-avrdude-devices.rules

# Allow skipping doc builds for faster mockbuilds without the
# literally hundreds of extra packages required for building docs.
%bcond_without docs

Name:           avrdude
Version:        8.0
Release:        6%{?dist}
Summary:        Software for programming Atmel AVR Microcontroller

License:        GPL-2.0-or-later AND GPL-3.0-only AND (WTFPL OR MIT)
URL:            https://github.com/avrdudes/avrdude

# Upstream avrdude have no 4big endian support planned.
# https://bugzilla.redhat.com/show_bug.cgi?id=2308947
# https://github.com/avrdudes/avrdude/issues/1917
ExcludeArch:    s390x

Source0:        https://github.com/avrdudes/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Debian have a more comprehensive list of programmer devices in their
# avrdude.dev file. We do cannot use this unchanged, though, as we do
# not want to grant blanket access to all ttyUSB and ttyACM devices.
# Source1:        https://salsa.debian.org/debian/avrdude/-/raw/master/debian/avrdude.udev
Source1:        avrdude.udev

# Remarks on the Fedora package for the users
Source2:        README.fedora

# Quick fix elf2tag man page
Source5:        elf2tag.1

# Stop granting blanket access to all /dev/tty{ACM,USB}* devices
Patch:          avrdude-udev-no-blanket-access.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  elfutils-libelf-devel
BuildRequires:  hidapi-devel
%if ((0%{?fedora} >= 1) || (0%{?rhel} >= 8))
BuildRequires:  libgpiod-devel
%endif
%if ((0%{?fedora} >= 1) || (0%{?rhel} >= 9))
BuildRequires:  libserialport-devel
%endif
# EL does not have libhid-devel
%if 0%{?fedora} >= 28
BuildRequires:  libhid-devel
%endif
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  libftdi-devel
BuildRequires:  pkgconfig(libusb-1.0)
%if %{with docs}
BuildRequires:  texi2html
BuildRequires:  texinfo
BuildRequires:  texinfo-tex
%endif
BuildRequires:  make

# https://fedoraproject.org/wiki/Changes/RemoveObsoleteScriptlets
%if !((0%{?fedora} >= 28) || (0%{?rhel} >= 8))
%{error:No install-info scriptlets for Fedora prior to F28 or EL prior to EL8.}
%endif


%description
AVRDUDE is a program for programming Atmel's AVR CPU's. It can program the
Flash and EEPROM, and where supported by the serial programming protocol, it
can program fuse and lock bits. AVRDUDE also supplies a direct instruction
mode allowing one to issue any programming instruction to the AVR chip
regardless of whether AVRDUDE implements that specific feature of a
particular chip.


%prep
%setup -q -n %{name}-%{version}
cp -p %{SOURCE1} avrdude.udev
%autopatch -v -p1
if test -d atmel-docs; then
  echo "Directory 'atmel-docs' still exists, aborting."
  exit 2
fi
sed -i 's|^find_package(SWIG|\# find_package(SWIG|' CMakeLists.txt


%build
%cmake \
       -D CMAKE_INSTALL_SYSCONFDIR:PATH=%{_sysconfdir} \
       -D CMAKE_BUILD_TYPE=build_type=RelWithDebInfo \
%if %{with docs}
       -D BUILD_DOC:BOOL=ON \
%else
       -D BUILD_DOC:BOOL=OFF \
%endif
       -D HAVE_LINUXSPI:BOOL=ON \
       -D HAVE_LINUXGPIO:BOOL=ON \
       -D HAVE_PARPORT:BOOL=ON \
       -D FETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
       -D FETCHCONTENT_QUIET:BOOL=OFF \
       -D BUILD_SHARED_LIBS:BOOL=NO \
       -D USE_STATIC_LIBS:BOOL=YES

if test -d _deps; then
  echo "cmake appears to have fetched some dependency despite our precautions:"
  ls -l _deps
  exit 2
fi

%cmake_build

# generate set of udev rules from avrdude.conf
%{__cmake_builddir}/src/avrdude -C %{__cmake_builddir}/src/avrdude.conf -c '*/u' \
  | sed -n '/ACTION!=/,$p' \
  | sed 's|, MODE="0660"||' \
  > genset.rules
test -s genset.rules


%install
%cmake_install

rm -f $RPM_BUILD_ROOT%{_infodir}/dir

rm -f $RPM_BUILD_ROOT%{_includedir}/libavrdude-avrintel.h
rm -f $RPM_BUILD_ROOT%{_includedir}/libavrdude.h
rm -f $RPM_BUILD_ROOT%{_libdir}/libavrdude.a

install -d -m 755              $RPM_BUILD_ROOT%{_udevrulesdir}
install -p -m 644 avrdude.udev $RPM_BUILD_ROOT%{_udevrulesdir}/%{udev_rules_old}
install -p -m 644 genset.rules $RPM_BUILD_ROOT%{_udevrulesdir}/%{udev_rules_gen}

install -d -m 755            $RPM_BUILD_ROOT%{_pkgdocdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_pkgdocdir}/README.fedora
install -p -m 644         -t $RPM_BUILD_ROOT%{_pkgdocdir} AUTHORS NEWS README.md

install -d -m 755            $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_mandir}/man1/elf2tag.1


%check
%ctest


%files
%license COPYING
%doc %{_pkgdocdir}/AUTHORS
%doc %{_pkgdocdir}/NEWS
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/README.fedora
%if %{with docs}
%doc %{_pkgdocdir}/avrdude-html/
%doc %{_pkgdocdir}/avrdude.pdf
%endif
%config(noreplace) %{_sysconfdir}/avrdude.conf
%{_udevrulesdir}/%{udev_rules_old}
%{_udevrulesdir}/%{udev_rules_gen}
%{_bindir}/avrdude
%{_bindir}/elf2tag
%{_mandir}/man1/avrdude.1*
%{_mandir}/man1/elf2tag.1*
%if %{with docs}
%{_infodir}/avrdude.info*
%endif


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Sep  1 2024 Hans Ulrich Niedermann <hun@n-dimensional.de> - 8.0-5
- ExcludeArch: s390x (#2308947)
- Add elf2tag.1 man page

* Fri Aug 30 2024 Hans Ulrich Niedermann <hun@n-dimensional.de> - 8.0-4
- Actually ship static copy of udev rules as s390x workaround

* Fri Aug 30 2024 Hans Ulrich Niedermann <hun@n-dimensional.de> - 8.0-3
- Ship static copy of udev rules as s390x workaround

* Thu Aug 29 2024 Hans Ulrich Niedermann <hun@n-dimensional.de> - 8.0-2
- Rebuilt for forgotten new-sources

* Sun Aug 25 2024 Hans Ulrich Niedermann <hun@n-dimensional.de> - 8.0-1
- Update to avrdude-8.0 release (#2307778)
- Enable libserialport support
- Build without old pre-1.0 libusb
- Build with libgpiod
- Move config file from /etc/avrdude/avrdude.conf to /etc/avrdude.conf
- Continue not shipping libavrdude library due to unstable API/ABI
- Do not build/ship libavrdude SWIG bindings (unstable API/ABI)
- Do not build/ship avrdude GUI based on the SWIG bindings
- Add new set of autogenerated udev rules

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Feb  7 2024 Hans Ulrich Niedermann <hun@n-dimensional.de> - 7.3-1
- Update to avrdude-7.3 release
- Enable linuxgpio (without libgpiod, though)

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Hans Ulrich Niedermann <hun@n-dimensional.de> - 7.2-1
- Updated to upstream avrdude-7.2 release from github.com (rhbz#2251649)
- Filter upstream release tarball to remove pdf docs due to licensing
- Migrated to SPDX license
- Switched to cmake build system
- Fixed upstream cmake detection of libreadline.so
- Switched to upstream's new URL (github instead of nongnu.org)
- Stop shipping PS doc format in favour of just avrdude.pdf
- Keep avrdude.conf at the old Fedora location /etc/avrdude/ for now

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.4-3
- Add README.fedora explaining USB device permission setup

* Wed Apr 20 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.4-2
- Install built documentation directly to %%{_pkgdocdir}
- Fix file locations in man page, texinfo docs
- Upstream already has fixed these files' x bits
- Disable silent rules to help with build problems
- Stop granting user access to ALL /dev/tty{ACM,USB}* devices
- Enable parallel port support
- Update BuildReqs for libusb* to use pkgconfig(...)
- Update URLS from http: to https: in spec file
- Fix date of 6.4-1 changelog entry

* Fri Feb 04 2022 Dan Horák <dan[at]danny.cz> - 6.4-1
- update to 6.4
- switch to Debian udev rules
- enable Linux SPI driver

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 6.3-16
- Remove hardcoded gzip suffix from GNU info pages

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.3-15
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 6.3-8
- Rebuild for readline 7.x

* Sat May 21 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.3-7
- Update to avrdude-6.3 release
- Build avrdude with linuxgpio support
- Do not ship new libavrdude as avrdude executable is statically linked

* Sat May 21 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.1-6
- Build avrdude with libhid and hidapi support

* Sat May 21 2016 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.1-5
- Build avrdude with libelf ELF support (#1325530)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 14 2014 Hans de Goede <hdegoede@redhat.com> - 6.1-1
- Upgrade to new upstream release 6.1 (rhbz#1056138)
- Some supported devices will only get build if libusb-0.1 is present, so
  build with both libusb-0.1 and libusbx-1.0

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 6.0.1-2
- Build with libusbx and libfdti 1

* Sat Mar 08 2014 Hans de Goede <hdegoede@redhat.com> - 6.0.1-1
- Upgrade to new upstream release 6.0.1 (rhbz#1056138)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 jcapik@redhat.com - 5.11.1-4
- Fixing texi errors (causing builds to fail)
- Introducing aarch64 support (#925062)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 22 2012 ndim <hun@n-dimensional.de> - 5.11.1-1
- Update to avrdude-5.11.1
- Build support for FTDI based devices (#742044)
- Use mktemp based BuildRoot for improved local .rpm building

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 12 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 5.11-1
- Update to avrdude-5.11

* Wed Mar 02 2011 Hans Ulrich Niedermann <hun@n-dimensional.de> - 5.10-3
- Rebuilt package from fixed sources (unchanged package content)
- Unify pkg source in git for el6, f13, f14, f15, rawhide

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 19 2010 Bart Vanbrabant <bart.vanbrabant@zoeloelip.be> - 5.10-1
- New upstream version. Several new devices and programmers supported. Some
  bugfixes and a new features to apply external reset if JTAG ID could not be
  read.

* Thu Sep 3 2009 Bart Vanbrabant <bart.vanbrabant@zoeloelip.be> - 5.8-1
- New upstream version: See the NEWS file for more information
- Removed patch: changes are included in upstream version

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.5-3
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Trond Danielsen <trond.danielsen@gmail.com> - 5.5-2
- Added patch for 64-bit systems.
- Corrected the URL to the avrude homepage.

* Sat Dec 29 2007 Trond Danielsen <trond.danielsen@gmail.com> - 5.5-1
- New upstream version
- Fixed minor rpmlint warning.

* Fri Mar 02 2007 Trond Danielsen <trond.danielsen@gmail.com> - 5.3.1-5
- Added missing BuildRequire tetex-dvips.

* Thu Mar 01 2007 Trond Danielsen <trond.danielsen@gmail.com> - 5.3.1-4
- Updated list of files.
- Corrected sed line in prep section.

* Wed Feb 28 2007 Trond Danielsen <trond.danielsen@gmail.com> - 5.3.1-3
- Added missing BuildRequires.
- Enable generation of documentation.
- Updated path to avrdude.conf in info page.

* Wed Feb 28 2007 Trond Danielsen <trond.danielsen@gmail.com> - 5.3.1-2
- Added missing BuildRequires readline-devel and ncurses-devel.
- Changed config file to noreplace and moved to separate folder.
- Corrected permission for file debuginfo package.

* Wed Feb 28 2007 Trond Danielsen <trond.danielsen@gmail.com> - 5.3.1-1
- Initial version.

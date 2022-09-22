%global udev_rules 70-avrdude_usbprog.rules

Name:           avrdude
Version:        6.4
Release:        4%{?dist}
Summary:        Software for programming Atmel AVR Microcontroller

License:        GPLv2+
URL:            https://www.nongnu.org/avrdude
Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:        https://salsa.debian.org/debian/avrdude/-/raw/master/debian/avrdude.udev
Source2:        README.fedora
# From: https://savannah.nongnu.org/bugs/?42517
Patch0:         avrdude-6.1_includes.patch
# Stop granting blanket access to all /dev/tty{ACM,USB}* devices
Patch1:         avrdude-udev-no-blanket-access.patch
# Mention proper doc and config file locations in texinfo documentation
Patch2:         avrdude-6.4-fix-file-locations-in-docs.patch

BuildRequires:  gcc
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  elfutils-libelf-devel
BuildRequires:  hidapi-devel
BuildRequires:  libhid-devel
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  libftdi-devel
BuildRequires:  pkgconfig(libusb)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  texi2html
BuildRequires:  texinfo-tex
BuildRequires:  tetex-dvips
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
%setup -q
cp -p %{SOURCE1} avrdude.udev
%patch0 -p0 -b .patch0
%patch1 -p1 -b .patch1
%patch2 -p1 -b .patch2

sed -i 's|${PREFIX}/etc/avrdude\.conf|/etc/avrdude/avrdude.conf|g' avrdude.1
sed -i 's|${PREFIX}/share/doc/avrdude/avrdude\.pdf|%{_pkgdocdir}/avrdude.pdf|g' avrdude.1

iconv -f ISO88591 -t UTF8 < ChangeLog-2003 > ChangeLog-2003~
mv ChangeLog-2003~ ChangeLog-2003
iconv -f ISO88591 -t UTF8 < NEWS > NEWS~
mv NEWS~ NEWS


%build
%configure --disable-silent-rules --enable-doc --enable-linuxgpio --enable-linuxspi --enable-parport --sysconfdir=%{_sysconfdir}/%{name}
%make_build


%install
%make_install DOC_INST_DIR="$RPM_BUILD_ROOT%{_pkgdocdir}"
rm -f $RPM_BUILD_ROOT%{_includedir}/libavrdude.h
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
rm -f $RPM_BUILD_ROOT%{_libdir}/libavrdude.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libavrdude.la
rm -f $RPM_BUILD_ROOT%{_libdir}/libavrdude.so
rm -f $RPM_BUILD_ROOT%{_libdir}/libavrdude.so.1
rm -f $RPM_BUILD_ROOT%{_libdir}/libavrdude.so.1.0.0
install -d -m 755 $RPM_BUILD_ROOT%{_udevrulesdir}
install -p -m 644 avrdude.udev $RPM_BUILD_ROOT%{_udevrulesdir}/%{udev_rules}
install -d -m 755 $RPM_BUILD_ROOT%{_pkgdocdir}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_pkgdocdir}/README.fedora


%files
%doc README AUTHORS ChangeLog* COPYING NEWS doc/TODO
%doc %{_pkgdocdir}/README.fedora
%doc %{_pkgdocdir}/avrdude-html/
%doc %{_pkgdocdir}/avrdude.pdf
%doc %{_pkgdocdir}/avrdude.ps
%config(noreplace) %{_sysconfdir}/%{name}
%{_udevrulesdir}/%{udev_rules}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_infodir}/%{name}.info.*


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Apr 20 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.4-3
- Add README.fedora explaining USB device permission setup

* Wed Apr 20 2022 Hans Ulrich Niedermann <hun@n-dimensional.de> - 6.4-2
- Install built documentation directly to %{_pkgdocdir}
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

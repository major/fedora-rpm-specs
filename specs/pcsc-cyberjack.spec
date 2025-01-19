%global readers_dir %(pkg-config libpcsclite --variable=usbdropdir)


Name:		pcsc-cyberjack
Summary:	PC/SC driver for REINER SCT cyberjack USB chip card reader
Version:	3.99.5final.SP15
%global version_prefix %(c=%{version}; echo ${c:0:6})
%global version_suffix %(c=%{version}; echo ${c:12:4})
Release:	10%{?dist}
License:	GPLv2+ and LGPLv2+
URL:		https://www.reiner-sct.com/
Source0:	https://support.reiner-sct.de/downloads/LINUX/V%{version_prefix}_%{version_suffix}/%{name}_%{version}.tar.bz2
Source1:	pcsc-cyberjack-3.99.5final.SP09-README-FEDORA
Source2:	libifd-cyberjack6.udev
# this patch replaces the obsoleted AC_PROG_LIBTOOLT macro with LT_INIT
# the patch is sent to upstream per email (20160528)
Patch0:		pcsc-cyberjack-3.99.5final.SP09-configure.patch

Requires:	udev
Requires:	pcsc-lite
Requires(pre):	shadow-utils

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	libusb1-devel
BuildRequires:	readline-devel
BuildRequires:	libsysfs-devel
BuildRequires:	pcsc-lite-devel >= 1.3.0
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires:	systemd-rpm-macros
%else
BuildRequires:	systemd
%endif
%{?systemd_requires}

%package cjflash
Summary:	Flash tool for cyberJack
Requires:	%{name}%{?_isa} = %{version}-%{release}

%package examples
Summary:	Sample code
Requires:	%{name} = %{version}-%{release}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
BuildArch:	noarch

%description
REINER SCT cyberJack USB chip card reader user space driver.

This package includes the IFD driver for the cyberJack non-contact (RFID)
and contact USB chip card reader.

For more information regarding installation under Linux see the README.txt
in the documentation directory, esp. regarding compatibility with host
controllers.

For more information about the reader, software updates and a shop see
https://www.reiner-sct.com/

%description cjflash
Tool to flash Reiner SCT cyberJack card readers.

%description examples
Sample code to use/test SCardControl() API by Ludovic Rousseau.

%prep
%setup -q
%patch -P0 -p1
autoreconf --force --install

# README-FEDORA
install -pm 644 %{SOURCE1} README-FEDORA.txt

%build
# while the docs say --enable-udev will create udev files, I get no rule
# in etc/udev, so making my own later, based on debian one
%configure \
	--disable-static \
	--enable-pcsc \
	--sysconfdir="%{_sysconfdir}" \
	--with-usbdropdir="%{readers_dir}" \
	--enable-release \
	--enable-udev \
	--enable-hal=no

%make_build
pushd doc
for file in LIESMICH.txt README.txt; do
  iconv -f iso-8859-1 -t utf-8 $file -o $file.conv
  touch -c -r $file $file.conv
  mv -f $file.conv $file
done
popd

# cjflash does not get built automatically
pushd tools/cjflash
%make_build
popd

%install
%make_install
rm %{buildroot}%{readers_dir}/libifd-cyberjack.bundle/Contents/Linux/libifd-cyberjack.la
mv %{buildroot}/etc/cyberjack.conf.default %{buildroot}/etc/cyberjack.conf

# udev rule from Debian, historically part of the debian sub-folder
# we need the devices to be in group cyberjack, not in group pcscd
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/93-cyberjack.rules
sed -e 's/GROUP="pcscd"/GROUP="cyberjack"/' -i %{buildroot}%{_udevrulesdir}/93-cyberjack.rules
touch -c -r %{SOURCE2} %{buildroot}%{_udevrulesdir}/93-cyberjack.rules

# cjflash does not get installed automatically
pushd tools/cjflash
%make_install
popd

%pre
getent group cyberjack >/dev/null || groupadd -r cyberjack

%post
%udev_rules_update
systemctl try-restart pcscd.socket
exit 0

%postun
%udev_rules_update
if [ $1 -eq 0 ]; then
  systemctl try-restart pcscd.socket
fi
exit 0

%files
# AUTHORS and ChangeLog do not contain actual information
%doc etc/cyberjack.conf.default README-FEDORA.txt debian/changelog
%doc doc/README.txt doc/README.pdf doc/README.html
%doc doc/LIESMICH.txt doc/LIESMICH.pdf doc/LIESMICH.html
%license COPYING COPYRIGHT.GPL COPYRIGHT.LGPL

%{_udevrulesdir}/93-cyberjack.rules
%{readers_dir}/libifd-cyberjack.bundle/

%config(noreplace) %{_sysconfdir}/cyberjack.conf


%files cjflash
%{_bindir}/cjflash
%license COPYING

%files examples
%doc doc/verifypin_ascii.c doc/verifypin_fpin2.c

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 3.99.5final.SP15-9
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP15-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Robert Scheck <robert@fedoraproject.org> - 3.99.5final.SP15-1
- Update to new upstream version SP15 (#2034951)
- Remove upstream stub ChangeLog file (#2031120)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Robert Scheck <robert@fedoraproject.org> - 3.99.5final.SP14-1
- Update to new upstream version SP14 (#1847488)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Jeff law <law@redhta.com> - 3.99.5final.SP13-2
- Fix narrowing convesion problem caught by gcc-10

* Sun Sep 01 2019 Robert Scheck <robert@fedoraproject.org> - 3.99.5final.SP13-1
- Update to new upstream version SP13 (#1554806)
- Drop requirements for 'initscripts' from specfile (#1592381)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP12-1
- new upstream version
- man8/cyberjack.8 no longer present it seems

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP11-3
- Added BuildRequires for gcc and gcc-c++.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Aug 11 2017 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP11-1
- New upstream release, fixes #1480509.
- Create source-url dynamically, so it can be used by
  upstream-release-monitoring.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP09-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP09-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP09-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri May 27 2016 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP09-1
- New upstream, which fixes an usb-bug.
- Gui finally removed by upstream, was not build/packaged anyway.
- The cyberjack binary, used for troubleshooting the install, was also
  removed upstream.

* Fri Feb 05 2016 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP08-4
- Add patch to build with gcc6 on rawhide.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.99.5final.SP08-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 10 2015 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP08-2
- The devices created by udev have to be in group "cyberjack", not in "pcscd"

* Mon Dec 07 2015 Jens Lody <fedora@jenslody.de> - 3.99.5final.SP08-2
- new upstream
- cleaned up spec-file to follow actual guidelines
- remove unneeded stuff from spec-file

* Sat Jul 18 2015 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP07-3
- adjusted patch, submitted by Jens, this one works on epel6 as well [1195002]

* Tue Jul 14 2015 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP07-2
- include Jens' PIN_VERIFY_MODIFY_STRUCTURE patch [1195002]

* Fri Jul 10 2015 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP07-1
- new upstream version
- not calling autoconf

* Tue Jun 23 2015 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP05-4
- added autoconf to build requires

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.5final.SP05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.5final.SP05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP05-1
- new upstream version
- when working past midnight, do not only look at day number when writing changelog date. Fixed two bogus dates.

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.5final.SP03-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jul 31 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.99.5final.SP03-14
- Fix build with unversioned %%{_docdir_fmt}.

* Thu Apr 25 2013 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-13
- removed /usr/lib64/cyberjack/pcscd_init.diff (#956604)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.99.5final.SP03-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 19 2013 Robert Scheck <robert@fedoraproject.org> 3.99.5final.SP03-11
- allow same package to be built on Red Hat Enterprise Linux

* Mon Oct 22 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-10
- moved udev rule

* Mon Oct 22 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-9
- added link to fedora-15-cyberjack-kartenleser-in-betrieb-nehmen to README-FEDORA.txt
- removed redirect of sysctl output to dev null
- fixed typos in description
- set the udev rule to be a non-replaced config

* Sun Oct 14 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-8
- move to systemd

* Sat Jun 2 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-7
- use %%{_mandir} in configure

* Fri Jun 1 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-6
- added unistd patch

* Wed Feb 29 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-5
- using /sbin/service again so this works on F16, F17, RHEL5 and RHEL6

* Sat Feb 25 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-4
- gui now only built if withGUI set

* Sat Feb 25 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-3
- back out man page patch
- change configure flags to match http://sources.gentoo.org/cgi-bin/viewvc.cgi/gentoo-x86/dev-libs/cyberjack/cyberjack-3.99.5_p02-r1.ebuild?view=markup

* Fri Feb 24 2012 Patrick C. F. Ernzer <pcsc-cyberjack.spec@pcfe.net> 3.99.5final.SP03-2
- cleanup of the spec file from upstream tarball for Fedora 16
- tarball version strings contains 'final', so adding --enable-release
- enforcing build of cjflash
- brutal patch to have man page in correct place, my automake-fu is non-existent
- what is that empty gui package defined in the orifginal spec file?
- debian/copyright says it's LGPLv2+

* Tue Jun 14 2011 09:53:20 +0200 - Frank Neuber <sct@kernelport.com>
+ pcsc-cyberjack-3.99.5final.SP02
- released 3.99.5final.SP02
- see changelog in debian/changelog in the source package


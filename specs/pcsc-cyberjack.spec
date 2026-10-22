%global readers_dir %(pkg-config libpcsclite --variable=usbdropdir)

Name:		pcsc-cyberjack
Summary:	PC/SC driver for REINER SCT cyberjack USB chip card reader
Version:	3.99.5final.SP17
%global version_prefix %(c=%{version}; echo ${c:0:6})
%global version_suffix %(c=%{version}; echo ${c:12:4})
Release:	%autorelease
License:	GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:		https://www.reiner-sct.com/
Source0:	https://support.reiner-sct.de/downloads/LINUX/V%{version_prefix}_%{version_suffix}/%{name}-%{version}.tar.bz2
Source1:	%{name}-3.99.5final.SP09-README-FEDORA
Source2:	libifd-cyberjack6.udev
Source3:	%{name}.sysusersd
# this patch replaces the obsoleted AC_PROG_LIBTOOLT macro with LT_INIT
# the patch is sent to upstream per email (20160528)
Patch0:		%{name}-3.99.5final.SP09-configure.patch

Requires:	udev
Requires:	pcsc-lite

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
BuildRequires:	systemd-rpm-macros
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
install -p -m 0644 %{SOURCE1} README-FEDORA.txt

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

install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre
%sysusers_create_compat %{SOURCE3}

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
%{_sysusersdir}/%{name}.conf


%files cjflash
%{_bindir}/cjflash
%license COPYING

%files examples
%doc doc/verifypin_ascii.c doc/verifypin_fpin2.c

%changelog
%autochangelog

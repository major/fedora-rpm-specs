%global dropdir %(pkg-config libpcsclite --variable usbdropdir 2>/dev/null)
%global pcsc_lite_ver 1.8.9

Name:           pcsc-lite-ccid
Version:        1.8.4
Release:        %{autorelease}
Summary:        Generic USB CCID smart card reader driver

License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://ccid.apdu.fr/files
Source0:        https://ccid.apdu.fr/files/ccid-%{version}.tar.xz
Source1:        https://ccid.apdu.fr/files/ccid-%{version}.tar.xz.asc
Source2:        https://ludovic-rousseau.pages-perso.free.fr/gpg_key_E8F9C57E.txt
Patch0:         ccid-1.4.26-omnikey-3121.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  perl-interpreter
BuildRequires:  perl-Getopt-Long
BuildRequires:  libusb1-devel
BuildRequires:  pcsc-lite-devel >= %{pcsc_lite_ver}
BuildRequires:  openpgpverify
BuildRequires:  flex
BuildRequires:  zlib-devel
# for udev.pc dependency
BuildRequires:  systemd
Requires(post): systemd
Requires(postun): systemd
Requires:       pcsc-lite%{?_isa} >= %{pcsc_lite_ver}
Provides:       pcsc-ifd-handler
# Provide upgrade path from 'ccid' package
Obsoletes:      ccid < 1.4.0-3
Provides:       ccid = %{version}-%{release}
# This is bundled from pcsc-lite upstream
Provides:       bundled(simclist) = 1.6

%description
Generic USB CCID (Chip/Smart Card Interface Devices) driver for use with the
PC/SC Lite daemon.


%prep
%{openpgpverify} --keyring=%{SOURCE2} --signature=%{SOURCE1} --data=%{SOURCE0}
%autosetup -n ccid-%{version} -p1

%build
%meson -Dserial=true

%meson_build

%install
%meson_install
cp -p src/openct/LICENSE LICENSE.openct


%post
%systemd_postun_with_restart pcscd.service


%preun
%systemd_preun pcscsd.service


%postun
%systemd_postun_with_restart pcscd.service


%files
%doc AUTHORS README.md
%license COPYING LICENSE.openct
%{dropdir}/ifd-ccid.bundle/
%{dropdir}/serial/
%config(noreplace) %{_sysconfdir}/reader.conf.d/libccidtwin
%{_prefix}/lib/udev/rules.d/92_pcscd_ccid.rules


%changelog
%autochangelog

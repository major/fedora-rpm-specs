%global forgeurl https://github.com/libimobiledevice/usbmuxd
%global commit 61b99ab5c25609c11369733a0df97c03a0581a56
%global date 20230720
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           usbmuxd
Version:        1.1.1^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Daemon for communicating with Apple's iOS devices
License:        GPL-3.0-only OR GPL-2.0-only
URL:            https://www.libimobiledevice.org/
Source:         %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  systemd

BuildRequires:  libimobiledevice-devel
BuildRequires:  libplist-devel
BuildRequires:  libusbx-devel

Requires(pre):  shadow-utils

%description
usbmuxd is a daemon used for communicating with Apple's iPod Touch, iPhone, 
iPad and Apple TV devices. It allows multiple services on the device to be 
accessed simultaneously.

%prep
%autosetup -p1 -n %{name}-%{commit}

%if %{defined commit}
echo %{version} > .tarball-version
%endif

# Set the owner of the device node to be usbmuxd
sed -i.owner 's/OWNER="usbmux"/OWNER="usbmuxd"/' udev/39-usbmuxd.rules.in
sed -i.user 's/--user usbmux/--user usbmuxd/' systemd/usbmuxd.service.in

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install

%pre
getent group usbmuxd >/dev/null || groupadd -r usbmuxd -g 113
getent passwd usbmuxd >/dev/null || \
useradd -r -g usbmuxd -d / -s /sbin/nologin \
	-c "usbmuxd user" -u 113 usbmuxd
exit 0

%post
%systemd_post usbmuxd.service

%preun
%systemd_preun usbmuxd.service

%postun
%systemd_postun_with_restart usbmuxd.service 

%files
%license COPYING.GPLv2 COPYING.GPLv3
%doc AUTHORS README.md
%{_unitdir}/usbmuxd.service
%{_udevrulesdir}/39-usbmuxd.rules
%{_sbindir}/usbmuxd
%{_datadir}/man/man8/usbmuxd.8.gz

%changelog
%autochangelog

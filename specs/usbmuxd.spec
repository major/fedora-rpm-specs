%global forgeurl https://github.com/libimobiledevice/usbmuxd
%global commit 0b1b233b57d581515978a09e5a4394bfa4ee4962
%global date 20240915
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

# Create a sysusers.d config file
cat >usbmuxd.sysusers.conf <<EOF
u usbmuxd 113 'usbmuxd user' - -
EOF

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install

install -m0644 -D usbmuxd.sysusers.conf %{buildroot}%{_sysusersdir}/usbmuxd.conf


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
%{_sysusersdir}/usbmuxd.conf

%changelog
%autochangelog

Name:           txnupd-snapper-plugin
Version:        1.0
Release:        1%{?dist}
Summary:        Bootable snapshot integration for Grub2

License:        GPL-2.0-only
URL:            https://codeberg.org/KalpaDesktop/txnupd-snapper-plugin
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake

Requires:       grub2-common
Requires:       snapper
Requires:       btrfs-progs
Requires:       /usr/bin/flock

BuildArch:      noarch

%description
A GRUB2 plugin that integrates with snapper to add Btrfs snapshot
boot entries to the GRUB2 menu.  When snapper creates or removes
read-only snapshots, this plugin updates the GRUB2 configuration so
users can boot into any snapshot directly from the boot menu.


%prep
%autosetup -C -p1

%conf
%cmake


%build
%cmake_build


%install
%cmake_install


%files
%license LICENSE
%{_libexecdir}/snapper/plugins/00-grub
%{_sysconfdir}/grub.d/80_suse_btrfs_snapshot


%changelog
* Thu Nov 05 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 1.0-1
- Initial Packaging

Name:           archlinux-keyring
Version:        20231222
Release:        %autorelease
Url:            https://archlinux.org/packages/core/any/archlinux-keyring/
Source0:        https://gitlab.archlinux.org/archlinux/archlinux-keyring/-/archive/%{version}/archlinux-keyring-%{version}.tar.gz
Patch:          archlinux-keyring-revert_to_sq-keyring-linter.diff
# see https://wiki.archlinux.org/index.php/Pacman-key for introduction
License:        LicenseRef-Fedora-Public-Domain
Summary:        GPG keys used by Arch Linux distribution to sign packages
BuildArch:      noarch

BuildRequires:  keyrings-filesystem
BuildRequires:  make
BuildRequires:  /usr/bin/sq
BuildRequires:  python3
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd
BuildRequires:  pkgconf
Requires:       pacman-filesystem
Requires:       keyrings-filesystem

%description
A set of GPG keys used to sign packages in the Arch distribution,
which can be used to verify that downloaded Arch packages are
valid.

This package simply packages the GPG keyring as published by Arch
developers into an RPM package to allow for safe and convenient
installation on Fedora systems.

%prep
%autosetup -p1

%build

%check
make check

%install
%make_install PREFIX=%{_prefix}
mkdir -p %{buildroot}%{_keyringsdir}/
ln --relative -s %{_datadir}/pacman/keyrings/archlinux.gpg %{buildroot}%{_keyringsdir}/

%files
%{_datadir}/pacman/keyrings
%{_keyringsdir}/archlinux.gpg
%{_bindir}/archlinux-keyring-wkd-sync
%{_unitdir}/archlinux-keyring-wkd-sync.*
%{_unitdir}/timers.target.wants/archlinux-keyring-wkd-sync.timer

%post
if [ -x /usr/bin/pacman-key ] && /usr/bin/pacman-key -l &>/dev/null; then
    /usr/bin/pacman-key --populate archlinux || :
    /usr/bin/pacman-key --updatedb || :
fi

%changelog
%autochangelog

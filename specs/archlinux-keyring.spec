Name:           archlinux-keyring
Version:        20241203
Release:        %autorelease
Url:            https://archlinux.org/packages/core/any/archlinux-keyring/
Source0:        https://gitlab.archlinux.org/archlinux/archlinux-keyring/-/archive/%{version}/archlinux-keyring-%{version}.tar.gz
# This should be a GPG-signed tarball with the precompiled keyring
Source1:        https://gitlab.archlinux.org/archlinux/archlinux-keyring/-/releases/%{version}/downloads/archlinux-keyring-%{version}.tar.gz.sig
# gpg2 --export --export-options export-minimal --armor 02FD1C7A934E614545849F19A6234074498E9CEE >gpgkey-02FD1C7A934E614545849F19A6234074498E9CEE.gpg
# sq cert export --cert 02FD1C7A934E614545849F19A6234074498E9CEE >gpgkey-02FD1C7A934E614545849F19A6234074498E9CEE.gpg
Source2:        gpgkey-02FD1C7A934E614545849F19A6234074498E9CEE.gpg

# see https://wiki.archlinux.org/index.php/Pacman-key for introduction
License:        LicenseRef-Fedora-Public-Domain
Summary:        GPG keys used by Arch Linux distribution to sign packages
BuildArch:      noarch

BuildRequires:  keyrings-filesystem
BuildRequires:  make
BuildRequires:  sequoia-sq
%if 0%{?el9}
BuildRequires:  python3.11
%else
BuildRequires:  python3
%endif
BuildRequires:  systemd-rpm-macros

Requires:       pacman-filesystem
Requires:       keyrings-filesystem

%description
A set of GPG keys used to sign packages in the Arch distribution, which can
be used to verify that downloaded Arch packages are valid.

This package simply packages the GPG keyring as published by Arch developers
into an RPM package to allow for safe and convenient installation on Fedora
systems.

%prep
%autosetup -p1
sq verify --signer-file=%{SOURCE2} --message %{SOURCE1} --output tmp.tar.gz
tar -xvf tmp.tar.gz

%if 0%{?el9}
sed -i 's|/usr/bin/env python3|/usr/bin/env python3.11|' keyringctl
%endif

%build
mkdir build
make wkd_sync_service SCRIPT_TARGET_DIR=%{_bindir}

%install
install -Dt %{buildroot}%{_bindir}/ wkd_sync/archlinux-keyring-wkd-sync
install -Dt %{buildroot}%{_unitdir}/ \
  wkd_sync/archlinux-keyring-wkd-sync.timer \
  build/archlinux-keyring-wkd-sync.service

install -m0644 -Dt %{buildroot}%{_datadir}/pacman/keyrings/ \
  archlinux-keyring-%{version}/{archlinux.gpg,archlinux-revoked,archlinux-trusted}

mkdir -p %{buildroot}%{_keyringsdir}/
ln --relative -s %{_datadir}/pacman/keyrings/archlinux.gpg %{buildroot}%{_keyringsdir}/

%files
%{_datadir}/pacman/keyrings
%{_keyringsdir}/archlinux.gpg
%{_bindir}/archlinux-keyring-wkd-sync
%{_unitdir}/archlinux-keyring-wkd-sync.*

%posttrans
if [ $1 == 1 ] && [ -x /usr/bin/pacman-key ] && ! /usr/bin/pacman-key -l &>/dev/null; then
    /usr/bin/pacman-key --init && \
    /usr/bin/pacman-key --populate archlinux --updatedb || :
fi

%transfiletriggerin -- /usr/bin/pacman-key
if [ -x /usr/bin/pacman-key ] && ! /usr/bin/pacman-key -l &>/dev/null; then
    /usr/bin/pacman-key --init && \
    /usr/bin/pacman-key --populate archlinux --updatedb || :
fi

%changelog
%autochangelog

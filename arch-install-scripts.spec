Name:           arch-install-scripts
Version:        28
Release:        %autorelease
Summary:        Scripts to bootstrap Arch Linux distribution
License:        GPL-2.0-only
URL:            https://github.com/archlinux/arch-install-scripts
%global forgeurl %url
%forgemeta
Source0:        %forgesource
BuildArch:      noarch
BuildRequires:  m4
BuildRequires:  asciidoc
BuildRequires:  make
Requires:       archlinux-keyring
Requires:       pacman

%description
A small suite of scripts aimed at automating some menial tasks when installing
Arch Linux, most notably including actually performing the installation.

To install and launch Arch in a container:
  pacman-key --init
  pacman-key --populate archlinux
  mkdir -p /var/lib/machines/arch
  pacstrap -G -M -i -c /var/lib/machines/arch base
  systemd-nspawn -bD /var/lib/machines/arch

%prep
%setup -q

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%check
make check

%files
%license COPYING
%{_bindir}/arch-chroot
%{_bindir}/genfstab
%{_bindir}/pacstrap
%{_datadir}/bash-completion/completions/arch-chroot
%{_datadir}/bash-completion/completions/genfstab
%{_datadir}/bash-completion/completions/pacstrap
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_archinstallscripts
%{_mandir}/man8/arch-chroot.8*
%{_mandir}/man8/genfstab.8*
%{_mandir}/man8/pacstrap.8*

%changelog
%autochangelog

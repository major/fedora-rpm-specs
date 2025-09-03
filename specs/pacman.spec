# We ship a .pc file but don't want to have a dep on pkg-config. We
# strip the automatically generated dep here and instead co-own the
# directory.
%global __requires_exclude pkg-config

%global libmajor 15
%global libminor 0

# Use the same directory of the main package for subpackage licence and docs
%global _docdir_fmt %{name}

Name:           pacman
Version:        7.0.0
Release:        %autorelease
Source0:        https://gitlab.archlinux.org/pacman/pacman/-/archive/v%{version}/pacman-v%{version}.tar.gz
Source1:        https://www.archlinux.org/mirrorlist/all
URL:            https://gitlab.archlinux.org/pacman/pacman
License:        GPL-2.0-or-later
Summary:        Package manager for the Arch distribution

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  m4
BuildRequires:  bsdtar
BuildRequires:  gettext-devel
BuildRequires:  asciidoc
BuildRequires:  doxygen
BuildRequires:  libarchive-devel
BuildRequires:  gpgme-devel
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  perl-generators
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       bsdtar
Recommends:     arch-install-scripts

# makepkg-template is an optional script that aims to make maintaining multiple
# PKGBUILDs easier. As we don't expect anybody to use this from a Fedora system
# and this script ends up adding a bunch of perl dependencies, we exclude it
# from the dependency generators.
%global __requires_exclude_from ^%{_bindir}/makepkg-template$

%description
Pacman is the package manager used by the Arch distribution. It can
be used to install Arch into a container or to recover an Arch
installation from a Fedora system (see arch-install-scripts package
for instructions).

Pacman is a frontend for the ALPM (Arch Linux Package Management)
library Pacman does not strive to "do everything." It will add, remove
and upgrade packages in the system, and it will allow you to query the
package database for installed packages, files and owners. It also
attempts to handle dependencies automatically and can download
packages from a remote server. Arch packages are simple archives, with
.pkg.tar.gz extension for binary packages and .src.tar.gz for source
packages.


%package -n libalpm
Summary: Arch Linux Package Management library

%description -n libalpm
This library is the backend behind Pacman — the package manager used
by the Arch distribution. It uses simple compressed files as a package
format, and maintains a text-based package database.


%package -n libalpm-devel
Summary: Development headers for libalpm
Requires: libalpm%{_isa} = %{version}-%{release}

%description -n libalpm-devel
This package contains the public headers necessary to use libalpm.


%package filesystem
Summary: Pacman filesystem layout
License: LicenseRef-Fedora-Public-Domain
BuildArch: noarch

%description filesystem
This package provides some directories used by pacman and related
packages.


%prep
%autosetup -p1 -n pacman-v%{version}

# Enable some servers by default. rackspace.com is in the "worldwide" section,
# and "kernel.org" seems to be a good default too.
sed -r 's+^#(Server = https://(mirrors.kernel.org|mirror.rackspace.com)/)+\1+' <%{SOURCE1} >mirrorlist

%build
CONFIGURE_OPTS=(
        -Ddoxygen=enabled
)

%meson "${CONFIGURE_OPTS[@]}"
%meson_build

%install
%meson_install

%find_lang pacman
%find_lang pacman-scripts
%find_lang libalpm
cat pacman-scripts.lang >>pacman.lang

install -Dm0644 mirrorlist %{buildroot}%{_sysconfdir}/pacman.d/mirrorlist

cat >>%{buildroot}%{_sysconfdir}/pacman.conf <<EOF
[core]
SigLevel = Required DatabaseOptional
Include = %{_sysconfdir}/pacman.d/mirrorlist

[extra]
SigLevel = Required DatabaseOptional
Include = %{_sysconfdir}/pacman.d/mirrorlist
EOF

%files -f pacman.lang
%{_bindir}/makepkg
%{_bindir}/makepkg-template
%{_bindir}/pacman
%{_bindir}/pacman-conf
%{_bindir}/pacman-db-upgrade
%{_bindir}/pacman-key
%{_bindir}/repo-add
%{_bindir}/repo-elephant
%{_bindir}/repo-remove
%{_bindir}/testpkg
%{_bindir}/vercmp
%config(noreplace) %{_sysconfdir}/makepkg.conf
%config(noreplace) %{_sysconfdir}/makepkg.conf.d/fortran.conf
%config(noreplace) %{_sysconfdir}/makepkg.conf.d/rust.conf
%config(noreplace) %{_sysconfdir}/pacman.conf
%config(noreplace) %{_sysconfdir}/pacman.d/mirrorlist
%{_datarootdir}/makepkg/
%dir %{_sharedstatedir}/pacman
%dir %{_localstatedir}/cache/pacman
%dir %{_localstatedir}/cache/pacman/pkg
%{_datadir}/pacman/*
%{_datadir}/pkgconfig/libmakepkg.pc
# https://bugzilla.redhat.com/show_bug.cgi?id=1819867
%exclude %{_datadir}/bash-completion/completions/makepkg
%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_pacman
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%license COPYING
%doc NEWS

%files -n libalpm -f libalpm.lang
%{_libdir}/libalpm.so.%{libmajor}.%{libminor}.*
%{_libdir}/libalpm.so.%{libmajor}
%license COPYING

%files -n libalpm-devel
%{_includedir}/alpm_list.h
%{_includedir}/alpm.h
%{_libdir}/pkgconfig/libalpm.pc
%{_libdir}/libalpm.so
%{_mandir}/man3/*
%license COPYING
%doc HACKING

%files filesystem
%dir %{_sysconfdir}/pacman.d
%dir %{_datadir}/pacman


%changelog
%autochangelog

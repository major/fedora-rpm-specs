%global _tag 2023.03.31
# manually read from Makefile
%global _deepin_version 20.6

Name:           deepin-desktop-base
Version:        %{_tag}
Release:        %autorelease
Summary:        Base component for Deepin
# migrated to SPDX
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        %{url}/archive/%{_tag}/%{name}-%{_tag}.tar.gz
Source1:        distribution.info
BuildArch:      noarch
Recommends:     deepin-wallpapers
Recommends:     deepin-screensaver
Recommends:     plymouth-theme-deepin
BuildRequires:  make
Requires:       fedora-logos
# since F31
Obsoletes:      deepin-clone <= 1.1.4
Obsoletes:      deepin-qml-widgets <= 2.3.6

%description
This package provides some components for Deepin desktop environment.

- deepin logo
- deepin desktop version
- login screen background image
- language information

%prep
%setup -q -n %{name}-%{_tag}

# Fix data path
sed -i 's|/usr/lib|%{_datadir}|' Makefile

# Set deepin type to Fedora
sed -i 's|Type=.*|Type=Fedora|; /Type\[/d' files/desktop-version.in

%build
# don't rely on upstream Makefile build since it depends on buildarch
VERSION=%{_deepin_version}
RELEASE=
sed -e "s|@@VERSION@@|$VERSION|g" -e "s|@@RELEASE@@|$RELEASE|g" files/lsb-release.in > files/lsb-release
sed -e "s|@@VERSION@@|$VERSION|g" -e "s|@@RELEASE@@|$RELEASE|g" files/desktop-version.in > files/desktop-version

%install
%make_install

install -Dm644 %{SOURCE1} -t %{buildroot}%{_datadir}/deepin

# Remove Deepin distro's lsb-release
rm %{buildroot}/etc/lsb-release

# Don't override systemd timeouts
rm -r %{buildroot}/etc/systemd

# Make a symlink for deepin-version
ln -sfv ..%{_datadir}/deepin/desktop-version %{buildroot}%{_sysconfdir}/deepin-version

# Install os-version and rename to uos-version
install -Dm644 files/os-version-amd %{buildroot}%{_sysconfdir}/uos-version

# Remove apt-specific templates
rm -r %{buildroot}%{_datadir}/python-apt

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/appstore.json
%{_sysconfdir}/deepin-version
%{_sysconfdir}/uos-version
%{_datadir}/deepin/
%dir %{_datadir}/distro-info/
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json
%dir %{_datadir}/plymouth
%{_datadir}/plymouth/deepin-logo.png

%changelog
%autochangelog

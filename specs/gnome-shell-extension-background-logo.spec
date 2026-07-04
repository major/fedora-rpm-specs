Name:           gnome-shell-extension-background-logo
Version:        50.1
Release:        %autorelease
Summary:        Background logo extension for GNOME Shell

License:        GPL-2.0-or-later
URL:            https://forge.fedoraproject.org/workstation/background-logo-extension
Source0:        https://forge.fedoraproject.org/workstation/background-logo-extension/releases/download/%{gnome_tarball_version}/background-logo-extension-%{gnome_tarball_version}.tar.xz
BuildArch:      noarch

%gnome_check_version

BuildRequires:  meson
BuildRequires:  glib2-devel
BuildRequires:  git-core

Requires:       gnome-shell(api) = %{gnome_major_version}
Requires:       system-logos

%description
Show your pride! Display the Fedora logo (or any other graphic) in the corner of your desktop.

%prep
%autosetup -n background-logo-extension-%{gnome_tarball_version} -S git

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%{_datadir}/glib-2.0/schemas/org.fedorahosted.background-logo-extension.gschema.xml
%{_datadir}/gnome-shell/extensions/background-logo@fedorahosted.org/

%changelog
%autochangelog

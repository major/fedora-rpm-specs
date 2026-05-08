%global tarball_version %%(echo %{version} | tr '~' '.')
%global shell_version %%(cut -d "~" -f 1 <<<%{version})

Name:           gnome-shell-extension-background-logo
Version:        50.0
Release:        %autorelease
Summary:        Background logo extension for GNOME Shell

License:        GPL-2.0-or-later
URL:            https://forge.fedoraproject.org/workstation/background-logo-extension
# The short tarball name is a bug. https://forge.fedoraproject.org/workstation/background-logo-extension/issues/53
Source0:        https://forge.fedoraproject.org/workstation/background-logo-extension/archive/%{tarball_version}.tar.gz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  glib2-devel
BuildRequires:  git

Requires:       gnome-shell(api) = %{shell_version}
Requires:       system-logos

%description
Show your pride! Display the Fedora logo (or any other graphic) in the corner of your desktop.

%prep
%autosetup -n background-logo-extension -S git

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

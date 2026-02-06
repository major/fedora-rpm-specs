%global tarball_version %%(echo %{version} | tr '~' '.')
%global shell_version %%(cut -d "~" -f 1 <<<%{version})

Name:           gnome-shell-extension-background-logo
Version:        50~beta
Release:        %autorelease
Summary:        Background logo extension for GNOME Shell

License:        GPL-2.0-or-later
URL:            https://pagure.io/background-logo-extension
Source0:        https://releases.pagure.org/background-logo-extension/background-logo-extension-%{tarball_version}.tar.xz
BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  glib2-devel
BuildRequires:  git

Requires:       gnome-shell(api) = %{shell_version}
Requires:       system-logos

%description
Show your pride! Display the Fedora logo (or any other graphic) in the corner of your desktop.

%prep
%autosetup -n background-logo-extension-%{tarball_version} -S git

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

%global extension   blur-my-shell
%global uuid        %{extension}@aunetx

Name:           gnome-shell-extension-%{extension}
Version:        68
Release:        %autorelease
Summary:        Adds a blur look to different parts of the GNOME Shell
License:        GPL-3.0-or-later
URL:            https://github.com/aunetx/blur-my-shell
BuildArch:      noarch

Source:         %{url}/archive/v%{version}-2/%{extension}-%{version}.tar.gz
# https://github.com/aunetx/blur-my-shell/pull/626
Patch:          0001-Use-meson-build-system.patch

BuildRequires:  meson
BuildRequires:  glib2
BuildRequires:  gettext
Requires:       gnome-shell >= 46
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Adds a blur look to different parts of the GNOME Shell, including the top
panel, dash and overview.


%prep
%autosetup -p 1 -n %{extension}-%{version}-2


%conf
%meson


%build
%meson_build


%install
%meson_install
%find_lang %{uuid}


%files -f %{uuid}.lang
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog

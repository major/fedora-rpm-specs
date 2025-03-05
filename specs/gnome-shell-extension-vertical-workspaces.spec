%global extension   vertical-workspaces
%global uuid        %{extension}@G-dH.github.com

Name:           gnome-shell-extension-%{extension}
Version:        48.3
Release:        %autorelease
Summary:        Customize your GNOME Shell UX to suit your workflow
License:        GPL-3.0-only
URL:            https://github.com/G-dH/vertical-workspaces
BuildArch:      noarch

Source:         %{url}/archive/v%{version}/%{extension}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  glib2
BuildRequires:  gettext
Requires:       gnome-shell >= 45
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Customize your GNOME Shell UX to suit your workflow, whether you like
horizontally or vertically stacked workspaces.


%prep
%autosetup -n %{extension}-%{version}


%conf
%meson


%build
%meson_build


%install
%meson_install
%find_lang %{extension}


%files -f %{extension}.lang
%license LICENSE
%doc CHANGELOG.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog

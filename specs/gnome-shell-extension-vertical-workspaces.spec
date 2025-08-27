%global extension   vertical-workspaces
%global uuid        %{extension}@G-dH.github.com
%global commit      65abb6b5f09fa8f0d48caa9b40e9fe3a302b139a
%global shortcommit %{sub %{commit} 1 7}

Name:           gnome-shell-extension-%{extension}
Version:        48.8^1.%{shortcommit}
Release:        %autorelease
Summary:        Customize your GNOME Shell UX to suit your workflow
License:        GPL-3.0-only
URL:            https://github.com/G-dH/vertical-workspaces
BuildArch:      noarch

Source:         %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz

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
%autosetup -n %{extension}-%{commit}


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

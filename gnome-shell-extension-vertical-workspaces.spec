%global extension   vertical-workspaces
%global uuid        %{extension}@G-dH.github.com

Name:           gnome-shell-extension-%{extension}
Version:        13
Release:        %autorelease
Summary:        Vertical orientation of workspaces for GNOME 40+
License:        GPL-3.0-only
URL:            https://github.com/G-dH/vertical-workspaces
BuildArch:      noarch

Source:         %{url}/archive/v%{version}/%{extension}-%{version}.tar.gz

Requires:       gnome-shell >= 40
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Vertical orientation of workspaces and options to customize Activities overview
layout and content for GNOME 40+.


%prep
%autosetup -n %{extension}-%{version}


%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install main extension files
cp -p *.js stylesheet.css metadata.json \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%files
%license LICENSE
%doc CHANGELOG.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog

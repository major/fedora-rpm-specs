%global extension   vertical-overview
%global uuid        %{extension}@RensAlthuis.github.com

Name:           gnome-shell-extension-%{extension}
Version:        10
Release:        %autorelease
Summary:        GNOME Shell extension for vertical overview and workspaces
License:        GPLv3+
BuildArch:      noarch
URL:            https://github.com/RensAlthuis/vertical-overview

Source:         %{url}/archive/v%{version}/%{extension}-%{version}.tar.gz

# https://github.com/RensAlthuis/vertical-overview/issues/117
# https://github.com/RensAlthuis/vertical-overview/pull/116
Patch:          0001-Fix-logic-when-calling-connectObject-disconnectObjec.patch
# https://github.com/RensAlthuis/vertical-overview/issues/122
# https://github.com/RensAlthuis/vertical-overview/pull/124
Patch:          0002-Fix-GS44-Meta.later_add-is-not-a-function.patch
Patch:          0003-update-metadata.patch

Requires:       gnome-shell-extension-common >= 42
Recommends:     gnome-extensions-app
Provides:       %{extension} = %{version}-%{release}


%description
Gnome has had vertically stacked workspaces for a long time.  The Gnome 40
update unfortunately made the switch to a horizontal layout.  A choice that
many Gnome users disagree with.  This extension Aims to replace the new Gnome
overview with something that resembles the old style.


%prep
%autosetup -p 1 -n %{extension}-%{version}


%install
install -d -m 0755 %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install main extension files
cp -r --preserve=mode,timestamps \
    *.js *.css *.ui metadata.json \
    %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml


%changelog
%autochangelog

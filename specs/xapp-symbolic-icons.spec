%global forgeurl https://github.com/xapp-project/xapp-symbolic-icons
%global tag      %{version}

Name:           xapp-symbolic-icons
Version:        1.1.2
Release:        %autorelease
%{forgemeta}
Summary:        A set of symbolic icons which replaces the GNOME-specific Adwaita set
License:        CC0-1.0 AND CC-BY-SA-4.0 AND LGPL-3.0-only AND MIT
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildSystem:    meson
Requires:       hicolor-icon-theme

%description
A set of symbolic icons which replaces the GNOME-specific Adwaita set.
All provided icons are prefixed with xsi-.
Icon names loosely follow the Adwaita names.

%prep
%forgeautosetup -p1

%transfiletriggerin -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/hicolor
gtk-update-icon-cache --force %{_datadir}/icons/hicolor &>/dev/null || :

%files
%license LICENSE LICENSES/*.txt
%doc AUTHORS README.md
%{_bindir}/xsi-replace-adwaita-symbolic
%{_datadir}/icons/hicolor/scalable/actions/xsi-*.svg
%{_datadir}/xapp/

%changelog
%autochangelog
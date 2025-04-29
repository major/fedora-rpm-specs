%global forgeurl https://github.com/ubuntu/yaru
%global tag %{version}-0ubuntu1
%global _license COPYING COPYING.LGPL-2.1 COPYING.LGPL-3.0 LICENSE_CCBYSA

Name:       yaru-theme
Version:    25.04.2
%forgemeta
Release:    %autorelease
Summary:    Ubuntu community theme "yaru"
BuildArch:  noarch

License:    GPL-3.0-or-later and CC-BY-SA-4.0
URL:        https://community.ubuntu.com/c/desktop/theme-refresh
Source0:    %{forgesource}

BuildRequires: meson >= 0.59
BuildRequires: sassc
BuildRequires: pkgconfig(appstream-glib)

Requires:   gnome-shell-theme-yaru = %{version}-%{release}
Requires:   yaru-gtk2-theme = %{version}-%{release}
Requires:   yaru-gtk3-theme = %{version}-%{release}
Requires:   yaru-gtk4-theme = %{version}-%{release}
Requires:   yaru-gtksourceview-theme = %{version}-%{release}
Requires:   yaru-icon-theme = %{version}-%{release}
Requires:   yaru-sound-theme = %{version}-%{release}

%global _description %{expand:
Yaru is the default theme for Ubuntu, backed by the community.

It contains:
  * a GNOME Shell theme based on the upstream GNOME shell theme
  * a light and dark GTK theme (gtk2 and gtk3) based on the upstream Adwaita
    Gtk theme
  * an icon & cursor theme, derived from the Unity8 Suru icons and Suru icon
    theme
  * a sound theme, combining sounds from the WoodenBeaver and Touch-Remix
    sound themes.}

%description %{_description}


%package     -n gnome-shell-theme-yaru
Summary:        Yaru GNOME Shell Theme

Requires:       gnome-shell-extension-user-theme

Recommends:     yaru-gtk3-theme
Recommends:     yaru-icon-theme

Suggests:       yaru-sound-theme
Suggests:       yaru-theme

%description -n gnome-shell-theme-yaru %{_description}

This package contains GNOME Shell Theme.


%package     -n yaru-gtk2-theme
Summary:        GTK+ 2 support for the Yaru GTK Theme

Requires:       adwaita-gtk2-theme
Requires:       gtk-murrine-engine

Recommends:     yaru-gtk3-theme

%description -n yaru-gtk2-theme %{_description}

This package contains GTK+ 2 theme.


%package     -n yaru-gtk3-theme
Summary:        GTK+ 3 support for the Yaru GTK Theme

Requires:       gtk3

Recommends:     yaru-gtk2-theme
Recommends:     yaru-gtk4-theme

%description -n yaru-gtk3-theme %{_description}

This package contains GTK+ 3 theme.


%package     -n yaru-gtk4-theme
Summary:        GTK+ 3 support for the Yaru GTK Theme

Requires:       gtk4

Recommends:     yaru-gtk2-theme
Recommends:     yaru-gtk3-theme

%description -n yaru-gtk4-theme %{_description}

This package contains GTK 4 theme.


%package     -n yaru-icon-theme
Summary:        Yaru icon theme
License:        CC-BY-SA

Requires:       hicolor-icon-theme

Suggests:       gnome-shell-theme-yaru
Suggests:       yaru-gtk3-theme
Suggests:       yaru-sound-theme

%description -n yaru-icon-theme %{_description}

This package contains the icon theme.


%package     -n yaru-sound-theme
Summary:        Yaru sound theme
License:        CC-BY-SA

%description -n yaru-sound-theme %{_description}

This package contains the sound theme following the XDG theming specification.


%package     -n yaru-gtksourceview-theme
Summary:        Yaru GtkSourceView theme
License:        CC-BY-SA

%description -n yaru-gtksourceview-theme %{_description}

This package contains the GtkSourceView theme.


%prep
%forgeautosetup -p1


%build
%meson
%meson_build


%install
%meson_install

rm  %{buildroot}%{_datadir}/glib-2.0/schemas/99_Yaru.gschema.override \
    %{buildroot}%{_datadir}/xsessions/Yaru-xorg.desktop \
    %{buildroot}%{_datadir}/wayland-sessions/Yaru.desktop \
    %{buildroot}%{_datadir}/gnome-shell/extensions/ubuntu-dock@ubuntu.com/yaru.css

touch %{buildroot}%{_datadir}/icons/Yaru/icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/Yaru
gtk-update-icon-cache --force %{_datadir}/icons/Yaru &>/dev/null || :


%files
%license %{_license}
%doc AUTHORS CONTRIBUTING.md README.md
%{_datadir}/themes/Yaru*/metacity-1/

%files -n gnome-shell-theme-yaru
%license %{_license}
%{_datadir}/gnome-shell/modes/yaru.json
%{_datadir}/gnome-shell/theme/Yaru*/
%{_datadir}/themes/Yaru-*/index.theme
%{_datadir}/themes/Yaru*/gnome-shell
%{_datadir}/themes/Yaru/index.theme

%files -n yaru-gtk2-theme
%license %{_license}
%{_datadir}/themes/Yaru-*/gtk-2.0/
%{_datadir}/themes/Yaru/gtk-2.0/
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark

%files -n yaru-gtk3-theme
%license %{_license}
%{_datadir}/themes/Yaru-*/gtk-3.*/
%{_datadir}/themes/Yaru/gtk-3.*/
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark

%files -n yaru-gtk4-theme
%license %{_license}
%{_datadir}/themes/Yaru-*/gtk-4.*/
%{_datadir}/themes/Yaru/gtk-4.*/
%dir %{_datadir}/themes/Yaru
%dir %{_datadir}/themes/Yaru-dark

%files -n yaru-icon-theme
%license %{_license}
%{_datadir}/icons/Yaru*/
%ghost %{_datadir}/icons/Yaru/icon-theme.cache

%files -n yaru-sound-theme
%license %{_license}
%{_datadir}/sounds/Yaru/

%files -n yaru-gtksourceview-theme
%license %{_license}
%{_datadir}/gtksourceview-*/styles/Yaru*.xml
%{_datadir}/libgedit-gtksourceview-300/styles/Yaru*.xml


%changelog
%autochangelog

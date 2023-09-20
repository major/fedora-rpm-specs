Name:           pop-gtk-theme
Version:        5.5.1
Release:        %autorelease
Summary:        Pop GTK Theme
# Most files: GPL-3.0-only
# Upstream Adwaita: LGPL-2.1-only
# SVG files: CC-BY-SA-4.0
License:        GPL-3.0-only AND LGPL-2.1-only AND CC-BY-SA-4.0
URL:            https://github.com/pop-os/gtk-theme
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/pop-os/gtk-theme/pull/596
Patch:          0001-fix-gtk4-include-some-missing-assets-in-gresource.patch
BuildArch:      noarch

BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  sassc


%description
The Pop theme for GTK.


# gtk2
%package -n pop-gtk2-theme
Summary:        Pop GTK 2 Theme
Requires:       gtk2
Requires:       gtk-murrine-engine
Supplements:    (pop-session and gtk2)

%description -n pop-gtk2-theme
%{summary}.

%files -n pop-gtk2-theme
%license COPYING COPYING.LGPL-2.1 LICENSE_CCBYSA
%dir %{_datadir}/themes/Pop
%{_datadir}/themes/Pop/gtk-2.0
%dir %{_datadir}/themes/Pop-dark
%{_datadir}/themes/Pop-dark/gtk-2.0


# gtk3
%package -n pop-gtk3-theme
Summary:        Pop GTK 3 Theme
Requires:       gnome-themes-extra
Supplements:    (pop-session and gtk3)

%description -n pop-gtk3-theme
%{summary}.

%files -n pop-gtk3-theme
%license COPYING COPYING.LGPL-2.1 LICENSE_CCBYSA
%dir %{_datadir}/themes/Pop
%{_datadir}/themes/Pop/gtk-3.0
%dir %{_datadir}/themes/Pop-dark
%{_datadir}/themes/Pop-dark/gtk-3.0


# gtk4
%package -n pop-gtk4-theme
Summary:        Pop GTK 4 Theme
Requires:       gnome-themes-extra
Supplements:    (pop-session and gtk4)

%description -n pop-gtk4-theme
%{summary}.

%files -n pop-gtk4-theme
%license COPYING COPYING.LGPL-2.1 LICENSE_CCBYSA
%dir %{_datadir}/themes/Pop
%{_datadir}/themes/Pop/gtk-4.0
%dir %{_datadir}/themes/Pop-dark
%{_datadir}/themes/Pop-dark/gtk-4.0


# shell
%package -n pop-gnome-shell-theme
Summary:        Pop GNOME Shell Theme
Requires:       gnome-shell

%description -n pop-gnome-shell-theme
%{summary}.

%files -n pop-gnome-shell-theme
%license COPYING COPYING.LGPL-2.1 LICENSE_CCBYSA
%{_datadir}/gnome-shell/theme/Pop
%{_datadir}/themes/Pop/gnome-shell
%{_datadir}/themes/Pop/index.theme
%{_datadir}/themes/Pop-dark/gnome-shell
%{_datadir}/themes/Pop-dark/index.theme


# sound
%package -n pop-sound-theme
Summary:        Pop sound theme
License:        CC-BY-SA-4.0

%description -n pop-sound-theme
%{summary}.

%files -n pop-sound-theme
%license LICENSE_CCBYSA
%{_datadir}/sounds/Pop


%prep
%autosetup -n gtk-theme-%{version} -p 1


%build
%meson -Dgnome-shell-gresource=true
%meson_build


%install
%meson_install


%changelog
%autochangelog

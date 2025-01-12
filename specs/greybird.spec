%global theme_name     Greybird

Name:           greybird
Version:        3.23.4
Release:        %autorelease
Summary:        A clean minimalistic theme for Xfce, GTK+ 2 and 3

# Automatically converted from old format: GPLv2+ or CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later OR LicenseRef-Callaway-CC-BY-SA
URL:            http://shimmerproject.org/project/%{name}/ 
Source0:        https://github.com/shimmerproject/%{theme_name}/archive/v%{version}.tar.gz


BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  sassc

Requires:       gtk-murrine-engine

BuildArch:      noarch

Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11

Provides:       greybird = %{name}-%{release}

%description
Greybird is a theme for GTK2/3 and xfwm4/metacity started out on the basis of
Bluebird, but aims at reworking the intense blue tone to a more neutral
grey-ish look that will be more pleasant to look at in everyday use.

%package light-theme
Summary:        Greybird light themes

Requires:       gtk-murrine-engine

Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11
Provides:       greybird-light-theme = %{name}-%{release}


%description light-theme
Light Themes as part of the Greybird theme.

%package dark-theme
Summary:        Greybird Dark themes

Requires:       gtk-murrine-engine

Obsoletes:      greybird-gtk2-theme < 3.22.11
Obsoletes:      greybird-gtk3-theme < 3.22.11
Obsoletes:      greybird-metacity-theme < 3.22.11
Obsoletes:      greybird-xfce4-notifyd-theme < 3.22.11
Obsoletes:      greybird-xfwm4-themes < 3.22.11
Provides:       greybird-dark-theme = %{name}-%{release}


%description dark-theme
Dark Themes as part of the Greybird theme.


%package metacity-theme
Summary:        Greybird Metacity themes
Requires:       metacity
Requires:       greybird-light-theme
Requires:       greybird-dark-theme

%description metacity-theme
Themes for Metacity as part of the Greybird theme.


%package xfwm4-theme
Summary:        Greybird Xfwm4 themes
Requires:       xfwm4
Requires:       greybird-light-theme
Requires:       greybird-dark-theme

%description xfwm4-theme
Themes for Xfwm4 as part of the Greybird theme.

%package xfce4-notifyd-theme
Summary:        Greybird Xfce4 notifyd theme
Requires:       xfce4-notifyd
Requires:       greybird-light-theme

%description xfce4-notifyd-theme
Themes for Xfce4 notifyd as part of the Greybird theme.

%package plank
Summary:        Greybird plank themes
Requires:       plank
Requires:       greybird-light-theme
Requires:       greybird-dark-theme

%description plank
Themes for plank as part of the Greybird theme.

%prep

%setup -q -n %{theme_name}-%{version}

# Cleanup
# Remove Unity theme
sed -i '/unity/d' light/meson.build
sed -i '/unity/d' dark/meson.build
rm -fr light/unity
rm -fr dark/unity


%build
%meson

%meson_build

%install
%meson_install


%files light-theme
%doc LICENSE.GPL LICENSE.CC
%{_datadir}/themes/%{theme_name}/index.theme
%{_datadir}/themes/%{theme_name}/%{theme_name}.emerald
%{_datadir}/themes/%{theme_name}/gnome-shell/
%{_datadir}/themes/%{theme_name}/gtk-2.0/
%{_datadir}/themes/%{theme_name}/gtk-3.0/
%{_datadir}/themes/%{theme_name}/gtk-4.0/
%{_datadir}/themes/%{theme_name}/openbox-3/


%files dark-theme
%doc LICENSE.GPL LICENSE.CC
%{_datadir}/themes/%{theme_name}-dark/index.theme
%{_datadir}/themes/%{theme_name}-dark/%{theme_name}-dark.emerald
%{_datadir}/themes/%{theme_name}-dark/gnome-shell/
%{_datadir}/themes/%{theme_name}-dark/gtk-2.0/
%{_datadir}/themes/%{theme_name}-dark/gtk-3.0/
%{_datadir}/themes/%{theme_name}-dark/openbox-3/


%files metacity-theme
%doc LICENSE.GPL LICENSE.CC
%dir %{_datadir}/themes/Greybird/
%{_datadir}/themes/%{theme_name}/metacity-1/
%{_datadir}/themes/%{theme_name}-dark/metacity-1/


%files xfwm4-theme
%doc LICENSE.GPL LICENSE.CC
%dir %{_datadir}/themes/Greybird/
%{_datadir}/themes/%{theme_name}-dark-accessibility/xfwm4/
%{_datadir}/themes/%{theme_name}-dark/xfwm4/
%{_datadir}/themes/%{theme_name}-accessibility/xfwm4/
%{_datadir}/themes/%{theme_name}-compact/xfwm4/
%{_datadir}/themes/%{theme_name}/xfwm4/

%files xfce4-notifyd-theme
%doc LICENSE.GPL LICENSE.CC
%dir %{_datadir}/themes/Greybird/
%{_datadir}/themes/%{theme_name}/xfce-notify-4.0/
%{_datadir}/themes/%{theme_name}-bright/xfce-notify-4.0/

%files plank
%doc LICENSE.GPL LICENSE.CC
%{_datadir}/themes/%{theme_name}/plank/
%{_datadir}/themes/%{theme_name}-dark/plank/

%changelog
%autochangelog

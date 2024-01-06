Name:           papirus-icon-theme
Version:        20231201
Release:        %autorelease
Summary:        Free and open source SVG icon theme based on Paper Icon Set

# Some icons are based on
# * Paper Icon Theme, CC-BY-SA-4.0
# * Breeze Plasma Theme, LGPL-3.0-or-later
#   https://invent.kde.org/frameworks/breeze-icons/-/blob/master/COPYING-ICONS
# The rest is GPL-3.0-only; see AUTHORS
License:        GPL-3.0-only AND CC-BY-SA-4.0 AND LGPL-3.0-or-later
URL:            https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make

%description
Papirus is a free and open source SVG icon theme for Linux, based on Paper
Icon Set with a lot of new icons and a few extras, like Hardcode-Tray support,
KDE colorscheme support, Folder Color support, and others.

This package contains the following variants:

 - Papirus (for Arc / Arc Darker)
 - Papirus Dark (for Arc Dark)
 - Papirus Light (light theme with Breeze colors)

%package -n epapirus-icon-theme
Summary:        Papirus icon theme for elementaryOS and Pantheon Desktop
Requires:       papirus-icon-theme = %{version}-%{release}

%description -n epapirus-icon-theme
Papirus is a free and open source SVG icon theme for Linux, based on Paper
Icon Set with a lot of new icons and a few extras, like Hardcode-Tray support,
KDE colorscheme support, Folder Color support, and others.

This package contains the following variants:

 - ePapirus (for elementary OS and Pantheon Desktop)
 - ePapirus-Dark (for elementary OS and Pantheon Desktop)

%prep
%autosetup

%build
# stub for rpmlint

%install
%make_install

export THEMES="ePapirus ePapirus-Dark Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /bin/touch %{buildroot}/%{_datadir}/icons/$t/icon-theme.cache
done

%post
export THEMES="Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
done

%post -n epapirus-icon-theme
export THEMES="ePapirus ePapirus-Dark"
for t in $THEMES; do
    /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null || :
done

%postun
if [ $1 -eq 0 ] ; then
    export THEMES="Papirus Papirus-Dark Papirus-Light"
    for t in $THEMES; do
        /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
        /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
    done
fi

%postun -n epapirus-icon-theme
if [ $1 -eq 0 ] ; then
    export THEMES="ePapirus ePapirus-Dark"
    for t in $THEMES; do
        /bin/touch --no-create %{_datadir}/icons/$t &>/dev/null
        /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
    done
fi

%posttrans
export THEMES="Papirus Papirus-Dark Papirus-Light"
for t in $THEMES; do
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
done

%posttrans -n epapirus-icon-theme
export THEMES="ePapirus ePapirus-Dark"
for t in $THEMES; do
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/$t &>/dev/null || :
done

%files
%license LICENSE
%doc AUTHORS README.md
%dir %{_datadir}/icons/Papirus-Dark
%dir %{_datadir}/icons/Papirus-Light
%dir %{_datadir}/icons/Papirus
%ghost %{_datadir}/icons/Papirus-Dark/icon-theme.cache
%ghost %{_datadir}/icons/Papirus-Light/icon-theme.cache
%ghost %{_datadir}/icons/Papirus/icon-theme.cache
%{_datadir}/icons/Papirus-Dark/*x*
%{_datadir}/icons/Papirus-Dark/symbolic
%{_datadir}/icons/Papirus-Light/*x*
%{_datadir}/icons/Papirus-Light/symbolic
%{_datadir}/icons/Papirus/*x*
%{_datadir}/icons/Papirus/symbolic

%files -n epapirus-icon-theme
%license LICENSE
%dir %{_datadir}/icons/ePapirus-Dark
%dir %{_datadir}/icons/ePapirus
%ghost %{_datadir}/icons/ePapirus-Dark/icon-theme.cache
%ghost %{_datadir}/icons/ePapirus/icon-theme.cache
%{_datadir}/icons/ePapirus-Dark/*x*
%{_datadir}/icons/ePapirus-Dark/symbolic
%{_datadir}/icons/ePapirus/*x*
%{_datadir}/icons/ePapirus/symbolic

%changelog
%autochangelog

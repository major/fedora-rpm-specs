%global forgeurl https://github.com/jgmenu/jgmenu
Version:	4.6.0
%forgemeta

Name:		jgmenu
Release:	%autorelease
Summary:	Simple X11 application menu
License:	GPL-2.0-or-later
URL:		%{forgeurl}
Source:		%{forgesource}

BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.46
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(xrandr)
Requires:	hicolor-icon-theme

%description
A simple, independent and contemporary-looking X11 menu, designed for scripting,
ricing and tweaking. Useful for tint2, polymenu, cairo-dock, plank, unity,
openbox, i3, dwm and other light environments.


%package	lx
Summary:	LXDE %{name} plugin
BuildRequires:	pkgconfig(libmenu-cache)
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	lx
LXDE plugin for %{name} package.


%package	pmenu
Summary:	Pmenu %{name} plugin
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description	pmenu
Pmenu plugin for %{name} package.


%package	gtktheme
Summary:	GTKtheme %{name} plugin
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}

%description	gtktheme
GTKtheme plugin for %{name} package.


%package	xfce4
Summary:	Xfce4 %{name} plugin
%if 0%{?fedora} > 33
BuildRequires:	pkgconfig(libxfce4panel-2.0)
%else
BuildRequires:	pkgconfig(libxfce4panel-1.0)
%endif
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	xfce4
Xfce4 plugin for %{name} package.


%prep
%forgeautosetup


%build
# default: --with-lx --with-pmenu --with-gtktheme --with-xfce4-panel-applet
%{configure} -a
%{make_build}


%install
%{make_install}
find %{buildroot}%{_libexecdir}/%{name}/ -type f -exec chmod 755 {} +


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
# Run test suite with correct compilation flags
%make_build test CFLAGS="%{optflags}"


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_libexecdir}/%{name}/%{name}-apps
%{_libexecdir}/%{name}/%{name}-config
%{_libexecdir}/%{name}/%{name}-greeneye
%{_libexecdir}/%{name}/%{name}-hide-app.sh
%{_libexecdir}/%{name}/%{name}-i18n
%{_libexecdir}/%{name}/%{name}-init.sh
%{_libexecdir}/%{name}/%{name}-ob
%{_libexecdir}/%{name}/%{name}-obtheme
%{_libexecdir}/%{name}/%{name}-socket
%{_libexecdir}/%{name}/%{name}-themes.sh
%{_libexecdir}/%{name}/%{name}-unity-hack.py
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/%{name}*.*
%exclude %{_mandir}/man1/%{name}-{lx,pmenu}.1.*

%files	lx
%{_libexecdir}/%{name}/%{name}-lx
%{_mandir}/man1/%{name}-lx.1.*

%files	pmenu
%{_libexecdir}/%{name}/%{name}-pmenu.py
%{_mandir}/man1/%{name}-pmenu.1.*

%files	gtktheme
%{_libexecdir}/%{name}/%{name}-gtktheme.py

%files	xfce4
%{_libdir}/xfce4/panel/plugins/lib%{name}.so
%{_datadir}/xfce4/panel/plugins/%{name}-applet.desktop


%changelog
%autochangelog

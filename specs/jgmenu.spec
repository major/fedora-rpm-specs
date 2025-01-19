Name:		jgmenu
Version:	4.5.0
Release:	2%{?dist}
Summary:	Simple X11 application menu
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		https://jgmenu.github.io
Source0:	https://github.com/johanmalm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires:	hicolor-icon-theme
BuildRequires:	gcc, desktop-file-utils
# libXrandr-devel
BuildRequires:	pkgconfig(xrandr)
# libxml2-devel
BuildRequires:	pkgconfig(libxml-2.0)
# cairo-devel
BuildRequires:	pkgconfig(cairo)
# pango-devel
BuildRequires:	pkgconfig(pango)
# librsvg2-devel
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.46

%description
A simple, independent and contemporary-looking X11 menu, designed for scripting,
ricing and tweaking. Useful for tint2, polymenu, cairo-dock, plank, unity,
openbox, i3, dwm and other light environments.


%package	lx
Summary:	LXDE %{name} plugin
# menu-cache-devel
BuildRequires:	pkgconfig(libmenu-cache)
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	lx
LXDE plugin for %{name} package.


%package	pmenu
Summary:	Pmenu %{name} plugin
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	pmenu
Pmenu plugin for %{name} package.


%package	gtktheme
Summary:	GTKtheme %{name} plugin
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description	gtktheme
GTKtheme plugin for %{name} package.


%package	xfce4
Summary:	Xfce4 %{name} plugin
# xfce4-panel-devel
%if 0%{?fedora} > 33
BuildRequires:	pkgconfig(libxfce4panel-2.0)
%else
BuildRequires:	pkgconfig(libxfce4panel-1.0)
%endif
BuildRequires: make
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	xfce4
Xfce4 plugin for %{name} package.


%prep
%autosetup


%build
# default: --with-lx --with-pmenu --with-gtktheme --with-xfce4-panel-applet
%{configure} -a
%{make_build}


%install
%{make_install}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
# TODO: make test (failed on aarch64: https://github.com/johanmalm/jgmenu/issues/123)


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}*
%{_libexecdir}/%{name}/%{name}-*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/%{name}*.*
%exclude %{_libexecdir}/%{name}/%{name}-{lx,pmenu.py,gtktheme.py}
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
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 14 2024 TI_Eugene <ti.eugene@gmail.com> - 4.5.0-1
- Version bump (close #2331624)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 4.4.1-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Florian Weimer <fweimer@redhat.com> - 4.4.1-2
- Fix xfce4-panel registration

* Tue Nov 01 2022 TI_Eugene <ti.eugene@gmail.com> - 4.4.1-1
- Version bump (close #2138771)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 TI_Eugene <ti.eugene@gmail.com> - 4.4.0-1
- Version bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 TI_Eugene <ti.eugene@gmail.com> - 4.3.0-1
- Version bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 TI_Eugene <ti.eugene@gmail.com> - 4.2.1-3
- Spec fixes

* Sat Jun 27 2020 TI_Eugene <ti.eugene@gmail.com> - 4.2.1-2
- Spec fixes

* Mon Jun 08 2020 TI_Eugene <ti.eugene@gmail.com> - 4.2.1-1
- Initial build

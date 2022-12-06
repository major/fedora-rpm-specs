%global sys_name nwg_panel

Name:       nwg-panel
Version:    0.7.14
Release:    %autorelease
Summary:    GTK3-based panel for sway window manager
BuildArch:  noarch

License:    MIT
URL:        https://github.com/nwg-piotr/nwg-panel
Source:     %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: python3-devel >= 3.4
BuildRequires: python3-setuptools
BuildRequires: systemd-rpm-macros

Requires:   gtk-layer-shell
Requires:   gtk3
Requires:   python3-gobject
Requires:   python3-i3ipc
Requires:   wlr-randr

Recommends: light
Recommends: playerctl
Recommends: python3-netifaces
Recommends: python3-psutil
Recommends: python3-pybluez

### Not packaged
# Recommends: pamixer

%description
I have been using sway since 2019 and find it the most comfortable working
environment, but... Have you ever missed all the graphical bells and whistles
in your panel, we used to have in tint2? It happens to me. That's why I
decided to try to code a GTK-based panel, including best features from my two
favourites: Waybar and tint2. Many thanks to Developers and Contributors of
the both projects!

There are 8 modules available at the moment, and I don't plan on many more.
Basis system controls are available in the Controls module, and whatever else
you may need, there's an executor for that.


%prep
%autosetup

sed -i 's|#!/usr/bin/python|#!/usr/bin/python3|' \
    nwg_panel/executors/arch_updates.py


%build
%py3_build


%install
%py3_install

# Remove shebang from Python libraries
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/{/,modules}/*.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# Remove shebang from Python libraries
for lib in %{buildroot}%{python3_sitelib}/%{sys_name}/*.py; do
 sed '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

install -Dpm 0644 %{name}.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0644 nwg-shell.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0755 %{name}-config.desktop -t %{buildroot}%{_datadir}/applications/
install -Dpm 0644 %{name}.service -t %{buildroot}%{_userunitdir}/


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-config
%{_bindir}/nwg-dwl-interface
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{_userunitdir}/%{name}.service
%{python3_sitelib}/%{sys_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{sys_name}/


%changelog
%autochangelog

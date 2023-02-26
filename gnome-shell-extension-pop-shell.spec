%global extension   pop-shell
%global uuid        %{extension}@system76.com
%global commit      dcf17f345856476bf1401c690fbdc3fe8dcbb650
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gnome-shell-extension-%{extension}
Version:        1.2.0^10.%{shortcommit}
Release:        1%{?dist}
Summary:        GNOME Shell extension for advanced tiling window management
License:        GPL-3.0-only
URL:            https://github.com/pop-os/shell
BuildArch:      noarch

Source0:        %{url}/archive/%{commit}/%{extension}-%{shortcommit}.tar.gz
Source1:        50_org.gnome.desktop.wm.keybindings.%{extension}.gschema.override
Source2:        50_org.gnome.mutter.%{extension}.gschema.override
Source3:        50_org.gnome.mutter.wayland.%{extension}.gschema.override
Source4:        50_org.gnome.settings-daemon.plugins.media-keys.%{extension}.gschema.override
Source5:        50_org.gnome.shell.%{extension}.gschema.override
# downstream-only patch
Patch0:         0001-Remove-schema-handling-from-transpile.sh.patch

BuildRequires:  typescript >= 3.8
BuildRequires:  make

Requires:       gnome-shell >= 3.36

Recommends:     gnome-extensions-app
Recommends:     %{name}-shortcut-overrides = %{version}-%{release}

Provides:       %{extension} = %{version}-%{release}


%description
Pop Shell is a keyboard-driven layer for GNOME Shell which allows for quick and
sensible navigation and management of windows.  The core feature of Pop Shell
is the addition of advanced tiling window management - a feature that has been
highly-sought within our community.  For many - ourselves included - i3wm has
become the leading competitor to the GNOME desktop.


%package shortcut-overrides
Summary:        Shortcut overrides for %{name}


%description shortcut-overrides
Shortcut overrides for %{name}.


%prep
%autosetup -p 1 -n shell-%{commit}


%build
%make_build compile


%install
%make_install

# install the schema file
install -D -p -m 0644 \
    schemas/org.gnome.shell.extensions.%{extension}.gschema.xml \
    %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml

# install the gnome-control-center keybindings
install -d -m 0755 %{buildroot}%{_datadir}/gnome-control-center/keybindings
install -p -m 0644 keybindings/*.xml %{buildroot}%{_datadir}/gnome-control-center/keybindings/

# install the schema override files
install -d -m 0755 %{buildroot}%{_datadir}/glib-2.0/schemas
install -p -m 0644 %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{buildroot}%{_datadir}/glib-2.0/schemas/


%files
%license LICENSE
%doc README.md
%{_datadir}/gnome-shell/extensions/%{uuid}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.%{extension}.gschema.xml
%{_datadir}/gnome-control-center/keybindings/*.xml


%files shortcut-overrides
%{_datadir}/glib-2.0/schemas/*.%{extension}.gschema.override


%changelog
* Fri Feb 24 2023 Carl George <carl@george.computer> - 1.2.0^10.dcf17f3-1
- Update to upstream snapshot for GNOME 44 compatibility

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0^9.886a069-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Carl George <carl@george.computer> - 1.2.0^9.886a069-1
- Latest upstream snapshot

* Fri Sep 02 2022 Carl George <carl@george.computer> - 1.2.0^8.4520e78-1
- Latest upstream snapshot (GNOME 43 compatibility)

* Wed Aug 31 2022 Carl George <carl@george.computer> - 1.2.0^7.4c03091-1
- Latest upstream snapshot

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0^6.af192b4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Mar 20 2022 Carl George <carl@george.computer> - 1.2.0^6.af192b4-1
- Latest upstream snapshot (GNOME 42 compatibility)

* Sun Jan 23 2022 Carl George <carl@george.computer> - 1.2.0^5.21745c4-1
- Latest upstream snapshot

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0^4.1fddaa8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 28 2021 Carl George <carl@george.computer> - 1.2.0^4.1fddaa8-1
- Latest upstream snapshot
- Upstream support for GNOME 41
- Upstream removal of pop-launcher

* Thu Aug 05 2021 Carl George <carl@george.computer> - 1.2.0^3.ab87042-2
- Rebuild to revert %%autochangelog

* Thu Aug 05 2021 Carl George <carl@george.computer> - 1.2.0^3.ab87042-1
- Latest upstream snapshot

* Sat Jul 24 2021 Carl George <carl@george.computer> - 1.2.0^2.9616931-1
- Latest upstream snapshot

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0^1.d59e373-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 26 2021 Carl George <carl@george.computer> - 1.2.0^1.d59e373-1
- Latest upstream snapshot
- Fixes: rhbz#1946867

* Mon Feb 15 2021 Carl George <carl@george.computer> - 1.2.0-3
- Fix org.gnome.mutter override

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Carl George <carl@george.computer> - 1.2.0-1
- Latest upstream

* Sun Jan 10 2021 Carl George <carl@george.computer> - 1.1.0-1
- Latest upstream

* Thu Dec 03 2020 Carl George <carl@george.computer> - 1.0.0-3.20201130gitee943b8
- Latest upstream

* Wed Nov 18 2020 Carl George <carl@george.computer> - 1.0.0-2.20201118git5137d52
- Latest upstream
- Include gnome-control-center keybindings

* Mon Nov 09 2020 Carl George <carl@george.computer> - 1.0.0-1.20201109git04eaf4f
- Latest upstream
- Provide pop-shell

* Thu Oct 29 2020 Carl George <carl@george.computer> - 1.0.0-1
- Latest upstream

* Thu Oct 22 2020 Carl George <carl@george.computer> - 0.1.0-1.20201016gita11d3c3
- Split gschema overrides to seperate files

* Tue Oct 20 2020 Carl George <carl@george.computer> - 0.1.0-0.9.20201016gita11d3c3
- Latest upstream commit
- Sync shortcut overrides with pop-session
- Move shortcut overrides to a subpackage
- Open shortcuts website if pop-shell-shortcuts is not installed

* Fri Oct 02 2020 Carl George <carl@george.computer> - 0.1.0-0.8.20201001gitff702bc
- Latest upstream commit
- Include new color-dialog file

* Fri Oct 02 2020 Drew DeVore <drew@devorcula.com> - 0.1.0-0.7.20200929gitb9f8d96
- Added override for stacking conflict

* Thu Oct 01 2020 Carl George <carl@george.computer> - 0.1.0-0.6.20200929gitb9f8d96
- Latest upstream commit

* Mon Sep 21 2020 Carl George <carl@george.computer> - 0.1.0-0.5.20200920git8791171
- Latest upstream commit

* Tue Sep 15 2020 Carl George <carl@george.computer> - 0.1.0-0.4.20200915gite5a80ea
- Latest upstream commit

* Thu Sep 10 2020 Carl George <carl@george.computer> - 0.1.0-0.3.20200908git017c92e
- Latest upstream commit
- Add primary-super-h/l versions of toggle-tiled-left/right keybindings

* Fri Aug 28 2020 Carl George <carl@george.computer> - 0.1.0-0.2.20200821git8416328
- Add keyboard shortcut overrides

* Thu Aug 27 2020 Carl George <carl@george.computer> - 0.1.0-0.1.20200821git8416328
- Initial package

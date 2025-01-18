%global upload_hash 4a5dcb11cec0b0438ad575db08aa755c

Name:           fragments
Version:        3.0.1
Release:        2%{?dist}
Summary:        Easy to use BitTorrent client which follows the GNOME HIG

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/Fragments
Source0:        %{url}/uploads/%{upload_hash}/fragments-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rust-packaging

Requires: adwaita-icon-theme
Requires: transmission-daemon       

%description
Fragments is an easy to use BitTorrent client which follows the GNOME HIG and
includes well thought-out features.


%prep
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc README.md
%license COPYING.md
%{_bindir}/fragments
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/fragments/*.gresource
%{_datadir}/icons/hicolor/*/*/*
%{_metainfodir}/*.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 03 2024 Pete Walter <pwalter@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1 (rhbz#2284003)

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 23 2024 Pete Walter <pwalter@fedoraproject.org> - 3.0.0-1
- Update to 3.0.0 (rhbz#2273879)
- Don't override RUSTFLAGS
- Use SPDX license IDs

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Pete Walter <pwalter@fedoraproject.org> - 2.1.1-1
- Update to 2.1.1 (rhbz#1878523)
- ExcludeArch i686 for https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval

* Thu Feb 24 2022 Fries <fries1234@protonmail.com> - 2.0.2-1
- Update to 2.0.2
- Switch to libadwaita-1
- Build now requires Rust

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.5-3
- Rebuilt with OpenSSL 3.0.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 25 2021 Kalev Lember <klember@redhat.com> - 1.5-1
- Update to 1.5
- Switch to libhandy-1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 19:10:31 EEST 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4-18
- Rebuild due libevent 2.1.12 with a soname bump 2

* Wed Sep 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4-17
- Rebuild due libevent 2.1.12 with a soname bump
- style: spec

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar 16 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4-13
- Initial package

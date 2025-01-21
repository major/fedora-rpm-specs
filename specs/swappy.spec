# -*-Mode: rpm-spec -*-

Name: swappy
Version: 1.5.1
Release: 6%{?dist}
Summary: Wayland native snapshot editing tool, inspired by Snappy on macOS
License: MIT
URL:     https://github.com/jtheoof/swappy
Source0: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
# gpg was downloaded by:
# gpg2 --recv-keys 0x6A6B35DBE9442683
# gpg2 --export --export-options export-minimal 0x6A6B35DBE9442683 > 6A6B35DBE9442683.gpg
Source2: 6A6B35DBE9442683.gpg

BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: meson
BuildRequires: scdoc
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: desktop-file-utils

# from the author re fontawesome: "Considering the icons that I
# currently use, swappy should work with FA 4. But if I need to add
# more tools (and so icons) in the future, I will pick from FA 5,
# which has a lot more than FA 4 so it might not work in the future.
# Therefore I would still recommend using FA >=5, but it's technically
# OK to have FA >= 4 at the moment."
Recommends: fontawesome-fonts
Recommends: wl-clipboard

%description
A Wayland native snapshot and editor tool, inspired by Snappy on
macOS. Works great with grim, slurp and sway. But can easily work with
other screen copy tools that can output a final PNG image to stdout.

%prep
%gpgverify -k 2 -s 1 -d 0
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
install -p -D -m 0644 -t %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps res/icons/hicolor/scalable/apps/%{name}.svg

desktop-file-install --dir %{buildroot}/%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/%{name}.desktop

sed -i 's/^Exec=.*$/Exec=sh -c "if [ -n \\"\\\\$*\\" ]; then exec swappy -f \\"\\\\$@\\"; else grim -g \\"\\\\$(slurp)\\" - | swappy -f -; fi" placeholder %F/' %{buildroot}/%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/icons/*

%license LICENSE

%doc README.md
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Bob Hepple <bob.hepple@gmail.com> - 1.5.1-1
- new version

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Bob Hepple <bob.hepple@gmail.com> - 1.4.0-1
- new version

* Mon Sep 06 2021 Bob Hepple <bob.hepple@gmail.com> - 1.3.1-4
- rebuilt with better Exec= key in desktop file

* Fri Jul 30 2021 Bob Hepple <bob.hepple@gmail.com> - 1.3.1-3
- fixed install path for .desktop file RHBZ#1988015

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Feb 20 2021 Bob Hepple <bob.hepple@gmail.com> - 1.3.1-1
- new version

* Thu Feb 18 2021 Bob Hepple <bob.hepple@gmail.com> - 1.3.0-1
- new version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Bob Hepple <bob.hepple@gmail.com> - 1.2.1-1
- new version and add gpgverify

* Mon Jul 06 2020 Bob Hepple <bob.hepple@gmail.com> - 1.2.0-1
- new version

* Tue Jun 30 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.0-3
- add swappy-fix-format for arm builds

* Mon Jun 29 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.0-2
- rebuilt for RHBZ#1849384

* Fri Jun 26 2020 Bob Hepple <bob.hepple@gmail.com> - 1.1.0-1
- new version

* Tue Apr 21 2020 Bob Hepple <bob.hepple@gmail.com> - 1.0.0-1
- version 1.0.0

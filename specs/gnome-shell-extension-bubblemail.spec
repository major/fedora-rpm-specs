%global upname bubblemail-gnome-shell

Name:           gnome-shell-extension-bubblemail
Version:        24
Release:        2%{?dist}
Summary:        GNOME Shell indicator for new and unread mail using Bubblemail 

License:        GPL-2.0-or-later
URL:            http://bubblemail.free.fr/
Source0:        https://framagit.org/razer/%{upname}/-/archive/v%{version}/%{upname}-v%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  gettext

Requires:       bubblemail >= 1.7
Requires:       gnome-shell >= 45.0

BuildArch:      noarch

%description
%{name} relies on the Bubblemail service to display
notifications in GNOME shell about new and unread messages in local (mbox,
Maildir) and remote (POP3, IMAP) mailboxes.


%prep
%autosetup -n %{upname}-v%{version}
mv src/LICENSE ./

%build	
%meson -Dgnome_shell_libdir=%{_datadir}/gnome-shell/extensions/ \
       -Dgsettings_schemadir=%{_datadir}/glib-2.0/schemas/
%meson_build

%install
%meson_install
%find_lang %{upname}

%files -f %{upname}.lang
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.bubblemail.gschema.xml
%{_datadir}/gnome-shell/extensions/bubblemail@razer.framagit.org/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 23 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 24-1
- Update to v24 - compatible with GNOME 47

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 30 2024 Alexander Ploumistos <alexpl@fedoraproject.org> - 23-1
- Update to v23 - compatible with GNOME 46

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 21.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 21.1-1
- Update to 21.1 (#2246814)
- Fix a typo in the changelog

* Tue Oct 24 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 21-1
- Update to v21 - compatible with GNOME >= 45

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu May 11 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 20.1-1
- Update to v20.1
- Fixes rendering bug on GNOME shell < 44

* Sun May 07 2023 Alexander Ploumistos <alexpl@fedoraproject.org> - 20-1
- Update to v20

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 01 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 19-1
- Update to v19
- Switch to SPDX license identifier

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 19 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 18-1
- Update to v18

* Thu May 12 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 17-1
- Update to v17

* Sat Apr 09 2022 Alexander Ploumistos <alexpl@fedoraproject.org> - 16-1
- Update to v16

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Nov 10 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 15-1
- Update to v15
- Bump required bubblemail service version to 1.5

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Apr 11 2021 Alexander Ploumistos <alexpl@fedoraproject.org> - 14-1
- Update to v14 - compatible with GNOME 40 
- New versioning scheme
- Bump required bubblemail service version to 1.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.3-1
- Update to v1.3

* Thu Aug 27 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.2-1
- Update to v1.2
- Fix typo in changelog

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 17 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.1-1
- Update to v1.1

* Sun May 24 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 1.0-1
- Update to v1.0

* Tue Apr 21 2020 Alexander Ploumistos <alexpl@fedoraproject.org> - 0.71-1
- Initial release for Fedora

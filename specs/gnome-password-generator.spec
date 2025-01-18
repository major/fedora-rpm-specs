%global project_owner Jenselme

Summary:        Graphical secure password generator
Name:           gnome-password-generator
Version:        2.1.0
Release:        19%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/%{project_owner}/%{name}
Source0:        https://github.com/%{project_owner}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires: make
Requires:       python3-gobject
Requires:       hicolor-icon-theme
BuildArch:      noarch


%description
Gnome Password Generator is a GUI based secure password generator. It allows
the user to generate a specified number of random passwords of a specified
length.


%prep
%autosetup -p 1


%build
%make_build


%install
%make_install


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%files
%license COPYING
%license AUTHORS
%doc ChangeLog
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/96x96/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.0-18
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-2
- Remove obsolete scriptlets

* Sat Aug 05  2017 Julien Enselme <jujens@jujens.eu> - 2.1.0-1
- Update to 2.1.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 06 2017 Julien Enselme <jujens@jujens.eu> - 2.0.4-3
- Correct BuildRequires to run appstream-util

* Wed Jul 05 2017 Julien Enselme <jujens@jujens.eu> - 2.0.4-2
- Don't create directories any more. The Makefile does it.
- Validate desktop file.
- Put %%license on two lines to be coherent.

* Wed Jul 05 2017 Julien Enselme <jujens@jujens.eu> - 2.0.4-1
- Update to 2.0.4

* Wed Jul 05 2017 Julien Enselme <jujens@jujens.eu> - 2.0.1-2
- Remove usage of %%github_name (redundant with %%name)
- Use %%autosetup
- Preserve timestamps with the install command
- Create all directories in one command
- Move AUTHORS to %%license
- Validate appdata
- Remove vendorization when installing desktop file

* Mon Jul 03 2017 Julien Enselme <jujens@jujens.eu> - 2.0.1-1
- Add appdata file
- Change source URL to rely on tag instead of commit

* Mon Jul 03 2017 Julien Enselme <jujens@jujens.eu> - 2.0.0-3.git0436b6d
- Correct make related macros

* Sun Jul 02 2017 Julien Enselme <jujens@jujens.eu> - 2.0.0-2.git0436b6d
- Add missing question mark (?) in %%{dist} macro

* Sat Jul 01 2017 Julien Enselme <jujens@jujens.eu> - 2.0.0-1.git0436b6d
- Update to 2.0.0
- Unretire

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 1.6-6
- Update icon cache scriptlet

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 07 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.6-2
- Replaced 'Requires: gnome-python2' with 'Requires: gnome-python2-gnome' on
  all distributions starting from Fedora 10. Closes Red Hat Bugzilla bug
  #460023.
- Trimmed the 'Requires' list.

* Sat May 17 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.6-1
- Version bump to 1.6. Closes Red Hat Bugzilla bug #438016.

* Sat Oct 06 2007 Debarshi Ray <rishi@fedoraproject.org> - 1.5-2
- Removed 'Requires: redhat-artwork' and fixed the sources. Closes Red Hat
  Bugzilla bug #313981.

* Wed Aug 22 2007 Debarshi Ray <rishi@fedoraproject.org> - 1.5-1
- Version bump to 1.5.
- Changed value of License according to Fedora licensing guidelines.
- Place icon in SVG format under /usr/share/icons/hicolor/scalable/apps.
- gnome-password-generator.desktop fixes added by upstream.

* Wed Aug 01 2007 Debarshi Ray <rishi@fedoraproject.org> - 1.4-5
- Removed Application from Categories.

* Tue Jul 31 2007 Debarshi Ray <rishi@fedoraproject.org> - 1.4-4
- Added 'Requires: redhat-artwork'.
- Trimmed the 'BuildRequires' list.
- Place icon under /usr/share/icons/hicolor/96x96/apps instead of
  /usr/share/icons/hicolor/48x48/apps.

* Sat Jul 28 2007 Debarshi Ray <rishi@fedoraproject.org> - 1.4-3
- Added 'Requires: hicolor-icon-theme'.
- Fixed 'gtk-update-icon-cache' in the post[un] scriptlets.
- Trimmed the 'make install ... DESTDIR=%%{buildroot}' command.
- Trimmed the 'BuildRequires' list.

* Sat Jun 30 2007 Debarshi Ray <rishi@fedoraproject.org> - 1.4-2
- Removed X-Fedora from Categories.
- Set vendor_id to "gnome".

* Tue Jun 26 2007 Debarshi Ray <rishi@fedoraproject.org> - 1.4-1
- Initial build. Imported SPECs from Dag Apt Repository and Fedora Extras 6.

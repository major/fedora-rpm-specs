# TODO: https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering
#       rpmlint warns about private-shared-object-provides
#       can't use filter because the package doesn't met any of the required criteria
#         ! Noarch package       ... caused by libreport wrappers shared library
#         ! no binaries in $PATH ... caused by gnome-abrt python script in /usr/bin

# Uncomment when building from a git snapshot.
#%%global snapshot 1
%global commit 3e3512d2d6c81a4ca9b3b4d3f3936c876a6482f7
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       gnome-abrt
Version:    1.5.0
Release:    2%{?dist}
Summary:    A utility for viewing problems that have occurred with the system

License:    GPL-2.0-or-later
URL:        https://github.com/abrt/%{name}
%if 0%{?snapshot}
Source0:    %{url}/archive/%{commit}.tar.gz#/%{name}-%{commit}.tar.gz
%else
Source0:    %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildRequires: git-core
BuildRequires: meson >= 0.59.0
BuildRequires: gettext
BuildRequires: libtool
BuildRequires: python3-devel
BuildRequires: desktop-file-utils
BuildRequires: asciidoc
BuildRequires: xmlto
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: libreport-gtk-devel > 2.14.0
BuildRequires: python3-libreport
BuildRequires: abrt-gui-devel > 2.14.0
BuildRequires: gtk4-devel
BuildRequires: libadwaita-devel
%if 0%{?fedora}
BuildRequires: python3-six
BuildRequires: python3-gobject
BuildRequires: python3-dbus
BuildRequires: python3-humanize
%endif

Requires:   glib2%{?_isa} >= 2.63.2
Requires:   gobject-introspection%{?_isa} >= 1.63.1
Requires:   python3-libreport
Requires:   python3-gobject
Requires:   python3-dbus
Requires:   python3-humanize
Requires:   python3-beautifulsoup4
Requires:   gtk4
Requires:   libadwaita

%description
A GNOME application allows users to browse through detected problems and
provides them with convenient way for managing these problems.


%prep
%autosetup -S git %{?snapshot:-n %{name}%-%{commit}}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}

%check
%meson_test


%files -f %{name}.lang
%doc COPYING README.md
%{python3_sitearch}/gnome_abrt
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/metainfo/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/*/apps/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 24 2024 Packit <hello@packit.dev> - 1.5.0-1
- Update to version 1.5.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 1.4.3-2
- Rebuilt for Python 3.13

* Wed Feb 07 2024 Packit <hello@packit.dev> - 1.4.3-1
- Release version 1.4.3-1 (Michal Srb)
- Update translations (mgrabovsky)
- views: Replace self-rolled function for human-readable dates (Nicolas Jeker)
- Update translations (mgrabovsky)
- Update translations (mgrabovsky)
- spec: Do not run Pylint as part of build (Matěj Grabovský)
- Update translations (mgrabovsky)
- Update translations (mgrabovsky)
- Use SPDX format for license field (Matěj Grabovský)
- Update translations (mgrabovsky)
- l10n: Remove unnecessary assignment (Matěj Grabovský)
- Add CodeQL workflow for GitHub code scanning (LGTM Migrator)
- Update translations (mgrabovsky)
- Update translations (mgrabovsky)
- Update translations (mgrabovsky)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 1.4.2-5
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.4.2-2
- Rebuilt for Python 3.11

* Mon May 23 2022 Packit <hello@packit.dev> - 1.4.2-1
- Release version 1.4.2-1 (Matěj Grabovský)
- meson: Remove duplicate code (Matěj Grabovský)
- views: Escape markup in link title (Matěj Grabovský)
- Update translations (mgrabovsky)
- views: Use maxsplit argument to rsplit() (Matěj Grabovský)
- github: Fix lint workflow (Matěj Grabovský)
- Update translations (mgrabovsky)
- ui: Change wording in popup menu (Matěj Grabovský)
- lint: Try to limit results  due to timeouts (Matěj Grabovský)
- gnome_abrt: Fix code style errors (Matěj Grabovský)
- l10n: Remove call to deprecated function (Matěj Grabovský)
- meson: Adjust environment for Pylint (Matěj Grabovský)
- meson: Copy spec file to build directory (Matěj Grabovský)
- Bump Meson dependency to >= 0.59.0 (Matěj Grabovský)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Matěj Grabovský <mgrabovs@redhat.com> - 1.4.1-2
- Rebuild for testing

* Tue Jan 18 2022 Packit Service <user-cont-team+packit-service@redhat.com> - 1.4.1-1
- Release version 1.4.1-1 (Matěj Grabovský)
- Update translations (Matěj Grabovský)

* Thu Aug 12 2021 Matej Grabovsky <mgrabovs@redhat.com> 1.4.0-2
- Recover changelog

* Wed Aug 11 2021 Matej Grabovsky <mgrabovs@redhat.com> 1.4.0-1
- New upstream release
- Handle connection and string decoding errors gracefully
- Bump required abrt and libreport versions to 2.14.0
- Update translations

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 07 2021 Python Maint <python-maint@redhat.com> - 1.3.6-9
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.3.6-7
- Rebuilt for Python 3.10

* Sat Mar 20 2021 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3.6-5
- Bump for upgrade path from F-33

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 24 2020 rebase-helper <rebase-helper@localhost.local> - 1.3.6-1
- new upstream release: 1.3.6

* Wed Aug 05 2020 Merlin Mathesius <mmathesi@redhat.com> - 1.3.5-5
- Minor ELN conditional fixes

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 - Ernestas Kulik <ekulik@redhat.com> - 1.3.5-3
- Add patch to fix https://bugzilla.redhat.com/show_bug.cgi?id=1854949

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.5-2
- Rebuilt for Python 3.9

* Mon May 25 2020 Ernestas Kulik <ekulik@redhat.com> - 1.3.5-1
- new upstream release: 1.3.5

* Thu May 21 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 1.3.4-1
- new upstream release: 1.3.4

* Wed May 20 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 1.3.3-1
- new upstream release: 1.3.3

* Mon May 18 2020 Ernestas Kulik <ekulik@redhat.com> - 1.3.2-3
- Add patch for https://bugzilla.redhat.com/show_bug.cgi?id=1836614

* Wed May 13 2020 Packit Service <user-cont-team+packit-service@redhat.com> - 1.3.2-1
- new upstream release: 1.3.2

* Mon Feb 03 2020 Ernestas Kulik <ekulik@redhat.com> - 1.3.1-1
- new upstream release: 1.3.1

* Mon Feb 03 2020 Ernestas Kulik <ekulik@redhat.com> - 1.3.0-1
- new upstream release: 1.3.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 10 2019 Rafal Luzynski <digitalfreak@lingonborough.com> - 1.2.9-3
- Apply upstream changes in the spec file
- Fix "gnome-abrt --help" not fully translated
- New translation language: Afrikaans
- Update translations: Czech, Danish, Dutch, French, Friulian, Indonesian,
  Polish, Portuguese (PT), Slovak, Swedish, Ukrainian

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.9-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Rafal Luzynski <digitalfreak@lingonborough.com> - 1.2.9-1
- Update to 1.2.9

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.8-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 22 2019 Rafal Luzynski <digitalfreak@lingonborough.com> - 1.2.8-1
- Update the spec file to 1.2.8 (downstream release)

* Fri Apr 26 2019 Ernestas Kulik <ekulik@redhat.com> - 1.2.8-1
- Update to 1.2.8

* Fri Feb 15 2019 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.7-2
- Add upstream patches
- Fix build failure
- Update translations: Polish, Serbian, Ukrainian
- Change the appdata location according to the current guidelines
- Bump required pygobject3 version

* Mon Feb 04 2019 Ernestas Kulik <ekulik@redhat.com> - 1.2.7-1
- Update to 1.2.7

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 18 2018 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.6-8
- Translation updates: Danish, Japanese, Portuguese (BR), Chinese (TW), and more

* Fri Jul 20 2018 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.6-7
- Fix incorrect parsing of reported_to file (resolves: #1600809)
- Remove explicit object inheritance reported by pylint(R0205)
- Fix python3-libreport dependency (the old name libreport-python3 is obsolete)
- Resolves: #1604140

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.6-5
- Rebuilt for Python 3.7

* Fri Jun 01 2018 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.6-4
- Remove "Group:" tag according to the current guidelines
- Remove Expert mode
- Mark "--help" text for translation
- Translation updates: Brazilian Portuguese, Czech, French, Turkish, and more
- Fix some pylint warnings

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.6-2
- Remove obsolete scriptlets

* Thu Nov 16 2017 Julius Milan <jmilan@redhat.com> 1.2.6-1
- Translation updates
- Satisfy pylint v1.7.1 warnings
- pylintrc: disable pylint no-else-return warnings
- Add fur, kk, nn languages into LINGUAS

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.5-4
- New translations: Friulian, Kazakh, Norwegian Nynorsk
- Translation updates: Dutch, Finnish, Marathi

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-2
- Rebuild for Python 3.6

* Mon Oct 31 2016 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.5-1
- Translation updates
- Fix some small issues to please pylint
- Fix padding of the list items
- Update the project URL

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 28 2016 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.4-2
- Translation updates (Albanian)
- Resolves: #1347951

* Tue Jun 07 2016 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.4-1
- Translation updates (Russian, Slovak)
- Add new translation languages - Albanian
- One more fix for the format of a package version
- Align the header buttons position to the sidebar size

* Wed Apr 13 2016 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.3-3
- Correct format of the package version
- Translation updates

* Fri Apr 08 2016 Rafal Luzynski <digitalfreak@lingonborough.com> 1.2.3-2
- Translation updates

* Wed Mar 23 2016 Jakub Filak <jfilak@redhat.com> 1.2.3-1
- Translation updates
- Let main title of the crash wrap
- Label all kernel oops problems with "System"
- Disambiguate the word "System"
- Use context gettext
- Reword "Detected" to "First Detected"
- Use "Problem Reporting" as the program name in the About box
- Remove "Report problem with ABRT"
- Fix dim-label being applied to proper app icons
- Make "Select" button unsensitive when list is empty
- Make titlebar blue in selection mode
- Use dim-label style, not hard-coded colours for labels
- Remove "ABRT Configuration" dialogue
- Add search button
- Add more keywords to .desktop

* Thu Feb 18 2016 Jakub Filak <jfilak@redhat.com> - 1.2.2-1
- Translation updates
- Fix the plural/singular translations for fancydate -Rafal Luzynski <digitalfreak@lingonborough.com>
- Details pane: new design - Rafal Luzynski <digitalfreak@lingonborough.com>

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Jan Beran <jberan@redhat.com> - 1.2.1-2
- Do not pass None to function expecting str object
- Add kudos to the AppData file
- Problem type included in the problem list: Rafal Luzynski <digitalfreak@lingonborough.com>
- Scroll whole details panel instead of its single widgets: Rafal Luzynski <digitalfreak@lingonborough.com>
- Fix broken build caused by pylint warning

* Thu Nov 19 2015 Jakub Filak <jfilak@redhat.com> - 1.2.1-1
- HTMLParseError replaced with generic Exception: Francesco Frassinelli <fraph24@gmail.com>
- Fix handling of the singular cases: Rafal Luzynski <digitalfreak@lingonborough.com>
- Don't scroll the sidebar horizontally: Rafal Luzynski <digitalfreak@lingonborough.com>
- Show HiDPI icons on HiDPI screens: Rafal Luzynski <digitalfreak@lingonborough.com>
- Get rid of the Gtk3 module loading warning
- Translation updates
- Resolves: #1283365

* Thu Nov 12 2015 Jakub Filak <jfilak@redhat.com> - 1.2.0-9
- Fix build with Python 3.5

* Thu Nov 12 2015 Jakub Filak <jfilak@redhat.com> - 1.2.0-8
- Temporarily stop using pylint and turn off 'make check'
- Rebuilt for Python3.5 rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov 6 2015 Jakub Filak <jfilak@redhat.com> - 1.2.0-6
- Rebuilt for Python3.5 rebuild

* Fri Aug 14 2015 Matej Habrnal <mhabrnal@redhat.com> - 1.2.0-5
- Correct testing of return values from ABRT D-Bus API wrrapper

* Mon Jul 13 2015 Jakub Filak <jfilak@redhat.com> - 1.2.0-4
- Fix loading applicaton icons
- Fix an exception when searching for a bug ID
- Resolves: #1242080

* Thu Jun 18 2015 Matej Habrnal <mhabrnal@redhat.com> - 1.2.0-3
- Use UTF-8 encoding when working with user files
- Remove the Details button from the top bar in non-GNOME desktops

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jakub Filak <jfilak@redhat.com> 1.2.0-1
- Enabled the Details also for the System problems
- Do not crash in the testing of availabitlity of XServer
- Remove a debug print introduced with port to Python3
- Fix 'Open problem's data directory'
- Quit Application on Ctrl+Q
- Translation updates
- Resolves: #1188002

* Mon May 11 2015 Matej Habrnal <mhabrnal@redhat.com> - 1.1.2-2
- Translations update

* Tue May 05 2015 Matej Habrnal <mhabrnal@redhat.com> - 1.1.2-1
- Add symbolic icon
- Use own window header also in GNOME Classic
- Let the theme handle the colour in the problems list
- Remove border's custom style in the problems list
- Resolves: #1193656

* Thu Apr 09 2015 Jakub Filak <jfilak@redhat.com> - 1.1.1-1
- Several bug fixes

* Tue Mar 17 2015 Jakub Filak <jfilak@redhat.com> - 1.1.0-2
- Fix a crash caused by i18n
- Fix a crash caused by problems without environment file
- Resolves: #1204524

* Tue Mar 17 2015 Jakub Filak <jfilak@redhat.com> - 1.1.0-1
- Switch to Python3
- Translation updates
- Search by Bug Tracker ID
- Always show an icon for problems
- Try to use environment to find the application
- Polished look

* Mon Oct 13 2014 Jakub Filak <jfilak@redhat.com> - 1.0.0-1
- New upstream release with updated look & feel

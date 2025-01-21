Name:           terminator
Version:        2.1.4
Release:        4%{?dist}.1
Summary:        Store and run multiple GNOME terminals in one window

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/gnome-terminator
Source0:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/terminator-%{version}.tar.gz
Source1:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/terminator-%{version}.tar.gz.asc
Source2:        https://github.com/gnome-terminator/terminator/releases/download/v%{version}/gpg-D11A7596F61705480C711598F2FAC7C7BAE930A5.asc

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gnupg2
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel

Requires:       keybinder3
Requires:       python3-configobj
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       vte291

Patch0:         0000-terminator-fix-desktop-file.patch


%description
Multiple GNOME terminals in one window.  This is a project to produce
an efficient way of filling a large area of screen space with
terminals. This is done by splitting the window into a resizeable
grid of terminals. As such, you can  produce a very flexible
arrangements of terminals for different tasks.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel 


%install
%pyproject_install
%pyproject_save_files terminatorlib
%find_lang %{name}


%check
%py3_check_import terminatorlib
desktop-file-validate %{buildroot}%{_datadir}/applications/terminator.desktop


%files -f %{pyproject_files} -f %{name}.lang
%doc CHANGELOG.md README.md
%license COPYING
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man5/%{name}_config.5.*
%{_bindir}/%{name}
%{_bindir}/remotinator
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/HighContrast/*/*/%{name}*.png
%{_datadir}/icons/HighContrast/*/*/%{name}*.svg
%{_datadir}/icons/HighContrast/16x16/status/terminal-bell.png
%{_datadir}/icons/hicolor/*/*/%{name}*.png
%{_datadir}/icons/hicolor/*/*/%{name}*.svg
%{_datadir}/icons/hicolor/16x16/status/terminal-bell.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1.4-3.1
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 Matt Rose <mattrose@folkwolf.net> - 2.1.4-1.1
- New Upstream Release: 2.1.4

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1.3-6.1
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 2.1.3-3.1
- Rebuilt for Python 3.12

* Tue Jun 27 2023 Matt Rose <mattrose@folkwolf.net> - 2.1.3-2.1
- fix pyproject_wheel command

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 2.1.3-2
- Rebuilt for Python 3.12

* Fri Mar 10 2023 Matt Rose <mattrose@folkwolf.net> - 2.1.3-1
- New upstream release: 2.1.3

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Matt Rose <mattrose@folkwolf.net> - 2.1.2-1
- New upstream release: 2.1.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Dominic Hopf <dmaphy@fedoraproject.org>- 2.1.1-1 
- Initial build for EPEL9

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.1-6
- Rebuilt for Python 3.11

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 07 2021 David King <amigadave@amigadave.com> - 2.1.1-4
- Own more directories
- Be consistent with use of %%{buildroot}
- Tighten globs in files list
- Avoid unnecessary gtk-update-icon-cache
- Use %%find_lang for locales
- Add license and documentation
- Import the module during %%check
- Verify GPG signature of sources

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.1-2
- Rebuilt for Python 3.10

* Sat Apr 03 2021 Dominic Hopf <dmaphy@fedoraproject.org> - 2.1.1-1
- New upstream release: 2.1.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Dominic Hopf <dmaphy@fedoraproject.org> - 2.1.0-1
- New upstream release: 2.1.0

* Sun Oct 11 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 2.0.1-1
- New upstream release: 2.0.1

* Tue Aug 25 2020 Hans de Goede <hdegoede@redhat.com> - 1.92-6
- Fix not being able to select text in the first column of a split terminal
  https://github.com/gnome-terminator/terminator/issues/191

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.92-4
- Rebuilt for Python 3.9

* Mon May 18 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.92-3
- Backport upstream patch for middle click issues on Wayland (RHBZ#1836812)

* Wed May 06 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.92-2
- Improve requirement listings
- Fix requirement for python3-psutil on EPEL8
- Add missing requirement for gtk-update-icon-cache

* Sat Apr 18 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.92-1
- New upstream release: 1.92

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Matt Rose <mattrose@folkwolf.net> - 1.91-14
- fix bug 1573927
* Tue Dec 17 2019 Matt Rose <mattrose@folkwolf.net> - 1.91-12
- Fix url Drag and Drop.  Thanks to Egmont Koblinger

* Mon Dec 16 2019 Matt Rose <mattrose@folkwolf.net> - 1.91-11
- Patched with python3 support, with thanks from Egmont Koblinger and Roman Kovtyukh

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Miro Hrončok <mhroncok@redhat.com> - 1.91-8
- Update Python macros to new packaging standards
  (See https://fedoraproject.org/wiki/Changes/Move_usr_bin_python_into_separate_package)

* Sat Jul 21 2018 Dominic Hopf <dmaphy@fedoraproject.org> - 1.91-7
- RHBZ#1606509: Fix FTBFS issue, explicitly use python2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.91-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.91-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.91-1
- New Upstream Release: Terminator 1.91

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Nov 30 2016 Matt Rose <mattrose@folkwolf.net> - 1.90-4
- add keybinder3 to requires

* Tue Nov 29 2016 Matt Rose <mattrose@folkwolf.net> - 1.90-3
- adjust requires for vte

* Thu Nov 24 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 1.90-2
- Adjust requires for python(2)-psutil for EPEL

* Wed Nov 23 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 1.90-1
- New Upstream Release: Terminator 1.90

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.98-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 10 2015 Marco Driusso <marcodriusso@gmail.com> - 0.98-2
- apply patch from upstream for fixing RHBZ#1268289 and add dependency to
  python-psutils

* Tue Sep 08 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 0.98-1
- New Upstream Release: Terminator 0.98

* Thu Jun 25 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-8
- add dependency to python-keybinder (RHBZ#1234627)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 05 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-5
- fix the new URL for the website

* Sun Jan 05 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-4
- update upstream URL to new website (RHBZ#1048553)
- fix bogus date in changelog-warnings

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-2
- fix an issue when inactive colour is set to 1.0 (RHBZ#968379)

* Fri May 17 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 0.97-1
- New upstream release: Terminator 0.97

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 24 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.96-1
- New upstream release: Terminator 0.96

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Oct 01 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.95-2
- readd dependency for gnome-python2-bonobo

* Wed Aug 25 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.95-1
- New upstream release: Terminator 0.95

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.94-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Jul 19 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.94-1
- New upstream release: Terminator 0.94

* Thu Apr 15 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.93-1
- New upstream release: Terminator 0.93

* Fri Apr 09 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.92-1
- New upstream release: Terminator 0.92

* Mon Apr 05 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.91-1
- New upstream release: Terminator 0.91

* Wed Mar 10 2010 Steven Fernandez <lonetwin@fedoraproject.org> 0.14-3
- Added patch to fix the traceback reported in bug 567861

* Wed Mar 3 2010 Steven Fernandez <lonetwin@fedoraproject.org> - 0.14-2
- Added dependency for deskbar-applets and gnome-python2-{bonobo,canvas}
  packages (bug 540551 and bug 509461)

* Thu Jan 14 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.14-1
- New terminator version 0.14

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul  7 2009 Ian Weller <ian@ianweller.org> - 0.13-2
- BuildRequires: intltool

* Thu Jul  2 2009 Ian Weller <ian@ianweller.org> - 0.13-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 20 2009 Ian Weller <ianweller@gmail.com> 0.12-1
- New upstream release
- Upstream fixed desktop file, removing patch0

* Mon Dec 08 2008 Ian Weller <ianweller@gmail.com> 0.11-3
- Patch version in terminatorlib/verison.py to the one we think it is
- Fix License tag
- Update post and postun scripts with one line

* Mon Dec 01 2008 Ian Weller <ianweller@gmail.com> 0.11-2
- Add BuildRequires: gettext
- Fix installation of .desktop file
- terminator-0.11-desktop.patch:
    Remove useless things
    Move to same category as gnome-terminal
- Uses spaces instead of tabs in the specfile because I can't stand tabs

* Mon Dec 01 2008 Ian Weller <ianweller@gmail.com> 0.11-1
- Update upstream
- Fix description to something useful
- Fix group
- Fix some specfile oddities
- Complete/restandardize file list
- Get rid of she-bangs in python_sitelib

* Sat Sep 13 2008 Max Spevack <mspevack AT redhat DOT com> 0.10
- New upstream release.
- Tried to make sure the spec file matches guidelines on Fedora wiki.

* Tue Jul 08 2008 chantra AatT rpm-based DdOoTt org 0.9.fc9.rb
- New upstream release

* Sat May 17 2008 chantra AatT rpm-based DdOoTt org 0.8.1.fc9.rb
- Initial release for Fedora 9.

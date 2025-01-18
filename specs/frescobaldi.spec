%{!?qt5_qtwebengine_arches:%global qt5_qtwebengine_arches %{ix86} x86_64 %{arm} aarch64 mips mipsel mips64el}

Name:           frescobaldi
Version:        3.3.0
Release:        9%{?dist}
Summary:        Edit LilyPond sheet music with ease!

# hyphenator.py is LGPLv2+
# The rest, including the core of the program, is GPLv2+
License:        GPLv2+ and LGPL-2.0-or-later
URL:            http://www.frescobaldi.org/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         frescobaldi-3.1.2-setup.patch

BuildArch:      noarch
ExclusiveArch: %{qt5_qtwebengine_arches}

BuildRequires:  desktop-file-utils
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires: make
Requires:       alsa-utils
Recommends:     lilypond
Requires:       python3-poppler-qt5
Requires:       portmidi
Requires:       python3-portmidi
Requires:       python3-ly >= 0.9.4
Requires:	python3-qt5-webengine
Requires:       python3-qpageview

%description
Frescobaldi is a LilyPond sheet music editor. It aims to be powerful,
yet lightweight and easy to use. It features:

    * Enter LilyPond scores, build and preview them with a mouse-click
    * Point-and-click support: click on notes or error messages to jump to the
      correct position
    * A powerful Score Wizard to quickly setup a musical score
    * Editing tools to:
          o manipulate the rhythm
          o hyphenate lyrics
          o quickly enter or add articulations and other symbols to existing
            music
          o run the document through convert-ly to update it to a newer
            LilyPond version
    * Context sensitive auto-complete, helping you to quickly enter LilyPond
      commands
    * Expansion manager to enter larger snippets of LilyPond input using short
      mnemonics
    * Built-in comprehensive User Guide


%prep
%setup -q
find -name "*.py"  -exec sed -i -e 's|#! python||' {} \;

%patch -P 0 -p0

%build
python3 ./setup.py build
make -C linux/

%install
python3 ./setup.py install --skip-build --root $RPM_BUILD_ROOT

# desktop file
desktop-file-install                                         \
   --dir=%{buildroot}%{_datadir}/applications                \
   --remove-category=Application                             \
   --add-category=AudioVideo                                 \
   --add-category=X-Notation                                 \
   --delete-original                                         \
   linux/org.frescobaldi.Frescobaldi.desktop

mkdir -p %{buildroot}%{_metainfodir}
install -m 0644 \
	linux/org.frescobaldi.Frescobaldi.metainfo.xml \
	%{buildroot}%{_metainfodir}/org.frescobaldi.Frescobaldi.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files
%license COPYING
%doc CHANGELOG.md README* THANKS TODO
%{_bindir}/%{name}
%{python3_sitelib}/%{name}_app
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info
%{_datadir}/applications/org.frescobaldi.Frescobaldi.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.frescobaldi.Frescobaldi.svg
%{_mandir}/man1/*
%{_metainfodir}/*.metainfo.xml

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.3.0-7
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Dec 01 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.3.0-4
- Drop webkit dependency.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.3.0-2
- Rebuilt for Python 3.12

* Mon Mar 27 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.3.0-1
- 3.3.0

* Thu Mar 09 2023 Nils Philippsen <nils@tiptoe.de> - 3.2-5
- Apply upstream fix for event issue (#2176793)
- Remove trailing white space

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.2-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 24 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.2-2
- Patch for event issue.

* Thu Aug 25 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.2-1
- 3.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.1.3-10
- Rebuilt for Python 3.11

* Mon Jan 31 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-9
- Line number float patch.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 05 2022 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-7
- More patches.

* Wed Oct 27 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-6
- Additional patch.

* Fri Oct 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-5
- Patches for qpageview, progressbar crashes.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.1.3-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 28 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.3-1
- 3.1.3

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-5
- BR python3-setuptools.

* Mon Jun 22 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-4
- Change lilypond to Recommends, per BZ 1847554.

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.1.2-3
- Rebuilt for Python 3.9

* Wed Apr 29 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-2
- Add appdata file, with patch.

* Mon Apr 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.2-1
- 3.1.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-3
- Add ExclusiveArch: %%{qt5_qtwebengine_arches}

* Thu Jan 09 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-2
- Require python3-qt5-webengine

* Mon Jan 06 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.1.1-1
- 3.1.1

* Mon Dec 30 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.1-1
- 3.1

* Wed Sep 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-14
- Drop sip.

* Wed Sep 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-13
- Patch to specify namespaced sip.

* Wed Sep 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.0.0-12
- Correct sip deps, BZ 1753266.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-11
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Gwyn Ciesla <limburgher@gmail.com> - 3.0.0-8
- Require python3-sip

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 3.0.0-6
- Python 3.7 fix.

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-5
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.0.0-3
- Remove obsolete scriptlets

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Gwyn Ciesla <limburgher@gmail.com> - 3.0.0-1
- Update to 3.0.0.

* Sat Feb 18 2017 Jon Ciesla <limburgher@gmail.com> - 2.20.0-1
- Update to 2.20.0.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 04 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.0-3
- Require PyQt4-webkit.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.19.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Apr 22 2016 Jon Ciesla <limburgher@gmail.com> - 2.19.0-1
- Update to 2.19.0.

* Tue Feb 02 2016 Jon Ciesla <limburgher@gmail.com> - 2.18.2-1
- Latest upstream.

* Sun Sep 20 2015 Jon Ciesla <limburgher@gmail.com> - 2.18.1-3
- Description fixes.

* Tue Sep 15 2015 Jon Ciesla <limburgher@gmail.com> - 2.18.1-2
- Include translations, BZ 1246869.

* Tue Jun 16 2015 Jon Ciesla <limburgher@gmail.com> - 2.18.1-1
- Latest upstream.

* Mon Mar 09 2015 Jon Ciesla <limburgher@gmail.com> - 2.18-1
- Latest upstream, now requires python-ly.

* Wed Jan 21 2015 Jon Ciesla <limburgher@gmail.com> - 2.17.2-1
- Latest upstream.

* Fri Jan 02 2015 Jon Ciesla <limburgher@gmail.com> - 2.17.1-1
- Latest upstream.

* Tue Aug 26 2014 Olivier Samyn <code@oleastre.be> - 2.0.16-1
- Update to 2.0.16
- Remove obsolete patch

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 03 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.10-2
- Fix special char handling in OS name, BZ 1010604.

* Tue Aug 13 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.10-1
- 2.0.10.
- Fix bogus changelog dates.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 Jon Ciesla <limburgher@gmail.com> - 2.0.9-1
- Update to 2.0.9, fix performance issues, BZ 952370.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jul 14 2012 Brendan Jones <brendan.jones.it@gmail.com> 2.0.6-1
- Update to version 2.0.6, correct language

* Wed Jan 18 2012 Brendan Jones <brendan.jones.it@gmail.com> - 2.0.2-3
- Exclude only .mo files, not the whole directory

* Wed Jan 18 2012 Brendan Jones <brendan.jones.it@gmail.com> - 2.0.2-2
- Removed rumor/timidity++ requires added portmidi and bindings

* Mon Jan 16 2012 Brendan Jones <brendan.jones.it@gmail.com> - 2.0.2-1
- New upstream version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.2.0-1
- New upstream version
- Drop upstreamed py2.7 patch

* Thu Aug 19 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.3-1
- New upstream version (for KDE 4.5)
- Drop BR: gettext ImageMagick lilypond that are no longer required

* Tue Jul 27 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.2-3
- Enable build for python-2.7

* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Feb 20 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.2-1
- New upstream version (for KDE 4.4)

* Sat Jan 30 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 1.0.1-1
- New upstream version

* Wed Nov 18 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.16-1
- New upstream version

* Thu Sep 17 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.14-1
- New upstream version

* Mon Aug 10 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.13-1
- New upstream version
- No need to rebuild .mo and .png files per new guidelines

* Wed Aug 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.12-3
- Update the .desktop file

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 05 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.12-1
- New upstream version

* Mon Jun 15 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.11-1
- New upstream version

* Tue Jun 09 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.10-1
- New upstream version
- Decompress the icon. RHBZ #491016 is being ignored.

* Sat May 23 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.9-1
- New upstream version

* Tue Mar 24 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.8-1
- New upstream version

* Tue Mar 17 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.7-2
- Remove BuildRequires:  dbus-python
- Fix the year of the previous changelog entry
- Add "Public Domain" to the license tag
- Add AudioVideo category to the .desktop file
- Add disttag

* Sun Mar 15 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> - 0.7.7-1
- Initial build

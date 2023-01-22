%global with_tests 0

Name:           retext
Version:        7.2.2
Release:        5%{?dist}
Summary:        Simple editor for Markdown and reStructuredText

License:        GPLv3+
URL:            https://github.com/retext-project/retext
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
# Man pages are taken from the Debian package.
Source1:        %{name}.1
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  librsvg2-tools
BuildRequires:  ImageMagick
BuildRequires:  python3-devel
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(markups)
BuildRequires:  python3dist(pyenchant)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(setuptools)
BuildRequires:  qt5-qttools-devel

%if 0%{?with_tests}
BuildRequires:  python3dist(pyqt5)
BuildRequires:  qt5-qtbase-gui
%endif

Requires:       hicolor-icon-theme
Requires:       python3-qt5-webkit
Requires:       qt5-qtlocation
Requires:       qt5-qtwebkit

%description
ReText is simple text editor that supports Markdown and reStructuredText markup
languages. It is written in Python using PyQt libraries. It supports live
preview, tabs, math formulas, export to various formats including PDF and
HTML.

%prep
%autosetup
sed \
  -i.python \
  -e "s|^#!/usr/bin/env python3$|#!%{__python3}|g" \
  retext.py ReText/__main__.py ReText/converterprocess.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m 0644 %SOURCE1 %{buildroot}/%{_mandir}/man1

# Generate resized icons
pushd icons
mkdir -p %{buildroot}/%{_datadir}/icons/hicolor/{16x16,22x22,24x24,32x32,48x48,64x64,72x72,96x96,128x128,scalable}/apps
for s in 16x16 22x22 24x24 32x32 48x48 64x64 72x72 96x96 128x128
do
    convert ./retext.png -resize $s %{buildroot}/%{_datadir}/icons/hicolor/$s/apps/retext.png;
done
install -p -m 0644 retext.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps
popd

desktop-file-install \
--dir=%{buildroot}%{_datadir}/applications \
%{_builddir}/%{name}-%{version}/data/*.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml || :

%if 0%{?with_tests}
%{__python3} setup.py test
%endif


%files
%doc changelog.md configuration.md README.md
%license  LICENSE_GPL
%{_bindir}/%{name}
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_mandir}/man1/*.1.*
%{python3_sitelib}/ReText/
%{python3_sitelib}/*egg-info

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 7.2.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 15 2021 Mattia Verga <mattia.verga@protonmail.com> - 7.2.2-1
- Update to 7.2.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 7.1.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul  6 2020 José Matos <jamatos@fedoraproject.org> - 7.1.0-2
- Remove scriptlets (now handled by triggers)
- Remove /usr/bin/env from shebang headers

* Sun May  3 2020 José Matos <jamatos@fedoraproject.org> - 7.1.0-1
- Update to latest stable release
- Clean the build requirements

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 7.0.3-2
- Rebuilt for Python 3.7

* Sat Jun 09 2018 Mike DePaulo <mikedep333@gmail.com> - 7.0.3-1
- New upstream version

* Tue Jun 05 2018 Mike DePaulo <mikedep333@gmail.com> - 7.0.1-2
- Fix the screenshot URL in the appdata file

* Tue Jun 05 2018 Mike DePaulo <mikedep333@gmail.com> - 7.0.1-1
- New upstream version
- Project moved to GitHub

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 19 2017 Mario Blättermann <mario.blaettermann@gmail.com> - 7.0.0-1
- New upstream version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 6.0.2-2
- Rebuild for Python 3.6

* Tue Oct 04 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 6.0.2-1
- New upstream version
- Fixed download link

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Jul 10 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 6.0.1-1
- New upstream version

* Fri May 13 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 6.0.0-1
- New upstream version
- Bump requirement to python3-markups >= 2.0.0

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 5.3.0-4
- Requires: python3-qt5-webkit

* Wed Feb 17 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 5.3.0-3
- Patch for Enchant (RHBZ #1309365)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Mario Blättermann <mario.blaettermann@gmail.com> - 5.3.0-1
- New upstream version

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 05 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 5.2.1-1
- New upstream version
- Removed custom appdata file

* Fri Sep 11 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 5.1.0-1
- New upstream version
- Remove wpgen stuff

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 5.0.2-2
- New upstream version
- Add qt5-qtlocation to runtime requirements (bz #1215369)

* Sat Jan 31 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 5.0.1-7
- Fix file permissions
- Add update-desktop-database scripts
- Fix download location
- Extended description in appdata file, fix license declaration

* Thu Jan 15 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 5.0.1-6
- Fix URLs of extra sources
- Add appdata file

* Sat Jan 10 2015 Mario Blättermann <mario.blaettermann@gmail.com> - 5.0.1-5
- Replace qt-devel with qt5-qttools-devel to use the correct
  linguist toolchain

* Tue Dec 30 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 5.0.1-4
- Use the %%license macro
- Keep the tests enabled, but make them optional

* Wed Dec 17 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 5.0.1-3
- Add qt-devel to BuildRequires

* Tue Dec 16 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 5.0.1-2
- Add noarch tag

* Mon Dec 01 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 5.0.1-1
- New upstream version
- Man pages from the Debian package
- Install *.desktop file
- Enable tests

* Wed Jan 08 2014 Mario Blättermann <mario.blaettermann@gmail.com> - 4.0.1-2
- Spec file cleanup

* Wed May 08 2013 Huaren Zhong <huaren.zhong@gmail.com> - 4.0.1
- Rebuild for Fedora

* Sat Feb 18 2012 i@marguerite.su
- update to 3.0beta1

* Thu Dec 29 2011 i@marguerite.su
- initial package 2.1.3

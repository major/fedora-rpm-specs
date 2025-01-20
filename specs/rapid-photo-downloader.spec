Name:           rapid-photo-downloader
Version:        0.9.33
Release:        14%{?dist}
Summary:        Images downloader for external devices

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://damonlynch.net/rapid/
Source0:        http://launchpad.net/rapid/pyqt/%{version}/+download/%{name}-%{version}.tar.gz
BuildArch:      noarch

# Conform to pep440 to fix FTBFS with setuptools >= 66.0.0
# Sent upstream: https://github.com/damonlynch/rapid-photo-downloader/pull/103
Patch:          pep440.patch

BuildRequires:  python3-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  python3-setuptools

Requires:       kf5-filesystem
Requires:       LibRaw
Requires:       libgexiv2
Requires:       libnotify
Requires:       gphoto2
Requires:       gstreamer1
Requires:       hicolor-icon-theme
Requires:       perl-Image-ExifTool
Requires:       python3-arrow
Requires:       python3-colorlog
Requires:       python3-colour
Requires:       python3-dateutil
Requires:       python3-easygui
Requires:       python3-gexiv2
Requires:       python3-gobject
Requires:       python3-psutil
Requires:       python3-pymediainfo
Requires:       python3-pyxdg
Requires:       python3-qt5
Requires:       python3-rawkit
Requires:       python3-requests
Requires:       python3-show-in-file-manager
Requires:       python3-sortedcontainers
Requires:       python3-tenacity
Requires:       python3-tornado
Requires:       python3-zmq
Requires:       qt5-qtimageformats
Requires:       udisks2

%description
Rapid Photo Downloader is written by a photographer for professional
and amateur photographers. It can download photos from multiple memory
cards and Portable Storage Devices simultaneously. It provides a variety
of options for sub-folder creation, image renaming and backup.
It does not download images directly from a camera unless the camera
is recognized as an external drive.

%prep
%autosetup -p1

%build
%{__python3} setup.py build

#build_icons and build_i18n simply stage those files for install (data_files) in setup.py 
%install
%{__python3} setup.py build_icons build_translations install -O1 --skip-build --root=%{buildroot}
desktop-file-install                                        \
    --dir=%{buildroot}%{_datadir}/applications              \
    %{buildroot}%{_datadir}/applications/net.damonlynch.rapid_photo_downloader.desktop
#%%find_lang %{name}

%files
%doc CHANGES.md README.md RELEASE_NOTES.md
%license LICENSE
%{_bindir}/%{name}
%{python3_sitelib}/raphodo/
%{python3_sitelib}/*.egg-info/
%{_datadir}/metainfo/net.damonlynch.rapid_photo_downloader.metainfo.xml
%{_datadir}/applications/net.damonlynch.rapid_photo_downloader.desktop
%{_datadir}/solid/actions/net.damonlynch.rapid_photo_downloader.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/locale/*/LC_MESSAGES/rapid-photo-downloader.mo
%{_mandir}/man1/*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.33-13
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.33-11
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.9.33-7
- Rebuilt for Python 3.12

* Tue Apr 04 2023 Charalampos Stratakis <cstratak@redhat.com> - 0.9.33-6
- Fix FTBFS with setuptools >= 66.0.0
Resolves: rhbz#2183371

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Gwyn Ciesla <gwync@protonmail.com> - 0.9.33-4
- LibRaw rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.33-2
- Rebuilt for Python 3.11

* Fri Apr 01 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.9.33-1
- Update to version 0.9.33

* Sun Jan 23 2022 Neal Gompa <ngompa@fedoraproject.org> - 0.9.28-1
- Update to version 0.9.28

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.24-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.24-1
- Update to latest upstream version 0.9.24

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.19-3
- Rebuilt for Python 3.9

* Mon May 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.9.19-2
- Rebuild for new LibRaw

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.19-1
- Update to latest upstream version 0.9.19

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.18-1
- Update to latest upstream version 0.9.17

* Sat Oct 12 2019 Matthew Kunkel <matt@mattkunkel.com> - 0.9.17-1
- Update to latest upstream version 0.9.17 (rhbz#1753707)
- Fixed missing dependencies (rhbz#1753704)
- Fixed License
- Fixed Icon and Translations

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.14-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.14-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.9.14-1
- Update to latest upstream version 0.9.14
- Fix Requires and sort them alpabetically

* Wed Mar 27 2019 Peter Lemenkov <lemenkov@gmail.com> - 0.9.13-1
- Update to latest upstream version 0.9.13

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.10-1
- Update to latest upstream version 0.9.10 (rhbz#1616274)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.11-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.4.11-7
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 24 2016 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.11-2
- Add missing requirement (rhbz#1294303)

* Fri Oct 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.11-1
- Update to latest upstream version 0.4.11 (rhbz#1272457)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.10-1
- Update to latest upstream version 0.4.10

* Wed Jan 22 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.9-1
- Update to latest upstream version 0.4.9

* Sat Dec 21 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.7-1
- Update to latest upstream version 0.4.7

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 12 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.6-1
- Updated to new upstream version 0.4.6

* Wed Jan 09 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.6-0.b1
- Updated to new upstream version 0.4.6-beta1 to fix critical bug

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.5-1
- Updated to new upstream version 0.4.5

* Wed Feb 08 2012 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.3-1
- Updated to new upstream version 0.4.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 13 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.2-1
- Updated to new upstream version 0.4.2

* Sat Jun 04 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.1-1
- Updated to new upstream version 0.4.1

* Sat Apr 30 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.4.0-1
- Updated to new upstream version 0.4.0

* Sat Apr 09 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.5-1
- Updated to new upstream version 0.3.5

* Mon Mar 28 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.4-1
- Updated to new upstream version 0.3.4

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 07 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.3-1
- Updated to new upstream version 0.3.3

* Sun Sep 19 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.2-1
- Updated to new upstream version 0.3.2

* Wed Aug 18 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Updated to new upstream version 0.3.1

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 11 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- TODO removed
- Added new requirements
- Updated to new upstream version 0.3.0

* Sat Feb 27 2010 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- Updated to new upstream version 0.1.3

* Fri Dec 18 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Updated to new upstream version 0.1.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 14 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.10-1
- Added translations
- Changed source url
- Updated to new upstream version

* Sat Apr 25 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.8-3.b7
- Added update of the icon cache
- Fixed license

* Sat Apr 25 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.8-2.b7
- Added notify-python as a requirement

* Sun Apr 12 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.8-1.b7
- Updated to new upstream version b7

* Wed Apr 8 2009 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.8-1.b6
- Initial package for Fedora

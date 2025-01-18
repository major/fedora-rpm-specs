Name:          gimagereader
Version:       3.4.2
Release:       6%{?dist}
Summary:       A front-end to tesseract-ocr

License:       GPL-3.0-or-later
URL:           https://github.com/manisandro/gimagereader
Source0:       https://github.com/manisandro/gimagereader/releases/download/v%{version}/%{name}-%{version}.tar.xz

Patch0:        0001-Work-around-enchant_get_prefix_dir-which-is-not-avai.patch

BuildRequires: desktop-file-utils
BuildRequires: djvulibre-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: make
BuildRequires: podofo-devel
BuildRequires: sane-backends-devel
BuildRequires: tesseract-devel

BuildRequires: cairomm-devel
BuildRequires: libappstream-glib
BuildRequires: libjpeg-turbo-devel
%if 0%{fedora} > 26
BuildRequires: libxml++30-devel
%else
BuildRequires: libxml++-devel
%endif
BuildRequires: libuuid-devel
BuildRequires: libzip-devel
BuildRequires: gtkmm30-devel
BuildRequires: gtksourceviewmm3-devel
BuildRequires: gtkspellmm30-devel
BuildRequires: json-glib-devel
BuildRequires: poppler-glib-devel
BuildRequires: python3-gobject

BuildRequires: poppler-qt5-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qtspell-qt5-devel
BuildRequires: quazip-qt5-devel

Requires:      hicolor-icon-theme
Requires:      gvfs

%description
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents


%package gtk
Summary:       A Gtk+ front-end to tesseract-ocr
# For glib networking operations
Requires:      gvfs-client
Requires:      %{name}-common = %{version}-%{release}
Obsoletes:     %{name} < 2.94-1

%description gtk
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents
This package contains the Gtk+ front-end.


%package qt
Summary:       A Qt front-end to tesseract-ocr
Requires:      %{name}-common = %{version}-%{release}

%description qt
gImageReader is a simple front-end to tesseract. Features include:
 - Import PDF documents and images from disk, scanning devices, clipboard and screenshots
 - Process multiple images and documents in one go
 - Manual or automatic recognition area definition
 - Recognize to plain text or to hOCR documents
 - Recognized text displayed directly next to the image
 - Post-process the recognized text, including spellchecking
 - Generate PDF documents from hOCR documents
This package contains the Qt front-end.

%package common
Summary:       Common files for %{name}
BuildArch:     noarch

%description common
Common files for %{name}.


%prep
%autosetup -p1


%build
%define _vpath_builddir %{_target_platform}-gtk
%cmake -DINTERFACE_TYPE=gtk -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%{_defaultdocdir}/%{name}-common"
%cmake_build

%define _vpath_builddir %{_target_platform}-qt
%cmake -DINTERFACE_TYPE=qt5 -DENABLE_VERSIONCHECK=0 -DMANUAL_DIR="%{_defaultdocdir}/%{name}-common"
%cmake_build


%install
%define _vpath_builddir %{_target_platform}-gtk
%cmake_install

%define _vpath_builddir %{_target_platform}-qt
%cmake_install

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-gtk.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt5.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}-gtk.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}-qt5.appdata.xml

%find_lang %{name}


%files common -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%doc %{_defaultdocdir}/%{name}-common/manual*.html

%files gtk
%{_bindir}/%{name}-gtk
%{_datadir}/metainfo/%{name}-gtk.appdata.xml
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.%{name}.gschema.xml

%files qt
%{_bindir}/%{name}-qt5
%{_datadir}/metainfo/%{name}-qt5.appdata.xml
%{_datadir}/applications/%{name}-qt5.desktop

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Nov 12 2024 Sandro Mani <manisandro@gmail.com> - 3.4.2-5
- Rebuild (tesseract)

* Wed Sep 25 2024 Michel Lind <salimma@fedoraproject.org> - 3.4.2-4
- Rebuild for tesseract-5.4.1-3 (soversion change from 5.4.1 to just 5.4)

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 13 2024 Sandro Mani <manisandro@gmail.com> - 3.4.2-2
- Rebuild for tesseract-5.4.1

* Mon Feb 05 2024 Sandro Mani <manisandro@gmail.com> - 3.4.2-1
- Update to 3.4.2

* Sun Jan 28 2024 Sandro Mani <manisandro@gmail.com> - 3.4.1-10
- Rebuild (tesseract)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 07 2023 Sandro Mani <manisandro@gmail.com> - 3.4.1-7
- Rebuild (tesseract)

* Wed Aug 16 2023 Sandro Mani <manisandro@gmail.com> - 3.4.1-6
- Rebuild against podofo-0.10

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Sandro Mani <manisandro@gmail.com> - 3.4.1-4
- Rebuild (tesseract)

* Fri May 05 2023 Nicolas Chauvet <kwizart@gmail.com> - 3.4.1-3
- Rebuilt for quazip 1.4

* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 3.4.1-2
- Rebuild (tesseract)

* Sun Jan 29 2023 Sandro Mani <manisandro@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Sandro Mani <manisandro@gmail.com> - 3.4.0-7
- Rebuild (tesseract)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Sandro Mani <manisandro@gmail.com> - 3.4.0-5
- Rebuild (tesseract)

* Tue May 03 2022 Sandro Mani <manisandro@gmail.com> - 3.4.0-4
- Rebuild (podofo)

* Mon Apr 18 2022 Miro Hrončok <mhroncok@redhat.com> - 3.4.0-3
- Rebuilt for quazip 1.3

* Thu Mar 10 2022 Sandro Mani <manisandro@gmail.com> - 3.4.0-2
- Rebuild for tesseract 5.1.0
- Spec cleanups

* Fri Jan 28 2022 Sandro Mani <manisandro@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Sandro Mani <manisandro@gmail.com> - 3.3.1-12
- Rebuild (qtspell)

* Sun Dec 19 2021 Sandro Mani <manisandro@gmail.com> - 3.3.1-11
- Rebuild (tesseract)

* Tue Dec 14 2021 Sandro Mani <manisandro@gmail.com> - 3.3.1-10
- Rebuild (tesseract)

* Thu Aug 19 2021 Björn Esser <besser82@fedoraproject.org> - 3.3.1-9
- Rebuild (quazip)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Jan  9 22:56:49 CET 2021 Sandro Mani <manisandro@gmail.com> - 3.3.1-6
- Rebuild (podofo)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.3.1-3
- Rebuild for poppler-0.84.0

* Sat Dec 28 2019 Sandro Mani <manisandro@gmail.com> - 3.3.1-2
- Rebuild (tesseract)

* Sun Jul 28 2019 Sandro Mani <manisandro@gmail.com> - 3.3.1-1
- Update to 3.3.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 01 2019 Sandro Mani <manisandro@gmail.com> - 3.3.0-4
- Fix crash when opening language manager
- Add requires: gvfs

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Sandro Mani <manisandro@gmail.com> - 3.3.0-2
- Rebuild (tesseract)

* Wed Sep 26 2018 Sandro Mani <manisandro@gmail.com> - 3.3.0-1
- Update to 3.3.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Sandro Mani <manisandro@gmail.com> - 3.2.99-3
- Rebuild (podofo)

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 3.2.99-2
- Rebuild for poppler-0.63.0

* Sun Feb 25 2018 Sandro Mani <manisandro@gmail.com> - 3.2.99-1
- Update to 3.2.99

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 3.2.3-6
- Add missing BR: gcc-c++, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.3-4
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Sandro Mani <manisandro@gmail.com> - 3.2.3-1
- Update to 3.2.3

* Fri Jun 30 2017 Sandro Mani <manisandro@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Wed May 17 2017 Sandro Mani <manisandro@gmail.com> - 3.2.1-4
- Backport patch to fix some icons missing in Gtk interface (#1451357)

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Feb 21 2017 Sandro Mani <manisandro@gmail.com> - 3.2.1-2
- Rebuild (tesseract)

* Fri Feb 10 2017 Sandro Mani <manisandro@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 03 2017 Sandro Mani <manisandro@gmail.com> - 3.2.0-2
- Rebuild (podofo)

* Wed Nov 23 2016 Sandro Mani <manisandro@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Fri Oct 14 2016 Sandro Mani <manisandro@gmail.com> - 3.1.99-1
- Update to 3.1.99

* Tue May 03 2016 Sandro Mani <manisandro@gmail.com> - 3.1.91-1
- Update to 3.1.91

* Thu Apr 28 2016 Sandro Mani <manisandro@gmail.com> - 3.1.90-1
- Update to 3.1.90

* Thu Feb 04 2016 Sandro Mani <manisandro@gmail.com> - 3.1.2-5
- Add patch to fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Sandro Mani <manisandro@gmail.com> - 3.1.2-3
- Rebuild (tesseract)

* Wed Oct 14 2015 Sandro Mani <manisandro@gmail.com> - 3.1.2-2
- Rebuild (tesseract)

* Tue Jun 30 2015 Sandro Mani <manisandro@gmail.com> - 3.1.2-1
- Update to 3.1.2

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Sandro Mani <manisandro@gmail.com> - 3.1.1-1
- Update to 3.1.1

* Fri May 01 2015 Sandro Mani <manisandro@gmail.com> - 3.1-1
- Update to 3.1

* Sun Jan 04 2015 Sandro Mani <manisandro@gmail.com> - 3.0.1-1
- Update to 3.0.1.

* Mon Dec 15 2014 Sandro Mani <manisandro@gmail.com> - 3.0-1
- Update to 3.0.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.93-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Aug 13 2014 Sandro Mani <manisandro@gmail.com> - 2.93-4
- Rebuild (tesseract)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 04 2014 Sandro Mani <manisandro@gmail.com> - 2.93-2
- Workaround rhbz #1065695

* Wed Apr 30 2014 Sandro Mani <manisandro@gmail.com> - 2.93-1
- Update to 2.93

* Wed Mar 19 2014 Sandro Mani <manisandro@gmail.com> - 2.92-1
- Update to 2.92

* Thu Feb 20 2014 Sandro Mani <manisandro@gmail.com> - 2.91-1
- Update to 2.91

* Sat Feb 15 2014 Sandro Mani <manisandro@gmail.com> - 2.91-0.2git20140216
- Update to newer 2.91 pre, work around crash at exit

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 2.91-0.1
- Update to 2.91 pre

* Thu Feb 13 2014 Sandro Mani <manisandro@gmail.com> - 2.90-3
- Require hicolor-icon-theme
- Add missing icon theme scriptlets

* Wed Feb 12 2014 Sandro Mani <manisandro@gmail.com> - 2.90-2
- Add appdata file

* Tue Feb 11 2014 Sandro Mani <manisandro@gmail.com> - 2.90-1
- Initial package.

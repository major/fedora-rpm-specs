%global with_qt6 0%{?fedora}
%global with_fitz 0%{?fedora}

Name:		qpdfview
Version:	0.5.0
Release:	19%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
Summary:	Tabbed PDF Viewer
Url:		https://launchpad.net/qpdfview
Source0:	%{url}/trunk/%{version}/+download/%{name}-0.5.tar.gz
Patch1:		qpdfview-c99.patch
# std::optional requires std=c++17 or later. Fixes:
# /usr/include/poppler/qt5/poppler-form.h:888:6: error: ‘optional’ in namespace ‘std’ does not name a template type
Patch2:         qpdfview-stdc++17.patch

BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	desktop-file-utils
BuildRequires:	file-devel
BuildRequires:	cups-devel
BuildRequires:	hicolor-icon-theme
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(ddjvuapi)
%if %{with_fitz}
BuildRequires:	mupdf-devel
%endif

%description
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.


%package common
Summary:	Common files for %{name}
BuildArch:	noarch

%description common
This package provides common files for %{name}.

%package qt5
Summary:	Tabbed PDF Viewer
BuildRequires:	qt5-qttools-devel
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Widgets)
Requires:	%{name}-common = %{version}-%{release}

%description qt5
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.


%if %{with_qt6}
%package qt6
Summary:	Tabbed PDF Viewer
BuildRequires:	qt6-qttools-devel
BuildRequires:	pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:	pkgconfig(Qt6Widgets)
Requires:	%{name}-common = %{version}-%{release}
# no poppler-qt6
ExcludeArch:	s390x

%description qt6
qpdfview is a tabbed PDF viewer.
It uses the Poppler library for rendering and CUPS for printing.
It provides a clear and simple graphical user interface using the Qt framework.
%endif


%prep
%setup -qc -n %{name}-0.5
# unifying
mv %{name}-0.5 %{name}-%{version}
cd %{name}-%{version}
%patch -P 1 -p1
%patch -P 2 -p1

%build
cp -a %{name}-%{version} build-qt5
pushd build-qt5
lrelease-qt5 qpdfview.pro
# Some adjustments to avoid conflicts between packages
sed -i "s/TARGET = qpdfview/TARGET = qpdfview-qt5/g" application.pro
sed -i "s,DESKTOP_FILE = miscellaneous/qpdfview.desktop,DESKTOP_FILE = miscellaneous/qpdfview-qt5.desktop,g" application.pro
sed "s/Exec=qpdfview/Exec=qpdfview-qt5/g" miscellaneous/qpdfview.desktop.in  > miscellaneous/qpdfview-qt5.desktop.in
sed -i "s/Name=qpdfview/Name=qpdfview (Qt5)/g" miscellaneous/qpdfview-qt5.desktop.in
%{qmake_qt5} \
    TARGET_INSTALL_PATH="%{_bindir}" \
    PLUGIN_INSTALL_PATH="%{_libdir}/%{name}-qt5" \
    DATA_INSTALL_PATH="%{_datadir}/%{name}" \
    MANUAL_INSTALL_PATH="%{_mandir}/man1" \
    ICON_INSTALL_PATH="%{_datadir}/icons/hicolor/scalable/apps" \
    LAUNCHER_INSTALL_PATH="%{_datadir}/applications" \
    APPDATA_INSTALL_PATH="%{_metainfodir}" \
%if %{with_fitz}
    CONFIG+=with_fitz \
    FITZ_PLUGIN_LIBS="-lmupdf" \
%endif
    qpdfview.pro
make %{?_smp_mflags}
popd

%if %{with_qt6}
cp -a %{name}-%{version} build-qt6
pushd build-qt6
lrelease-qt6 qpdfview.pro
# Some adjustments to avoid conflict between packages
sed -i "s/TARGET = qpdfview/TARGET = qpdfview-qt6/g" application.pro
sed -i "s,DESKTOP_FILE = miscellaneous/qpdfview.desktop,DESKTOP_FILE = miscellaneous/qpdfview-qt6.desktop,g" application.pro
sed "s/Exec=qpdfview/Exec=qpdfview-qt6/g" miscellaneous/qpdfview.desktop.in  > miscellaneous/qpdfview-qt6.desktop.in
sed -i "s/Name=qpdfview/Name=qpdfview (Qt6)/g" miscellaneous/qpdfview-qt6.desktop.in
%{qmake_qt6} \
    TARGET_INSTALL_PATH="%{_bindir}" \
    PLUGIN_INSTALL_PATH="%{_libdir}/%{name}-qt6" \
    DATA_INSTALL_PATH="%{_datadir}/%{name}" \
    MANUAL_INSTALL_PATH="%{_mandir}/man1" \
    ICON_INSTALL_PATH="%{_datadir}/icons/hicolor/scalable/apps" \
    LAUNCHER_INSTALL_PATH="%{_datadir}/applications" \
    APPDATA_INSTALL_PATH="%{_metainfodir}" \
%if %{with_fitz}
    CONFIG+=with_fitz \
    FITZ_PLUGIN_LIBS="-lmupdf" \
%endif
    qpdfview.pro
make %{?_smp_mflags}
popd
%endif


%install
pushd build-qt5
make INSTALL_ROOT=%{buildroot} install
popd

%if %{with_qt6}
pushd build-qt6
make INSTALL_ROOT=%{buildroot} install
popd
%endif

%find_lang %{name} --with-qt --without-mo
# Common files are equal for all QtX
cd %{name}-%{version}
install -Dm 0644 icons/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt5.desktop
%if %{with_qt6}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-qt6.desktop
%endif
# unknown languages (epel7..9, f34) - qpdfview_{ast,ber,nds,rue,zdh}.qm
%if 0%{?rhel}
    rm -f %{buildroot}/%{_datadir}/%{name}/%{name}_???.qm
%endif


# Scriptlets qt5 subpackage
%ldconfig_scriptlets qt5


%if %{with_qt6}
# Scriptlets qt6 subpackage
%ldconfig_scriptlets qt6
%endif


%files qt5
%{_bindir}/%{name}-qt5
%{_libdir}/%{name}-qt5
%{_datadir}/applications/%{name}-qt5.desktop

%if %{with_qt6}
%files qt6
%{_bindir}/%{name}-qt6
%{_libdir}/%{name}-qt6
%{_datadir}/applications/%{name}-qt6.desktop
%endif

%files common -f %{name}.lang
%license %{name}-%{version}/COPYING
%doc %{name}-%{version}/CHANGES %{name}-%{version}/CONTRIBUTORS %{name}-%{version}/README %{name}-%{version}/TODO
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help*.html
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man?/*

%changelog
* Sat Feb 08 2025 Michael J Gruber <mjg@fedoraproject.org> - 0.5.0-19
- Rebuild (mupdf)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Oct 05 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.5.0-17
- Rebuild (mupdf)

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0-16
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.5.0-14
- Rebuild against mupdf 1.24.6

* Wed May 29 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.5.0-13
- Rebuild against mupdf 1.24.2

* Thu Apr 11 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.5.0-12
- Rebuild against mupdf 1.24.1

* Wed Mar 20 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.5.0-11
- Rebuild against mupdf 1.24.0

* Fri Mar 01 2024 Michael J Gruber <mjg@fedoraproject.org> - 0.5.0-10
- adjust to mupdf shared.

* Fri Mar 01 2024 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.5.0-9
- Remove references to mupdf-third.
- Use %%patch -P <N> instead of %%patch<N>.
- Rebuild against gumbo-parser-0.12.1.

* Sun Jan 28 2024 Sandro Mani <manisandro@gmail.com> - 0.5.0-8
- Rebuild (tesseract)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 07 2023 Sandro Mani <manisandro@gmail.com> - 0.5.0-5
- Rebuild (tesseract)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 06 2023 Sandro Mani <manisandro@gmail.com> - 0.5.0-3
- Rebuild (tesseract)

* Tue Feb 07 2023 Florian Weimer <fweimer@redhat.com> - 0.5.0-2
- Fix C99 compatibility issue

* Mon Feb 06 2023 TI_Eugene <ti.eugene@gmail.com> - 0.5.0-1
- Release

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 23 2022 Sandro Mani <manisandro@gmail.com> - 0.5.0-0.2.beta1
- Rebuild (tesseract)

* Sun Nov 13 2022 TI_Eugene <ti.eugene@gmail.com> - 0.5.0-0.1.beta1
- Version bump
- Enabled fitz plugin for Fedora (EPUB, FB2, CBR/CBZ etc support)
- Enabled Djvu for EPEL
- Removed Qt4 build (because of EL7 because of C11 requirement)
- Qt5 build is mandatory
- Added Qt6 build (Fedora)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jan 24 2022 TI_Eugene <ti.eugene@gmail.com> - 0.4.18-9
- EPEL8..9 fix

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 18 2021 TI_Eugene <ti.eugene@gmail.com> - 0.4.18-8
- F35 fix

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 TI_Eugene <ti.eugene@gmail.com> - 0.4.18-5
- Move Qt4 things into qpdfview-qt4 subpackage
- Disable Qt4 version for F34

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 0.4.18-2
- Rebuild for poppler-0.84.0

* Sat Aug 17 2019 Zamir SUN <sztsian@gmail.com - 0.4.18-1
- Update to 0.4.18

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.10.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.9.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.8.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 0.4.17-0.7.beta1
- Rebuild for poppler-0.63.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.6.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.4.17-0.5.beta1
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.3.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.17-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Christian Dersch <lupinix@mailbox.org> - 0.4.17-0.1.beta1
- new version
- added Qt5 build
- added missing scriptlets for icon cache and desktop-database

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 0.4.16-2
- use %%qmake_qt4 macro to ensure proper build flags

* Thu Jan 07 2016 TI_Eugene <ti.eugene@gmail.com> 0.4.16-1
- Version bump

* Fri Oct 09 2015 TI_Eugene <ti.eugene@gmail.com> 0.4.15-1
- Version bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.4.13-2
- Rebuilt for GCC 5 C++11 ABI change

* Tue Nov 18 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.13-1
- Version bump

* Mon Oct 06 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.12-1
- Version bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.11-1
- Version bump

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 05 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.10-1
- Version bump

* Sun Mar 23 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.9-1
- Version bump

* Thu Jan 30 2014 TI_Eugene <ti.eugene@gmail.com> 0.4.8-1
- Version bump

* Sun Dec 08 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.7-1
- Version bump

* Sun Oct 13 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.6-1
- Version bump

* Fri Sep 06 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.5-1
- Version bump

* Tue Jul 30 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.4-1
- Version bump

* Sun May 26 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.3-1
- Version bump
- Translations added
- post/postun ldconfig added

* Mon Mar 25 2013 TI_Eugene <ti.eugene@gmail.com> 0.4.1-1
- New version
- License changed to GPLv2+

* Sat Mar 23 2013 TI_Eugene <ti.eugene@gmail.com> 0.4-1
- initial packaging for Fedora

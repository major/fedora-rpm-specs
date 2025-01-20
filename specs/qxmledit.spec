%global bigname QXmlEdit
Name:           qxmledit
Version:        0.9.18
Release:        7%{?dist}
# QXmlEdit - LGPLv2, some icons (oxygen) - GPLv3, QwtPlot3D - zlib-like
# Automatically converted from old format: LGPLv2+ and GPLv3 and zlib - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-3.0-only AND Zlib
Summary:        Simple XML Editor and XSD Viewer
Url:            http://qxmledit.org/
Source:         https://github.com/lbellonda/qxmledit/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  qt5-linguist
# qt5-qtbase-devel (Qt5Core..Qt5Xml)
BuildRequires:  pkgconfig(Qt5)
# qt5-qtsvg-devel
BuildRequires:  pkgconfig(Qt5Svg)
# qt5-qtscxml-devel
BuildRequires:  pkgconfig(Qt5Scxml)
# qt5-qtxmlpatterns-devel
BuildRequires:  pkgconfig(Qt5XmlPatterns)
# qt5-qtdeclarative-devel
BuildRequires:  pkgconfig(Qt5Qml)
# mesa-libGLU-devel
BuildRequires:  pkgconfig(glu)
Requires:       libqxmledit%{?_isa} = %{version}-%{release}

%description
QXmlEdit is a simple XML editor based on qt libraries. Its main features are
unusual data visualization modes, nice XML manipulation and presentation and it
is multi platform. It can split very big XML files into fragments, and compare
XML files. It is one of the few graphical Open Source XSD viewers.

%package        doc
Summary:        Simple XML Editor documentatio
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
QXmlQXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit documentation.

%package -n     libqxmledit
Summary:        XML Editor Shared Libraries

%description -n libqxmledit
QXmlQXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit shared libraries.

%package -n     libqxmledit-devel
Summary:        XML Editor Development Files
Requires:       libqxmledit%{?_isa} = %{version}-%{release}

%description -n libqxmledit-devel
QXmlEdit is a simple XML editor based on qt libraries.
This package includes QXmlEdit development files.


%prep
%autosetup
# tmp fix (https://github.com/lbellonda/qxmledit/issues/74)
desktop-file-edit --add-mime-type=application/xml install_scripts/environment/desktop/%{bigname}.desktop

%build
lrelease-qt5 {src/QXmlEdit.pro,src/QXmlEditWidget.pro,src/sessions/QXmlEditSessions.pro}
%{qmake_qt5} \
    QXMLEDIT_INST_DIR=%{_bindir} \
    QXMLEDIT_INST_LIB_DIR=%{_libdir} \
    QXMLEDIT_INST_DATA_DIR=%{_datadir}/%{name} \
    QXMLEDIT_INST_TRANSLATIONS_DIR=%{_datadir}/%{name}/translations \
    QXMLEDIT_INST_INCLUDE_DIR=%{_includedir}/%{name} \
    QXMLEDIT_INST_ICON_DIR=%{_datadir}/pixmaps \
    QXMLEDIT_INST_DOC_DIR=%{_datadir}/doc/%{name} \
    QXMLEDIT_INST_DESKTOPINFO_DIR=%{_datadir}/applications \
    QXMLEDIT_INST_METAINFO_DIR=%{_metainfodir} \
    QXMLEDIT_INST_USE_C11=y
%{make_build}


%install
%{make_install} INSTALL_ROOT=%{buildroot}
# extras
install -Dm 0644 install_scripts/environment/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
# i18n
%find_lang QXmlEdit --with-qt --without-mo
%find_lang QXmlEditSessions --with-qt --without-mo
%find_lang QXmlEditWidget --with-qt --without-mo
%find_lang SCXML --with-qt --without-mo


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{bigname}.desktop


%files -f QXmlEdit.lang -f QXmlEditSessions.lang -f QXmlEditWidget.lang -f SCXML.lang
%license COPYING GPLV3.txt LGPLV3.txt
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{bigname}.desktop
%{_metainfodir}/%{bigname}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1.*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/sample.style
%{_datadir}/%{name}/snippets/

%files doc
%license COPYING GPLV3.txt LGPLV3.txt
%{_datadir}/doc/%{name}/QXmlEdit_manual.pdf

%files -n libqxmledit
%license COPYING GPLV3.txt LGPLV3.txt
%{_libdir}/libQXmlEdit{Sessions,Widget}.so.0*

%files -n libqxmledit-devel
%license COPYING GPLV3.txt LGPLV3.txt
%{_includedir}/%{name}/
%{_libdir}/libQXmlEdit{Sessions,Widget}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.18-6
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 14 2023 TI_Eugene <ti.eugene@gmail.com> - 0.9.18-1
- Version bump

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 TI_Eugene <ti.eugene@gmail.com> - 0.9.17-1
- Version bump
- Patches removed

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 07 2021 TI_Eugene <ti.eugene@gmail.com> - 0.9.16-1
- Version bump

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 TI_Eugene <ti.eugene@gmail.com> 0.9.15-3
- Spec fixes

* Sun Jul 05 2020 TI_Eugene <ti.eugene@gmail.com> 0.9.15-2
- Spec fixes

* Tue Jun 09 2020 TI_Eugene <ti.eugene@gmail.com> 0.9.15-1
- Initial packaging

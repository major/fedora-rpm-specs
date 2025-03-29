Name:           deepin-editor
Version:        6.5.18
Release:        %autorelease
Summary:        Text editor for DDE
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

# patch from https://github.com/linuxdeepin/deepin-editor/pull/338.patch
Patch0:         fix-build-with-icu-75+.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# provides lrelease-qt5
BuildRequires:  qt5-linguist

BuildRequires:  cmake(DtkWidget)
BuildRequires:  cmake(DtkCore)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(DFrameworkdbus)

BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(chardet)
BuildRequires:  uchardet-devel

BuildRequires:  desktop-file-utils

Requires:       deepin-qt5integration
Recommends:     deepin-manual

%description
Deepin Editor is a desktop text editor that supports common text editing
features.

%prep
%autosetup -p1

sed -i 's|lrelease|lrelease-qt5|; s|lupdate|lupdate-qt5|' \
    translate_generation.sh

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install
%find_lang deepin-editor --with-qt --all-name
rm %{buildroot}%{_datadir}/deepin-editor/translations/deepin-editor.qm

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f deepin-editor.lang
%doc README.md
%license LICENSE.txt
%{_bindir}/deepin-editor
%{_datadir}/applications/deepin-editor.desktop
%{_datadir}/icons/hicolor/scalable/apps/deepin-editor.svg
%dir %{_datadir}/deepin-editor
%dir %{_datadir}/deepin-editor/org.kde.syntax-highlighing
%{_datadir}/deepin-editor/org.kde.syntax-highlighing/syntax/vbscript.xml
%dir %{_datadir}/deepin-editor/themes
%{_datadir}/deepin-editor/themes/*.theme
%{_datadir}/deepin-manual/manual-assets/application/deepin-editor/
%{_datadir}/dsg/configs/org.deepin.editor/org.deepin.editor.json

%changelog
%autochangelog

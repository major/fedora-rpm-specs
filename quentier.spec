%global commit          e802d0abd15f0c03faf1457b98ea8f35381f3600
%global shortcommit     %(c=%{commit}; echo ${c:0:7})
%global snapshotdate    20220710

Name:       quentier
Summary:    Cross-platform desktop Evernote client
Version:    0.5.0
Release:    %autorelease

License:    GPLv3
URL:        https://github.com/d1vanov/quentier
Source0:    %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

ExclusiveArch: %{qt5_qtwebengine_arches}

BuildRequires: cmake
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Libquentier-qt5)
BuildRequires: cmake(QEverCloud-qt5)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5WebEngine)
BuildRequires: cmake(Qt5WebEngineCore)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5WebSockets)
BuildRequires: cmake(Qt5WebChannel)
BuildRequires: cmake(libxml2)
BuildRequires: cmake(QEverCloud-qt5)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: pkgconfig(hunspell)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libsecret-1)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: boost-devel
BuildRequires: libtidy-devel
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

Requires:      hicolor-icon-theme
Requires:      oxygen-icon-theme
Requires:      tango-icon-theme

%description
Quentier is a cross-platform desktop note taking app capable of working as
Evernote client. You can also use Quentier for local notes without any
connection to Evernote and synchronization.

%prep
%autosetup -p1 -n %{name}-%{commit}

sed -i "/tango.qrc/d; /oxygen.qrc/d" CMakeLists.txt
sed -i "s/QStringLiteral(\"tango\")/QStringLiteral(\"Tango\")/" bin/quentier/src/MainWindow.cpp

%build
%cmake -DQt5_LUPDATE_EXECUTABLE=%{_bindir}/lupdate-qt5 \
       -DQt5_LRELEASE_EXECUTABLE=%{_bindir}/lrelease-qt5 \
       -DUSE_LD_GOLD=OFF
%cmake_build
%cmake_build --target lupdate
%cmake_build --target lrelease

%install
%cmake_install

rm -rf %{buildroot}%{_datadir}/icons/hicolor/1024x1024

for size in "16x16" "22x22" "32x32" ; do
    for icon in "actions/mail-send.png" \
                "actions/checkbox.png" \
                "actions/format-list-ordered.png" \
                "actions/format-list-unordered.png" \
                "actions/tools-check-spelling.png" \
                "actions/insert-horizontal-rule.png" \
                "actions/format-text-color.png" \
                "actions/fill-color.png" \
                "actions/insert-table.png" \
                "mimetypes/application-pdf.png" \
                "mimetypes/application-enex.png" ; do
        install -Dpm 0644 resource/icons/themes/tango/$size/$icon %buildroot%{_datadir}/icons/Tango/$size/$icon
    done
done
for size in "16x16" "22x22" "32x32" ; do
    install -Dpm 0644 resource/icons/themes/oxygen/$size/mimetypes/application-enex.png %buildroot%{_datadir}/icons/oxygen/$size/mimetypes/application-enex.png
done

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.quentier.Quentier.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.quentier.Quentier.appdata.xml

%files
%doc CONTRIBUTING.md CodingStyle.md README.md
%license COPYING
%{_bindir}/%{name}
%{_bindir}/%{name}-%{version}
%{_datadir}/applications/org.quentier.Quentier.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*.png
%{_datadir}/icons/oxygen/
%{_datadir}/icons/Tango/
%{_metainfodir}/org.quentier.Quentier.appdata.xml
%dir %{_datadir}/quentier
%{_datadir}/quentier/translations

%changelog
%autochangelog

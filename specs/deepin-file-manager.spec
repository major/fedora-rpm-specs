%global repo dde-file-manager

Name:           deepin-file-manager
Version:        6.0.56
Release:        %autorelease
Summary:        File manager for deepin desktop environment.
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-file-manager
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

Patch0:         deepin-file-manager-6.0.56-uint8_t.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# qhelpgenerator-qt5
BuildRequires:  qt5-doctools
# lrelease-qt5
BuildRequires:  qt5-linguist

BuildRequires:  cmake(DtkCore)
BuildRequires:  cmake(DtkCMake)
BuildRequires:  cmake(DtkWidget)
BuildRequires:  cmake(KF5Codecs)

BuildRequires:  pkgconfig(dtkgui)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(liblucene++)
BuildRequires:  pkgconfig(liblucene++-contrib)
BuildRequires:  pkgconfig(docparser)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(dfm-io)
BuildRequires:  pkgconfig(dfm-mount)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(dfm-burn)
BuildRequires:  libicu-devel
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(deepin-pdfium)
BuildRequires:  pkgconfig(libcryptsetup)
BuildRequires:  poppler-cpp-devel
BuildRequires:  boost-devel
BuildRequires:  doxygen

BuildRequires:  desktop-file-utils

Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
# run command by QProcess
Requires:       deepin-shortcut-viewer
Requires:       deepin-terminal
Requires:       deepin-desktop
Requires:       file-roller
Requires:       gvfs-client
Requires:       samba
Requires:       xdg-user-dirs
Recommends:     deepin-manual

%description
Deepin File Manager is a file management tool independently developed by Deepin
Technology, featured with searching, copying, trash, compression/decompression,
viewing file property and other file management functions.

%package        lib
Summary:        Shared library for %{name}

%description    lib
This package provides shared library %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%package -n     deepin-desktop
Summary:        Deepin desktop environment - desktop module
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Requires:       deepin-launcher
Requires:       deepin-session-ui
Requires:       deepin-control-center

%description -n deepin-desktop
Deepin desktop environment - desktop module.

%prep
%autosetup -p1 -n %{repo}-%{version}

# fix file permissions
find -type f -perm 775 -exec chmod 644 {} \;

sed -i 's/lupdate/lupdate-qt5/' src/lupdate.sh
sed -i 's/lrelease/lrelease-qt5/' src/translate_generation.sh
sed -i 's/qhelpgenerator/qhelpgenerator-qt5/' docs/CMakeLists.txt

sed -i 's/Deepin;//' src/apps/dde-desktop/data/applications/dde-home.desktop \
    src/apps/dde-desktop/data/applications/dde-trash.desktop \
    src/apps/dde-desktop/data/applications/dde-computer.desktop

%build
%cmake -GNinja \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -DSYSTEMD_USER_UNIT_DIR=%{_userunitdir} \
    -DQCH_INSTALL_DESTINATION=%{_qt5_docdir} \
%cmake_build

%install
%cmake_install

%find_lang dde-file-manager --with-qt
rm %{buildroot}%{_datadir}/dde-file-manager/translations/dde-file-manager.qm
rm %{buildroot}%{_datadir}/deepin/dde-file-manager/oem-menuextensions/.readme
rm %{buildroot}%{_datadir}/dde-file-manager/extensions/appEntry/.readme
rm %{buildroot}%{_datadir}/applications/context-menus/.readme

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f dde-file-manager.lang
%doc README.md
%license LICENSE
%{_bindir}/dde-*
%{_bindir}/dfm-open.sh
%{_bindir}/file-manager.sh
%{_libexecdir}/dde-file-manager
%{_unitdir}/dde-filemanager-daemon.service
%{_userunitdir}/dde-file-manager.service
%{_userunitdir}/dde-session-initialized.target.wants/dde-file-manager.service
%{_datadir}/applications/dde-file-manager.desktop
%{_datadir}/applications/dde-open.desktop
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/com.deepin.filemanager.daemon.service
%{_datadir}/deepin-manual/manual-assets/application/dde-file-manager/
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/mime/packages/dtk-dci.xml
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.file-manager.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/dde-file-manager.json
%dir %{_datadir}/dsg/configs/org.deepin.dde.file-manager
%{_datadir}/dsg/configs/org.deepin.dde.file-manager/*.json
%dir %{_datadir}/dde-file-manager
%{_datadir}/dde-file-manager/mimetypeassociations/
%{_datadir}/dde-file-manager/mimetypes/
%{_datadir}/dde-file-manager/templates/
%{_sysconfdir}/X11/Xsession.d/99dfm-dlnfs-automount
%{_sysconfdir}/dbus-1/system.d/com.deepin.filemanager.daemon.conf
%{_sysconfdir}/deepin/dde-file-manager/dfm-dlnfs-automount

%files lib
%{_prefix}/lib/dde-dock/plugins/system-trays/libdde-disk-mount-plugin.so
%dir %{_libdir}/dde-file-manager
%{_libdir}/dde-file-manager/plugins/
%{_libdir}/dde-file-manager/tools/libdfm-upgrade.so
%{_libdir}/libdde-file-manager.so.1*
%{_libdir}/libdfm-base.so.1*
%{_libdir}/libdfm-extension.so.1*
%{_libdir}/libdfm-framework.so.1*

%files devel
%{_libdir}/libdde-file-manager.so
%{_libdir}/libdfm-base.so
%{_libdir}/libdfm-extension.so
%{_libdir}/libdfm-framework.so
%{_includedir}/dfm-base/
%{_includedir}/dfm-extension/
%{_includedir}/dfm-framework/
%{_libdir}/cmake/dfm-base/
%{_libdir}/cmake/dfm-extension/
%{_libdir}/cmake/dfm-framework/
%{_libdir}/pkgconfig/dfm-base.pc
%{_libdir}/pkgconfig/dfm-extension.pc
%{_libdir}/pkgconfig/dfm-framework.pc
%{_qt5_docdir}/filemanager.qch

%files -n deepin-desktop
%{_bindir}/dde-desktop
%{_datadir}/applications/dde-computer.desktop
%{_datadir}/applications/dde-trash.desktop
%{_datadir}/applications/dde-home.desktop
%{_datadir}/dbus-1/services/com.deepin.dde.desktop.service

%changelog
%autochangelog

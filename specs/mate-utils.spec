%global branch 1.28

Name:          mate-utils
Version:       %{branch}.0
Release:       %autorelease
Summary:       MATE utility programs
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:       GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: e2fsprogs-devel
BuildRequires: gtk-layer-shell-devel
BuildRequires: hardlink
BuildRequires: libcanberra-devel
BuildRequires: libgtop2-devel
BuildRequires: libudisks2-devel
BuildRequires: libX11-devel
BuildRequires: libXmu-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: mate-panel-devel
BuildRequires: mesa-libGL-devel
BuildRequires: popt-devel
BuildRequires: usermode
BuildRequires: yelp-tools
%if 0%{?fedora} && 0%{?fedora} >= 29
BuildRequires: gcc-c++
%endif

Requires: mate-dictionary = %{version}-%{release}
Requires: mate-screenshot = %{version}-%{release}
Requires: mate-search-tool = %{version}-%{release}
Requires: mate-system-log = %{version}-%{release}
Requires: mate-disk-usage-analyzer = %{version}-%{release}

%description
The mate-utils package contains a set of small "desk accessory" utility
applications for MATE, such as a dictionary, a disk usage analyzer,
a screen-shot tool and others.

%package common
Summary: Common files for %{name}
BuildArch: noarch
%description common
%{summary}.

%package devel
Summary: Development files for mate-utils
Requires:  mate-dictionary%{?_isa} = %{version}-%{release}
%description devel
The mate-utils-devel package contains header files and other resources
needed to develop programs using the libraries contained in mate-utils.

%package -n mate-system-log
Summary: A log file viewer for the MATE desktop
Requires: %{name}-common = %{version}-%{release}
Requires: usermode
# rhbz (#1016935)
Requires: mate-desktop-libs
%description -n mate-system-log
An application that lets you view various system log files.

%package -n mate-screenshot
Summary: A utility to take a screen-shot of the desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-screenshot
An application that let you take a screen-shot of your desktop.

%package -n mate-dictionary
Summary: A dictionary for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-dictionary
The mate-dictionary package contains a dictionary application for MATE Desktop.

%package -n mate-search-tool
Summary: A file searching tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
Requires: mate-desktop-libs
%description -n mate-search-tool
An application to search for files on your computer.

%package -n mate-disk-image-mounter
Summary: A disk image mounter tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-disk-image-mounter
An application to mount disk images.

%package -n mate-disk-usage-analyzer
Summary: A disk usage analyzing tool for MATE Desktop
Requires: %{name}-common = %{version}-%{release}
%description -n mate-disk-usage-analyzer
An application to help analyze disk usage.


%prep
%autosetup -p1

#NOCONFIGURE=1 ./autogen.sh

# disable pt language for help in search tool
sed -i s/"IGNORE_HELP_LINGUAS ="/"IGNORE_HELP_LINGUAS = pt"/g gsearchtool/help/Makefile.am
# pt translation fix
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
    --disable-static            \
    --disable-schemas-compile   \
    --enable-gdict-applet       \
    --enable-in-process         \
    --enable-wayland            \
    --enable-gtk-doc-html       \
    --enable-ipv6=yes           \
    --enable-maintainer-flags=no  \
    --with-x

make %{?_smp_mflags} V=1

%install
%{make_install}

# make mate-system-log use consolehelper until it starts using polkit
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cat <<EOF >%{buildroot}%{_sysconfdir}/pam.d/mate-system-log
#%%PAM-1.0
auth      include      config-util
account      include      config-util
session      include      config-util
EOF

mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
cat <<EOF >%{buildroot}%{_sysconfdir}/security/console.apps/mate-system-log
USER=root
PROGRAM=%{_libexecdir}/mate-system-log
SESSION=true
FALLBACK=true
EOF

mkdir -p  %{buildroot}%{_libexecdir}
mv %{buildroot}%{_bindir}/mate-system-log %{buildroot}%{_libexecdir}
ln -s %{_bindir}/consolehelper %{buildroot}%{_bindir}/mate-system-log

rm -fv %{buildroot}%{_libdir}/*.la
rm -fv %{buildroot}%{_datadir}/MateConf/gsettings/*.convert

# weird new files
rm -rf %{buildroot}%{_datadir}/icons/shot.png

desktop-file-install                          \
  --delete-original                           \
  --dir %{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome --all-name
%find_lang mate-disk-usage-analyzer --with-gnome --all-name
%find_lang mate-dictionary --with-gnome --all-name
%find_lang mate-search-tool --with-gnome --all-name
%find_lang mate-system-log --with-gnome --all-name


%files
# empty

%files common -f %{name}.lang
%doc COPYING COPYING.libs
%doc NEWS README.md

%files devel
%{_libdir}/libmatedict.so
%{_libdir}/pkgconfig/mate-dict.pc
%{_includedir}/mate-dict/
%{_datadir}/gtk-doc/html/mate-dict/

%files -n mate-system-log -f mate-system-log.lang
%{_bindir}/mate-system-log
%{_libexecdir}/mate-system-log
%{_sysconfdir}/security/console.apps/mate-system-log
%{_sysconfdir}/pam.d/mate-system-log
%{_datadir}/glib-2.0/schemas/org.mate.system-log.gschema.xml
%{_datadir}/applications/mate-system-log.desktop
%{_mandir}/man1/mate-system-log.1.*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/mate-system-log-symbolic.svg

%files -n mate-screenshot
%{_bindir}/mate-screenshot
%{_bindir}/mate-panel-screenshot
%{_datadir}/metainfo/mate-screenshot.appdata.xml
%{_datadir}/applications/mate-screenshot.desktop
%{_mandir}/man1/mate-screenshot.1.*
%{_mandir}/man1/mate-panel-screenshot.1.gz
%{_datadir}/glib-2.0/schemas/org.mate.screenshot.gschema.xml

%files -n mate-dictionary -f mate-dictionary.lang
%doc mate-dictionary/AUTHORS
%doc mate-dictionary/README.md
%{_bindir}/mate-dictionary
%{_datadir}/metainfo/mate-dictionary.appdata.xml
%{_datadir}/applications/mate-dictionary.desktop
%{_datadir}/mate-dict/
%{_datadir}/mate-dictionary/
#%%{_libexecdir}/mate-dictionary-applet
%{_libdir}/libmatedict.so.*
%{_libdir}/mate-utils/libmate-dictionary-applet.so*
%{_mandir}/man1/mate-dictionary.1.*
%{_datadir}/glib-2.0/schemas/org.mate.dictionary.gschema.xml
%{_datadir}/mate-panel/applets/org.mate.DictionaryApplet.mate-panel-applet
#%%{_datadir}/dbus-1/services/org.mate.panel.applet.DictionaryAppletFactory.service

%files -n mate-search-tool -f mate-search-tool.lang
%{_bindir}/mate-search-tool
%{_datadir}/metainfo/mate-search-tool.appdata.xml
%{_datadir}/applications/mate-search-tool.desktop
%{_mandir}/man1/mate-search-tool.1.*
%{_datadir}/glib-2.0/schemas/org.mate.search-tool.gschema.xml
%{_datadir}/pixmaps/mate-search-tool/

%files -n mate-disk-image-mounter
%{_bindir}/mate-disk-image-mounter
%{_datadir}/applications/mate-disk-image-mounter.desktop

%files -n mate-disk-usage-analyzer -f mate-disk-usage-analyzer.lang
%doc baobab/AUTHORS
%doc baobab/README.md
%{_bindir}/mate-disk-usage-analyzer
%{_datadir}/metainfo/mate-disk-usage-analyzer.appdata.xml
%{_datadir}/applications/mate-disk-usage-analyzer.desktop
%{_mandir}/man1/mate-disk-usage-analyzer.1.*
%{_datadir}/glib-2.0/schemas/org.mate.disk-usage-analyzer.gschema.xml
%{_datadir}/icons/hicolor/*/apps/mate-disk-usage-analyzer.*


%changelog
%autochangelog

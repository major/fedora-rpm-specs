%global branch 1.28

Name:          marco
Version:       %{branch}.2
Release:       %autorelease
Summary:       MATE Desktop window manager
# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gtk3-devel
BuildRequires: libcanberra-devel
BuildRequires: libgtop2-devel
BuildRequires: libSM-devel
BuildRequireS: libsoup-devel
BuildRequires: libXdamage-devel
BuildRequires: libXpresent-devel
BuildRequires: libXres-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: zenity
BuildRequires: startup-notification-devel
BuildRequires: yelp-tools

Requires:      mate-desktop-libs
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

# http://bugzilla.redhat.com/873342
# https://bugzilla.redhat.com/962009
Provides: firstboot(windowmanager) = marco

%description
MATE Desktop window manager

# to avoid that marco will install in other DE's by compiz-0.8.10
%package libs
Summary:       Libraries for marco
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+

%description libs
This package provides Libraries for marco.

%package devel
Summary:       Development files for marco
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for marco


%prep
%autosetup -p1

# weird tarball, no generated files
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static           \
           --disable-schemas-compile  \
           --with-x

# fix rpmlint unused-direct-shlib-dependency warning
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

make %{?_smp_mflags} V=1


%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -vf {} ';'

desktop-file-install                                \
        --delete-original                           \
        --dir=%{buildroot}%{_datadir}/applications  \
%{buildroot}%{_datadir}/applications/marco.desktop

%find_lang %{name} --with-gnome --all-name


%files
%doc AUTHORS COPYING README ChangeLog
%{_bindir}/marco
%{_bindir}/marco-message
%{_bindir}/marco-theme-viewer
%{_datadir}/applications/marco.desktop
%{_datadir}/themes/Atlanta
%{_datadir}/themes/ClearlooksRe
%{_datadir}/themes/Dopple-Left
%{_datadir}/themes/Dopple
%{_datadir}/themes/DustBlue
%{_datadir}/themes/Esco
%{_datadir}/themes/Gorilla
%{_datadir}/themes/Motif
%{_datadir}/themes/Raleigh
%{_datadir}/themes/Spidey-Left
%{_datadir}/themes/Spidey
%{_datadir}/themes/Splint-Left
%{_datadir}/themes/Splint
%{_datadir}/themes/WinMe
%{_datadir}/themes/eOS
%dir %{_datadir}/marco
%dir %{_datadir}/marco/icons
%{_datadir}/marco/icons/marco-window-demo.png
%{_datadir}/mate-control-center/keybindings/50-marco*.xml
%{_datadir}/mate/wm-properties
%{_mandir}/man1/*

%files libs -f %{name}.lang
%{_libdir}/libmarco-private.so.2*
%{_datadir}/glib-2.0/schemas/org.mate.marco.gschema.xml

%files devel
%{_bindir}/marco-window-demo
%{_includedir}/marco-1
%{_libdir}/libmarco-private.so
%{_libdir}/pkgconfig/libmarco-private.pc
%{_mandir}/man1/marco-theme-viewer.1.*
%{_mandir}/man1/marco-window-demo.1.*


%changelog
%autochangelog

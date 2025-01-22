Name:       ibus-table
Version:    1.17.10
Release:    %autorelease
Summary:    The Table engine for IBus platform
License:    LGPL-2.1-or-later
URL:        https://github.com/mike-fabian/ibus-table
Source0:    https://github.com/mike-fabian/ibus-table/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires:       ibus > 1.3.0
%{?__python3:Requires: %{__python3}}
# To play a sound on error:
Recommends: python3-simpleaudio
BuildRequires:  gcc
BuildRequires:  ibus-devel > 1.3.0
BuildRequires:  python3-devel >= 3.6.0
# for the unit tests
%if 0%{?fedora}
BuildRequires:  appstream
%endif
BuildRequires:  docbook-utils
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-base
BuildRequires:  dbus-x11
BuildRequires:  ibus-table-chinese-wubi-jidian
BuildRequires:  ibus-table-chinese-cangjie
BuildRequires:  ibus-table-chinese-stroke5
BuildRequires:  ibus-table-code
BuildRequires:  ibus-table-latin
BuildRequires:  ibus-table-translit
BuildRequires:  ibus-table-tv
BuildRequires: make

Obsoletes:   ibus-table-additional < 1.2.0.20100111-5

BuildArch:  noarch

%description
The Table engine for IBus platform.

%package -n %{name}-devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}, pkgconfig

%description -n %{name}-devel
Development files for %{name}.

%package tests
Summary:        Tests for the %{name} package
Requires:       %{name} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%setup -q

%build
export PYTHON=%{__python3}
%configure --disable-static --disable-additional --enable-installed-tests
%make_build

%install
%__rm -rf $RPM_BUILD_ROOT
export PYTHON=%{__python3}
%make_install NO_INDEX=true pkgconfigdir=%{_datadir}/pkgconfig
%py_byte_compile %{python3} %{buildroot}/usr/share/ibus-table/engine
%py_byte_compile %{python3} %{buildroot}/usr/share/ibus-table/setup

%find_lang %{name}

%check
%if 0%{?fedora}
appstreamcli validate --pedantic --explain --no-net %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml
%endif
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.metainfo.xml
desktop-file-validate \
    $RPM_BUILD_ROOT%{_datadir}/applications/ibus-setup-table.desktop
pushd engine
# run doctests
    python3 table.py -v
    python3 it_util.py -v
popd
mkdir -p /tmp/glib-2.0/schemas/
cp org.freedesktop.ibus.engine.table.gschema.xml \
   /tmp/glib-2.0/schemas/org.freedesktop.ibus.engine.table.gschema.xml
glib-compile-schemas /tmp/glib-2.0/schemas #&>/dev/null || :
export XDG_DATA_DIRS=/tmp
eval $(dbus-launch --sh-syntax)
dconf dump /
dconf write /org/freedesktop/ibus/engine/table/wubi-jidian/chinesemode 1
dconf write /org/freedesktop/ibus/engine/table/wubi-jidian/spacekeybehavior false
dconf dump /

make check && rc=0 || rc=1
cat tests/*.log
if [ $rc != 0 ] ; then
    exit $rc
fi

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_datadir}/%{name}
%{_datadir}/metainfo/*.metainfo.xml
%{_datadir}/ibus/component/table.xml
%{_datadir}/icons/hicolor/16x16/apps/ibus-table.png
%{_datadir}/icons/hicolor/22x22/apps/ibus-table.png
%{_datadir}/icons/hicolor/32x32/apps/ibus-table.png
%{_datadir}/icons/hicolor/48x48/apps/ibus-table.png
%{_datadir}/icons/hicolor/64x64/apps/ibus-table.png
%{_datadir}/icons/hicolor/128x128/apps/ibus-table.png
%{_datadir}/icons/hicolor/256x256/apps/ibus-table.png
%{_datadir}/icons/hicolor/scalable/apps/ibus-table.svg
%{_datadir}/applications/ibus-setup-table.desktop
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.table.gschema.xml
%{_bindir}/%{name}-createdb
%{_libexecdir}/ibus-engine-table
%{_libexecdir}/ibus-setup-table
%{_mandir}/man1/*

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%files tests
%dir %{_libexecdir}/installed-tests
%{_libexecdir}/installed-tests/%{name}
%dir %{_datadir}/installed-tests
%{_datadir}/installed-tests/%{name}

%changelog
%autochangelog

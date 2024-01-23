# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.26

# Settings used for build from snapshots.
%{!?rel_build:%global commit c1ca209172a8b3a0751ac0a1e2dbec33c1894290}
%{!?rel_build:%global commit_date 20140712}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

# provides are in a private subdirectory of %%{_libdir}
%global __provides_exclude_from ^%{_libdir}/pluma/plugins

Summary:  Modules for the pluma text editor
Name:     pluma-plugins
Version:  %{branch}.0
%if 0%{?rel_build}
Release:  8%{?dist}
%else
Release:  0.7%{?git_rel}%{?dist}
%endif
License:  GPLv2+
URL:      https://mate-desktop.org

# for downloading the tarball use 'spectool -g -R pluma.spec'
# Source for release-builds.
%{?rel_build:Source0:     https://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    https://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

# from upstream 1.26 branch
Patch1:        pluma_plugins_0001-Fix-synctex-plugin-dependency-detection.patch

BuildRequires: gcc
BuildRequires: gtk3-devel
BuildRequires: gtksourceview4-devel
BuildRequires: libpeas-devel
BuildRequires: make
BuildRequires: mate-common
BuildRequires: pluma-devel
BuildRequires: python3-dbus
BuildRequires: python3-devel
BuildRequires: vte291-devel
BuildRequires: yelp-tools

Requires:      %{name}-data = %{version}-%{release}
Requires:      pluma
Requires:      python3-dbus
Requires:      libpeas-loader-python3

%description
Modules for the pluma text editor

%package data
Summary:   Data files for pluma-plugins
BuildArch: noarch
Requires:  %{name} = %{version}-%{release}

%description data
This package contains shared data needed for pluma-plugins.


%prep
%if 0%{?rel_build}
%autosetup -p1
%else
%autosetup -n %{name}-%{commit} -p1
%endif

%if 0%{?rel_build}
# for releases
#NOCONFIGURE=1 ./autogen.sh
%else
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif

# Until Patch1 is part of an upstream release
NOCONFIGURE=1 ./autogen.sh

sed -i "1d" plugins/synctex/synctex/atril_dbus.py

%build
%configure \
        --enable-verify-all   \
        --enable-python       \
        --enable-deprecations

# fix unused-direct-shlib-dependency
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build V=1

%install
%{make_install}

# clean up all the static libs for plugins
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%find_lang %{name} --with-gnome --all-name


%files
%{_libdir}/pluma/plugins/*
%{_datadir}/metainfo/pluma-bookmarks.metainfo.xml
%{_datadir}/metainfo/pluma-codecomment.metainfo.xml
%{_datadir}/metainfo/pluma-synctex.metainfo.xml
%{_datadir}/metainfo/pluma-terminal.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.sourcecodebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.terminal.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.pluma.plugins.wordcompletion.gschema.xml

%files data -f %{name}.lang
%doc AUTHORS ChangeLog NEWS
%license COPYING
%{_datadir}/pluma/plugins/sourcecodebrowser/


%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Jul 31 2022 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-5
- fix synctex plugin dependency detection

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Robert Scheck <robert@fedoraproject.org> - 1.26.0-3
- Fix upstream dependency from dbus-python-devel to python3-dbus

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Aug 07 2021 Wolfgang Ulbrich <fedora@raveit.de> - 1.26.0-1
- initial build


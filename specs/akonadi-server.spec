%if 0%{?flatpak}
%global database_backend SQLITE
%endif

Name:    akonadi-server
Summary: PIM Storage Service
Version: 24.12.1
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:     https://invent.kde.org/frameworks/akonadi

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/akonadi-%{version}.tar.xz

## mysql config
Source10:       akonadiserverrc.mysql
Source11:       akonadiserverrc.sqlite


## upstreamable patches

## upstream patches (lookaside cache)

## downstream patches

%define mysql_conf_timestamp 20170512

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel

BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Crash)

BuildRequires:  boost-devel
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sqlite3) >= 3.6.23


## (some) optional deps
BuildRequires:  pkgconfig(Qt6Designer)
BuildRequires:  cmake(AccountsQt6)
BuildRequires:  cmake(KAccounts6)

# ^^ sqlite3 driver plugin needs versioned qt6 dep
BuildRequires: qt6-qtbase-private-devel

%if ! 0%{?flatpak}
BuildRequires: mariadb-server
%endif

Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%if ! 0%{?flatpak}
Recommends:     %{name}-mysql = %{version}-%{release}
%endif

# Plasma 6
Obsoletes:      kf5-akonadi-server < 24.01.80-1

%description
%{summary}.

%package devel
Summary:        Developer files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF6Config)
Requires:       cmake(KF6ConfigWidgets)
Requires:       cmake(KF6CoreAddons)
Requires:       cmake(KF6ItemModels)
Requires:       cmake(KF6KIO)
Requires:       cmake(KF6XmlGui)
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6DBus)
Requires:       cmake(Qt6Gui)
Requires:       cmake(Qt6Network)
Requires:       cmake(Qt6Widgets)
Requires:       cmake(Qt6Xml)
# For testing
Requires:       cmake(Qt6Test)

# at least dbus-1/interfaces conflict, maybe more -- rex
Conflicts:      akonadi-devel
Conflicts:      kf5-akonadi-server-devel
%description devel
%{summary}.

%package mysql
Summary:        Akonadi MySQL backend support
# upgrade path
Obsoletes:      kf5-akonadi-server-mysql < 24.01.80-1
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mariadb-server
Requires:       qt6-qtbase-mysql%{?_isa}
Requires(post): /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives
%description mysql
Configures akonadi to use mysql backend by default.

Requires an available instance of mysql server at runtime.
Akonadi can spawn a per-user one automatically if the mysql-server
package is installed on the machine.
See also: %{_sysconfdir}/akonadi/mysql-global.conf

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n akonadi-%{version} -p1

# Remove together with move-translations.patch once released
find ./po -type f -name libakonadi5.po -execdir mv {} libakonadi6.po \;


%build
%cmake_kf6 \
  %{?database_backend:-DDATABASE_BACKEND=%{database_backend}} \
  -DINSTALL_APPARMOR:BOOL=OFF \
  -DMYSQLD_EXECUTABLE:FILEPATH=%{_libexecdir}/mysqld \
  -DMYSQLD_SCRIPTS_PATH:FILEPATH=%{_bindir}/mysql_install_db \
  -DPOSTGRES_PATH:FILEPATH=%{_bindir}/pg_ctl
%cmake_build


%install
%cmake_install

%find_lang libakonadi6 --all-name --with-html --with-qt

install -p -m644 -D %{SOURCE10} %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
install -p -m644 -D %{SOURCE11} %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite

mkdir -p %{buildroot}%{_datadir}/akonadi/agents

touch -d %{mysql_conf_timestamp} \
  %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-global*.conf \
  %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-local.conf

# create/own these dirs
mkdir -p %{buildroot}%{_kf6_datadir}/akonadi/plugins
mkdir -p %{buildroot}%{_kf6_libdir}/akonadi

# %%ghost'd global akonadiserverrc
touch akonadiserverrc
install -p -m644 -D akonadiserverrc %{buildroot}%{_sysconfdir}/xdg/akonadi/akonadiserverrc

## unpackaged files
# omit mysql-global-mobile.conf
rm -fv %{buildroot}%{_sysconfdir}/xdg/akonadi/mysql-global-mobile.conf


%post
/usr/sbin/update-alternatives \
  --install %{_sysconfdir}/xdg/akonadi/akonadiserverrc \
  akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite \
  8

%postun
if [ $1 -eq 0 ] ; then
/usr/sbin/update-alternatives \
  --remove akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite
fi


%files -f libakonadi6.lang
%doc AUTHORS
%doc README*
%license LICENSES/*
%dir %{_sysconfdir}/xdg/akonadi/
%ghost %config(missingok,noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc
%config(noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc.sqlite
%{_kf6_datadir}/qlogging-categories6/akonadi.*
%{_kf6_bindir}/akonadi-db-migrator
%{_kf6_bindir}/akonadi_agent_launcher
%{_kf6_bindir}/akonadi_agent_server
%{_kf6_bindir}/akonadi_control
%{_kf6_bindir}/akonadi_rds
%{_kf6_bindir}/akonadictl
%{_kf6_bindir}/akonadiserver
%{_kf6_bindir}/asapcat
%{_kf6_bindir}/akonadi2xml
%{_kf6_bindir}/akonadiselftest
%{_kf6_bindir}/akonaditest
%{_kf6_datadir}/dbus-1/services/org.freedesktop.Akonadi.*.service
%{_kf6_datadir}/mime/packages/akonadi-mime.xml
%{_kf6_datadir}/akonadi/
%{_kf6_datadir}/config.kcfg/resourcebase.kcfg
%{_kf6_datadir}/kf6/akonadi/
%{_kf6_libdir}/libKPim6Akonadi*.so.*
%{_kf6_datadir}/icons/hicolor/*/apps/akonadi.*

# akonadi_knut_resource
%{_kf6_bindir}/akonadi_knut_resource
%{_kf6_datadir}/kf6/akonadi_knut_resource/

%files devel
%{_kf6_datadir}/dbus-1/interfaces/org.freedesktop.Akonadi.*.xml
%{_includedir}/KPim6/Akonadi/
%{_includedir}/KPim6/AkonadiAgentBase/
%{_includedir}/KPim6/AkonadiCore/
%{_includedir}/KPim6/AkonadiWidgets/
%{_includedir}/KPim6/AkonadiXml/
%{_kf6_libdir}/libKPim6Akonadi*.so
%{_kf6_libdir}/cmake/KPim6Akonadi/
%{_kf6_qtplugindir}/pim6/akonadi/akonadi_test_searchplugin.so
%{_kf6_qtplugindir}/designer/akonadi6widgets.so
%{_kf6_datadir}/kdevappwizard/templates/akonadiresource.tar.bz2
%{_kf6_datadir}/kdevappwizard/templates/akonadiserializer.tar.bz2
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%post mysql
/usr/sbin/update-alternatives \
  --install %{_sysconfdir}/xdg/akonadi/akonadiserverrc \
  akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql \
  10

%postun mysql
if [ $1 -eq 0 ]; then
/usr/sbin/update-alternatives \
  --remove akonadiserverrc \
  %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
fi

%files mysql
%config(noreplace) %{_sysconfdir}/xdg/akonadi/akonadiserverrc.mysql
%config(noreplace) %{_sysconfdir}/xdg/akonadi/mysql-global.conf
%config(noreplace) %{_sysconfdir}/xdg/akonadi/mysql-local.conf


%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 24.08.2-2
- Rebuild (qt6)

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 24.02.1-2
- Rebuild (qt6)

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Sun Mar 10 2024 Marie Loise Nolden <loise@kde.org> - 24.02.0-3
- add missing BuildArch: noarch to -doc package

* Sun Mar 3 2024 Marie Loise Nolden <loise@kde.org> - 24.02.0-2
- move qt designer plugin to -devel

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 24.01.95-2
- Rebuild (qt6)

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 31 2024 Alessandro Astone <ales.astone@gmail.com> - 24.01.90-5
- Generic mysql is no more, switch to requiring mariadb

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Alessandro Astone <ales.astone@gmail.com> - 24.01.90-2
- Restore mariadb preference as in KF5 akonadi

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90
- Add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-4
- Backport rename translation files

* Sun Dec 17 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-3
- Make upgrade path for mysql subpackage

* Sat Dec 16 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-2
- Obsolete the old Akonadi

* Wed Dec 6 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

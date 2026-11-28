# The System Settings module for KDE is compiled, so it is a bcond. Without it
# everything is Python, and the whole build is noarch.
#
# No binary package is named after the source, as there is no %%files section for
# it, so that the application can be noarch next to the compiled module. The
# License of the preamble is therefore that of the sources.
%bcond kcm 1

Name:           mddm-config
Version:        0.2.1
Release:        1%{?dist}
Summary:        Configuration tool for the MDDM display manager

License:        GPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0
URL:            https://forge.moderndesktop.dev/ModernDesktopInitiative/mddm-config
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%if %{without kcm}
BuildArch:      noarch
%endif

BuildRequires:  cmake
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pytest)


%description
Configuration tools for the MDDM display manager: a graphical application,
and a System Settings module for KDE Plasma.

%dnl --------------------------------------------------------------

%package -n mddm-conf
Summary:        Configuration tool for the MDDM display manager
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  scdoc
BuildRequires:  python3dist(pyqt6)
BuildRequires:  python3dist(commented-configparser)

Requires:       mddm
Requires:       polkit
Requires:       PolicyKit-authentication-agent
Requires:       python3dist(commented-configparser)
Requires:       python3dist(pyqt6)
Provides:       %{name} = %{version}-%{release}

%description -n mddm-conf
A graphical tool to configure the MDDM display manager. It selects the
greeter theme, with previews, and edits the behavior, autologin and
advanced options of MDDM.

Changes are written to a drop-in file,
%{_sysconfdir}/mddm.conf.d/50-mddm-config.conf, by a small privileged
helper that is authorized through polkit, so %{_sysconfdir}/mddm.conf is
never modified.

%files -n mddm-conf
%license LICENSES
%doc README.md
%{_bindir}/mddm-config
%{_libexecdir}/mddm-config-helper
%{_datadir}/applications/mddm-config.desktop
%{_datadir}/mddm-config/
%{_datadir}/polkit-1/actions/org.moderndesktop.mddm-config.policy
%{_mandir}/man1/mddm-config.1*
%{_mandir}/man8/mddm-config-helper.8*

%dnl --------------------------------------------------------------

%if %{with kcm}
%package -n kcm-mddm
Summary:        System Settings module for the MDDM login manager
License:        GPL-3.0-only AND GPL-3.0-or-later AND GPL-2.0-or-later AND LGPL-2.1-or-later AND CC0-1.0

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Test)
# the QML modules, the style of KDE and kcmshell6, for the tests of the module
BuildRequires:  qt6qml(org.kde.kcmutils)
BuildRequires:  qt6qml(org.kde.kirigami)
BuildRequires:  qt6qml(org.kde.desktop)

Requires:       qt6qml(org.kde.kirigami)
Requires:       mddm
Requires:       polkit
Supplements:    (mddm and plasma-systemsettings)

%description -n kcm-mddm
A System Settings module for KDE Plasma, "Login Screen (MDDM)", modeled on
sddm-kcm. It selects the greeter theme, with previews, and edits the autologin,
user, command and greeter settings of MDDM.

Changes are written to the same drop-in file as mddm-conf writes, by a KAuth
helper that runs as root and is authorized through polkit, so
%{_sysconfdir}/mddm.conf is never modified. It does not need mddm-conf.

%files -n kcm-mddm
%license LICENSES
%{_qt6_plugindir}/plasma/kcms/systemsettings/kcm_mddm.so
%{_libexecdir}/kf6/kauth/kcmmddm_authhelper
%{_datadir}/applications/kcm_mddm.desktop
%{_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmmddm.service
%{_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmmddm.conf
%{_datadir}/polkit-1/actions/org.kde.kcontrol.kcmmddm.policy

%endif

%dnl --------------------------------------------------------------

%prep
%autosetup -C -p1


%conf
%cmake -DWITH_KCM:STRING=%{?with_kcm:ON}%{!?with_kcm:OFF}


%build
%cmake_build


%install
%cmake_install


%check
%ctest


%changelog
* Wed Nov 25 2026 Shawn W Dunn <sfalken@kalpadesktop.org> - 0.2.1-1
- Initial Packaging


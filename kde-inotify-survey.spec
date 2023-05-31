Name:          kde-inotify-survey
Version:       23.04.1
Release:       1%{?dist}
Summary:       Monitors inotify limits and lets the user know when exceeded
#*No copyright* BSD 3-Clause License
#-----------------------------------
#kde-inotify-survey-v1.0.0/CMakeLists.txt
#kde-inotify-survey-v1.0.0/LICENSES/BSD-3-Clause.txt
#kde-inotify-survey-v1.0.0/autotests/CMakeLists.txt
#kde-inotify-survey-v1.0.0/src/CMakeLists.txt
#kde-inotify-survey-v1.0.0/src/Messages.sh
#kde-inotify-survey-v1.0.0/src/helper/CMakeLists.txt
#kde-inotify-survey-v1.0.0/src/kded/CMakeLists.txt
#kde-inotify-survey-v1.0.0/src/survey/CMakeLists.txt
#
#*No copyright* Creative Commons CC0 1.0
#---------------------------------------
#kde-inotify-survey-v1.0.0/.git-blame-ignore-revs
#kde-inotify-survey-v1.0.0/.gitlab-ci.yml
#kde-inotify-survey-v1.0.0/.kde-ci.yml
#kde-inotify-survey-v1.0.0/LICENSES/CC0-1.0.txt
#kde-inotify-survey-v1.0.0/README.md
#kde-inotify-survey-v1.0.0/screenshot.png.license
#kde-inotify-survey-v1.0.0/src/helper/org.kde.kded.inotify.actions
#kde-inotify-survey-v1.0.0/src/kded/inotify.json.license
#kde-inotify-survey-v1.0.0/src/kded/org.kde.kded.inotify.notifyrc
#
#*No copyright* FSF All Permissive License
#-----------------------------------------
#kde-inotify-survey-v1.0.0/LICENSES/FSFAP.txt
#kde-inotify-survey-v1.0.0/org.kde.inotify-survey.metainfo.xml
#
#*No copyright* GNU General Public License, Version 2
#----------------------------------------------------
#kde-inotify-survey-v1.0.0/autotests/entriestest.cpp
#kde-inotify-survey-v1.0.0/src/helper/helper.h
#kde-inotify-survey-v1.0.0/src/kded/kded.cpp
#kde-inotify-survey-v1.0.0/src/survey/entries.cpp
#kde-inotify-survey-v1.0.0/src/survey/entries.h
#kde-inotify-survey-v1.0.0/src/survey/main.cpp
#
#*No copyright* GNU General Public License, Version 2 [generated file]
#---------------------------------------------------------------------
#kde-inotify-survey-v1.0.0/src/helper/helper.cpp
#
#*No copyright* GNU General Public License, Version 3
#----------------------------------------------------
#kde-inotify-survey-v1.0.0/LICENSES/LicenseRef-KDE-Accepted-GPL.txt
#
#*No copyright* GNU Lesser General Public License, Version 2.1
#-------------------------------------------------------------
#kde-inotify-survey-v1.0.0/po/uk/kde-inotify-survey.po
#
#Creative Commons CC0 1.0
#------------------------
#kde-inotify-survey-v1.0.0/.reuse/dep5
#
#GNU General Public License, Version 2
#-------------------------------------
#kde-inotify-survey-v1.0.0/LICENSES/GPL-2.0-only.txt
#
#GNU General Public License, Version 3
#-------------------------------------
#kde-inotify-survey-v1.0.0/LICENSES/GPL-3.0-only.txt
License:       BSD-3-Clause and CC0-1.0 and FSFAP and GPL-2.0-only and GPL-3.0-only
URL:           https://invent.kde.org/system/%{name}

Source:        https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Updates the dbus service config to use the right policies to satisfy a rpmlint error
# Merge Request: https://invent.kde.org/frameworks/kauth/-/merge_requests/44
Source1:       org.kde.kded.inotify.conf

Requires:      kf5-kded
Requires:      dbus-common
Requires:      polkit
BuildRequires: kf5-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: qt5-qtbase-devel
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Notifications)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5Auth)

%description
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name
rm %{buildroot}%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
install -m644 -p -D %{SOURCE1} %{buildroot}%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf

%files -f %{name}.lang
%license LICENSES/* screenshot.png.license
%doc README.md screenshot.png
%{_bindir}/kde-inotify-survey
%{_kf5_plugindir}/kded/inotify.so
%{_kf5_libexecdir}/kauth/kded-inotify-helper
%{_datadir}/dbus-1/system-services/org.kde.kded.inotify.service
%{_datadir}/dbus-1/system.d/org.kde.kded.inotify.conf
%{_datadir}/knotifications5/org.kde.kded.inotify.notifyrc
%{_datadir}/metainfo/org.kde.inotify-survey.metainfo.xml
%{_datadir}/polkit-1/actions/org.kde.kded.inotify.policy

%changelog
* Mon May 29 2023 Steve Cossette <farchord@gmail.com> - 23.04.1-1
- Initial release

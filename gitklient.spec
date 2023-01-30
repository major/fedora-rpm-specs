%global gitcommit_full a4246d28f8600f4bf5a77253c2a8f3f1e1ae2cb1
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20230128

Name:           gitklient
Version:        0
Release:        2.%{date}git%{gitcommit}%{?dist}
Summary:        Git gui client for KDE

License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:            https://apps.kde.org/gitklient/
Source0:        https://invent.kde.org/sdk/gitklient/-/archive/%{gitcommit_full}/%{name}-%{gitcommit_full}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kdbusaddons-devel
BuildRequires:  kf5-kdoctools-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-ktexteditor-devel
BuildRequires:  kf5-syntax-highlighting-devel

Requires:       kf5-filesystem
Requires:       hicolor-icon-theme


%description
Git gui client for KDE.

%prep
%autosetup -n %{name}-%{gitcommit_full}


%build
%cmake
%cmake_build


%install
%cmake_install
%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.gitklient.appdata.xml


%files -f %{name}.lang
%license COPYING LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}diff
%{_bindir}/%{name}merge
%{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.4.0
%{_libdir}/lib%{name}diff.so.0
%{_libdir}/lib%{name}diff.so.0.4.0
%{_libdir}/lib%{name}gui.so.0
%{_libdir}/lib%{name}gui.so.0.4.0
%{_libdir}/qt5/plugins/kf5/kfileitemaction/gitklientitemaction.so
%{_libdir}/qt5/plugins/kf5/overlayicon/gitklientoverlayplugin.so
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/actions/*.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/qlogging-categories5/gitklient.categories
%{_defaultdocdir}/HTML/en/%{name}


%changelog
* Sat Jan 28 2023 Vasiliy Glazov <vascom2@gmail.com> - 0-1.20230128gita4246d28
- Update to latest git

* Thu Jan 19 2023 Vasiliy Glazov <vascom2@gmail.com> - 0-1.20230119git0645ced
- Initial packaging

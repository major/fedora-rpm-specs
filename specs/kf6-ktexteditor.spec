%global framework ktexteditor

Name:    kf6-%{framework}
Version: 6.10.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 with advanced embeddable text editor

License: BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

Source0: https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{version}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(Qt6TextToSpeech)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  pkgconfig(libgit2) >= 0.22.0
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(xkbcommon)
Requires: kf6-filesystem

%description
KTextEditor provides a powerful text editor component that you can embed in your
application, either as a KPart or using the KF6::TextEditor library (if you need
more control).

The text editor component contains many useful features, from syntax
highlighting and automatic indentation to advanced scripting support, making it
suitable for everything from a simple embedded text-file editor to an advanced
IDE.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       cmake(KF6Parts)
Requires:       cmake(KF6SyntaxHighlighting)
#Requires:       kf6-syntax-highlighting-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{framework}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name
# create/own dirs
mkdir -p %{buildroot}%{_kf6_qtplugindir}/ktexteditor
# Removing empty file
rm -f %{buildroot}%{_kf6_datadir}/katepart5/script/README.md

%files -f %{name}.lang
%dir %{_kf6_plugindir}/parts/
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/dbus-1/system-services/org.kde.ktexteditor6.katetextbuffer.service
%{_kf6_datadir}/dbus-1/system.d/org.kde.ktexteditor6.katetextbuffer.conf
%{_kf6_datadir}/polkit-1/actions/org.kde.ktexteditor6.katetextbuffer.policy
%{_kf6_datadir}/qlogging-categories6/%{framework}.*
%{_kf6_libdir}/libKF6TextEditor.so.*
%{_kf6_plugindir}/parts/katepart.so
%{_kf6_qtplugindir}/ktexteditor/
%{_kf6_libexecdir}/kauth/kauth_ktexteditor_helper
%{_kf6_bindir}/ktexteditor-script-tester6

%files devel
%{_kf6_datadir}/kdevappwizard/templates/ktexteditor6-plugin.tar.bz2
%{_kf6_includedir}/KTextEditor/
%{_kf6_libdir}/cmake/KF6TextEditor/
%{_kf6_libdir}/libKF6TextEditor.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Fri Jan 03 2025 Steve Cossette <farchord@gmail.com> - 6.10.0-1
- 6.10.0

* Sat Dec 14 2024 Steve Cossette <farchord@gmail.com> - 6.9.0-1
- 6.9.0

* Sat Nov 02 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.8.0-1
- 6.8.0

* Fri Oct 04 2024 Steve Cossette <farchord@gmail.com> - 6.7.0-1
- 6.7.0

* Mon Sep 16 2024 Steve Cossette <farchord@gmail.com> - 6.6.0-1
- 6.6.0

* Sat Aug 10 2024 Steve Cossette <farchord@gmail.com> - 6.5.0-1
- 6.5.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jul 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.0-2
- ktexteditor-script-tester6 does not belong to the -devel subpackage

* Sat Jul 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.4.0-1
- 6.4.0

* Sat Jun 01 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Sat May 04 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Wed Apr 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 6.0.0-3
- add missing BuildArch: noarch to -doc package

* Thu Feb 22 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-2
- Rebuild due to re-spin

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.249.0-1
- 5.249.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.248.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.248.0-1
- 5.248.0

* Tue Jan 09 2024 Marie Loise Nolden <loise@kde.org> - 5.247.0-2
- add doc package for KF6 API

* Wed Dec 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.247.0-1
- 5.247.0

* Sat Dec 02 2023 Justin Zobel <justin.zobel@gmail.com> - 5.246.0-1
- Update to 5.246.0

* Thu Nov 09 2023 Steve Cossette <farchord@gmail.com> - 5.245.0-1
- 5.245.0

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20231012.021300.814f396-1
- Initial release

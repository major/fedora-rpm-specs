Name:           rkward
Version:        0.7.5
Release:        %autorelease
Summary:        Graphical frontend for R language

License:        GPL-2.0-or-later
URL:            https://%{name}.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++, cmake, extra-cmake-modules
BuildRequires:  R-core-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Qml)
%ifarch %{qt5_qtwebengine_arches}
BuildRequires:  cmake(Qt5WebEngine)
%endif
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5WebKit)
BuildRequires:  hicolor-icon-theme, desktop-file-utils
Requires:       hicolor-icon-theme, shared-mime-info

%description
RKWard aims to provide an easily extensible, easy to use IDE/GUI for the
R-project. RKWard tries to combine the power of the R-language with the
(relative) ease of use of commercial statistics tools. Long term plans
include integration with office suites

%prep
%autosetup

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

## File lists
# locale's
%find_lang %{name} --with-kde || touch %{name}.lang

%files -f %{name}.lang
%doc README COPYING TODO AUTHORS
%doc %{_datadir}/doc/HTML/en/%{name}/
%doc %{_datadir}/doc/HTML/en/%{name}plugins/
%doc %lang(it) %{_datadir}/doc/HTML/it/%{name}/
%doc %lang(nl) %{_datadir}/doc/HTML/nl/%{name}/
%doc %lang(nl) %{_datadir}/doc/HTML/nl/%{name}plugins/
%doc %lang(sv) %{_datadir}/doc/HTML/sv/%{name}/
%doc %lang(sv) %{_datadir}/doc/HTML/sv/%{name}plugins/
%doc %lang(uk) %{_datadir}/doc/HTML/uk/%{name}/
%doc %lang(uk) %{_datadir}/doc/HTML/uk/%{name}plugins/
%{_datadir}/applications/org.kde.%{name}.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_datadir}/org.kde.syntax-highlighting/syntax/r*.xml
%{_datadir}/kservices5/%{name}.protocol
%{_datadir}/ktexteditor_snippets/data/RKWard*.xml
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_datadir}/mime/packages/vnd.%{name}.r.xml
%{_datadir}/mime/packages/vnd.kde.%{name}-output.xml
%{_datadir}/mime/packages/vnd.kde.rmarkdown.xml
%{_datadir}/%{name}/
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%lang(ca) %{_mandir}/ca/man1/%{name}.1*
%lang(de) %{_mandir}/de/man1/%{name}.1*
%lang(it) %{_mandir}/it/man1/%{name}.1*
%lang(nl) %{_mandir}/nl/man1/%{name}.1*
%lang(sv) %{_mandir}/sv/man1/%{name}.1*
%lang(uk) %{_mandir}/uk/man1/%{name}.1*
%{_libexecdir}/%{name}.rbackend

%changelog
%autochangelog

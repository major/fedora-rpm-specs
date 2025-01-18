Name:    cool-retro-term
Summary: Terminal emulator mimicking a CRT display
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License: GPL-3.0-or-later

Version: 1.2.0
Release: 9%{?dist}

URL: https://github.com/Swordfish90/%{name}
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: make
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtquickcontrols2-devel

Requires: hicolor-icon-theme
Requires: qt5-qtbase
Requires: qt5-qtbase-gui
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtdeclarative
Requires: qt5-qtquickcontrols
Requires: qt5-qtquickcontrols2

# Version requirement includes a release number as well,
# since we want a fresher git snapshot, not the original v0.2.0
%global qtw_version 0.2.0-9.20220109git6322802
BuildRequires: qmltermwidget >= %{qtw_version}
Requires: qmltermwidget >= %{qtw_version}


%description
%{name} is a terminal emulator which tries to mimic the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.


%prep
%setup -q

# qmltermwidget is included in the project via a git submodule.
# Since we serve it as a separate package, we modify
# the project file so it doesn't try to compile the bundled library.
rm -rf ./qmltermwidget
sed -e "s/SUBDIRS += qmltermwidget//" -i %{name}.pro


%build
%qmake_qt5 CONFIG+=force_debug_info
make %{?_smp_mflags}


%install
make INSTALL_ROOT=%{buildroot} install

desktop-file-install                         \
  --dir=%{buildroot}%{_datadir}/applications \
  %{name}.desktop

install -m 755 -d %{buildroot}%{_datadir}/metainfo/
install -m 644 packaging/appdata/%{name}.appdata.xml %{buildroot}%{_datadir}/metainfo/

install -m 755 -d %{buildroot}%{_mandir}/man1/
install -m 644 packaging/debian/%{name}.1 %{buildroot}%{_mandir}/man1/


%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml


%files
%doc README.md
%license gpl-3.0.txt
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/%{name}.appdata.xml


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.0-8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 1.2.0-1
- Update to v1.2.0

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Artur Iwicki <fedora@svgames.pl> - 1.1.1-6
- Don't BuildRequire the qt5-devel metapackage, properly list individual packages

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Artur Iwicki <fedora@svgames.pl> - 1.1.1-1
- Update to new upstream release

* Sun Dec 23 2018 Artur Iwicki <fedora@svgames.pl> - 1.1.0-2
- Make the Requires: and BuildRequires: on qmltermwidget versioned
- Don't remove screenshot sizes from appdata (issue fixed upstream)

* Fri Dec 21 2018 Artur Iwicki <fedora@svgames.pl> - 1.1.0-1
- Update to latest upstream version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.1-6
- Remove obsolete scriptlets

* Wed Nov 29 2017 Artur Iwicki <fedora@svgames.pl> 1.0.1-5
- Add missing runtime dependencies

* Sun Nov 26 2017 Artur Iwicki <fedora@svgames.pl> 1.0.1-4
- Use the %%_qt5_qmake macro during build
- Add runtime dependency on qmltermwidget
- Fix manpage permissions during install (-ax)

* Fri Nov 10 2017 Artur Iwicki <fedora@svgames.pl> 1.0.1-3
- Request tarball using %%{version} instead of %%{commit}
- Unbundle qmltermwidget
- Include manpage in package

* Sun Nov 05 2017 Artur Iwicki <fedora@svgames.pl> 1.0.1-2
- Add missing "Requires:"
- Invoke gtk-update-icon-cache after install/removal
- Remove ownership of libdir/qt5/qml/

* Sat Nov 04 2017 Artur Iwicki <fedora@svgames.pl> 1.0.1-1
- Initial packaging


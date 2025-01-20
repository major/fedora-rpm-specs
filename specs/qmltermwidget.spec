Name:       qmltermwidget
Summary:    A port of QTermWidget to QML

# Most of the project's code is under the GPL.
#
# The few files subject to the LGPL are:
# - lib/TerminalCharacterDecoder.cpp
# - lib/TerminalCharacterDecoder.h
# - lib/kprocess.cpp
# - lib/kprocess.h
# - lib/kpty.cpp
# - lib/kpty.h
# - lib/kpty_p.h
# - lib/kptydevice.cpp
# - lib/kptydevice.h
# - lib/kptyprocess.cpp
# - lib/kptyprocess.h
# - lib/qtermwidget.cpp
# - lib/qtermwidget.h
# - lib/qtermwidget_version.h.in
#
# There are also some build scripts under BSD-3-Clause,
# but since these are not included in the resulting package,
# said license is omitted from the License tag.
License:    GPL-2.0-or-later AND LGPL-2.0-or-later

%global git_date   20220109
%global git_commit 63228027e1f97c24abb907550b22ee91836929c5
%global git_commit_short %(c="%{git_commit}"; echo "${c:0:7}")

Version:    0.2.0^%{git_date}git%{git_commit_short}
Release:    5%{?dist}

URL:        https://github.com/Swordfish90/%{name}
Source0:    %{URL}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildRequires: make
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Quick)

%description
This project is a QML port of QTermWidget. It is written
to be as close as possible to the upstream project in order
to make cooperation possible.

%prep
%setup -q -n %{name}-%{git_commit}


%build
%qmake_qt5
%make_build


%install
make install INSTALL_ROOT=%{buildroot}
%if 0%{?flatpak}
# qtbase is part of runtime in /usr, this is built in /app
mv %{buildroot}/usr %{buildroot}%{_prefix}
%endif


%files
%license LICENSE LICENSE.LGPL2+
%doc README.md AUTHORS
%{_qt5_qmldir}/QMLTermWidget/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0^20220109git6322802-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0^20220109git6322802-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0^20220109git6322802-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0^20220109git6322802-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.0^20220109git6322802-1
- Update the license tag and migrate to SPDX
- Move snapshot information from release to caret-version

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-12.20220109git6322802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11.20220109git6322802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10.20220109git6322802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jan 30 2022 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0.2.0-9.20220109git6322802
- Update to latest git snapshot (required by cool-retro-term)
- Drop Patch0 (issue fixed upstream)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Artur Iwicki <fedora@svgames.pl> - 0.2.0-5
- Fix build errors due to missing #includes

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Artur Iwicki <fedora@svgames.pl> - 0.2.0-1
- Update to latest upstream version

* Sat Jul 21 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.0-6.20171027git08958f7
- Use "%%{_qt5_qmldir}" instead of "%%{_qt5_prefix}/qml"

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5.20171027git08958f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4.20171027git08958f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Artur Iwicki <fedora@svgames.pl> 0.1.0-3.20171027git08958f7
- Fix typo in Source0
- Fix typo in License: tag
- Remove the 'pkgconfig(Qt5Declarative)' build-requirement

* Fri Nov 10 2017 Artur Iwicki <fedora@svgames.pl> 0.1.0-2.20171027.git.08958f7
- Update to newest upstream snapshot (contains some bugfixes)

* Wed Jul 13 2016 Neal Gompa <ngompa13@gmail.com> 0.1.0-1
- Initial packaging

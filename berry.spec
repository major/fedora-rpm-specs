Name:           berry
Version:        1.0.0
Release:        20%{?dist}
Summary:        Modern and light image viewer

# The entire source code is GPLv3+
# except the following files in
# asemantools/qml/AsemanTools/Controls/Styles/Desktop/ which are BSD
# CalendarStyle.qml, FocusFrameStyle.qml, MenuBarStyle.qml, SliderStyle.qml
# StatusBarStyle.qml, TableViewStyle.qml, TextAreaStyle.qml, ToolBarStyle.qml

License:        GPLv3+ and BSD
Url:            http://aseman.co/en/products/berry
Source0:        http://aseman.co/downloads/berry/1/%{name}-%{version}-src.tar.gz
# https://github.com/Aseman-Land/Berry/issues/9
Source1:        %{name}.appdata.xml
# For a breakdown of the licensing, see PACKAGE-LICENSING
Source2:        %{name}-PACKAGE-LICENSING

# PATCH-FIX-OPENSUSE install.patch avvissu@yandex.ru -- Changed the paths install files
Patch0:         berry-1.0.0_install.patch
# PATCH-FIX-UPSTREAM qt5-5.5.patch avvissu@yandex.ru -- Fix build with Qt5 >= 5.5
Patch1:         berry-1.0.0_qt5-5.5.patch

BuildRequires:  libappstream-glib
BuildRequires:  hicolor-icon-theme
BuildRequires:  desktop-file-utils
BuildRequires:  chrpath
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(exiv2)
BuildRequires: make

%description
Berry is a modern and new image viewer which is focusing on User interface.
Berry is trying to provide an easy to use and touch screen compatible user
interface.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
cp -p %{SOURCE2} .

# fixes W: spurious-executable-perm
find . -type f  \( -name "*.cpp" -o -name "*.h" \) -exec chmod a-x {} \;

rm -rf debian

%build
mkdir build
pushd build
%{qmake_qt5} ../Berry.pro
%make_build
popd

%install
pushd build
%make_install INSTALL_ROOT=%{buildroot}
# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/%{name}
popd

install -Dp -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

find %{buildroot}%{_datadir}/%{name}/files/translations -name "*.qm" | sed 's:'%{buildroot}'::
s:.*/\([a-zA-Z]\{2\}\).qm:%lang(\1) \0:' > %{name}.lang

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files -f %{name}.lang
%license LICENSE LICENSE.html %{name}-PACKAGE-LICENSING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/Berry.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/application/%{name}-lock.xml
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/files
%dir %{_datadir}/%{name}/files/translations

%changelog
* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 30 2019 Rex Dieter <rdieter@fedoraproject.org> - 1.0.0-9
- rebuild (exiv2)

* Tue Oct 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-8
- Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-6
- Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-4
- Remove obsolete scriptlets

* Wed Aug 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-3
- add license breakdown

* Tue Aug 22 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-2
- add %%{name}.appdata.xml
- dropped /sbin/ldconfig not needed
- dropped update-desktop-database should not be used on Fedora 24+
- dropped update-mime-info it's obsolete
- add %%find-lang to handle translation


* Fri Jul 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1
- Initial release

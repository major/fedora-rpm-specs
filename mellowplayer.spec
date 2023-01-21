%undefine _package_note_flags
#%%global         commit b2968c3ebcb5ef20919be6f87ab1fe8b9dd66ffa
#%%global         shortcommit %%(c=%{commit}; echo ${c:0:7})
#%%global         commitdate 20200219
%global         rname MellowPlayer

Name:           mellowplayer
Version:        3.6.8
#Release:        1.%%{commitdate}git%%{shortcommit}%%{?dist}
Release:        11%{?dist}
Summary:        Cloud music integration for your desktop
License:        GPLv2
Url:            https://colinduquesnoy.github.io/MellowPlayer/
Source0:        https://gitlab.com/ColinDuquesnoy/%{rname}/-/archive/%{version}/%{rname}-%{version}.tar.bz2

ExclusiveArch:  %{qt5_qtwebengine_arches}

BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5WebChannel) >= 5.9.3
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(Qt5QuickControls2)
%if 0%{?fedora} > 32
BuildRequires:  qt5-qtbase-private-devel
%endif
BuildRequires:  pkgconfig(qxtglobalshortcut)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-linguist
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
#BuildRequires:  xorg-x11-server-Xvfb
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2
Requires:       hicolor-icon-theme

%description 
MellowPlayer is a free, open source and cross-platform desktop application that
integrates online music services with your desktop.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
%setup -q -n %{rname}-%{version}

# remove uneeded stuff
rm -rf scripts/packaging/osx
# remove commend in first line
sed -i '1,1d' src/main/share/applications/%{name}.desktop
sed -i '6d' src/main/share/applications/%{name}.desktop
# Wayland desktop file
sed -i -e 's|Exec=MellowPlayer|Exec=env QT_QPA_PLATFORM=xcb MellowPlayer|' src/main/share/applications/%{name}.desktop
sed -i -e 's|Exec=MellowPlayer --play-pause|Exec=env QT_QPA_PLATFORM=xcb MellowPlayer --play-pause|' src/main/share/applications/%{name}.desktop
sed -i -e 's|Exec=MellowPlayer --next|Exec=env QT_QPA_PLATFORM=xcb MellowPlayer --next|' src/main/share/applications/%{name}.desktop
sed -i -e 's|Exec=MellowPlayer --previous|Exec=env QT_QPA_PLATFORM=xcb MellowPlayer --previous|' src/main/share/applications/%{name}.desktop
# unbundle 3rdpary libqxt (qxtglobalshortcut) sources
rm -rf src/3rdparty/libqxt

%build
%cmake
%cmake_build

# Generate man page and html documentation (needs python3-sphinx)
sphinx-build-3 -N -bhtml docs/ docs/html
sphinx-build-3 -N -bman docs/ docs/man

%install
%cmake_install

# install man page
install -p -d -m755 %{buildroot}%{_mandir}/man1
install -p -m644 docs/man/%{name}.1 %{buildroot}%{_mandir}/man1/%{rname}.1

# install html docs
install -p -d -m755 %{buildroot}%{_docdir}/%{name}
mv docs/html %{buildroot}%{_docdir}/%{name}

# Fix W: file-not-utf8
iconv -f iso8859-1 -t utf-8 %{buildroot}%{_docdir}/%{name}/html/objects.inv > \
objects.inv.conv && mv -f objects.inv.conv %{buildroot}%{_docdir}/%{name}/html/objects.inv

# Fix W: hidden-file-or-dir
rm -rf %{buildroot}%{_docdir}/%{name}/html/{.buildinfo,.doctrees}

%check
# test suite fails
# to enable test suite, use "%%cmake -DBUILD_TESTS=ON ." 
# cd tests && xvfb-run -a ctest -V
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/*.%{rname}.metainfo.xml
 
%files
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE
%dir %{_datadir}/%{name}
%{_bindir}/%{rname}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/*.%{rname}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mellowplayer/plugins

%files doc
%{_datadir}/doc/%{name}/html
%{_mandir}/man1/%{rname}.1.*

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 3.6.8-9
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 3.6.8-8
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 3.6.8-7
- Rebuild (qt5)

* Mon Feb 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.6.8-6
- Set QT_QPA_PLATFORM=xcb in desktop file to help with wayland issues
  avoid crash on Wayland (#2008048)

* Sat Jan 29 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.6.8-5
- Add i%%undefine _package_note_flags

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Martin Gansser <martinkg@fedoraproject.org> - 3.6.8-1
- Update to 3.6.8

* Tue Dec 08 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.6.7-1
- Update to 3.6.7

* Fri Sep 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.6.6-1
- Update to 3.6.6

* Fri Aug 07 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.6.5-1
- Update to 3.6.5

* Tue Aug 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.6.4-4
- Fixed FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-3
- Second attempt - Rebuilt for
- https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.6.4-1
- Update to 3.6.4-1

* Fri Jun 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.6.3-1
- Update to 3.6.3-1
- Add BR qt5-qtbase-private-devel for fedora > 32
- Add BR pkgconfig(qxtglobalshortcut)

* Wed Feb 05 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.5.10-1
- Update to 3.5.10-1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.9-2.20200219gitb2968c3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.5.9-1.20200119gitb2968c3
- Update to 3.5.9-1.20290119gitb2968c3

* Sat Jan 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.5.8-2.20191227git9fd6cee
- Bump version due #8482 Koji build fails with "GenericError: Build already in progress"

* Fri Jan 03 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.5.8-1.20191227git9fd6cee
- Update to 3.5.8-1.20191227git9fd6cee

* Mon Nov 25 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5.6-1.20191124git433f80b
- Update to 3.5.6-1.20191124git433f80b

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.5-2.20190713git0154d81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5.5-1.20190716git0154d81
- Update to 3.5.5-1.20190716git0154d81

* Tue May 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5.4-1.20190521git28ffca9
- Update to 3.5.4-1.20190521git28ffca9

* Tue Apr 30 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5.3-2.20190310git4ac4b13
- Switch to python3

* Mon Mar 11 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5.3-1.20190310git4ac4b13
- Update to 3.5.3-1.20190310git4ac4b13

* Sun Feb 10 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5.2-1.20190206git54a1714
- Update to 3.5.2-1.20190206git54a1714

* Thu Feb 07 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5.1-1.20190206git402e336
- Update to 3.5.1-1.20190206git402e336
- Add patch for F30 %%{name}-suppress-compiler-warnings.patch

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-2.20181227git40ef9dd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0-1
- QBS is deprecated: swich back to CMake
- Moving to gitlab

* Mon Nov 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.4.0-4
- Add Make_sure_that_debug_builds_behave_the_same_as_release_builds.patch

* Sun Nov 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.4.0-3
- Add flag config:release due restore window doesn't work from
  GNOME Shell launcher or from GNOME notification center

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.4.0-1
- Update to 3.4.0
- Adapt to qbs build system
- Add BR qbs
- Remove BR cmake

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.3.5-2
- Rebuilt for Python 3.7

* Sun Mar 04 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.3.5-1
- Update to 3.3.5

* Mon Feb 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.3.4-1
- Update to 3.3.4
- Dropped %%{name}-fix-sphinx-build.patch
- Dropped %%{name}-CMakeLists.patch

* Sun Feb 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.3.3-2
- Add %%{name}-fix-sphinx-build.patch

* Sun Feb 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.3.3-1
- Update to 3.3.3
- Add %%{name}-CMakeLists.patch

* Tue Feb 06 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Wed Jan 03 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Sun Nov 05 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.1.0-3
- Use %%{buildroot} macro for consistency
- Large documentation must go in a -doc subpackage

* Sun Nov 05 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.1.0-2
- Don't add: %%dir %%{_datadir}/icons/hicolor/scalable and
             %%dir %%{_datadir}/icons/hicolor/scalable/apps
  These directories should be owned by the Requires to hicolor-icon-theme 
- Per the new guidelines, appdata files must now be installed in
  %%{_datadir}/metainfo/ instead of %%{_datadir}/appdata/
- Add Icon cache scriplet
- Add changelog and authors to %%doc
- Use simplified URL
- Use ExclusiveArch: %%{qt5_qtwebengine_arches} due Qt Web Engine is only
  available on some arches

* Wed Nov 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.1.0-1
- Initial build

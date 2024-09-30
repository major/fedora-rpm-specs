%global __provides_exclude_from ^%{_libdir}/%{name}/libMellowPlayer\\.so
%global __requires_exclude ^libMellowPlayer\.so

#For git snapshots, set to 0 to use release instead:
%global usesnapshot 1
%if 0%{?usesnapshot}
%global commit0 d5f3381284274b37e6b762e0b5b69a57a12fb564
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif
%global         rname MellowPlayer
%global         desktop_name ColinDuquesnoy.gitlab.com.MellowPlayer

Name:           mellowplayer
%if 0%{?usesnapshot}
Version:        3.6.9
Release:        0.3%{?snapshottag}%{?dist}
%else
Version:        3.6.8
Release:        2%{?dist}
%endif

Summary:        Cloud music integration for your desktop
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
Url:            https://colinduquesnoy.github.io/MellowPlayer/
%if 0%{?usesnapshot}
Source0:        https://gitlab.com/ColinDuquesnoy/%{rname}/-/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

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
BuildRequires:  pkgconfig(Qt5X11Extras)
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
BuildRequires:  chrpath
#BuildRequires:  xorg-x11-server-Xvfb
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtquickcontrols2
Requires:       hicolor-icon-theme

%description 
MellowPlayer is a free, open source and cross-platform desktop application that
integrates online music services with your desktop.

%package        doc
Summary:        Documentation files for %{name}
Group:          Documentation
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%prep
%if 0%{?usesnapshot}
%setup -q -n %{rname}-%{commit0}
%else
%autosetup -p1
%endif

# remove uneeded stuff
rm -rf scripts/packaging/osx
# remove commend in first line
sed -i '1,1d' src/main/share/applications/%{desktop_name}.desktop
sed -i '6d' src/main/share/applications/%{desktop_name}.desktop
# Wayland desktop file
sed -i -e 's|Exec=MellowPlayer|Exec=env QT_QPA_PLATFORM=xcb MellowPlayer|' src/main/share/applications/%{desktop_name}.desktop
sed -i -e 's|Exec=MellowPlayer --play-pause|Exec=env QT_QPA_PLATFORM=xcb MellowPlayer --play-pause|' src/main/share/applications/%{desktop_name}.desktop
sed -i -e 's|Exec=MellowPlayer --next|Exec=env QT_QPA_PLATFORM=xcb MellowPlayer --next|' src/main/share/applications/%{desktop_name}.desktop
sed -i -e 's|Exec=MellowPlayer --previous|Exec=env QT_QPA_PLATFORM=xcb MellowPlayer --previous|' src/main/share/applications/%{desktop_name}.desktop
# unbundle 3rdpary libqxt (qxtglobalshortcut) sources
rm -rf src/3rdparty/libqxt
 
%build
%set_build_flags
# Add RUNPATH pointing to %%{_libdir}/mellowplayer
export LDFLAGS="%{build_ldflags} -Wl,-rpath,%{_libdir}/%{name}"
%cmake .
%cmake_build

# Generate man page and html documentation (needs python-sphinx)
sphinx-build -N -bhtml docs/ docs/html
sphinx-build -N -bman docs/ docs/man

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

# E: invalid-soname
# A shared library without SONAME in %%{_libdir} should be moved out of linker search path
# Move the shared library to a package-specific directory
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/libMellowPlayer.*.so %{buildroot}%{_libdir}/%{name}/

# Fix RPATH using chrpath
# ERROR   0002: file '/usr/bin/MellowPlayer' contains an invalid rpath '/usr/' in [/usr/lib64/mellowplayer:/usr/]
chrpath --replace %{_libdir}/mellowplayer %{buildroot}%{_bindir}/%{rname}
# ERROR   0002: file '/usr/lib64/mellowplayer/libMellowPlayer.Application.so' contains an invalid rpath '/usr/' in [/usr/lib64/mellowplayer:/usr/]
# ERROR   0002: file '/usr/lib64/mellowplayer/libMellowPlayer.Infrastructure.so' contains an invalid rpath '/usr/' in [/usr/lib64/mellowplayer:/usr/]
# ERROR   0002: file '/usr/lib64/mellowplayer/libMellowPlayer.Presentation.so' contains an invalid rpath '/usr/' in [/usr/lib64/mellowplayer:/usr/]
# ERROR   0002: file '/usr/lib64/mellowplayer/libMellowPlayer.Domain.so' contains an invalid rpath '/usr/' in [/usr/lib64/mellowplayer:/usr/]
chrpath --replace %{_libdir}/%{name} %{buildroot}%{_libdir}/%{name}/libMellowPlayer.Application.so
chrpath --replace %{_libdir}/%{name} %{buildroot}%{_libdir}/%{name}/libMellowPlayer.Infrastructure.so
chrpath --replace %{_libdir}/%{name} %{buildroot}%{_libdir}/%{name}/libMellowPlayer.Presentation.so
chrpath --replace %{_libdir}/%{name} %{buildroot}%{_libdir}/%{name}/libMellowPlayer.Domain.so

# Remove duplicate files and create symlinks
rm -f %{buildroot}%{_datadir}/%{name}/plugins/amazon\ music/theme.json
ln -s ../radio\ paradise/theme.json %{buildroot}%{_datadir}/%{name}/plugins/amazon\ music/theme.json

rm -f %{buildroot}%{_datadir}/%{name}/plugins/last.fm/theme.json
ln -s ../radio\ paradise/theme.json %{buildroot}%{_datadir}/%{name}/plugins/last.fm/theme.json

rm -f %{buildroot}%{_datadir}/%{name}/plugins/youtube-music/logo.svg
ln -s ../youtube/logo.svg %{buildroot}%{_datadir}/%{name}//plugins/youtube-music/logo.svg

rm -f %{buildroot}%{_datadir}/%{name}/plugins/youtube-music/settings.json
ln -s ../youtube/settings.json %{buildroot}%{_datadir}/%{name}/plugins/youtube-music/settings.json

%check
# test suite fails
# to enable test suite, use "%%cmake -DBUILD_TESTS=ON ." 
# cd tests && xvfb-run -a ctest -V
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/com.gitlab.ColinDuquesnoy.%{rname}.metainfo.xml

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
fi
 
%files
%doc AUTHORS.md CHANGELOG.md README.md
%license LICENSE
%dir %{_datadir}/%{name}
%{_libdir}/%{name}/libMellowPlayer.*.so
%{_bindir}/%{rname}
%{_datadir}/applications/ColinDuquesnoy.gitlab.com.%{rname}.desktop
%{_datadir}/metainfo/com.gitlab.ColinDuquesnoy.%{rname}.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mellowplayer/plugins

%files doc
%{_datadir}/doc/%{name}/html
%{_mandir}/man1/%{rname}.1.*

%changelog
* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 3.6.9-0.3.gitd5f3381
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.9-0.2.gitd5f3381
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jul 04 2024 Martin Gansser <martinkg@fedoraproject.org> - 3.6.9-0.1.gitd5f3381
- Update to 3.6.9-0.1.gitd5f3381

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

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

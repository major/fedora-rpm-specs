#For git snapshots, set to 0 to use release instead:
%global usesnapshot 1
%if 0%{?usesnapshot}
%global commit 617ff8761250aa4c9f1dd8fde6dec45e0b96639a
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20240825
%global core_commit 277792824801495e868580ca86f6e7a1b53e4779
%global core_shortcommit %(c=%{core_commit}; echo ${c:0:7})
%global kddw_commit 8d2d0a5764f8393cc148a2296d511276a8ffe559
%global kddw_shortcommit %(c=%{kddw_commit}; echo ${c:0:7})
%endif
%global unique_name org.olivevideoeditor.Olive
%global appl_name application-vnd.olive-project

Name:           olive
%if 0%{?usesnapshot}
Version:        0.2.0^%{gitdate}git%{shortcommit}
%else
Version:        0.2.0
%endif
Release:        3%{?dist}
Summary:        A free non-linear video editor
# app/widget/flowlayout/flowlayout.*: BSD-3-Clause
# ext/KDDockWidgets/LICENSE.txt: GPL-2.0-only OR GPL-3.0-only
# ext/core/include/olive/core/util/sse2neon.h: MIT
License:        GPL-3.0-or-later AND BSD-3-Clause AND ( GPL-2.0-only OR GPL-3.0-only ) AND MIT
Url:            https://www.olivevideoeditor.org
%if 0%{?usesnapshot}
Source0:        https://github.com/olive-editor/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        https://github.com/olive-editor/core/archive/%{core_commit}/libolivecore-%{core_shortcommit}.tar.gz
Source2:        https://github.com/olive-editor/KDDockWidgets/archive/%{kddw_commit}/KDDockWidgets-%{kddw_shortcommit}.tar.gz
# https://github.com/olive-editor/olive/issues/2200
Patch0:         %{name}-qt6.patch
# https://github.com/olive-editor/olive/pull/2294
Patch1:         %{name}-ocio-2.3.patch
# fix build with FFmpeg 7.0+
# https://github.com/olive-editor/olive/issues/2325
Patch2:         %{name}-ffmpeg-7.patch
%else
Source0:        https://github.com/olive-editor/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  OpenColorIO-devel
BuildRequires:  OpenEXR-devel
BuildRequires:  OpenImageIO-devel
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  portaudio-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttranslations
Requires:       hicolor-icon-theme
# ext/KDDockWidgets
Provides:       bundled(KDDockWidgets) = 1.6.95
# ext/core
Provides:       bundled(libolivecore) = 1.0.0
# ext/core/include/olive/core/util/sse2neon.h
# older than 2022-10-28
Provides:       bundled(sse2neon)
# OpenImageIO and OpenColorIO are missing on i686
ExcludeArch:    i686

%description
%{name} is a free non-linear video editor with completely configurable render
pipeline and open source codebase designed to provide users with as much
control as possible over both their work and their workflow.

Olive's key feature is its render pipeline. Every step can be modified,
rearranged, or augmented to achieve whatever results the user desires. Control
is provided through a node-based compositor, which is the gold standard for
compositing workflows in the visual effects industry. By adding and connecting
nodes together, users "visually program" how their video and audio is generated
and processed. Compared to traditional "layer-based" workflows, this provides
much more freedom in what can be created, and requires far fewer steps to
achieve the same results.

%prep
%if 0%{?usesnapshot}
%autosetup -N -n %{name}-%{commit}
pushd ext
rmdir core
tar xzf %{S:1}
mv core{-%{core_commit},}
rmdir KDDockWidgets
tar xzf %{S:2}
mv KDDockWidgets{-%{kddw_commit},}
popd
%autopatch -p1
%else
%autosetup -p1 -n %{name}-%{version}
%endif

%build
%cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_QT6=ON \
  -DBUILD_SHARED_LIBS=OFF \
  -DBUILD_TESTS=ON \
  -DKDDockWidgets_EXAMPLES=OFF \
  -DOLIVECORE_BUILD_TESTS=ON \
  -DUSE_WERROR=OFF \

%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{unique_name}.appdata.xml
%ctest

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}-editor
%{_datadir}/applications/%{unique_name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{unique_name}.png
%{_datadir}/icons/hicolor/*/mimetypes/%{appl_name}.png
%{_metainfodir}/%{unique_name}.appdata.xml
%{_datadir}/mime/packages/%{unique_name}.xml

%changelog
* Thu Dec 26 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.2.0^20240825git617ff87-3
- Add missing BuildRequires: gcc-c++

* Sat Dec 21 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.2.0^20240825git617ff87-2
- Apply patch to fix build with FFmpeg 7.x (Mamoru Tasaka)

* Fri Sep 13 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.2.0^20240825git617ff87-1
- Update to latest snapshot
- Use post-release versioning with caret
- Update description
- Drop patch for unsupported architecture
- Update and sort BuildRequires alphabetically
- Use SPDX identifiers and enumerate all licenses
- Fix compilation with Qt6
- Fix compilation with OpenColorIO 2.3

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-0.14.20221118git5fce683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.2.0-0.13.20221118git5fce683
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 01 2023 Leigh Scott <leigh123linux@gmail.com> - 0.2.0-0.12.20221118git5fce683
- Rebuild for new ffmpeg

* Wed Feb 08 2023 Leigh Scott <leigh123linux@gmail.com> - 0.2.0-0.11.20221118git5fce683
- rebuilt

* Sat Nov 19 2022 Sérgio Basto <sergio@serjux.com> - 0.2.0-0.10.20221118git5fce683
- Update to olive-20221118git5fce683
- add armv7_build_fix.patch

* Fri Nov 11 2022 Leigh Scott <leigh123linux@gmail.com> - 0.1.2-0.9.20220818gitb169ad9
- rebuilt

* Mon Aug 22 2022 Sérgio Basto <sergio@serjux.com> - 0.1.2-0.8.20220818gitb169ad9
- Update snapshot to 20220818

* Sun Aug 07 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.2-0.7.20220228git41a49c4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Mar 03 2022 Nicolas Chauvet <kwizart@gmail.com> - 0.1.2-0.6.20220228git41a49c4
- Rebuilt

* Wed Mar 02 2022 Sérgio Basto <sergio@serjux.com> - 0.1.2-0.5.20220228git41a49c4
- New snapshot, ffmpeg 5 compatible

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan  1 2021 Leigh Scott <leigh123linux@gmail.com> - 0.1.2-5
- Rebuilt for new ffmpeg snapshot
- Add olive-0.1.2-qt5.15.patch

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 0.1.2-3
- Rebuild for ffmpeg-4.3 git

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.2-1
- Update to 0.1.2-1

* Wed Aug 07 2019 Leigh Scott <leigh123linux@gmail.com> - 0.1.0-0.4.20190515git55c5b00
- Rebuild for new ffmpeg version

* Fri May 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-0.3.20190515git55c5b00
- Add a more meaningful description and summary

* Thu May 16 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-0.2.20190515git55c5b00
- Update to 0.1.0-0.2.20190515git55c5b00
- Switch Build to cmake
- Remove BR hicolor-icon-theme
- Use %%autsetup
- Add BR pkgconfig(Qt5Svg)
- Add BR cmake3
- Use %%cmake3 macro instead of %%cmake
- Use %%{_metainfodir} macro

* Fri May 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-0.1.20190503git99b6ba6
- Update to 0.1.0-0.1.20190503git99b6ba6

* Wed Feb 06 2019 Martin Gansser <martinkg@fedoraproject.org> - 0-0.1.20190206gitfc96ad7
- initial package, not even released as version 0.1...

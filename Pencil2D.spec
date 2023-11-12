Name:           Pencil2D
Version:        0.6.6
Release:        %autorelease
Summary:        Create traditional hand-drawn animation using both bitmap and vector graphics

# The entire source is GPL-2.0-only, except:
#
# The following sources are copied and modified from an unknown version
# (copyright date 2016) of the Qt example. Since they are based on example code
# rather than library code, we do not consider this a case of bundling.
#   - core_lib/src/interface/flowlayout.{h,cpp} are BSD-3-Clause
#
# The following sources are derived, but not copied, from QAquarelle, which is
# GPL-2.0-or-later; however, it is not clearly indicated that the resulting
# source file is under the same license, so we assume the overall project
# license of GPL-2.0-only applies.
#   - core_lib/src/tool/strokemanager.cpp is derived from GPL-2.0-or-later
#     code, but is probably GPL-2.0-only
#
# Additionally, the following are under other allowed licenses but, for one
# reason or another, do not contribute to the licenses of the binary RPMs.
#
# The following sources belong to a bundled copy of the miniz library (version
# 2.1.0 as of this writing); they are removed in %%prep in order to use the
# system miniz library, and their licenses do not contribute to the licenses of
# the binary RPMs.
#   - core_lib/src/miniz.cpp is MIT
#   - core_lib/src/miniz.h appears to be Unlicense, although there is some
#     ambiguity
#
# The following source belongs to a bundled copy of Catch (catch2) (version
# 2.5.0 as of this writing); it is removed in %%prep in order to use the system
# Catch library. Because version 2.x (catch2) is header-only, it is treated as
# a static library and would contribute to the licenses of the binary RPMs,
# except that it is used only for test executables that are not installed.
#   - tests/src/catch.hpp is BSL-1.0
License:        GPL-2.0-only AND BSD-3-Clause
URL:            https://github.com/pencil2d/pencil
Source:         %{url}/archive/v%{version}/pencil-%{version}.tar.gz

# Add a LICENSE.QT.TXT file for BSD-3-Clause code from Qt
# https://github.com/pencil2d/pencil/pull/1757
# Modified for 0.6.6 to remove mention of source files not yet introduced.
Patch:          0001-Add-a-LICENSE.QT.TXT-file-for-BSD-3-Clause-code-from.patch

# Fix deprecated top-level developer_name in AppData XML
# https://github.com/pencil2d/pencil/pull/1796
Patch:          %{url}/pull/1796.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  pkgconfig(Qt5)
# app/app.pro:
# QT += core widgets gui xml multimedia svg network
# core_lib/core_lib.pro:
# QT += core widgets gui xml xmlpatterns multimedia svg
# tests/tests.pro:
# QT += core widgets gui xml xmlpatterns multimedia svg testlib
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)

BuildRequires:  miniz-devel
# Header-only:
BuildRequires:  catch2-static

BuildRequires:  desktop-file-utils
# Required by guidelines (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  help2man
BuildRequires:  xorg-x11-server-Xvfb

# Required to import and export videos. This is essential functionality for an
# animation tool, so we make it a hard dependency.
BuildRequires:  /usr/bin/ffmpeg
Requires:       /usr/bin/ffmpeg

# Provides plugins required for loading SVG icons
# https://github.com/pencil2d/pencil/pull/1796#issuecomment-1805940297
Requires:       qt5-qtsvg

# For %%{_datadir}/icons/hicolor
Requires:       hicolor-icon-theme

%global app_id org.pencil2d.Pencil2D

%description
%{summary}.


%prep
%autosetup -n pencil-%{version} -p1

# Unbundle miniz
rm -v core_lib/src/miniz.h core_lib/src/miniz.cpp
sed -r -i '/\bminiz\.(h|cpp)/d' core_lib/core_lib.pro
echo 'LIBS_PRIVATE += -lminiz' | tee -a */*.pro >/dev/null

# Unbundle catch2
rm -v tests/src/catch.hpp
sed -r -i '/\bcatch\.hpp/d' tests/tests.pro
echo 'INCLUDEPATH += "%{_includedir}/catch2"' >> tests/tests.pro


%build
# We want the compiled-in version information to describe this as a release
# build to the user. We could set DEFINES+=PENCIL2D_RELEASE, but that would set
# QT_NO_DEBUG_OUTPUT; we would rather preserve that to help with debugging, as
# it does no harm except for a slight impact on performance. Instead, we define
# PENCIL2D_RELEASE_BUILD directly. See common.pri for details.
%{qmake_qt5} PREFIX='%{_prefix}' DEFINES+=PENCIL2D_RELEASE_BUILD
%make_build

# Sometimes the formatting in help2man-generated man pages is of poor to
# marginal quality; in this case, it is good enough that it is not worth
# furnishing a hand-written man page. We need xvfb-run to generate the man page
# because the application aborts when it is run in a headless environment.
xvfb-run -a -- help2man --no-info --output=pencil2d.1 ./bin/pencil2d


%install
%make_install INSTALL_ROOT='%{buildroot}'

install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 pencil2d.1


%check
desktop-file-validate '%{buildroot}%{_datadir}/applications/%{app_id}.desktop'
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'
appstreamcli validate --no-net --explain \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'

# Run catch tests
./tests/bin/tests


%files
%license LICENSE.TXT LICENSE.QT.TXT

%doc README.md
%doc ChangeLog.md

%{_bindir}/pencil2d
%{_mandir}/man1/pencil2d.1*

%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/%{app_id}.png
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/mime/packages/%{app_id}.xml

%{_datadir}/bash-completion/completions/pencil2d
%{_datadir}/zsh/site-functions/_pencil2d


%changelog
%autochangelog

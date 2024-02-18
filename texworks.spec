%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Name:           texworks
Version:        0.6.9
Release:        %autorelease
Summary:        A simple IDE for authoring TeX documents

License:        GPL-2.0-or-later
URL:            https://tug.org/texworks/
Source0:        https://github.com/TeXworks/texworks/archive/release-%{version}/texworks-release-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  hunspell-devel
BuildRequires:  poppler-qt6-devel

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  lua-devel
# provides /usr/bin/xvfb-run
BuildRequires:  xorg-x11-server-Xvfb
# for testing
BuildRequires:  urw-base35-fonts

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc) documents,
with a Unicode-based, TeX-aware editor, integrated PDF viewer, and a clean,
simple interface accessible to casual and non-technical users.

TeXworks is inspired by Dick Koch's award-winning TeXShop program for macOS,
which has made quality typesetting through TeX accessible to a wider community
of users, without a technical or intimidating face. The goal of TeXworks is to
deliver a similarly integrated, easy-to-use environment for users on all
platforms, especially GNU/Linux and Windows.

%prep
%autosetup -p1 -n texworks-release-%{version}

%build
%cmake \
    -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DWITH_PYTHON=ON \
    -DTW_BUILD_ID=Fedora \
    -DTeXworks_DIC_DIR=%{_datadir}/hunspell \
    -DTeXworks_PLUGIN_DIR=%{_libdir}/texworks \
    -DQT_DEFAULT_MAJOR_VERSION=6

%cmake_build

%install
%cmake_install
rm %{buildroot}%{_docdir}/%{name}/COPYING

%check
# https://koji.fedoraproject.org/koji/taskinfo?taskID=111182097
# https://kojipkgs.fedoraproject.org//work/tasks/2208/111182208/build.log
# https://github.com/TeXworks/texworks/issues/1035
%ifarch s390x
xvfb-run -a bash -c "%ctest -E test_poppler-qt6"
%else
xvfb-run -a bash -c "%ctest"
%endif

desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml

%files
%license COPYING
%doc %{_docdir}/%{name}/
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.so
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/TeXworks.png
%{_datadir}/metainfo/texworks.appdata.xml

%changelog
%autochangelog

%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so$

Name:           texworks
Version:        0.6.8
Release:        %autorelease
Summary:        A simple IDE for authoring TeX documents
# SPDX migration
License:        GPL-2.0-or-later
URL:            http://tug.org/texworks/
Source0:        https://github.com/TeXworks/texworks/archive/release-%{version}/texworks-release-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  hunspell-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  lua-devel
BuildRequires:  desktop-file-utils
BuildRequires:  cmake

# Description adopted from Debian with modification
%description
TeXworks is an environment for authoring TeX (LaTeX, ConTeXt, etc) documents,
with a Unicode-based, TeX-aware editor, integrated PDF viewer, and a clean,
simple interface accessible to casual and non-technical users.

You may install the texlive-* packages to make this program useful.

%prep
%setup -q -n %{name}-release-%{version}

%build
%cmake -DWITH_PYTHON=ON -DTW_BUILD_ID=Fedora -DTeXworks_DIC_DIR=%{_datadir}/hunspell -DTeXworks_PLUGIN_DIR=%{_libdir}/texworks -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake_build

%install
%cmake_install
rm %{buildroot}/%{_docdir}/%{name}/COPYING

%files
%license COPYING
%{_docdir}/%{name}/
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/TeXworks*
%{_datadir}/metainfo/*


%changelog
%autochangelog

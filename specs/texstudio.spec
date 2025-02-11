Name:           texstudio
Version:        4.8.6
Release:        %autorelease

Summary:        A feature-rich editor for LaTeX documents
# texstudio binary: GPLv3 due to static linkage of bundled qcodeedit
# texstudio data and image files: GPLv2+
# Automatically converted from old format: GPLv2+ and GPLv3 - review is highly recommended.
License:        GPL-2.0-or-later AND GPL-3.0-only
URL:            https://www.texstudio.org

Source0:        https://github.com/texstudio-org/texstudio#/archive/%{name}-%{version}.tar.gz
Source1:        texstudio.desktop
Patch1:         texstudio-disable-update-check.patch


BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qttools-static
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  hunspell-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  poppler-devel
BuildRequires:  poppler-qt6-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  qtsingleapplication-qt6-devel
BuildRequires:  qtsinglecoreapplication-qt6-devel
# Not present in EPEL
%if 0%{?fedora}
BuildRequires:  qtermwidget-devel
%endif
BuildRequires:  quazip-qt6-devel
BuildRequires:  zlib-devel

Recommends:     tex(latex)
Recommends:     tex(preview.sty)
Recommends:     tex-dvipng
Requires:       qt6-qtsvg
# Not present in EPEL
%if 0%{?fedora}
Requires:       qtermwidget
%endif
Provides:       bundled(qcodeedit) 
Provides:       texmakerx = %{version}-%{release}
Obsoletes:      texmakerx < 2.2-1
%description
TeXstudio gives you an environment where you can 
easily create and manage LaTeX documents.
It provides modern writing support, like interactive spell checking, 
code folding, syntax highlighting, integrated pdf viewer
and various assistants. 
Also it serves as a starting point from where you can easily run 
all necessary LaTeX tools.

%prep
%setup -q -n %{name}-%{version}

%patch -P 1 -p1 -b .update_check

rm -rf {hunspell,qtsingleapplication,quazip}

%build
%cmake \
%ifnarch %{ix86} x86_64 %{arm}
    -DTEXSTUDIO_ENABLE_CRASH_HANDLER=OFF \
%endif
%cmake_build

%install
%cmake_install

install -Dp -m 0644 utilities/texstudio16x16.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio22x22.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/22x22/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio32x32.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio48x48.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/texstudio.png
install -Dp -m 0644 utilities/texstudio64x64.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/46x46/apps/texstudio.png


rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,COPYING,*.desktop,tex*.png}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/utilities/manual/source/CHANGELOG.md
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{*.dic,*.aff}
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/qt_*.qm

%find_lang %{name} --with-qt

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
desktop-file-install --dir %{buildroot}%{_datadir}/applications %{SOURCE1}

%files -f %{name}.lang
%{_bindir}/texstudio
%dir %{_datadir}/texstudio/
%{_datadir}/texstudio/*.png
%{_datadir}/texstudio/*.stopWords
%{_datadir}/texstudio/*.stopWords.level2
%{_datadir}/texstudio/de_DE.badWords
%{_datadir}/texstudio/template_*.tex
%{_datadir}/texstudio/template_*.zip
%{_datadir}/texstudio/*.json
%{_datadir}/texstudio/*.js
%{_datadir}/texstudio/th_*.dat
%{_datadir}/texstudio/*.html
%{_datadir}/texstudio/latex2e.css
%{_datadir}/texstudio/_sphinx_design_static/
%{_datadir}/texstudio/_images/*.webp
%{_datadir}/texstudio/_static/
%{_datadir}/texstudio/README_*
%{_datadir}/texstudio/CHANGELOG.md
%{_datadir}/applications/texstudio.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg
%{_datadir}/metainfo/texstudio.metainfo.xml

%doc utilities/AUTHORS utilities/COPYING utilities/manual/source/CHANGELOG.md

%changelog
%autochangelog

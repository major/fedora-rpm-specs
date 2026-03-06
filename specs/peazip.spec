Name:    peazip
%global rtld_name io.github.peazip.PeaZip

Summary: File archiver utility

# PeaZip's original code is LGPL.
#
# It reuses some existing code for calculating checksums, hashes and such;
# said code is subject to Zlib. For a list of Zlib-licensed files,
# grep the sources for the author's name: Wolfgang Ehrhardt.
#
# The AppStream metainfo file borrowed from FlatHub is subject to FTL.
License: LGPL-3.0-only AND Zlib AND FTL

Version: 10.9.0
Release: 1%{?dist}

URL:     https://peazip.github.io
Source0: https://github.com/peazip/PeaZip/releases/download/%{version}/peazip-%{version}.src.zip

# AppStream metainfo file borrowed from FlatHub:
# https://github.com/flathub/io.github.peazip.PeaZip/blob/8b9f7f2124cef5e095df907894d710630bc07710/io.github.peazip.PeaZip.appdata.xml
Source9: peazip.metainfo.xml

# Change file search paths to match packaging
Patch0:  %{name}--paths.patch

BuildRequires: fpc
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: lazarus-tools

# Set to 0 (or remove) to disable a particular build.
%global ws_gtk2 1
%global ws_gtk3 1
%global ws_qt5 1
%global ws_qt6 1

ExclusiveArch: %{fpc_arches}


%global desc %{expand:
PeaZip is fully-featured, user-friendly file archiver utility,
supporting over 180 archive formats. It also contains a powerful and complete
file manager for viewing, browsing and searching archive files.}

%description %{desc}

# -- Subpackages start

%package common
Summary: Data files for PeaZip
BuildArch: noarch

# All the files in common are subject to LGPL-3.0-only, except for
# /usr/share/peazip/share/peazip_help.pdf, which is licensed under GFDL.
License: LGPL-3.0-only AND GFDL-1.1-or-later

Requires: hicolor-icon-theme

# PeaZip tries to serve as a universal archive manipulation GUI.
# As such, it relies on external programs for handling some archive formats.
Recommends: %{_bindir}/7z
Recommends: %{_bindir}/arc
Recommends: %{_bindir}/brotli
Recommends: %{_bindir}/upx
Recommends: %{_bindir}/unrar-free
Recommends: %{_bindir}/zpaq
Recommends: %{_bindir}/zstd

# Can't recommend these since they're not in the official Fedora repos
# Recommends: %%{_bindir}/unace

%description common
This package provides common data files (icons, translations, etc.)
used by the PeaZip file archiving utility.

# -- Widgetset subpackages start

%if 0%{?ws_gtk2}
%package gtk2
Summary: File archiver utility (GTK2 version)
BuildRequires: lazarus-lcl-gtk2
RemovePathPostfixes: .gtk2

Conflicts: %{name}-gtk3
Conflicts: %{name}-qt5
Conflicts: %{name}-qt6

Requires: %{name}-common = %{version}-%{release}

%description gtk2 %{desc}

This package provides a GTK2 build of the program.
%endif

%if 0%{?ws_gtk3}
%package gtk3
Summary: File archiver utility (GTK3 version)
BuildRequires: lazarus-lcl-gtk3
RemovePathPostfixes: .gtk3

Conflicts: %{name}-gtk2
Conflicts: %{name}-qt5
Conflicts: %{name}-qt6

Requires: %{name}-common = %{version}-%{release}

%description gtk3 %{desc}

This package provides a GTK3 build of the program.
%endif

%if 0%{?ws_qt5}
%package qt5
Summary: File archiver utility (Qt version)
BuildRequires: lazarus-lcl-qt5
RemovePathPostfixes: .qt5

Conflicts: %{name}-gtk2
Conflicts: %{name}-gtk3
Conflicts: %{name}-qt6

Requires: %{name}-common = %{version}-%{release}

%description qt5 %{desc}

This package provides a Qt5 build of the program.
%endif

%if 0%{?ws_qt6}
%package qt6
Summary: File archiver utility (Qt6 version)
BuildRequires: lazarus-lcl-qt6
RemovePathPostfixes: .qt6

Conflicts: %{name}-gtk2
Conflicts: %{name}-gtk3
Conflicts: %{name}-qt5

Requires: %{name}-common = %{version}-%{release}

%description qt6 %{desc}

This package provides a Qt6 build of the program.
%endif

# -- Subpackages end

%global widgetsets %{expand: \\
%if 0%{?ws_gtk2}
	gtk2 \\
%endif
%if 0%{?ws_gtk3}
	gtk3 \\
%endif
%if 0%{?ws_qt5}
	qt5 \\
%endif
%if 0%{?ws_qt6}
	qt6 \\
%endif
}


%prep
%autosetup -p1 -n %{name}-%{version}.src

# Patch the project configuration files to enable debuginfo generation
for PROJECT in dev/project_pea.lpi dev/project_peach.lpi; do
	sed  \
		-e 's|<GenerateDebugInfo Value="False"[ ]*/>|<GenerateDebugInfo Value="True"/><DebugInfoType Value="dsDwarf2"/>|g'  \
		-e 's|<StripSymbols Value="True"[ ]*/>|<StripSymbols Value="False"/>|g'  \
		-i "${PROJECT}"
done

# Move around some files so it's easier to install them later
mv res/share/batch/freedesktop_integration/peazip.desktop ./
mv dev/copying_we.txt res/share/copying/

# Remove unused files
rm -rf res/share/batch/
rm -rf res/share/copying/third-parties/
rm -rf res/share/lang-wincontext/
find res/bin -name '*.txt' -delete
rm res/portable



%build
lazbuild \
	--add-package dev/metadarkstyle/metadarkstyle.lpk

for WIDGETSET in %{widgetsets}; do
	lazbuild \
		--widgetset="${WIDGETSET}" \
		--lazarusdir="%{_libdir}/lazarus" \
		-B dev/project_pea.lpi dev/project_peach.lpi

	mv ./dev/pea    "./pea.${WIDGETSET}"
	mv ./dev/peazip "./peazip.${WIDGETSET}"
done


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}%{_metainfodir}
for WIDGETSET in %{widgetsets}; do
	install -m 755 "./pea.${WIDGETSET}"    %{buildroot}%{_bindir}/
	install -m 755 "./peazip.${WIDGETSET}" %{buildroot}%{_bindir}/

	sed -e "s|WIDGETSET|${WIDGETSET}|g" \
		< "%{SOURCE9}" \
		> "%{buildroot}%{_metainfodir}/%{rtld_name}-${WIDGETSET}.metainfo.xml"
done

install -m 755 -d %{buildroot}%{_datadir}/
cp -a res %{buildroot}%{_datadir}/
mv %{buildroot}%{_datadir}/res %{buildroot}%{_datadir}/%{name}

# Create symlinks to external programs.
# This could be patched in the source code, but doing it like this is easier.
function link_binary() {
	SRC_NAME="$1"
	DST_DIR="$2"
	DST_NAME="$3"

	DST_DIR="%{buildroot}%{_datadir}/%{name}/bin/${DST_DIR}"
	mkdir -m 755 -p "${DST_DIR}"
	ln -srf "%{buildroot}%{_bindir}/${SRC_NAME}" "${DST_DIR}/${DST_NAME}"
}
link_binary 7z 7z 7z
link_binary arc arc arc
link_binary brotli brotli brotli
link_binary upx upx upx
link_binary unrar-free unrar unrar
link_binary zpaq zpaq zpaq
link_binary zstd zstd zstd

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/
ln -srf \
	%{buildroot}%{_datadir}/%{name}/share/icons/peazip.png \
	%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

install -m 755 -d %{buildroot}%{_datadir}/applications/
install -m 655 %{name}.desktop %{buildroot}%{_datadir}/applications/%{rtld_name}.desktop


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.peazip.PeaZip.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rtld_name}-*.metainfo.xml


%files gtk2
%{_bindir}/pea.gtk2
%{_bindir}/peazip.gtk2
%{_datadir}/applications/%{rtld_name}.desktop
%{_metainfodir}/%{rtld_name}-gtk2.metainfo.xml

%files gtk3
%{_bindir}/pea.gtk3
%{_bindir}/peazip.gtk3
%{_datadir}/applications/%{rtld_name}.desktop
%{_metainfodir}/%{rtld_name}-gtk3.metainfo.xml

%files qt5
%{_bindir}/pea.qt5
%{_bindir}/peazip.qt5
%{_datadir}/applications/%{rtld_name}.desktop
%{_metainfodir}/%{rtld_name}-qt5.metainfo.xml

%files qt6
%{_bindir}/pea.qt6
%{_bindir}/peazip.qt6
%{_datadir}/applications/%{rtld_name}.desktop
%{_metainfodir}/%{rtld_name}-qt6.metainfo.xml

%files common
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png


%changelog
* Tue Mar 03 2026 Artur Frenszek-Iwicki <fedora@svgames.pl> - 10.9.0-1
- Initial packaging

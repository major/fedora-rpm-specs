Name:           NiaAML-GUI
Version:        0.4.3
Release:        %autorelease
Summary:        GUI for NiaAML Python package

# SPDX
License:        MIT
URL:            https://github.com/firefly-cpp/NiaAML-GUI
# Also distributed via PyPI (https://pypi.org/project/niaaml-gui/) but without
# tests and other auxiliary files.
Source:         %{url}/archive/%{version}/NiaAML-GUI-%{version}.tar.gz

BuildSystem:    pyproject
BuildOption(install): --no-assert-license niaaml_gui

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
 
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# pyproject.toml: [tool.poetry.dev-dependencies]
BuildRequires:  python3dist(pytest)

Requires:       hicolor-icon-theme

%global app_id io.github.firefly-cpp.niaaml_gui

%global common_description %{expand:
This is a basic graphical user interface intended for users of the NiaAML
Python package.}

%description %{common_description}


%prep -a
# Do not upper-bound the version of Python!
# https://github.com/firefly-cpp/NiaAML-GUI/commit/d0084e6d2f05c6af848678db731c41a49c1a2a22#commitcomment-146060179
sed --regexp-extended --in-place \
    's/^(python[[:blank:]]*=[[:blank:]]*"[^"]+),[^"]+"/\1"/' pyproject.toml


%install -a
desktop-file-install --dir='%{buildroot}%{_datadir}/applications' \
    AppData/%{app_id}.desktop
install -D --target='%{buildroot}%{_metainfodir}' \
    --preserve-timestamps --mode=0644 AppData/%{app_id}.metainfo.xml
install -D --target='%{buildroot}%{_datadir}/icons/hicolor/256x256/apps' \
    --preserve-timestamps --mode=0644 AppData/niaaml-gui.png


%check -a
appstream-util validate-relax --nonet \
    '%{buildroot}%{_metainfodir}/%{app_id}.metainfo.xml'

%pytest


%files -f %{pyproject_files}
%license LICENSE
%doc CITATION.cff
%doc README.md

%{_bindir}/NiaAML-GUI
# There is no need for a man page, since this is a pure GUI application with no
# useful command-line options.

%{_datadir}/applications/%{app_id}.desktop
%{_metainfodir}/%{app_id}.metainfo.xml
%{_datadir}/icons/hicolor/256x256/apps/niaaml-gui.png


%changelog
%autochangelog

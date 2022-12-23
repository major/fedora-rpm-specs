%bcond_with         clatexmath

%global forgeurl    https://github.com/blackhole89/notekit/

%global uuid        com.github.blackhole89.notekit

Name:       notekit
Version:    0.2.0
Release:    %autorelease
Summary:    Hierarchical markdown notetaking application with tablet support

#global commit      66a31147f83b93542f0c53f0eda65b1576bc4756
%forgemeta

# The app is under the GPLv3+ license while the fonts are under the Charter
# license.
License:    GPLv3+ and Charter
URL:        %{forgeurl}
Source0:    %{forgesource}

BuildRequires:  meson
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
%if %{with clatexmath}
BuildRequires:  cLaTeXMath-devel
%endif
BuildRequires:  gtkmm30-devel
BuildRequires:  gtksourceviewmm3-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme

%description
This program is a structured notetaking application based on GTK+ 3.
Write your notes in instantly-formatted Markdown, organise them in a
tree of folders that can be instantly navigated from within the program,
and add hand-drawn notes by mouse, touchscreen or digitiser.

%prep
%forgeautosetup

%build
%meson %{!?with_clatexmath:-Dclatexmath=false}

%meson_build

%install
%meson_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml

%files
%doc README.md
%license LICENSE "data/fonts/Charter license.txt"
%{_bindir}/%{name}
%{_metainfodir}/%{uuid}.metainfo.xml
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/icons/hicolor/*/apps/%{uuid}.*
%{_datadir}/%{name}/

%changelog
%autochangelog

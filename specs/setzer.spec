%global forgeurl    https://github.com/cvfosammmm/Setzer
%global uuid        org.cvfosammmm.Setzer

Name:           setzer
Version:        66
Release:        %autorelease
Summary:        LaTeX editor written in Python with Gtk

%forgemeta

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://www.cvfosammmm.org/setzer/
Source0:        %{forgesource}
BuildArch:      noarch


BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel

BuildRequires:  gtk4-devel
BuildRequires:  gtksourceview5-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libportal-devel
BuildRequires:  gspell-devel
BuildRequires:  pango-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  python3-bibtexparser
BuildRequires:  python3-cairo
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-pexpect
BuildRequires:  python3-willow
BuildRequires:  webkitgtk6.0
Requires:       gtk4
Requires:       gtksourceview5
Requires:       libadwaita
Requires:       libportal
Requires:       gspell
Requires:       hicolor-icon-theme
Requires:       pango
Requires:       poppler-glib
Requires:       python3-bibtexparser
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-numpy
Requires:       python3-pexpect
Requires:       python3-willow
Requires:       webkitgtk6.0

Requires:       texlive
Requires:       texlive-synctex

# LaTeX engines
Requires:       texlive-xetex
Recommends:     latexmk
Recommends:     texlive-pdftex
Recommends:     texlive-luatex

%description
Write LaTeX documents with an easy to use yet full-featured editor.

- Buttons and shortcuts for many LaTeX elements and special characters.
- Document creation wizard.
- Dark mode.
- Helpful error messages in the build log.
- Looks great on the Gnome desktop.
- Good screen to content ratio.
- Arguably the best .pdf viewer of any LaTeX editor.

%prep
%forgeautosetup -p1

%build
# Removing unnecessary shebangs
find ./setzer -name "*.py" -type f -exec sed -i '1d' {} \;
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/Setzer/
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{uuid}.svg
%{_datadir}/mime/packages/%{uuid}.mime.xml
%{_metainfodir}/%{uuid}.metainfo.xml
%{_mandir}/man1/%{name}.1.*
%{python3_sitelib}/%{name}/


%changelog
%autochangelog

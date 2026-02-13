%global forgeurl https://github.com/phase1geo/Minder
%global uuid com.github.phase1geo.%{name}

Name:           minder
Version:        2.0.6
Release:        %autorelease
Summary:        Mind-mapping application
%forgemeta

License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source:         %{url}/archive/%{version}/Minder-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libmarkdown-devel
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite-7) >= 7.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       hicolor-icon-theme

%description
Use the power of mind-mapping to make your ideas come to life.

  * Quickly create visual mind-maps using the keyboard and automatic layout.
  * Choose from many tree layout choices.
  * Support for Markdown formatting.
  * Support for insertion of Unicode characters.
  * Add notes, tasks, and images to your nodes.
  * Add node-to-node connections with optional text and notes.
  * Stylize nodes, callouts, links and connections to add more meaning and
    improve readability.
  * Save and reuse style settings within and across open mindmaps.
  * Add stickers, tags, callouts and node groups to call out and visibly
    organize information.
  * Quick search of node and connection titles and notes, including filtering
    options.
  * Zoom in or enable focus mode to focus on certain ideas or zoom out to see
    the bigger picture.
  * Enter focus mode to better view and understand portions of the map.
  * Quickly brainstorm ideas with the brainstorming interface and worry about
    where those ideas belong in the mind map later.
  * Unlimited undo/redo of any change.
  * Automatically and manual saving supported.
  * Colorized node branches.
  * Open multiple mindmaps with the use of tabs.
  * Built-in and customizable theming.
  * Gorgeous animations.
  * Import from OPML, FreeMind, Freeplane, PlainText/Markdown (formatted),
    Mermaid (mindmap), Outliner, Portable Minder, filesystem and XMind formats.
  * Export to CSV, FreeMind, Freeplane, JPEG, BMP, SVG, WebP, Markdown, Mermaid,
    Mermaid Mindmap, OPML, Org-Mode, Outliner, PDF, PNG, PlainText, filesystem,
    XMind and yEd formats.
  * Printer support.


%prep
%forgeautosetup -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{uuid}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{uuid}.lang
%license LICENSE COPYING
%doc README.md AUTHORS
%{_bindir}/%{uuid}
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/%{name}/gtksourceview-4/language-specs/*.lang
%{_datadir}/%{name}/gtksourceview-4/styles/*.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.xml


%changelog
%autochangelog

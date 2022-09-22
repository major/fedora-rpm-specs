%global uuid com.github.phase1geo.%{name}

Name:           minder
Version:        1.14.0
Release:        3%{?dist}
Summary:        Mind-mapping application

License:        GPLv3+
URL:            https://github.com/phase1geo/Minder
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

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
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)

Requires:       hicolor-icon-theme

%description
Use the power of mind-mapping to make your ideas come to life.

  * Quickly create visual mind-maps using the keyboard and automatic layout.
  * Choose from many tree layout choices.
  * Support for Markdown formatting.
  * Add notes, tasks and images to your nodes.
  * Add node-to-node connections with optional text and notes.
  * Stylize nodes, links and connections to add more meaning and improve
    readability.
  * Add stickers and node groups to call out and visibly organize information.
  * Quick search of node and connection titles and notes, including filtering
    options.
  * Zoom in or enable focus mode to focus on certain ideas or zoom out to see
    the bigger picture.
  * Enter focus mode to better view and understand portions of the map.
  * Unlimited undo/redo of any change.
  * Automatically saves in the background.
  * Colorized node branches.
  * Open multiple mindmaps with the use of tabs.
  * Built-in and customizable theming.
  * Gorgeous animations.
  * Import from OPML, FreeMind, Freeplane, PlainText (formatted), Outliner,
    Portable Minder and XMind formats.
  * Export to CSV, FreeMind, Freeplane, JPEG, BMP, SVG, Markdown, Mermaid,
    OPML, Org-Mode, Outliner, PDF, PNG, Portable Minder, PlainText, XMind and
    yEd formats.
  * Printer support.


%prep
%autosetup -n Minder-%{version} -p1


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
%{_datadir}/gtksourceview-3.0/styles/*.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/mime/packages/*.xml
%{_metainfodir}/*.xml


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 17 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1.14.0-1
- chore(update): 1.14.0

* Fri Aug 13 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.13.1-1
- build(update): 1.13.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 15 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.12.5-1
- build(update): 1.12.5

* Thu Jun 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.12.4-1
- build(update): 1.12.4

* Sat May 22 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.12.3-1
- build(update): 1.12.3

* Fri Apr 23 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.12.2-1
- build(update): 1.12.2

* Fri Apr 16 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.12.1-1
- build(update): 1.12.1

* Fri Feb 19 2021 Fabio Valentini <decathorpe@gmail.com> - 1.12.0-2
- Rebuilt for granite 6 soname bump.

* Fri Feb 12 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 1.12.0-1
- build(update): 1.12.0

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11.2-1
- build(update): 1.11.2

* Fri Sep 25 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11.1-1
- Update to 1.11.1

* Tue Sep 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.11.0-1
- Update to 1.11.0

* Thu Aug 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.10.0-1
- Update to 1.10.0

* Sat Aug 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.2-1
- Update to 1.9.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 15 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.1-1
- Update to 1.9.1

* Wed Jul 01 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.9.0-1
- Update to 1.9.0

* Sun May 17 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.8.0-1
- Update to 1.8.0

* Tue Apr 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.3-1
- Update to 1.7.3

* Fri Mar 27 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.2-1
- Update to 1.7.2

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.1-1
- Update to 1.7.1

* Sat Mar 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.6.0-1
- Update to 1.6.0
- Add new BR

* Sun Nov 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.1-1
- Update to 1.5.1

* Sun Sep 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Thu Jul 25 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Sat Jun 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Wed May 29 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Tue Apr 23 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.2.1-1
- Initial package

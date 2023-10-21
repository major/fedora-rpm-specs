%global appid org.gnome.gitlab.somas.Apostrophe
%global libhandy_version 1.6

%global forgeurl https://gitlab.gnome.org/World/%{name}
%global tag v%{version}

Name:           apostrophe
Version:        2.6.3
%forgemeta
Release:        %autorelease
Epoch:          1
Summary:        Distraction free Markdown editor for GNU/Linux made with GTK+

# Entire source code is GPL-3.0-or-later except:
#   * GPL-2.0-only:     help/stump/
#   * LGPL-2.1-only:    apostrophe/plugins/bibtex/gi_composites.py
#   * MIT:              apostrophe/latex_to_PNG.py
#                       apostrophe/plugins/bibtex/fuzzywuzzy/
License:        GPL-3.0-or-later and GPL-2.0-only and LGPL-2.1-only and MIT
URL:            https://apps.gnome.org/Apostrophe
Source0:        %{forgesource}
# https://fedoraproject.org/wiki/Changes/Remove_webkit2gtk-4.0_API_Version
Patch0:         webkit2gtk4.1.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson >= 0.50.0
BuildRequires:  python3-devel >= 3.8
BuildRequires:  python3-setuptools
BuildRequires:  sassc

BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= %{libhandy_version}

Requires:       gspell
Requires:       hicolor-icon-theme
Requires:       libhandy1 >= %{libhandy_version}
Requires:       mozilla-fira-mono-fonts
Requires:       mozilla-fira-sans-fonts
Requires:       python3-cairo
Requires:       python3-chardet
Requires:       python3-enchant
Requires:       python3-Levenshtein
Requires:       python3-pypandoc
Requires:       python3-regex
Requires:       webkit2gtk4.1

%description
Apostrophe is a GTK+ based distraction free Markdown editor, mainly developed by
Wolf Vollprecht and Manuel Genovés. It uses pandoc as backend for markdown
parsing and offers a very clean and sleek user interface.


%prep
%forgeautosetup -p1

# Bug 1953395 - Apostrophe can't export to HTML.
sed -i "s|/app/share/fonts/FiraSans-Regular.ttf|%{_datadir}/fonts/mozilla-fira/FiraSans-Regular.otf|" \
    data/media/css/web/base.css
sed -i "s|/app/share/fonts/FiraMono-Regular.ttf|%{_datadir}/fonts/mozilla-fira/FiraMono-Regular.otf|" \
    data/media/css/web/base.css

# W: hidden-file-or-dir
rm apostrophe/.pylintrc


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appid}.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS tests/markdown_test.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.metainfo.xml
%{python3_sitelib}/%{name}/


%changelog
%autochangelog

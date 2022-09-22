%global appname org.gnome.gitlab.somas.Apostrophe

Name:           apostrophe
Version:        2.6.3
Release:        3%{?dist}
Epoch:          1
Summary:        Distraction free Markdown editor for GNU/Linux made with GTK+

# Entire source code is GPLv3+ except:
#   * GPLv2:    help/stump/
#   * LGPLv2.1: apostrophe/plugins/bibtex/gi_composites.py
#   * MIT:      apostrophe/latex_to_PNG.py
#               apostrophe/plugins/bibtex/fuzzywuzzy/
License:        GPLv3+ and GPLv2 and LGPLv2 and MIT
URL:            https://gitlab.gnome.org/World/apostrophe
Source0:        %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
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
BuildRequires:  pkgconfig(libhandy-1) >= 1.6

Requires:       gspell
Requires:       hicolor-icon-theme
Requires:       libhandy1 >= 1.6
Requires:       mozilla-fira-mono-fonts
Requires:       mozilla-fira-sans-fonts
Requires:       python3-cairo
Requires:       python3-chardet
Requires:       python3-enchant
Requires:       python3-Levenshtein
Requires:       python3-pypandoc
Requires:       python3-regex

%description
Apostrophe is a GTK+ based distraction free Markdown editor, mainly developed by
Wolf Vollprecht and Manuel Genovés. It uses pandoc as backend for markdown
parsing and offers a very clean and sleek user interface.


%prep
%autosetup -n %{name}-v%{version} -p1

# Bug 1953395 - Apostrophe can't export to HTML.
sed -i 's|/app/share/fonts/FiraSans-Regular.ttf|/usr/share/fonts/mozilla-fira/FiraSans-Regular.otf|' \
    data/media/css/web/base.css
sed -i 's|/app/share/fonts/FiraMono-Regular.ttf|/usr/share/fonts/mozilla-fira/FiraMono-Regular.otf|' \
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
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{appname}.desktop


%files -f %{name}.lang
%license LICENSE
%doc README.md AUTHORS tests/markdown_test.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
%{python3_sitelib}/%{name}/


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1:2.6.3-2
- Rebuilt for Python 3.11

* Fri Apr 29 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1:2.6.3-1
- chore(update): 2.6.3

* Thu Mar 31 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1:2.6.2-1
- chore(update): 2.6.2

* Sun Mar 27 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 1:2.6.1-2
- build: Bump epoch due rh#2068897

* Sun Mar 27 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6.1-1
- chore(update): 2.6.1

* Sat Mar 19 2022 Artem Polishchuk <ego.cordatus@gmail.com> - 2.6-1
- chore(update): 2.6

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 27 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5-2
- fix(add dep): python3-chardet | rh#2008184

* Mon Aug 30 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.5-1
- build(update): 2.5

* Wed Jul 28 2021 Artem Polishchuk <ego.cordatus@gmail.com>
- fix: LGPLv2.1 to LGPLv2
- chore: Update URL

* Wed Jul 28 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4-6
- fix: gspell is hardep | rh#1986986

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.4-4
- Rebuilt for Python 3.10

* Tue Apr 27 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4-3
- fix: Typo

* Mon Apr 26 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4-2
- fix: RH#1953395

* Wed Mar 10 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4-1
- build(update): 2.4

* Wed Mar 03 2021 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3-1
- build(update): 2.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0.3-3
- Rebuilt for Python 3.9

* Fri May 08 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.3-2
- Add patch for compatibility with old pandoc | Thanks to @suve

* Mon May 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.3-1
- Update to 2.2.0.3

* Thu Apr 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.2-2
- Add few recommended deps

* Mon Apr 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.2-1
- Update to 2.2.0.2

* Mon Apr 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0.1-3
- Update to 2.2.0.1
- Ported to Meson and renamed to Apostrophe now

* Tue Jul 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.5-4
- Initial package

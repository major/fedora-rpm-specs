%global forgeurl    https://github.com/cvfosammmm/Setzer
%global uuid        org.cvfosammmm.Setzer

Name:           setzer
Version:        0.4.8
Release:        2%{?dist}
Summary:        LaTeX editor written in Python with Gtk

%forgemeta

License:        GPLv3+
URL:            https://www.cvfosammmm.org/setzer/
Source0:        %{forgesource}
BuildArch:      noarch


BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel

BuildRequires:  gtk3-devel
BuildRequires:  gtksourceview4-devel
BuildRequires:  gspell-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  python3-cairo
BuildRequires:  python3-pdfminer
BuildRequires:  python3-pyxdg
BuildRequires:  python3-gobject-devel
BuildRequires:  webkit2gtk3
Requires:       gtk3
Requires:       gtksourceview4
Requires:       gspell
Requires:       hicolor-icon-theme
Requires:       poppler-glib
Requires:       python3-cairo
Requires:       python3-pdfminer
Requires:       python3-pyxdg
Requires:       python3-gobject
Requires:       webkit2gtk3
Requires:       xdg-utils

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
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uuid}.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/Setzer/
%{_datadir}/applications/%{uuid}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{uuid}.svg
%{_datadir}/mime/packages/%{uuid}.mime.xml
%{_metainfodir}/%{uuid}.appdata.xml
%{_mandir}/man1/%{name}.1.*
%{python3_sitelib}/%{name}/


%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 29 2022 Lyes Saadi <fedora@lyes.eu> - 0.4.8-1
- Updating to 0.4.8 (fix #2112453)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.4.7-2
- Rebuilt for Python 3.11

* Sat Mar 26 2022 Lyes Saadi <fedora@lyes.eu> - 0.4.7-1
- Updating to 0.4.7 (fix #2068713)

* Tue Mar 08 2022 Lyes Saadi <fedora@lyes.eu> - 0.4.6-1
- Updating to 0.4.6 (fix #2061920)

* Wed Mar 02 2022 Lyes Saadi <fedora@lyes.eu> - 0.4.5-1
- Updating to 0.4.5 (fix #2058437)

* Mon Feb 21 2022 Lyes Saadi <fedora@lyes.eu> - 0.4.4-1
- Updating to 0.4.4 (fix #2055916)

* Sun Feb 13 2022 Lyes Saadi <fedora@lyes.eu> - 0.4.3-1
- Updating to 0.4.3 (fix #2053320 #2036772)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Lyes Saadi <fedora@lyes.eu> - 0.4.2-1
- Updating to 0.4.2 (fix #2025308)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Lyes Saadi <fedora@lyes.eu> - 0.4.1-1
- Updating to 0.4.1
- Fix #1918066

* Sun Jan 17 2021 Lyes Saadi <fedora@lyes.eu> - 0.4.0-1
- Updating to 0.4.0
- Fix #1917066

* Sun Jan 03 2021 Lyes Saadi <fedora@lyes.eu> - 0.3.9-2
- Adding pycairo and PyPDF2 dependencies

* Sun Jan 03 2021 Lyes Saadi <fedora@lyes.eu> - 0.3.9-1
- Updating to 0.3.9

* Mon Dec 14 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.8-1
- Updating to 0.3.8

* Sun Nov 29 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.7-1
- Updating to 0.3.7

* Mon Nov 09 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.6-1
- Updating to 0.3.6

* Thu Oct 29 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.5-1
- Updating to 0.3.5
- Fix #1888889
- Fix #1891239

* Fri Oct 16 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.4-1
- Updating to 0.3.4

* Wed Oct 07 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.3-1
- Updating to 0.3.3

* Thu Sep 10 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.2-1
- Updating to 0.3.2

* Tue Sep 01 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.1-1
- Updating to 0.3.1

* Thu Aug 20 2020 Lyes Saadi <fedora@lyes.eu> - 0.3.0-1
- Updating to 0.3.0

* Thu Aug 13 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.9-1
- Updating to 0.2.9

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 26 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.8-3
- Fix #1851601

* Fri Jun 26 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.8-2
- Correcting License from GPLv3 -> GPLv3+

* Sat May 30 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.8-1
- Updating to 0.2.8

* Tue May 19 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.6-1
- Updating to 0.2.6

* Tue May 05 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.5-1
- Updating to 0.2.5

* Sat Apr 18 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.3-3
- Removing shebangs and changing poppler-glib dependency

* Sat Apr 18 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.3-2
- Adding synctex dependency

* Sat Apr 18 2020 Lyes Saadi <fedora@lyes.eu> - 0.2.3-1
- Initial package

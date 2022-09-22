%global uuid    com.github.fabiocolacio.%{name}
%global vergit  2020.04.04

Name:           marker
Version:        0.0.%{vergit}
Release:        7%{?dist}
Summary:        GTK 3 markdown editor

# The entire source code is GPLv3+ except:
#
# Apache License (v2.0)
# ------------------------------------
# data/scripts/mathjax/
#
# Creative Commons Attribution-ShareAlike Public License (v3.0)
# ----------------------------------------------------------------------------
# help/C/legal.xml
#
# Creative Commons Attribution-ShareAlike Public License (v4.0)
# ----------------------------------------------------------------------------
# data/scripts/highlight/styles/
#
# Creative Commons CC0 Public License (v1.0)
# ---------------------------------------------------------
# data/scripts/highlight/styles/hopscotch.css
#
# zlib/libpng license
# ----------------------------------
# src/scidown/src/charter/src/tinyexpr/README.md
#
# BSD 3-clause "New" or "Revised" License
# ---------------------------------------
# data/scripts/highlight/LICENSE
#
# Creative Commons CC0 Public License (v5)
# ----------------------------------------
# data/scripts/mathjax/fonts/HTML-CSS/TeX/png/SansSerif/Regular/336/0035.png
#
# Expat License
# -------------
# data/scripts/highlight/styles/dracula.css
# data/scripts/mathjax/extensions/a11y/wgxpath.install.js
#
# ISC License
# -----------
# src/scidown/LICENSE
#
# SIL Open Font License
# ---------------------
# data/scripts/mathjax/fonts/HTML-CSS/STIX-Web/
#
# SIL Open Font License (v1.1)
# ----------------------------
# data/scripts/katex/fonts/
# data/scripts/mathjax/fonts/HTML-CSS/Asana-Math/
# data/scripts/mathjax/fonts/HTML-CSS/Neo-Euler/
# data/scripts/mathjax/fonts/HTML-CSS/STIX-Web/
# data/scripts/mathjax/fonts/HTML-CSS/TeX/
#
License:        GPLv3+ and GPLv2 and LGPLv3+ and CC-BY-SA and ISC and BSD and ASL 2.0 and MIT and CC0 and OFL and zlib
URL:            https://github.com/fabiocolacio/Marker
Source0:        %{url}/releases/download/%{vergit}/%{name}.zip#/%{name}-%{version}.zip

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       %{name}-data = %{version}-%{release}
Requires:       hicolor-icon-theme

Provides:       bundled(highlight-js) = 9.12.0
Provides:       bundled(katex)
Provides:       bundled(mathjax) = 2.7.4
Provides:       bundled(scidown) = 0.1.0~a7b7f06

# Fonts
Provides:       bundled(asana-math-fonts)
Provides:       bundled(gyre-pagella-fonts)
Provides:       bundled(gyre-termes-fonts)
Provides:       bundled(katex-fonts)
Provides:       bundled(latin-modern-fonts)
Provides:       bundled(neo-euler-fonts)
Provides:       bundled(stix-web-fonts)
Provides:       bundled(tex-fonts)

%description
Marker is a markdown editor for Linux made with Gtk+-3.0.


%package        data
Summary:        Data files for %{name}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}

%description    data
Data files for %{name}.


%prep
%autosetup -n %{name} -p1


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}
%find_lang Marker --with-gnome
rm %{buildroot}%{_datadir}/%{uuid}/icons/hicolor/generate.sh


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang -f Marker.lang
%license LICENSE.md
%doc README.md CONTRIBUTING.md example.md
%{_bindir}/%{name}

# E: arch-dependent-file-in-usr-share
# libscroll-extension.so
# * https://github.com/fabiocolacio/Marker/issues/293
%{_datadir}/%{uuid}/extensions/

%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml

%files data
%{_datadir}/%{uuid}/
%exclude %{_datadir}/%{uuid}/extensions/


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.04.04-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.04.04-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.04.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.04.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep  2 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.2020.04.04-3
- Remove old LTO macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2020.04.04-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.0.2020.04.04-1
- Update to 2020.04.04

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2019.11.06-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 04 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2019.11.06-5
- Switch to release tarballs
- Provides all bundled components

* Tue Dec 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2019.11.06-1.20191210git49a7e14
- Update to 2019.11.06

* Tue Apr 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2018.07.03-1.20190430gitc0f8c7e
- Update to latest snapshot

* Fri Apr 05 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 2018.07.03-3.20190227gited56a04
- Initial package

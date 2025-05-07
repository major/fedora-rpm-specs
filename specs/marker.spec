%global uuid    com.github.fabiocolacio.%{name}

# Git submodules
#   * scidown
%global submodule1              scidown
%global submodule1_commit       a7b7f063de4f272ef0ec12d00b98470888e8cb32
%global submodule1_shortcommit  %(c=%{submodule1_commit}; echo ${c:0:7})
#   * charter
%global submodule2              charter
%global submodule2_commit       a25dee1214ea9ba5882325066555cb813efbb489
%global submodule2_shortcommit  %(c=%{submodule2_commit}; echo ${c:0:7})
#   * tinyexpr
%global submodule3              tinyexpr
%global submodule3_commit       9476568b69de4c384903f1d5f255907b92592f45
%global submodule3_shortcommit  %(c=%{submodule3_commit}; echo ${c:0:7})

Name:           marker
Version:        2023.05.02
Release:        %autorelease
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
License:        GPL-3.0-or-later AND GPL-2.0-only AND LGPL-3.0-or-later AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC0-1.0 AND ISC AND BSD-3-Clause AND Apache-2.0 AND MIT AND CC0-1.0 AND OFL-1.1 AND Zlib
URL:            https://github.com/fabiocolacio/Marker
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/Mandarancio/%{submodule1}/archive/%{submodule1_commit}/%{submodule1}-%{submodule1_shortcommit}.tar.gz
Source2:        https://github.com/Mandarancio/%{submodule2}/archive/%{submodule2_commit}/%{submodule2}-%{submodule2_shortcommit}.tar.gz
Source3:        https://github.com/codeplea/%{submodule3}/archive/%{submodule3_commit}/%{submodule3}-%{submodule3_shortcommit}.tar.gz
# https://github.com/fabiocolacio/Marker/pull/427
Patch:          0001-fix-incompatible-pointer-type.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)

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
%autosetup -n Marker-%{version} -p1
%autosetup -n Marker-%{version} -D -T -a1 -N
%autosetup -n Marker-%{version} -D -T -a2 -N
%autosetup -n Marker-%{version} -D -T -a3 -N

cp %{submodule1}-%{submodule1_commit}/LICENSE LICENSE.%{submodule1}
cp %{submodule2}-%{submodule2_commit}/LICENSE LICENSE.%{submodule2}
cp %{submodule3}-%{submodule3_commit}/LICENSE LICENSE.%{submodule3}

mv %{submodule1}-%{submodule1_commit}/* src/%{submodule1}/
mv %{submodule2}-%{submodule2_commit}/* src/%{submodule1}/src/%{submodule2}/
mv %{submodule3}-%{submodule3_commit}/* src/%{submodule1}/src/%{submodule2}/src/%{submodule3}/


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
%license LICENSE.md LICENSE.%{submodule1} LICENSE.%{submodule2} LICENSE.%{submodule3}
%doc README.md CONTRIBUTING.md example.md
%{_bindir}/%{name}
# FIXME
# Still incorrect place for libraries. Need to report upstream. Continuation of
# https://github.com/fabiocolacio/Marker/issues/293
%dir %{_prefix}/lib/Marker.extensions
%{_prefix}/lib/Marker.extensions/*.so

%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml

%files data
%{_datadir}/%{uuid}/


%changelog
%autochangelog

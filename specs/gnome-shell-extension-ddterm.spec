Name:           gnome-shell-extension-ddterm
Version:        64.0.0
Release:        %autorelease
Summary:        Drop-down terminal extension for GNOME Shell with tabs
URL:            https://github.com/ddterm/gnome-shell-extension-ddterm

# Licensing breakdown, per upstream REUSE.toml / SPDX-License-Identifier headers:
# - GPL-3.0-or-later: ddterm's own JS sources (extension.js, prefs.js, ddterm/**),
#   data files (desktop entry, D-Bus service/interface, gschema) and CHANGELOG.md
# - CC0-1.0: icons, AUTHORS, build config and other trivial files
# - MIT: subprojects/gjs-typelib-installer (bundled as Source1)
# Not included: GPL-2.0-or-later and MPL-2.0, both used only by developer/CI
# tooling under tools/, eslint.config.mjs and tests/, none of which is installed
License:        GPL-3.0-or-later AND CC0-1.0 AND MIT

Source0:        %{url}/archive/v%{version}/ddterm-%{version}.tar.gz
# meson subproject pulled in via subprojects/gjs-typelib-installer.wrap;
# bundled as a separate source so the build doesn't need network access
%global gjs_ti_commit e6e5802db1578dea38494ffc4b63580138ccf749
%global gjs_ti_shortcommit %{sub %{gjs_ti_commit} 1 7}
%global gjs_ti_commitdate 20260916
Source1:        https://github.com/ddterm/gjs-typelib-installer/archive/%{gjs_ti_commit}/gjs-typelib-installer-%{gjs_ti_shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  glib2
BuildRequires:  meson
BuildRequires:  mutter-common
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
BuildRequires:  wl-clipboard
BuildRequires:  xsltproc

# Runtime+Buildtime deps
BuildRequires:  (gnome-shell >= 48 with gnome-shell < 52~~)
Requires:       (gnome-shell >= 48 with gnome-shell < 52~~)
BuildRequires:  /usr/bin/gjs
Requires:       /usr/bin/gjs

# typelibs the ddterm app needs at runtime (see meson.build's gjs-typelib-installer
# subproject call); also BuildRequires'd so gjs-typelib-installer (see Source1)
# doesn't try to fetch them itself during %%check
BuildRequires:  gtk3
BuildRequires:  libhandy
BuildRequires:  pango
BuildRequires:  vte291
Requires:       gtk3
Requires:       libhandy
Requires:       pango
Requires:       vte291

Recommends:     gnome-extensions-app
Provides:       ddterm = %{version}-%{release}
# gjs-typelib-installer has no upstream releases/versions, so use a git snapshot
Provides:       bundled(gjs-typelib-installer) = 0~%{gjs_ti_commitdate}git%{gjs_ti_shortcommit}

%global uuid    ddterm@amezin.github.com

%description
ddterm is a drop-down terminal extension for GNOME Shell,
inspired by Guake and drop-down-terminal-x.

Distinguishing features:

- Runs on Wayland natively
- Can be controlled from the command line
- Terminal window can be resized by dragging the border with mouse
- All tabs are restored automatically after restart
- Preferences window with a lot of different settings


%prep
%autosetup -p1 -a1
grep -qF "revision = %{gjs_ti_commit}" subprojects/gjs-typelib-installer.wrap || \
    { echo "error: %%gjs_ti_commit out of sync with subprojects/gjs-typelib-installer.wrap" >&2; exit 1; }
mv gjs-typelib-installer-%{gjs_ti_commit} subprojects/gjs-typelib-installer
tr -d ' \n' < meson.build | grep -qF "'typelibs':['Gtk-3.0','Gdk-3.0','Pango-1.0','Vte-2.91','Handy-1',]," || \
    { echo "error: meson.build's gjs-typelib-installer 'typelibs' list changed; update the gtk3/pango/vte291/libhandy Requires accordingly" >&2; exit 1; }


%conf
%meson -Dtests_x11=disabled


%build
%meson_build


%install
%meson_install
ln -s com.github.amezin.ddterm %{buildroot}%{_bindir}/ddterm

# A lang-aware recursive filelist (%%find_lang not useful here)
extdir=%{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
echo "%%dir ${extdir#%{buildroot}}" > extension-files.list
for f in "$extdir"/*; do
    rel=${f#%{buildroot}}
    if [ "$(basename "$f")" = locale ]; then
        echo "%%dir $rel" >> extension-files.list
        for langdir in "$f"/*; do
            lang=$(basename "$langdir")
            lang=${lang%%_*}
            echo "%%lang($lang) ${langdir#%{buildroot}}" >> extension-files.list
        done
    else
        echo "$rel" >> extension-files.list
    fi
done


%check
%meson_test


%files -f extension-files.list
%license LICENSE
%license LICENSES/CC0-1.0.txt
%license LICENSES/MIT.txt
%doc README.md
%doc CHANGELOG.md
%{_bindir}/com.github.amezin.ddterm
%{_bindir}/ddterm
%{_datadir}/applications/com.github.amezin.ddterm.desktop
%{_datadir}/dbus-1/services/com.github.amezin.ddterm.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.ddterm.gschema.xml


%changelog
%autochangelog

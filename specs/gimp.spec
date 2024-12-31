#### options:
# Use the following --with/--without <option> switches to control how the
# package will be built:

# is_default_version: This is the default GIMP version in a Fedora release
# label_overlay: Put version label in app icons
%if ! 0%{?fedora} || 0%{?fedora} >= 41
%bcond is_default_version 1
%bcond label_overlay 0
%else
%bcond is_default_version 0
%bcond label_overlay 1
%endif

# libunwind support (only available on some architectures)
%if ! 0%{?fedora}%{?rhel} || 0%{?fedora} >= 40 || 0%{?rhel} >= 11
%global unwind_arches %{arm} aarch64 hppa ia64 mips ppc %{power64} %{ix86} x86_64 riscv64
%else
%global unwind_arches %{arm} aarch64 hppa ia64 mips ppc %{power64} %{ix86} x86_64
%endif

%ifarch %unwind_arches
%bcond libunwind 1
%else
%bcond libunwind 0
%endif

%bcond tests 1

# When building in Koji or mock, networking isn’t available.
%bcond skip_networking_tests 1
# Skip known problematic tests
%bcond skip_problematic_tests 1
# Some tests fail under normal user environments, don’t skip them by default.
%bcond skip_user_tests 0

# The lists of tests to skip should not have leading or trailing white space,
# this breaks the logic in %%check.

# tests known to fail if networking isn’t available
%global skip_tests_networking gimp:desktop / appdata_file

# tests known to fail for being problematic
%global skip_tests_problematic gimp:app / save-and-export

# tests known to fail in a normal user environment
%global skip_tests_user gimp:app / save-and-export\
gimp:app / single-window-mode\
gimp:app / ui

# luajit isn’t available on all arches
%global plain_lua_arches riscv64 ppc64le s390x

%global prerelease 1

Summary:        GNU Image Manipulation Program
Name:           gimp
Epoch:          2
Version:        3.0.0~RC2
Release:        %autorelease
# https://bugzilla.redhat.com/show_bug.cgi?id=2318369
ExcludeArch:    s390x

# Compute some version related macros.

# In the case of a snapshot version (e.g. "Version: 2.99.19^20240814git256e0ca5a0") or a pre-release
# (e.g. "Version: 3.0.0~RC1"), this computes the "plain" version (as defined in upstream sources),
# %%snapshot and %%git_rev macros. In the case of a normal release, %%plain_version will be the same
# as %%version.
%global plain_version %{lua:
    local non_snapshot_version = (string.gsub(macros.version, '^(.*)%^.*$', '%1'))
    if non_snapshot_version ~= macros.version then
        macros.snapshot = (string.gsub(macros.version, '^.*%^(.*)$', '%1'))
        macros.git_rev = (string.gsub(macros.snapshot, '^.*git(.*)$', '%1'))
    end
    local plain_version = (string.gsub(non_snapshot_version, "~", "-"))
    print(plain_version)
}
%global major %{lua:
    print((string.gsub(macros.plain_version, '^(%d+)%..*$', '%1')))
}
%global minor %{lua:
    print((string.gsub(macros.plain_version, '^%d+%.(%d+)%..*$', '%1')))
}
%global micro %{lua:
    print((string.gsub(macros.plain_version, '^%d+%.%d+%.(%d+).*$', '%1')))
}
%global bin_version %{major}.%{minor}
%global interface_age 0
%if %prerelease
%global gettext_version 30
%global api_version 3.0
%global lib_api_version 3.0
%else
%global gettext_version %{major}0
%global api_version %{major}.0
%global lib_api_version %{major}.0
%endif
%global lib_minor %{lua: print(tonumber(macros.minor) * 100)}
%global lib_micro %micro

# gimp core app is GPL-3.0-or-later, libgimp and other libraries are LGPL-3.0-or-later
# plugin file-dds is GPL-2.0-or-later and plugins script-fu/libscriptfu/{ftx,tinyscheme}
# are BSD-3-Clause, icon themes are CC-BY-SA-{3.0,4.0}, data files such as brushes and
# patterns are CC0-1.0
License:        LGPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-SA-4.0 AND CC0-1.0
URL:            https://www.gimp.org
%if %{with label_overlay}
BuildRequires:  ImageMagick
%endif
BuildRequires:  aalib-devel
BuildRequires:  appdata-tools
BuildRequires:  appstream
BuildRequires:  coreutils
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gegl04-tools
BuildRequires:  gettext >= 0.19.8
BuildRequires:  gi-docgen
BuildRequires:  gjs
BuildRequires:  glib-networking
BuildRequires:  libgs-devel
BuildRequires:  libxml2
BuildRequires:  libxslt
%ifnarch %plain_lua_arches
BuildRequires:  lua-lgi-compat
BuildRequires:  luajit
%else
BuildRequires:  lua >= 5.4
BuildRequires:  lua-lgi
%endif
BuildRequires:  meson
BuildRequires:  perl >= 5.10.0
BuildRequires:  pkgconfig(alsa) >= 1.0.0
BuildRequires:  pkgconfig(appstream-glib) >= 0.7.7
BuildRequires:  pkgconfig(atk) >= 2.4.0
BuildRequires:  pkgconfig(babl-0.1) >= 0.1.110
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= 1.14.0
BuildRequires:  pkgconfig(cairo-pdf) >= 1.12.2
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(fontconfig) >= 2.12.4
BuildRequires:  pkgconfig(freetype2) >= 2.1.7
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.8
BuildRequires:  pkgconfig(gegl-0.4) >= 0.4.50
BuildRequires:  pkgconfig(gexiv2) >= 0.14.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.70.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gudev-1.0) >= 167
BuildRequires:  pkgconfig(harfbuzz) >= 2.8.2
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.2.6
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(libheif) >= 1.15.1
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl) >= 0.7.0
BuildRequires:  pkgconfig(libjxl_threads) >= 0.7.0
BuildRequires:  pkgconfig(liblzma) >= 5.0.0
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmypaint) >= 1.3.0
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libpng) >= 1.6.25
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(libtiff-4) >= 4.0.0
%if %{with libunwind}
BuildRequires:  pkgconfig(libunwind) >= 1.1.0
%endif
BuildRequires:  pkgconfig(libwebp) >= 0.6.0
BuildRequires:  pkgconfig(libwebpdemux) >= 0.6.0
BuildRequires:  pkgconfig(libwebpmux) >= 0.6.0
BuildRequires:  pkgconfig(libwmf) >= 0.2.8
BuildRequires:  pkgconfig(mypaint-brushes-1.0) >= 1.3.0
BuildRequires:  pkgconfig(OpenEXR) >= 1.6.1
BuildRequires:  pkgconfig(pango) >= 1.50.0
BuildRequires:  pkgconfig(pangocairo) >= 1.50.0
BuildRequires:  pkgconfig(pangoft2) >= 1.50.0
BuildRequires:  pkgconfig(poppler-data) >= 0.4.9
BuildRequires:  pkgconfig(poppler-glib) >= 0.69.0
BuildRequires:  pkgconfig(python3) >= 3.6.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3dist(pygobject) >= 3.0
BuildRequires:  vala
BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  yelp-tools

Requires:       gjs
Requires:       hicolor-icon-theme
%ifnarch %plain_lua_arches
Requires:       lua-lgi-compat
Requires:       luajit
%else
Requires:       lua >= 5.4
Requires:       lua-lgi
%endif
Requires:       xdg-utils
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       python3dist(pygobject) >= 3.0

Recommends:     mypaint-brushes

Obsoletes:      gimp3 < %{version}-%{release}
Provides:       gimp3 = %{version}-%{release}

%if ! %defined snapshot
Source0:        https://download.gimp.org/pub/gimp/v%{bin_version}/gimp-%{plain_version}.tar.xz
%else
# Tarball built from git snapshot with `meson dist` and renamed accordingly
Source0:        gimp-%{plain_version}-git%{git_rev}.tar.xz
%endif

# Fedora specific patches:

# Try using the system monitor profile for color management by default.
Patch1:         gimp-2.99.19-cm-system-monitor-profile-by-default.patch

# don't phone home to check for updates by default
Patch2:         gimp-2.99.19-no-phone-home-default.patch

# use external help browser directly if help browser plug-in is not built
Patch3:         gimp-2.99.19-external-help-browser.patch

%description
GIMP (GNU Image Manipulation Program) is a powerful image composition and
editing program, which can be extremely useful for creating logos and other
graphics for web pages. GIMP has many of the tools and filters you would expect
to find in similar commercial offerings, and some interesting extras as well.
GIMP provides a large image manipulation toolbox, including channel operations
and layers, effects, sub-pixel imaging and anti-aliasing, and conversions, all
with multi-level undo.

%package libs
Summary:        GIMP libraries
License:        LGPL-3.0-or-later
Obsoletes:      gimp3-libs < %{version}-%{release}
Provides:       gimp3-libs = %{version}-%{release}

%description libs
The %{name}-libs package contains shared libraries needed for the GNU Image
Manipulation Program (GIMP).

%package devel
Summary:        GIMP plugin and extension development kit
License:        LGPL-3.0-or-later
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel-tools = %{epoch}:%{version}-%{release}
Obsoletes:      gimp3-devel < %{version}-%{release}
Provides:       gimp3-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains the files needed for writing GNU Image
Manipulation Program (GIMP) plug-ins and extensions.

%package devel-tools
Summary:        GIMP plugin and extension development tools
License:        LGPL-3.0-or-later
Requires:       %{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:      gimp3-devel-tools < %{version}-%{release}
Provides:       gimp3-devel-tools = %{version}-%{release}

%description devel-tools
The %{name}-devel-tools package contains gimptool, a helper program to
build GNU Image Manipulation Program (GIMP) plug-ins and extensions.

%prep
cat << EOF
--- 8< --- Build options ---------------------------------------------------
is default version: %{with is_default_version}
label overlay:      %{with label_overlay}
tests:              %{with tests}
%if %defined snapshot
snapshot:           %{snapshot}
plain_version:      %{plain_version}
git_rev:            %{git_rev}
%endif
--- >8 ---------------------------------------------------------------------
EOF

%setup -q -n gimp-%{plain_version}

%patch 1 -p1 -b .cm-system-monitor-profile-by-default
%patch 2 -p1 -b .no-phone-home-default
%patch 3 -p1 -b .external-help-browser

%build
# Use hardening compiler/linker flags because gimp is likely to deal with files
# coming from untrusted sources
%global _hardened_build 1

%meson \
%if %{with is_default_version}
    -Denable-default-bin=enabled \
%else
    -Denable-default-bin=disabled \
%endif
    -Dg-ir-doc=true \
    -Dilbm=disabled \
    -Dbug-report-url="https://bugzilla.redhat.com/"

%meson_build

%install
%meson_install

# Generate RPM macros from pkg-config data:
# %%_gimp_datadir -- toplevel directory for brushes, gradients, scripts, ...
# %%_gimp_libdir -- toplevel directory for modules, plug-ins, ...
# %%_gimp_sysconfdir -- system-wide runtime configuration
# %%_gimp_localedir -- toplevel directory for translation files
# %%_gimp_scriptdir -- script-fu scripts directory
# %%_gimp_plugindir -- plug-in directory
gimp_pc_extract_normalize() {
    PKG_CONFIG_PATH="%{buildroot}%{_libdir}/pkgconfig" \
        pkg-config --variable="$1" gimp-%{lib_api_version} | \
    sed \
        -e 's|^%_mandir|%%{_mandir}|' \
        -e 's|^%_infodir|%%{_infodir}|' \
        -e 's|^%_includedir|%%{_includedir}|' \
        -e 's|^%_libdir|%%{_libdir}|' \
        -e 's|^%_localstatedir|%%{_localstatedir}|' \
        -e 's|^%_sharedstatedir|%%{_sharedstatedir}|' \
        -e 's|^%_sysconfdir|%%{_sysconfdir}|' \
        -e 's|^%_datadir|%%{_datadir}|' \
        -e 's|^%_libexecdir|%%{_libexecdir}|' \
        -e 's|^%_sbindir|%%{_sbindir}|' \
        -e 's|^%_bindir|%%{_bindir}|' \
        -e 's|^%_exec_prefix|%%{_exec_prefix}|' \
        -e 's|^%_prefix|%%{_prefix}|'
}

_gimp_datadir="$(gimp_pc_extract_normalize gimpdatadir)"
_gimp_libdir="$(gimp_pc_extract_normalize gimplibdir)"
_gimp_sysconfdir="$(gimp_pc_extract_normalize gimpsysconfdir)"
_gimp_localedir="$(gimp_pc_extract_normalize gimplocaledir)"
_gimp_scriptdir="${_gimp_datadir}/scripts"
_gimp_plugindir="${_gimp_libdir}/plug-ins"

cat << EOF > macros.gimp
# RPM macros for GIMP

%%_gimp_datadir ${_gimp_datadir}
%%_gimp_libdir ${_gimp_libdir}
%%_gimp_sysconfdir ${_gimp_sysconfdir}
%%_gimp_localedir ${_gimp_localedir}
%%_gimp_scriptdir ${_gimp_scriptdir}
%%_gimp_plugindir ${_gimp_plugindir}
EOF

install -D -m0644 macros.gimp %{buildroot}%{_rpmconfigdir}/macros.d/macros.gimp

echo "%{__python3}=%{__python3}" >> %{buildroot}%{_libdir}/gimp/%{api_version}/interpreters/pygimp.interp
echo "%{_bindir}/gimp-script-fu-interpreter-%{api_version}=%{_bindir}/gimp-script-fu-interpreter-%{api_version}" >> %{buildroot}%{_libdir}/gimp/%{api_version}/interpreters/gimp-script-fu-interpreter.interp

#
# Plugins and modules change often (grab the executeable ones)
#
find %{buildroot}%{_libdir}/gimp/%{api_version} -type f | sed "s@^%{buildroot}@@g" | grep -v '\.a$' > gimp-plugin-files
find %{buildroot}%{_libdir}/gimp/%{api_version}/* -type d | sed "s@^%{buildroot}@%%dir @g" >> gimp-plugin-files

grep '\.py$' gimp-plugin-files | \
    sed 's+/[^/]*\.py$+/__pycache__+g' | \
    sort -u > gimp-plugin-files-pycache

cat gimp-plugin-files-pycache >> gimp-plugin-files

%py_byte_compile %{__python3} %{buildroot}%{_libdir}/gimp/%{api_version}

#
# Auto detect the lang files.
#
%find_lang gimp%{gettext_version}
%find_lang gimp%{gettext_version}-std-plug-ins
%find_lang gimp%{gettext_version}-script-fu
%find_lang gimp%{gettext_version}-libgimp
%find_lang gimp%{gettext_version}-python

cat gimp%{gettext_version}.lang gimp%{gettext_version}-std-plug-ins.lang gimp%{gettext_version}-script-fu.lang gimp%{gettext_version}-libgimp.lang gimp%{gettext_version}-python.lang > gimp-all.lang

#
# Build the master filelists generated from the above mess.
#
cat gimp-plugin-files gimp-all.lang > gimp.files

%if %{with is_default_version}
# install default binary symlinks
ln -snf gimp-%{bin_version} %{buildroot}%{_bindir}/gimp
ln -snf gimp-%{bin_version}.1 %{buildroot}%{_mandir}/man1/gimp.1
ln -snf gimp-console-%{bin_version} %{buildroot}/%{_bindir}/gimp-console
ln -snf gimp-console-%{bin_version}.1 %{buildroot}/%{_mandir}/man1/gimp-console.1
ln -snf gimptool-%{bin_version} %{buildroot}%{_bindir}/gimptool
ln -snf gimptool-%{bin_version}.1 %{buildroot}%{_mandir}/man1/gimptool.1
ln -snf gimprc-%{bin_version}.5 %{buildroot}/%{_mandir}/man5/gimprc.5
%endif

# Hardcode python interpreter in shipped python plug-ins. This actually has no
# effect because gimp maps hashbangs with and without the /usr/bin/env detour
# to the system python interpreter, but this will avoid false alarms.
grep -E -rl '^#!\s*/usr/bin/env\s+python' --include=\*.py "%{buildroot}" |
    while read file; do
        sed -r '1s,^#!\s*/usr/bin/env\s+python$,#!%{__python3},' -i "$file"
        sed -r '1s,^#!\s*/usr/bin/env\s+python3$,#!%{__python3},' -i "$file"
    done

# Hardcode Script Fu interpreter path in shipped Scheme plug-ins. This preempts
# brp-mangle-shebangs and so prevents it from mangling this to /usr/bin/... in
# Flatpak builds (the interpreter comes with GIMP and is put into /app/bin).
grep -E -rl '^#!\s*/usr/bin/env\s+gimp-script-fu' --include=\*.scm "%{buildroot}" |
    while read file; do
        sed -r '1s,^#!\s*/usr/bin/env\s+(gimp-script-fu-interpreter.*)$,#!%{_bindir}/\1,' -i "$file"
    done

rm -rf devel-docs/gimp-%{bin_version}
mv %{buildroot}%{_docdir}/gimp-%{bin_version} devel-docs
rm -rf %{buildroot}%{_datadir}/gimp/%{api_version}/tests

%if %{without is_default_version}
rm -rf %{buildroot}%{_datadir}/metainfo
%endif

%if %{with tests}
%check
# Some tests in the gimp:app suite are known to fail when run in a normal desktop environment, but
# they work in isolated builds (mock, koji): save-and-export, single-window-mode, ui

# skip tests known to fail
skip_tests=""

%if %{with skip_networking_tests}
skip_tests="$skip_tests
%skip_tests_networking"
%endif

%if %{with skip_problematic_tests}
skip_tests="$skip_tests
%skip_tests_problematic"
%endif

%if %{with skip_user_tests}
skip_tests="$skip_tests
%skip_tests_user"
%endif

all_tests="$(%meson_test --list 2>/dev/null)"
suites="$(echo "$all_tests" | while read suite ignore; do echo "${suite%+*}"; done | sort -u)"
for suite in $suites; do
    suite_tests="$(
        echo "$all_tests" | grep "^$suite\(+\S\+\)\?" | while read ignore ignore test; do
            if ! echo "$skip_tests" | grep -qFx "$suite / $test"; then echo "$test"; fi
        done | sort -u
    )"
    if [ -n "$suite_tests" ]; then
        %meson_test --suite "$suite" $suite_tests
    fi
done
%endif

%ldconfig_scriptlets libs

%files -f gimp.files
%license LICENSE COPYING
%doc AUTHORS NEWS README
%doc docs/*.xcf*
%{_datadir}/applications/*.desktop
%if %{with is_default_version}
%{_datadir}/metainfo/*.appdata.xml
%endif

%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/%{api_version}
%{_datadir}/gimp/%{api_version}/dynamics/
%{_datadir}/gimp/%{api_version}/file-raw/
%{_datadir}/gimp/%{api_version}/menus/
%{_datadir}/gimp/%{api_version}/tags/
%{_datadir}/gimp/%{api_version}/tips/
%{_datadir}/gimp/%{api_version}/tool-presets/
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{api_version}

%{_datadir}/gimp/%{api_version}/brushes/
%{_datadir}/gimp/%{api_version}/fractalexplorer/
%{_datadir}/gimp/%{api_version}/gfig/
%{_datadir}/gimp/%{api_version}/gflare/
%{_datadir}/gimp/%{api_version}/gimpressionist/
%{_datadir}/gimp/%{api_version}/gradients/
%{_datadir}/gimp/%{api_version}/icons/
%{_datadir}/gimp/%{api_version}/images/
%{_datadir}/gimp/%{api_version}/palettes/
%{_datadir}/gimp/%{api_version}/patterns/
%{_datadir}/gimp/%{api_version}/scripts/
%{_datadir}/gimp/%{api_version}/themes/
%{_datadir}/gimp/%{api_version}/gimp-release

%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/%{api_version}
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/controllerrc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/gimp.css
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/gimprc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/unitrc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/sessionrc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/templaterc
%config(noreplace) %{_sysconfdir}/gimp/%{api_version}/toolrc

%{_bindir}/gimp-%{bin_version}
%{_bindir}/gimp-console-%{bin_version}
%{_bindir}/gimp-script-fu-interpreter-%{lib_api_version}

%if %{with is_default_version}
%{_bindir}/gimp
%{_bindir}/gimp-console
%{_bindir}/gimp-%{major}
%{_bindir}/gimp-console-%{major}
%endif

%{_bindir}/gimp-test-clipboard-%{bin_version}
%{_libexecdir}/gimp-debug-tool-%{bin_version}

%if %{with is_default_version}
%{_bindir}/gimp-test-clipboard
%{_libexecdir}/gimp-debug-tool
%{_bindir}/gimp-test-clipboard-%{major}
%{_libexecdir}/gimp-debug-tool-%{major}
%endif

%{_mandir}/man1/gimp-%{bin_version}.1*
%{_mandir}/man1/gimp-console-%{bin_version}.1*
%{_mandir}/man5/gimprc-%{bin_version}.5*

%if %{with is_default_version}
%{_mandir}/man1/gimp.1*
%{_mandir}/man1/gimp-%{major}.1*
%{_mandir}/man1/gimp-console.1*
%{_mandir}/man1/gimp-console-%{major}.1*
%{_mandir}/man5/gimprc.5*
%{_mandir}/man5/gimprc-%{major}.5*
%endif

%{_datadir}/icons/hicolor/*/apps/gimp*

%files libs
%license LICENSE COPYING
%doc AUTHORS NEWS README
%{_libdir}/libgimp-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimp-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimp-scriptfu-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimp-scriptfu-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimpbase-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimpbase-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimpcolor-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimpcolor-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimpconfig-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimpconfig-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimpmath-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimpmath-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimpmodule-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimpmodule-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimpthumb-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimpthumb-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimpui-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimpui-%{lib_api_version}.so.%{interface_age}
%{_libdir}/libgimpwidgets-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimpwidgets-%{lib_api_version}.so.%{interface_age}
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%doc README.i18n
%doc devel-docs/*

%{_libdir}/*.so
%{_includedir}/gimp-%{lib_api_version}
%{_libdir}/pkgconfig/*
%{_rpmconfigdir}/macros.d/macros.gimp
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Gimp*.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gimp*.deps
%{_datadir}/vala/vapi/gimp*.vapi

%files devel-tools
%{_bindir}/gimptool-%{bin_version}
%{_mandir}/man1/gimptool-%{bin_version}.1*

%if %{with is_default_version}
%{_bindir}/gimptool
%{_bindir}/gimptool-%{major}
%{_mandir}/man1/gimptool.1*
%{_mandir}/man1/gimptool-%{major}.1*
%endif

%changelog
%autochangelog

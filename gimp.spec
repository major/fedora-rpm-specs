#### options:
# Use the following --with/--without <option> switches to control how the
# package will be built:
#
# default_binary: install unversioned binary
%bcond_without default_binary
# libunwind support (only available on some architectures)
%ifarch %{arm} aarch64 hppa ia64 mips ppc %{power64} %{ix86} x86_64
%bcond_without libunwind
%else
%bcond_with libunwind
%endif

# skip tests known to be problematic in a specific version
#global skip_checks_version X.Y.Z
#global skip_checks test1 test2 test3

Summary:        GNU Image Manipulation Program
Name:           gimp
Epoch:          2
Version:        2.10.36
Release:        %autorelease

# Compute some version related macros.
# Ugly, need to get quoting percent signs straight.
%global major %(ver=%{version}; echo ${ver%%%%.*})
%global minor %(ver=%{version}; ver=${ver#%major.}; echo ${ver%%%%.*})
%global micro %(ver=%{version}; ver=${ver#%major.%minor.}; echo ${ver%%%%.*})
%global binver 2.10
%global interface_age 0
%global gettext_version %{major}0
%global lib_api_version %{major}.0
%global lib_minor %(echo $[%minor * 100])
%global lib_micro %micro

# gimp core app is GPL-3.0-or-later, libgimp and other libraries are LGPL-3.0-or-later
# plugin file-dds is GPL-2.0-or-later and plugins script-fu/{ftx,tinyscheme} are BSD-3-Clause
License:        LGPL-3.0-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-3-Clause
URL:            https://www.gimp.org/
BuildRequires:  aalib-devel
BuildRequires:  appdata-tools
BuildRequires:  chrpath >= 0.13-5
BuildRequires:  gcc
BuildRequires:  gegl04-tools
BuildRequires:  gettext >= 0.19
BuildRequires:  glib-networking
BuildRequires:  gtk-doc >= 1.0
BuildRequires:  intltool >= 0.40.1
BuildRequires:  libgs-devel
BuildRequires:  make
BuildRequires:  perl >= 5.10.0
BuildRequires:  pkgconfig(alsa) >= 1.0.0
BuildRequires:  pkgconfig(atk) >= 2.2.0
%if ! 0%{?fedora} || 0%{?fedora} >= 39
BuildRequires:  pkgconfig(babl-0.1) >= 0.1.74
%else
BuildRequires:  pkgconfig(babl) >= 0.1.74
%endif
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo) >= 1.12.2
BuildRequires:  pkgconfig(fontconfig) >= 2.12.4
BuildRequires:  pkgconfig(freetype2) >= 2.1.7
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.30.8
BuildRequires:  pkgconfig(gegl-0.4) >= 0.4.32
BuildRequires:  pkgconfig(gexiv2) >= 0.10.6
BuildRequires:  pkgconfig(gio-2.0) >= 2.56.2
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.56.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.2
BuildRequires:  pkgconfig(gmodule-no-export-2.0) >= 2.56.2
BuildRequires:  pkgconfig(gobject-2.0) >= 2.56.2
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.32
BuildRequires:  pkgconfig(gudev-1.0) >= 167
BuildRequires:  pkgconfig(harfbuzz) >= 0.9.19
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(jasper)
BuildRequires:  pkgconfig(lcms2) >= 2.8
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl) >= 0.6.1
BuildRequires:  pkgconfig(libjxl_threads) >= 0.6.1
BuildRequires:  pkgconfig(liblzma) >= 5.0.0
BuildRequires:  pkgconfig(libmng)
BuildRequires:  pkgconfig(libmypaint) >= 1.3.0
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libpng) >= 1.6.25
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.40.6
BuildRequires:  pkgconfig(libtiff-4)
%if %{with libunwind}
BuildRequires:  pkgconfig(libunwind) >= 1.1.0
%endif
BuildRequires:  pkgconfig(libwebp) >= 0.6.0
BuildRequires:  pkgconfig(libwebpdemux) >= 0.6.0
BuildRequires:  pkgconfig(libwebpmux) >= 0.6.0
BuildRequires:  pkgconfig(libwmf) >= 0.2.8
BuildRequires:  pkgconfig(mypaint-brushes-1.0) >= 1.3.0
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(pangocairo) >= 1.29.4
BuildRequires:  pkgconfig(pangoft2) >= 1.29.4
BuildRequires:  pkgconfig(poppler-data) >= 0.4.7
BuildRequires:  pkgconfig(poppler-glib) >= 0.50.0
BuildRequires:  pkgconfig(pycairo) >= 1.0.2
BuildRequires:  pkgconfig(pygobject-2.0)
BuildRequires:  pkgconfig(pygtk-2.0) >= 2.10.4
BuildRequires:  pkgconfig(python2) >= 2.5.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)

Requires:       hicolor-icon-theme
Recommends:     mypaint-brushes
Requires:       xdg-utils
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-help-browser < %{epoch}:%{version}-%{release}
Conflicts:      %{name}-help-browser < %{epoch}:%{version}-%{release}

#Remove dependency on RPM Fusion repository
Obsoletes:      gimp-heif-plugin < 1.1.0-13

Source0:        https://download.gimp.org/pub/gimp/v%{binver}/gimp-%{version}.tar.bz2

# Try using the system monitor profile for color management by default.
# Fedora specific.
Patch1:         gimp-2.10.0-cm-system-monitor-profile-by-default.patch

# bz#1706653
Patch2:         gimp-2.10.12-default-font.patch

# don't phone home to check for updates by default
Patch3:         gimp-2.10.18-no-phone-home-default.patch

# use external help browser directly if help browser plug-in is not built
Patch100:       gimp-2.10.24-external-help-browser.patch

Patch101:       gimp-configure-c99.patch

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
License:        LGPLv3+

%description libs
The %{name}-libs package contains shared libraries needed for the GNU Image
Manipulation Program (GIMP).

%package devel
Summary:        GIMP plugin and extension development kit
License:        LGPLv3+
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel-tools = %{epoch}:%{version}-%{release}

%description devel
The %{name}-devel package contains the files needed for writing GNU Image
Manipulation Program (GIMP) plug-ins and extensions.

%package devel-tools
Summary:        GIMP plugin and extension development tools
License:        LGPLv3+
Requires:       %{name}-devel = %{epoch}:%{version}-%{release}

%description devel-tools
The %{name}-devel-tools package contains gimptool, a helper program to
build GNU Image Manipulation Program (GIMP) plug-ins and extensions.

%prep
cat << EOF
--- 8< --- Build options ---------------------------------------------------
install default binary:      %{with default_binary}
--- >8 ---------------------------------------------------------------------
EOF

%setup -q -n gimp-%{version}

%patch 1 -p1 -b .cm-system-monitor-profile-by-default
%patch 2 -p1 -b .font-default
%patch 3 -p1 -b .no-phone-home-default

%patch 100 -p1 -b .external-help-browser
%patch 101 -p1 -b .configure-c99

# Avoid re-running autotools.
touch -r aclocal.m4 configure*

%build
# allow python2 package for RHEL-8
export RHEL_ALLOW_PYTHON2_FOR_BUILD=1

# Use hardening compiler/linker flags because gimp is likely to deal with files
# coming from untrusted sources
%global _hardened_build 1
%configure \
    --enable-python \
    --enable-mp \
    --disable-static \
    --with-print \
    --enable-gimp-console \
    --with-aa \
    --with-gudev \
%ifos linux
    --with-linux-input \
%endif
    --without-webkit \
    --with-webp \
%if %{with default_binary}
    --enable-default-binary=yes \
%else
    --enable-default-binary=no \
%endif
    --with-libmng --with-libxpm --with-alsa --with-cairo-pdf --with-libheif \
%if 0%{?flatpak}
    --with-icc-directory=/run/host/usr/share/color/icc/ \
%endif
    --without-appdata-test

%make_build

# Generate RPM macros from pkg-config data:
# %%_gimp_datadir -- toplevel directory for brushes, gradients, scripts, ...
# %%_gimp_libdir -- toplevel directory for modules, plug-ins, ...
# %%_gimp_sysconfdir -- system-wide runtime configuration
# %%_gimp_localedir -- toplevel directory for translation files
# %%_gimp_scriptdir -- script-fu scripts directory
# %%_gimp_plugindir -- plug-in directory
gimp_pc_extract_normalize() {
    PKG_CONFIG_PATH="$PWD" \
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

%install
%make_install
install -D -m0644 macros.gimp %{buildroot}%{_rpmconfigdir}/macros.d/macros.gimp

# remove rpaths
find %buildroot -type f -print0 | xargs -0 -L 20 chrpath --delete --keepgoing 2>/dev/null || :

# remove .la files
find %buildroot -name \*.la -exec %__rm -f {} \;

#
# Plugins and modules change often (grab the executeable ones)
#
find %{buildroot}%{_libdir}/gimp/%{lib_api_version} -type f | sed "s@^%{buildroot}@@g" | grep -v '\.a$' > gimp-plugin-files
find %{buildroot}%{_libdir}/gimp/%{lib_api_version}/* -type d | sed "s@^%{buildroot}@%%dir @g" >> gimp-plugin-files

# .pyc and .pyo files don't exist yet
grep "\.py$" gimp-plugin-files > gimp-plugin-files-py
for file in $(cat gimp-plugin-files-py); do
    for newfile in ${file}c ${file}o; do
        grep -F -q -x "$newfile" gimp-plugin-files || echo "$newfile"
    done
done >> gimp-plugin-files

%py_byte_compile %{__python2} %{buildroot}%{_libdir}/gimp/%{lib_api_version}

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

%if %{with default_binary}
# install default binary symlinks
ln -snf gimp-%{binver} %{buildroot}%{_bindir}/gimp
ln -snf gimp-%{binver}.1 %{buildroot}%{_mandir}/man1/gimp.1
ln -snf gimp-console-%{binver} %{buildroot}/%{_bindir}/gimp-console
ln -snf gimp-console-%{binver}.1 %{buildroot}/%{_mandir}/man1/gimp-console.1
ln -snf gimptool-%{lib_api_version} %{buildroot}%{_bindir}/gimptool
ln -snf gimptool-%{lib_api_version}.1 %{buildroot}%{_mandir}/man1/gimptool.1
ln -snf gimprc-%{binver}.5 %{buildroot}/%{_mandir}/man5/gimprc.5
%endif

# Hardcode python interpreter in shipped python plug-ins. This actually has no
# effect because gimp maps hashbangs with and without the /usr/bin/env detour
# to the system python interpreter, but this will avoid false alarms.
grep -E -rl '^#!\s*/usr/bin/env\s+python' --include=\*.py "%{buildroot}" |
    while read file; do
        sed -r '1s,^#!\s*/usr/bin/env\s+python$,#!%{__python2},' -i "$file"
        sed -r '1s,^#!\s*/usr/bin/env\s+python2$,#!%{__python2},' -i "$file"
    done

echo "%{__python2}=%{__python2}" >> %{buildroot}%{_libdir}/gimp/%{lib_api_version}/interpreters/pygimp.interp

%check
# skip tests known to be problematic in a specific version
%if "%{version}" == "%{?skip_checks_version}"
pushd app/tests
for problematic in %{?skip_checks}; do
    rm -f "$problematic"
    cat << EOF > "$problematic"
#!/bin/sh
echo Skipping test "$problematic"
EOF
    chmod +x "$problematic"
done
popd
%endif
make check %{?_smp_mflags}

%ldconfig_scriptlets libs

%files -f gimp.files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc docs/*.xcf*
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/metainfo/*.metainfo.xml

%dir %{_datadir}/gimp
%dir %{_datadir}/gimp/%{lib_api_version}
%{_datadir}/gimp/%{lib_api_version}/dynamics/
%{_datadir}/gimp/%{lib_api_version}/file-raw/
%{_datadir}/gimp/%{lib_api_version}/menus/
%{_datadir}/gimp/%{lib_api_version}/tags/
%{_datadir}/gimp/%{lib_api_version}/tips/
%{_datadir}/gimp/%{lib_api_version}/tool-presets/
%{_datadir}/gimp/%{lib_api_version}/ui/
%dir %{_libdir}/gimp
%dir %{_libdir}/gimp/%{lib_api_version}

%{_datadir}/gimp/%{lib_api_version}/brushes/
%{_datadir}/gimp/%{lib_api_version}/fractalexplorer/
%{_datadir}/gimp/%{lib_api_version}/gfig/
%{_datadir}/gimp/%{lib_api_version}/gflare/
%{_datadir}/gimp/%{lib_api_version}/gimpressionist/
%{_datadir}/gimp/%{lib_api_version}/gradients/
%{_datadir}/gimp/%{lib_api_version}/icons/
%{_datadir}/gimp/%{lib_api_version}/images/
%{_datadir}/gimp/%{lib_api_version}/palettes/
%{_datadir}/gimp/%{lib_api_version}/patterns/
%{_datadir}/gimp/%{lib_api_version}/scripts/
%{_datadir}/gimp/%{lib_api_version}/themes/
%{_datadir}/gimp/%{lib_api_version}/gimp-release

%dir %{_sysconfdir}/gimp
%dir %{_sysconfdir}/gimp/%{lib_api_version}
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/controllerrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/gimprc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/gtkrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/unitrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/sessionrc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/templaterc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/menurc
%config(noreplace) %{_sysconfdir}/gimp/%{lib_api_version}/toolrc

%{_bindir}/gimp-%{binver}
%{_bindir}/gimp-console-%{binver}

%if %{with default_binary}
%{_bindir}/gimp
%{_bindir}/gimp-console
%endif

%{_bindir}/gimp-test-clipboard-%{lib_api_version}
%{_libexecdir}/gimp-debug-tool-%{lib_api_version}

%{_mandir}/man1/gimp-%{binver}.1*
%{_mandir}/man1/gimp-console-%{binver}.1*
%{_mandir}/man5/gimprc-%{binver}.5*

%if %{with default_binary}
%{_mandir}/man1/gimp.1*
%{_mandir}/man1/gimp-console.1*
%{_mandir}/man5/gimprc.5*
%endif

%{_datadir}/icons/hicolor/*/apps/gimp.png

%files libs
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgimp-%{lib_api_version}.so.%{interface_age}.%{lib_minor}.%{lib_micro}
%{_libdir}/libgimp-%{lib_api_version}.so.%{interface_age}
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

%files devel
%doc HACKING README.i18n
%doc %{_datadir}/gtk-doc

%{_libdir}/*.so
%ifnos linux
%{_libdir}/*.la
%{_libdir}/gimp/%{lib_api_version}/modules/*.la
%endif
%{_datadir}/aclocal/*.m4
%{_includedir}/gimp-%{lib_api_version}
%{_libdir}/pkgconfig/*
%{_rpmconfigdir}/macros.d/macros.gimp

%files devel-tools
%{_bindir}/gimptool-%{lib_api_version}
%{_mandir}/man1/gimptool-%{lib_api_version}.1*

%if %{with default_binary}
%{_bindir}/gimptool
%{_mandir}/man1/gimptool.1*
%endif

%changelog
%autochangelog

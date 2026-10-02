%bcond thumbnailer %[0%{?fedora} >= 41]

# un-double the %% to uncomment
#%%global gitcommit f692950aaf0e9dc3cf275b25bfcc0b1df9a96bb6
%{?gitcommit:%global gitcommitshort %(c=%{gitcommit}; echo ${c:0:7})}

Summary: Image browser and viewer
Name: geeqie
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Version: 3.2
Release: %autorelease
URL: https://www.geeqie.org

%if %{defined gitcommit}
Source:  https://github.com/BestImageViewer/%{name}/archive/%{gitcommit}/%{name}-%{gitcommitshort}.tar.gz
%else
Source0: https://github.com/BestImageViewer/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1: https://github.com/BestImageViewer/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
# Find which key was used for signing the release:
#
# $ LANG=C gpg --verify geeqie-2.4.tar.xz.asc geeqie-2.4.tar.xz
# gpg: Signature made Сб 23 мар 2024 14:57:48 CET
# gpg:                using RSA key 91EC400226201276E2ADCEC7D0DA6F44C936D1DA
# gpg: Can't check signature: No public key
#
# Now export the key required as follows:
#
# gpg --no-default-keyring --keyring ./keyring.gpg --keyserver keyserver.ubuntu.com --recv-key 91EC400226201276E2ADCEC7D0DA6F44C936D1DA
# gpg --no-default-keyring --keyring ./keyring.gpg  --output 91EC400226201276E2ADCEC7D0DA6F44C936D1DA.gpg --export
Source2: 91EC400226201276E2ADCEC7D0DA6F44C936D1DA.gpg
%endif

ExcludeArch: %{ix86}

BuildRequires: desktop-file-utils
BuildRequires: evince
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gnome-doc-utils
# for %%gpgverify
BuildRequires: gnupg2
BuildRequires: intltool
BuildRequires: make
BuildRequires: meson
BuildRequires: yelp-tools
# for /usr/bin/appstream-util
BuildRequires: libappstream-glib

BuildRequires: cfitsio-devel
BuildRequires: clutter-devel
BuildRequires: djvulibre-devel
BuildRequires: glib2-devel
BuildRequires: gtk4-devel
BuildRequires: exiv2-devel
BuildRequires: lcms2-devel
BuildRequires: libarchive-devel
BuildRequires: libchamplain-devel
BuildRequires: libheif-devel
BuildRequires: libjpeg-devel
BuildRequires: libjxl-devel
BuildRequires: LibRaw-devel
BuildRequires: libshumate-devel
BuildRequires: libspelling-devel
BuildRequires: libtiff-devel
BuildRequires: libwebp-devel
BuildRequires: lirc-devel
BuildRequires: lua-devel
BuildRequires: openexr-devel
BuildRequires: openjpeg2-devel
BuildRequires: pango-devel
BuildRequires: poppler-glib-devel
BuildRequires: webp-pixbuf-loader

%if %{with thumbnailer}
BuildRequires: ffmpegthumbnailer-devel
%endif
# BuildRequires: xvfb-run

# Experimental, still disabled by default.
#BuildRequires: libchamplain-gtk-devel >= 0.4

# This is needed to generate one of the icc headers in the build
# process. Kind of annoyingly, this is part of _vim_, but, eh,
# I guess it doesn't _really_ matter for a build dep.
BuildRequires: /usr/bin/xxd

# for the included plug-in scripts
BuildRequires: exiv2
BuildRequires: fbida
BuildRequires: ImageMagick
BuildRequires: zenity
Requires:      exiv2
Requires:      fbida
Requires:      ImageMagick
Requires:      zenity
%if 0%{?fedora} > 40
Requires: gdk-pixbuf2-modules-extra%{?_isa}
%endif


%description
Geeqie has been forked from the GQview project with the goal of picking up
development and integrating patches. It is an image viewer for browsing
through graphics files. Its many features include single click file viewing,
support for external editors, previewing images using thumbnails, and zoom.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 %{?gitcommit:-n %{name}-%{gitcommit}}


%build
# guard against missing executables at (re)build-time,
# these are needed by the plug-in scripts
for f in exiftran exiv2 mogrify zenity ; do
    type $f || exit 1
done

export CXXFLAGS="$CXXFLAGS -Wno-deprecated-declarations -Wno-unused-variable -Wno-unused-but-set-variable -Wno-unused-parameter"

%meson %{!?with_thumbnailer: -Dvideothumbnailer=disabled}
%meson_build


# this will fail w/o git repo structure
#touch ChangeLog ChangeLog.html

%install
%meson_install

# add missing html doc
cp -av %{_vpath_builddir}/doc/html %{buildroot}%{_pkgdocdir}/

# guard against missing HTML tree
test -f %{buildroot}%{_pkgdocdir}/html/index.html

# We want these _docdir files in GQ_HELPDIR.
install -p -m 0644 COPYING NEWS README* \
    %{buildroot}%{_pkgdocdir}

ln -s NEWS %{buildroot}%{_pkgdocdir}/ChangeLog

%find_lang %name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.geeqie.Geeqie.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.geeqie.Geeqie.metainfo.xml


%files -f %{name}.lang
%doc %{_pkgdocdir}/
%license COPYING
%{_bindir}/%{name}*
%{_prefix}/lib/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/
# %%{_datadir}/pixmaps/%%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/org.geeqie.Geeqie.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/org.geeqie.Geeqie.desktop
# %%{_datadir}/applications/org.geeqie.cache-maintenance.desktop
%{_metainfodir}/org.geeqie.Geeqie.metainfo.xml
%{bash_completions_dir}/%{name}


%changelog
%autochangelog

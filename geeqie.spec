# un-double the %% to uncomment
#%%global gitcommit f692950aaf0e9dc3cf275b25bfcc0b1df9a96bb6
%{?gitcommit:%global gitcommitshort %(c=%{gitcommit}; echo ${c:0:7})}

Summary: Image browser and viewer
Name: geeqie
License: GPLv2+
Version: 1.7.3
Release: %autorelease
URL: https://www.geeqie.org

%if %{defined gitcommit}
Source0: https://github.com/BestImageViewer/%{name}/archive/%{gitcommit}/%{name}-%{gitcommitshort}.tar.gz
%else
Source0: https://github.com/BestImageViewer/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
%endif

Patch:   sun_path.patch

BuildRequires: gcc-c++
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: yelp-tools
# for /usr/bin/appstream-util
BuildRequires: libappstream-glib
BuildRequires: gtk3-devel
BuildRequires: clutter-devel
BuildRequires: djvulibre-devel
BuildRequires: libchamplain-devel
BuildRequires: lcms2-devel
BuildRequires: exiv2-devel
BuildRequires: lirc-devel
BuildRequires: libarchive-devel
BuildRequires: libjpeg-devel
BuildRequires: libjxl-devel
BuildRequires: libtiff-devel
# BuildRequires: libheif-devel (uncomment when available in Fedora)
BuildRequires: libwebp-devel
BuildRequires: openjpeg2-devel
BuildRequires: poppler-glib-devel
BuildRequires: lua-devel
BuildRequires: gettext intltool desktop-file-utils
BuildRequires: gnome-doc-utils

# for the included plug-in scripts
BuildRequires: exiv2
BuildRequires: fbida
BuildRequires: ImageMagick
BuildRequires: zenity
Requires:      exiv2
Requires:      fbida
Requires:      ImageMagick
Requires:      zenity
# at run-time, it is only displayed in menus, if ufraw executable is available
%if 0%{?fedora}
BuildRequires: ufraw
%endif
BuildRequires: make


# Experimental, still disabled by default.
#BuildRequires: libchamplain-gtk-devel >= 0.4


%description
Geeqie has been forked from the GQview project with the goal of picking up
development and integrating patches. It is an image viewer for browsing
through graphics files. Its many features include single click file viewing,
support for external editors, previewing images using thumbnails, and zoom.


%prep
%autosetup -p1 %{?gitcommit:-n %{name}-%{gitcommit}}

# fix autoconf problem with missing version
sed -r -i 's/m4_esyscmd_s\(git rev-parse --quiet --verify --short HEAD\)/[%{version}]/' configure.ac

%build

autoreconf -f -i ; intltoolize
# guard against missing executables at (re)build-time,
# these are needed by the plug-in scripts
for f in exiftran exiv2 mogrify zenity ; do
    type $f || exit -1
done
%if 0%{?fedora}
for f in ufraw-batch ; do
    type $f || exit -1
done
%endif

cflags=(
	-Wno-error=unused-variable
	-Wno-error=maybe-uninitialized
	-Wno-error=unused-function
	-Wno-error=unused-but-set-variable
	-Wno-error=parentheses
	-Wno-deprecated-declarations
)

%configure --enable-lirc \
    --with-readmedir=%{_pkgdocdir} CFLAGS="$CFLAGS ${cflags[*]}"

# this will fail w/o git repo structure
touch ChangeLog ChangeLog.html

%make_build

%install
mkdir -p %{buildroot}%{_pkgdocdir}/html
%make_install

# guard against missing HTML tree
[ ! -f %{buildroot}%{_pkgdocdir}/html/index.html ] && exit 1

# We want these _docdir files in GQ_HELPDIR.
install -p -m 0644 AUTHORS COPYING NEWS README* TODO \
    %{buildroot}%{_pkgdocdir}

desktop-file-install \
    --delete-original \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %name

mv %{buildroot}/usr/share/metainfo %{buildroot}%{_datadir}/appdata
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/org.geeqie.Geeqie.appdata.xml

%files -f %{name}.lang
%doc %{_pkgdocdir}/
%license COPYING
%{_bindir}/%{name}*
%{_prefix}/lib/%{name}/
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/appdata/org.geeqie.Geeqie.appdata.xml


%changelog
%autochangelog

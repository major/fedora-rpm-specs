# Don't bother building debug packages as koji bitches about n-v-r from nemo package
%global debug_package %{nil}
%global cjs_version 140.0

%global upstream_version 6.7.2-unstable
%global sversion 6.7.2

Name:           nemo-extensions
Version:        6.7.2^unstable
Release:        %autorelease
Summary:        Extensions for Nemo

License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/linuxmint/%{name}
Source0:        %url/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  desktop-file-utils
BuildRequires:  gpgme-devel
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libnemo-extension) >= 6.7.0
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(cjs-1.0) >= %{cjs_version}
BuildRequires:  pkgconfig(xreader-view-1.5)
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  perl(XML::Parser)

%description
Extensions for Nemo

%package     -n nemo-audio-tab
Summary:     Audio tag information extension for Nemo
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:     GPL-3.0-or-later
BuildArch:   noarch
Requires:    python3-mutagen
Requires:    nemo-python

%description -n nemo-audio-tab
nemo-audio-tab is an extension to view audio tag information from the properties tab.

%package     -n nemo-pastebin
Summary:     Pastebin extension for Nemo
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later
BuildArch:   noarch
Requires:    pastebinit
Requires:    nemo-python

%description -n nemo-pastebin
nemo-pastebin is an extension for the Nemo file manager, which allows
users to send files to pastebins just a right-click away.

%package     -n nemo-fileroller
Summary:     File Roller extension for Nemo
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later
Requires:    file-roller

%description -n nemo-fileroller
This package contains the file-roller extension for the Nemo.

%package     -n nemo-python
Summary:     Python scripting extension for Nemo
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later
Obsoletes:   python2-nemo < %{version}-%{release}
Obsoletes:   python3-nemo < %{version}-%{release}
Provides:    python3-nemo = %{version}-%{release}
Requires:    nemo >= 6.6.0
Requires:    python3-gobject-base

%description -n nemo-python
Python scripting extension for Nemo

%package     -n nemo-python-devel
Summary:     Python scripting extension for Nemo
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later
Obsoletes:   python2-nemo-devel < %{version}-%{release}
Obsoletes:   python3-nemo-devel < %{version}-%{release}
Requires:    nemo-python%{?_isa} = %{version}-%{release}

%description -n nemo-python-devel
Python scripting extension for Nemo

%package     -n nemo-terminal
Summary:     Embedded terminal window for Nemo
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:     GPL-3.0-or-later
BuildArch:   noarch
Requires:    vte291
Requires:    nemo-python = %{version}-%{release}

%description -n nemo-terminal
Embedded terminal window for Nemo

%package     -n nemo-preview
Summary:     A quick previewer for Nemo
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:     GPL-2.0-or-later
Requires:    nemo
Requires:    cjs >= %{cjs_version}

%description -n nemo-preview
Nemo Preview is a GtkClutter and Javascript-based quick previewer
for Nemo.
It is capable of previewing documents, PDFs, sound and video files,
some text files, and possibly others in the future.

To activate the preview, left-click the file and hit space.
The preview can be closed by hitting space again, or escape.

%package     -n nemo-emblems
Summary:     Emblem support for nemo
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:     GPL-3.0-or-later
BuildArch:   noarch
Requires:    nemo-python = %{version}-%{release}

%description -n nemo-emblems
Restores the emblems functionality that used to be in GNOME 2.

%package     -n nemo-image-converter
Summary:     Nemo extension to mass resize images
Requires:    ImageMagick
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:     GPL-3.0-or-later

%description -n nemo-image-converter
Adds a "Resize Images..." menu item to the context menu.
This opens a dialog where you set the desired image size and file name.

%package     -n nemo-compare
Summary:     Context menu comparison extension for nemo
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:     GPL-3.0-or-later
BuildArch:   noarch
Requires:    nemo-python = %{version}-%{release}
Recommends:  meld

%description -n nemo-compare
Context menu comparison extension for Nemo file manager.

%package     -n nemo-seahorse
Summary:     PGP encryption and signing for Nemo
License:     GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
Requires:    seahorse%{?_isa}

%description -n nemo-seahorse
Seahorse nemo is an extension for nemo which allows encryption
and decryption of OpenPGP files using GnuPG.

%prep
%autosetup -p1 -n %{name}-%{upstream_version}
# use relative paths in data_files to support wheel-based installation
# TODO send upstream
sed -Ei '/^ *data_files *= *\[/,/^ *\]/ { s@/usr/@@ }' */setup.py

%generate_buildrequires
pushd nemo-audio-tab >&2
%pyproject_buildrequires
popd >&2

pushd nemo-pastebin >&2
%pyproject_buildrequires
popd >&2

pushd nemo-terminal >&2
%pyproject_buildrequires
popd >&2

pushd nemo-emblems >&2
%pyproject_buildrequires
popd >&2

pushd nemo-compare >&2
%pyproject_buildrequires
popd >&2

%build
pushd nemo-audio-tab
%pyproject_wheel
popd

pushd nemo-pastebin
%pyproject_wheel
popd

pushd nemo-fileroller
%meson
%meson_build
popd

pushd nemo-python
%meson
%meson_build
popd

pushd nemo-terminal
%pyproject_wheel
popd

pushd nemo-preview
%meson
%meson_build
popd

pushd nemo-emblems
%pyproject_wheel
popd

pushd nemo-image-converter
%meson
%meson_build
popd

pushd nemo-compare
%pyproject_wheel
popd

pushd nemo-seahorse
%meson
%meson_build
popd

%install
%pyproject_install

pushd nemo-fileroller
%meson_install
popd

pushd nemo-python
%meson_install
popd

pushd nemo-preview
%meson_install
popd

pushd nemo-image-converter
%meson_install
popd

pushd nemo-seahorse
%meson_install
popd

%py_byte_compile %{python3} %{buildroot}%{_datadir}/nemo*

rm -rf %{buildroot}/%{_datadir}/doc/nemo-python/

%files -n nemo-audio-tab
%license nemo-audio-tab/COPYING.GPL3
%{_datadir}/nemo-python/extensions/nemo-audio-tab.py
%{_datadir}/nemo-audio-tab/
%{python3_sitelib}/nemo_audio_tab-%{sversion}.dist-info/


%files -n nemo-pastebin
%doc nemo-pastebin/README
%doc nemo-pastebin/NEWS
%license nemo-pastebin/COPYING
%{_bindir}/nemo-pastebin-configurator
%{_datadir}/nemo-python/extensions/nemo-pastebin.py
%{python3_sitelib}/nemo_pastebin-%{sversion}.dist-info/
%{_datadir}/glib-2.0/schemas/nemo-pastebin.gschema.xml
%{_datadir}/nemo-pastebin/
%{_datadir}/icons/hicolor/*/apps/nemo-pastebin.*

%files -n nemo-fileroller
%doc nemo-fileroller/README
%license nemo-fileroller/COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-fileroller.so

%files -n nemo-python
%doc nemo-python/README
%doc nemo-python/examples
%license nemo-python/COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-python.so
%{_datadir}/nemo-python/
%exclude %{_datadir}/nemo-python/extensions/*

%files -n nemo-python-devel
%{_libdir}/pkgconfig/nemo-python.pc

%files -n nemo-terminal
%doc nemo-terminal/README
%license nemo-terminal/COPYING
%{_bindir}/nemo-terminal-prefs
%{_datadir}/nemo-python/extensions/nemo_terminal.py
%{_datadir}/nemo-terminal/
%{_datadir}/glib-2.0/schemas/org.nemo.extensions.nemo-terminal.gschema.xml
%{python3_sitelib}/nemo_terminal-%{sversion}.dist-info/

%files -n nemo-preview
%doc nemo-preview/README
%license nemo-preview/COPYING
%{_bindir}/nemo-preview
%{_libdir}/nemo-preview/
%{_libexecdir}/nemo-preview-start
%{_datadir}/nemo-preview/
%{_datadir}/dbus-1/services/org.nemo.Preview.service

%files -n nemo-emblems
%license nemo-emblems/COPYING.GPL3
%{_datadir}/nemo-python/extensions/nemo-emblems.py
%{python3_sitelib}/nemo_emblems-%{sversion}.dist-info/

%files -n nemo-image-converter
%doc nemo-image-converter/README
%license nemo-image-converter/COPYING
%{_libdir}/nemo/extensions-3.0/libnemo-image-converter.so
%{_datadir}/nemo-image-converter/

%files -n nemo-compare
%{_bindir}/nemo-compare-preferences
%{_datadir}/nemo-python/extensions/nemo-compare.py
%{_datadir}/nemo-compare/
%{python3_sitelib}/nemo_compare-%{sversion}.dist-info/

%files -n nemo-seahorse
%doc nemo-seahorse/{AUTHORS,COPYING,README,NEWS,ChangeLog}
%{_bindir}/nemo-seahorse-tool
%{_datadir}/glib-2.0/schemas/org.nemo.plugins.seahorse*gschema.xml
%{_datadir}/nemo/actions/nemo-seahorse-*.nemo_action
%{_mandir}/man1/nemo-seahorse-tool.1.*

%changelog
%autochangelog
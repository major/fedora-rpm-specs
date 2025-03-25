%undefine _package_note_file

Name:           rmlint
Version:        2.10.3
Release:        %autorelease
Summary:        Find space waste and other broken things on your filesystem

# GPLv3: main code
# MIT: metrohash
# BSD: xxHash Library
# CC0 or ASL 2.0 or OpenSSL: blake2
# Public code: MurmurHash3, sha3
# Automatically converted from old format: GPLv3 and MIT and BSD and (CC0 or ASL 2.0 or OpenSSL) and Public Domain - review is highly recommended.
License:        GPL-3.0-only AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND (CC0-1.0 OR Apache-2.0 OR OpenSSL) AND LicenseRef-Callaway-Public-Domain

URL:            https://rmlint.rtfd.org
Source0:        https://github.com/sahib/rmlint/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Add-RPM_BUILD_ROOT-to-env.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  scons

BuildRequires:  elfutils-libelf-devel
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libblkid-devel
BuildRequires:  sqlite-devel

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

Provides:       bundled(blake2)
Provides:       bundled(sha3)
Provides:       bundled(xxhash)
Provides:       bundled(metrohash)
Provides:       bundled(murmurhash3)

# Split into two sub-packages since v2.10.3.
# Can be removed in F44+.
Obsoletes:      %{name} < 2.10.3

%package gui
Summary:        %{summary}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       gtksourceview4

# Can be removed in F44+.
Obsoletes:      %{name} < 2.10.3

%description gui
rmlint-gui (a.k.a. Shredder) is a graphical user interface to rmlint.
It uses rmlint to find space waste and other broken things on your filesystem
and offers to remove them.


%description
rmlint finds space waste and other broken things and offers to remove it.
It is an extremely fast tool to remove duplicates from your filesystem.

%global rmlint_scons_flags --prefix="%{buildroot}%{_prefix}" --actual-prefix="%{_prefix}" --libdir="%{_lib}" --without-compile-glib-schemas DEBUG=1 SYMBOLS=1 VERBOSE=1

%prep
%autosetup -p1
for f in `find gui/shredder -name "*.py"`; do
    sed '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done

desktop-file-edit \
	--set-key "Exec" --set-value "shredder" \
	--remove-key "TryExec" \
	gui/shredder.desktop


%build
scons config %{?_smp_mflags} %{rmlint_scons_flags}
scons


%install
scons install %{rmlint_scons_flags}
%find_lang %{name}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/shredder.desktop


%files -f %{name}.lang
%doc README.rst
%license COPYING
%{_bindir}/rmlint
%{_mandir}/man1/rmlint.1*

%files gui
%{_bindir}/shredder
%{_datadir}/applications/shredder.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Shredder.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/shredder.svg
%{python3_sitelib}/shredder/
%{python3_sitelib}/shredder-%{version}-py*.egg-info

%changelog
%autochangelog

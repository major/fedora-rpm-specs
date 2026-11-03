%undefine _package_note_file

Name:           rmlint
Version:        2.11.0
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
Patch1:         0001-unbundle-blake3.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  scons

BuildRequires:  blake3-devel
BuildRequires:  elfutils-libelf-devel
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libblkid-devel
BuildRequires:  sqlite-devel

BuildRequires:  python3-build
BuildRequires:  python3-devel
BuildRequires:  python3-installer
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%global with_pytest 0
%if 0%{?with_pytest}
BuildRequires:  python3dist(blake3)
BuildRequires:  python3dist(py-cpuinfo)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(xattr)
BuildRequires:  python3dist(xxhash)
BuildRequires:  python3-pytest
%endif

Provides:       bundled(blake2)
Provides:       bundled(sha3)
Provides:       bundled(xxhash)
Provides:       bundled(metrohash)
Provides:       bundled(murmurhash3)

%package gui
Summary:        %{summary}
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       gtksourceview4

%global shredder_rtld io.github.sahib.rmlint.Shredder

%description gui
rmlint-gui (a.k.a. Shredder) is a graphical user interface to rmlint.
It uses rmlint to find space waste and other broken things on your filesystem
and offers to remove them.


%description
rmlint finds space waste and other broken things and offers to remove it.
It is an extremely fast tool to remove duplicates from your filesystem.

%global rmlint_scons_flags --without-compile-glib-schemas DEBUG=0 SYMBOLS=1 VERBOSE=1 PREFIX=%{_prefix} LIBDIR=%{_lib} DESTDIR=%{buildroot}

%prep
%autosetup -p1
rm -rf lib/checksums/blake3/

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
scons --show-config %{?_smp_mflags} %{rmlint_scons_flags}


%install
scons install %{rmlint_scons_flags}
%find_lang %{name}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{shredder_rtld}.desktop
%if 0%{?with_pytest}
%pytest
%endif


%files -f %{name}.lang
%doc README.rst
%license COPYING
%{_bindir}/rmlint
%{_mandir}/man1/rmlint.1*

%files gui
%{_bindir}/shredder
%{_datadir}/applications/%{shredder_rtld}.desktop
%{_datadir}/glib-2.0/schemas/%{shredder_rtld}.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/shredder.svg
%{python3_sitelib}/shredder/
%{python3_sitelib}/shredder-%{version}.dist-info/

%changelog
%autochangelog

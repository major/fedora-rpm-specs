# https://github.com/swami/libinstpatch/issues/34
#
# Since this has never worked, we do not have %%files entries for the result.
%bcond introspection 0

Name:           libinstpatch
Version:        1.1.6
%global api_version 1.0
%global so_version 2
Release:        %autorelease
Summary:        Instrument file software library

URL:            http://www.swamiproject.org/
# The entire source is LGPL-2.1-only, except:
# • The following are LicenseRef-Fedora-Public-Domain:
#     - libinstpatch/md5.{c,h}
#         The algorithm is due to Ron Rivest.  This code was
#         written by Colin Plumb in 1993, no copyright is claimed.
#         This code is in the public domain; do with it what you wish.
#     - examples/create_sf2.c
#         Use this example as you please (public domain)
#     - examples/split_sfont.c
#         Public domain use as you please
#   Texts were added to public-domain-text.txt in fedora-license-data:
#   https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/228
License:        LGPL-2.1-only AND LicenseRef-Fedora-Public-Domain
# Additionally, the following unused files are removed in %%prep:
# • The following are GPL-2.0-only:
#     - utils/ipatch_convert.c
#
# …and the following files are used only for build-time testing and do not
# contribute to the licenses of the binary RPMs:
# • The following are LicenseRef-Fedora-Public-Domain:
#     - tests/*.py
#         License: Public Domain
SourceLicense:  %{license} AND GPL-2.0-only

%global forgeurl https://github.com/swami/libinstpatch
Source:         %{forgeurl}/archive/v%{version}/libinstpatch-%{version}.tar.gz

# Fix warning from libinstpatch-scan.c (gtkdoc)
# https://github.com/swami/libinstpatch/pull/71
Patch:          %{forgeurl}/pull/71.patch
# Rename variables called “bool”
# https://github.com/swami/libinstpatch/pull/80
#
# Fixes failure to compile with GCC 15, where C23 is the default, so bool is a
# keyword.
Patch:          %{forgeurl}/pull/80.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(sndfile)
# GTKDOC_ENABLED
BuildRequires:  pkgconfig(gtk-doc)
%if %{with introspection}
# INTROSPECTION_ENABLED
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%endif

# This is a forked copy:
# Changed so as no longer to depend on Colin Plumb's `usual.h' header
# definitions; now uses stuff from dpkg's config.h.
#  - Ian Jackson <ijackson@nyx.cs.du.edu>.
# Josh Coalson: made some changes to integrate with libFLAC.
# Josh Green: made some changes to integrate with libInstPatch.
Provides:       bundled(md5-plumb)

%description
libInstPatch stands for lib-Instrument-Patch and is a library for processing
digital sample based MIDI instrument “patch” files. The types of files
libInstPatch supports are used for creating instrument sounds for wavetable
synthesis. libInstPatch provides an object framework (based on GObject) to load
patch files into, which can then be edited, converted, compressed and saved.


%package devel
Summary:        Development files for libinstpatch
# The entire source is LGPL-2.1-only, except:
# • The following are LicenseRef-Fedora-Public-Domain:
#     - libinstpatch/md5.{c,h}
#     - examples/create_sf2.c
#     - examples/split_sfont.c
# See the comment above the License field for the base package for full
# details.
# None of the LicenseRef-Fedora-Public-Domain files are included in this
# subpackage.
License:        LGPL-2.1-only

Requires:       libinstpatch%{?_isa} = %{version}-%{release}
Requires:       glib2-devel%{?_isa}
Requires:       libsndfile-devel%{?_isa}

%description devel
The libinstpatch-devel package contains libraries and header files for
developing applications that use libinstpatch.


%package doc
Summary:        Documentation and examples for libinstpatch
BuildArch:      noarch
# The entire source is LGPL-2.1-only, except:
# • The following are LicenseRef-Fedora-Public-Domain:
#     - libinstpatch/md5.{c,h}
#     - examples/create_sf2.c
#     - examples/split_sfont.c
# See the comment above the License field for the base package for full
# details.
#
# The examples are included in this subpackage. The License is implicitly the
# same as the base package.

%description doc
The libinstpatch-doc package contains documentation and examples for
libinstpatch.


%prep
%autosetup -p1

# Remove example for nonexistent Python bindings
find examples -type f -name '*.py' -print -delete


%conf
# We cannot reliably build gtkdoc documentation at the same time as the
# library. It appears that gtkdoc-scangobj attempts to link the library before
# it is built.
#
# The best fix would be to find the missing dependency relationship or other
# problem in the CMake build scripts, but this is not quite obvious.
#
# Historically this could be worked around by setting _smp_ncpus_max to 1, but
# this has stopped working.
#
# Instead, we build with gtkdoc documentation disabled to get the library, then
# enable the gtkdoc documentation and rebuild. This guarantees the library is
# ready when gtkdoc-scangobj runs.
#
# See: 1.1.6: build with GTKDOC_ENABLED=ON fails
#      https://github.com/swami/libinstpatch/issues/65
%cmake \
    -DGTKDOC_ENABLED:BOOL=OFF \
    -DINTROSPECTION_ENABLED:BOOL=\
%{?with_introspection:ON}%{!?with_introspection:OFF} \
    -GNinja


%build
%cmake_build

# Enable the GTK docs and build again.
%{__cmake} %{_vpath_builddir} -DGTKDOC_ENABLED:BOOL=ON
%cmake_build


%install
%cmake_install


%files
%license COPYING
%{_libdir}/libinstpatch-%{api_version}.so.%{so_version}{,.*}


%files devel
%{_includedir}/libinstpatch-%{so_version}/
%{_libdir}/libinstpatch-%{api_version}.so
%{_libdir}/pkgconfig/libinstpatch-%{api_version}.pc


%files doc
%license COPYING
%doc ABOUT-NLS
%doc AUTHORS
%doc ChangeLog
%doc README.md
%doc TODO.tasks
%doc examples/
# gtkdoc
%doc %{_vpath_builddir}/docs/reference/html/


%changelog
%autochangelog

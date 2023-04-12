# https://github.com/swami/libinstpatch/issues/34
#
# Since this has never worked, we do not have %%files entries for the result.
%bcond_with introspection

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
#
# Additionally, the following unused files are removed in %%prep:
# • The following are GPL-2.0-only:
#     - utils/ipatch_convert.c
#
# …and the following files are used only for build-time testing and do not
# contribute to the licenses of the binary RPMs:
# • The following are LicenseRef-Fedora-Public-Domain:
#     - tests/*.py
#         License: Public Domain
License:        LGPL-2.1-only AND LicenseRef-Fedora-Public-Domain

%global forgeurl https://github.com/swami/%{name}/
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

# Fix warning from libinstpatch-scan.c (gtkdoc)
# https://github.com/swami/libinstpatch/pull/71
Patch:          %{forgeurl}/pull/71.patch

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
Summary:        Development files for %{name}
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

Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel%{?_isa}
Requires:       libsndfile-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package doc
Summary:        Documentation and examples for %{name}
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
The %{name}-doc package contains documentation and examples for
%{name}.


%prep
%autosetup -p1

# Remove example for nonexistent Python bindings
find examples -type f -name '*.py' -print -delete


%build
# In the RPM build environment, a parallel build with gtkdoc documentation
# enabled fails with:
#   /usr/bin/ld: cannot find -linstpatch-1.0: No such file or directory
#
# The best fix would be to find the missing dependency relationship or other
# problem in the CMake build scripts, but this is not quite obvious.
#
# Additionally, the problem seems to be triggered by something in the RPM build
# environment (CMake options, CFLAGS, etc.), and we haven’t narrowed this down
# yet, which means we aren’t prepared to report the problem upstream.
# Assistance is welcome.
#
# For now, the workaround is fine on Fedora (although it does not work on
# EPEL7–EPEL9).
%constrain_build -c 1

%cmake \
    -DGTKDOC_ENABLED:BOOL=ON \
    -DINTROSPECTION_ENABLED:BOOL=\
%{?with_introspection:ON}%{!?with_introspection:OFF} \
    -GNinja
%cmake_build


%install
%cmake_install


%files
%license COPYING
%{_libdir}/%{name}-%{api_version}.so.%{so_version}{,.*}


%files devel
%{_includedir}/%{name}-%{so_version}/
%{_libdir}/%{name}-%{api_version}.so
%{_libdir}/pkgconfig/%{name}-%{api_version}.pc


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

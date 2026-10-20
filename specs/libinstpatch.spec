# https://github.com/swami/libinstpatch/issues/34
#
# Since this has never worked, we do not have %%files entries for the result.
%bcond introspection 0

# EPEL doesn’t have the fluid-soundfont-gm
%bcond ctest %{undefined rhel}
# List copied from gcc.spec
# Current as of 16.0.1 (line 83)
# Note that asan is available on all Fedora primary architectures.
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le ppc64p7 s390 s390x %{arm} aarch64 riscv64
%global arch_has_asan 1
%endif

Name:           libinstpatch
Version:        1.1.8
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

BuildSystem:    cmake
BuildOption(conf): -DGTKDOC_ENABLED:BOOL=ON
BuildOption(conf): -DINTROSPECTION_ENABLED:BOOL=%{with introspection}
# Upstream provides no tests.

BuildRequires:  gcc

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
%if %{with ctest}
# Test app loads hard-coded path /usr/share/soundfonts/FluidR3_GM.sf2
BuildRequires:  fluid-soundfont-gm
%if 0%{?arch_has_asan}
BuildRequires:  libasan
%endif
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


%prep -a
# Remove example for nonexistent Python bindings
find examples -type f -name '*.py' -print -delete

# -Werror and similar make sense for upstream CI, but are too strict for
# downstream packaging with various compiler and dependency versions
sed --regexp-extended --in-place \
    's/([" ])-Wfatal-errors([" ])/\1\2/' CMakeLists.txt


%if %{with ctest}
%build -a
# There are no tests that can be run with ctest, but we can build a sample
# application that loads a soundfont from a hard-coded path. There is a
# test-app/Makefile, but the details are rigid and don’t fit well with our
# build process; it’s easier to do this manually.
mkdir --parents %{_vpath_builddir}/test-app
${CC} -c test-app/src/main.c -o %{_vpath_builddir}/test-app/main.o \
    ${CFLAGS} %{?arch_has_asan:-fsanitize=address} -I%{_vpath_builddir} -I. \
    $(pkg-config --cflags glib-2.0 gobject-2.0)
${CC} -o %{_vpath_builddir}/test-app/test_instpa_a \
    %{_vpath_builddir}/test-app/main.o %{?arch_has_asan:-fsanitize=address} \
    ${LDFLAGS} -L%{_vpath_builddir}/libinstpatch \
    -linstpatch-%{api_version} $(pkg-config --libs glib-2.0 gobject-2.0)


%check
LD_LIBRARY_PATH=%{_vpath_builddir}/libinstpatch \
    %{_vpath_builddir}/test-app/test_instpa_a
%endif


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

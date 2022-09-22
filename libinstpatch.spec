# https://github.com/swami/libinstpatch/issues/34
#
# Since this has never worked, we do not have %%files entries for the result.
%bcond_with introspection

# Fails with
# CMake Error: Error required internal CMake variable not set, cmake may not be
#   built correctly.
# Missing variable is:
# CMAKE_FIND_LIBRARY_PREFIXES
#
# When/if this is fixed, we will probably want a -doc subpackage.
%bcond_with gtkdoc

Name:           libinstpatch
Version:        1.1.6
%global api_version 1.0
%global so_version 2
Release:        %autorelease
Summary:        Instrument file software library

URL:            http://www.swamiproject.org/
# The entire source is LGPLv2 except:
#
# Public Domain:
#   libinstpatch/md5.{c,h}
#   examples/*
#
# The resulting effective license is LGPLv2.
License:        LGPLv2
# Additionally, the following unused files are removed in %%prep:
#
# GPLv2:
#   utils/ipatch_convert.c
%global forgeurl https://github.com/swami/%{name}/
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz

%if 0%{?el7}
%global cmake %cmake3
%global cmake_build %cmake3_build
%global cmake_install %cmake3_install
%global ctest %ctest3
%endif

BuildRequires:  cmake%{?el7:3}
BuildRequires:  gcc
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(sndfile)
%if %{with gtkdoc}
# GTKDOC_ENABLED
BuildRequires:  pkgconfig(gtk-doc)
%endif
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
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       glib2-devel%{?_isa}
Requires:       libsndfile-devel%{?_isa}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%if %{with gtkdoc}
%package doc
Summary:        Documentation and examples for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation and examples for
%{name}.
%endif


%prep
%autosetup

# Remove example for nonexistent Python bindings
find examples -type f -name '*.py' -print -delete


%build
%cmake \
    -DGTKDOC_ENABLED:BOOL=%{?with_gtkdoc:ON}%{!?with_gtkdoc:OFF} \
    -DINTROSPECTION_ENABLED:BOOL=\
%{?with_introspection:ON}%{!?with_introspection:OFF} \
    -GNinja
%cmake_build

%install
%cmake_install


%files
%license COPYING
%if %{without gtkdoc}
%doc ABOUT-NLS
%doc AUTHORS
%doc ChangeLog
%doc README.md
%doc TODO.tasks
%endif
%{_libdir}/%{name}-%{api_version}.so.%{so_version}
%{_libdir}/%{name}-%{api_version}.so.%{so_version}.*


%files devel
%if %{without gtkdoc}
%doc examples
%endif
%{_includedir}/%{name}-%{so_version}
%{_libdir}/%{name}-%{api_version}.so
%{_libdir}/pkgconfig/%{name}-%{api_version}.pc

%if %{with gtkdoc}
%files doc
%license COPYING
%doc ABOUT-NLS
%doc AUTHORS
%doc ChangeLog
%doc README.md
%doc TODO.tasks
%doc examples
# TODO: built gtkdoc documentation
%endif


%changelog
%autochangelog

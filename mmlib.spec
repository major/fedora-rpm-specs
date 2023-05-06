Name:           mmlib
Version:        1.4.2
# Upstream users a linker version script, src/libmmlib.map.
%global so_version 1
Release:        %autorelease
Summary:        OS abstraction layer and helpers

License:        Apache-2.0
URL:            https://opensource.mindmaze.com/projects/mmlib
# The GitHub project https://github.com/mmlabs-mindmaze/mmlib is a mirror of
# https://review.gerrithub.io/admin/repos/mmlabs-mindmaze/mmpack.
%global forgeurl https://github.com/mmlabs-mindmaze/mmlib
Source0:        %{forgeurl}/archive/%{version}/mmlib-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
# This is not a Python package, but uses Python scripts in the build process.
BuildRequires:  python3-devel

# tests option
BuildRequires:  pkgconfig(check)

# docs option
#   We do not rebuild the documentation, and do not install Sphinx-generated
#   documentation, because:
#     “Building documentation does not seem to work as expected”
#     https://github.com/mmlabs-mindmaze/mmlib/issues/6
#   Prior to Fedora 39, we also lack the python3dist(linuxdoc) dependency.

# nls option
BuildRequires:  gettext

%global common_description %{expand:
mmlib is an Operating System abstraction layer.

It provides an API for application developer, so that they can write portable
code using relatively advanced OS features without having to care about system
specifics.

The reference design in mind in its conception is POSIX, meaning that if some
posix functionality is not available for given platform, mmlib will implement
that same functionality itself.}

%description %{common_description}


%package devel
Summary:        Development files for mmlib
Requires:       mmlib%{?_isa} = %{version}-%{release}

%description devel %{common_description}

The mmlib-devel package contains libraries and header files for developing
applications that use mmlib.


%prep
%autosetup
%py3_shebang_fix read_version.py


%build
%meson -Dtests=enabled -Ddocs=disabled -Dnls=enabled
%meson_build


%install
%meson_install
%find_lang %{name}
# The files doc/mm*.3 in the source tree are not usable man pages; we would
# have to generate the documentation to get the real man pages.


%check
# Do not run tests in parallel; some are sensitive to execution order.
%meson_test -- --num-processes 1


%files -f %{name}.lang
%license LICENSE
%doc README.md
%doc TODO.md

%{_libdir}/libmmlib.so.%{so_version}{,.*}


%files devel
# Examples would be automatically installed if we enabled the “docs” meson
# option; we choose to install them manually anyway.
%doc doc/examples/

%{_libdir}/libmmlib.so

%{_libdir}/pkgconfig/mmlib.pc

%{_includedir}/mmargparse.h
%{_includedir}/mmdlfcn.h
%{_includedir}/mmerrno.h
%{_includedir}/mmlib.h
%{_includedir}/mmlog.h
%{_includedir}/mmpredefs.h
%{_includedir}/mmprofile.h
%{_includedir}/mmsysio.h
%{_includedir}/mmthread.h
%{_includedir}/mmtime.h


%changelog
%autochangelog

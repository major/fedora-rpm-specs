%bcond tests 1

Name:           v-hacd
Version:        4.1.0
Release:        %autorelease
Summary:        Decomposes a 3D surface into a set of “near” convex parts

# The entire source is BSD-3-Clause, except:
#   - app/wavefront.{h,cpp} are MIT
License:        BSD-3-Clause AND MIT
URL:            https://github.com/kmammou/%{name}
# This has the app/meshes/ directory stripped out. The .obj files therein have
# unclear or unspecified licenses, which makes them unsuitable for Fedora.
#
# Unfortunately, this prevents us from running the example command from
# README.rst as a sanity check.
#
# Generated with ./get_source.sh %%{version}
Source0:        %{name}-%{version}-filtered.tar.xz
# Script to generate Source0; see comments above.
Source1:        get_source.sh
# Man page hand-written for Fedora in groff_man(7) format based on help output
# and README.md contents.
Source2:        TestVHACD.1

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
# Our choice; the make backend would work just fine.
BuildRequires:  ninja-build

%if %{with tests}
BuildRequires:  vtk-data
%endif

%global common_description %{expand:
The V-HACD library decomposes a 3D surface into a set of “near” convex parts.

Why do we need approximate convex decomposition?

Collision detection is essential for realistic physical interactions in video
games and computer animation. In order to ensure real-time interactivity with
the player/user, video game and 3D modeling software developers usually
approximate the 3D models composing the scene (e.g. animated characters, static
objects…) by a set of simple convex shapes such as ellipsoids, capsules or
convex-hulls. In practice, these simple shapes provide poor approximations for
concave surfaces and generate false collision detection.

Convex-hull vs. ACD

A second approach consists in computing an exact convex decomposition of a
surface S, which consists in partitioning it into a minimal set of convex
sub-surfaces. Exact convex decomposition algorithms are NP-hard and
non-practical since they produce a high number of clusters. To overcome these
limitations, the exact convexity constraint is relaxed and an approximate
convex decomposition of S is instead computed. Here, the goal is to determine a
partition of the mesh triangles with a minimal number of clusters, while
ensuring that each cluster has a concavity lower than a user defined
threshold.}

%description %{common_description}


%package        devel
Summary:        Development files for V-HACD

# The MIT-licensed app/wavefront.{h,cpp} do not contribute to this subpackage.
License:        BSD-3-Clause


BuildArch:      noarch

# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_packaging_header_only_libraries
Provides:       %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel %{common_description}

The %{name}-devel package contains the header-only library for developing
applications that use V-HACD.


%package        tools
Summary:        Command-line tools based on the V-HACD library

License:        BSD-3-Clause AND MIT

# The files app/wavefront.{h,cpp} are attributed to John W. Ratcliff and were
# likely originally published on https://codesuppository.blogspot.com/. They
# were never part of a maintained, versioned library, and the original context
# is now unclear, so we do not treat this as a case of bundling.

%description    tools %{common_description}

The %{name}-tools package contains command-line tools based on the V-HACD
library. Currently, this means TestVHACD; despite the name, this tool has
general utility beyond testing.


%prep
%autosetup -n %{name}-%{version}


%build
pushd app >/dev/null
%cmake -GNinja
%cmake_build
popd >/dev/null


%install
pushd app >/dev/null
# There are currently no install targets in app/CMakeLists.txt, so
# %%cmake_install will not work. We install the executable manually instead.
install -t '%{buildroot}%{_bindir}' -p -D '%{_vpath_builddir}/TestVHACD'
popd >/dev/null

install -t '%{buildroot}%{_includedir}' -m 0644 -p -D 'include/VHACD.h'

install -t '%{buildroot}%{_mandir}/man1' -m 0644 -p -D '%{SOURCE2}'


%if %{with tests}
%check
# Use the example from README.md as a sanity check, but use an arbitrary mesh
# from vtk as input since we cannot ship upstream’s sample meshes. Decrease the
# max recursion depth from 15 to the default (10) so this doesn’t explode on
# 32-bit ARM in Fedora 36.
%{buildroot}%{_bindir}/TestVHACD \
    %{_datadir}/vtkdata/Testing/Data/Viewpoint/cow.obj \
    -e 0.01 -d 10 -r 10000000 -r 128
%endif


%files devel
%license LICENSE

%doc README.md
# Contains PNG images for rendered README.md
%doc doc/

%{_includedir}/VHACD.h


%files tools
%license LICENSE

%{_bindir}/TestVHACD
%{_mandir}/man1/TestVHACD.1*


%changelog
%autochangelog

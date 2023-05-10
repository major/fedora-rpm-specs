Name:           python-trimesh
Version:        3.21.6
Release:        %autorelease
Summary:        Import, export, process, analyze and view triangular meshes

# The entire source is (SPDX) MIT, except:
#   - trimesh/transformations.py is BSD-3-Clause
#   - trimesh/exchange/openctm.py is Zlib
# Additionally, the following are under the same (SPDX) MIT license as the
# overall source, but with a different copyright statement:
License:        MIT AND BSD-3-Clause AND Zlib
URL:            https://trimsh.org
Source0:        https://github.com/mikedh/trimesh/archive/%{version}/trimesh-%{version}.tar.gz

# The combination of an arched package with only noarch binary packages makes
# it easier for us to detect arch-dependent test failures, since the tests will
# always be run on every platform, and easier for us to skip failing tests if
# necessary, since we can be sure that %%ifarch macros work as expected.
#
# Since the package still contains no compiled machine code, we still have no
# debuginfo.
%global debug_package %{nil}

# Turn off automatic python byte-compilation. One .py file,
# trimesh/resources/templates/blender_boolean.py, is actually a *template for a
# Python source* rather than an *actual Python source*, and trying to
# byte-compile it will break the build. We will byte-compile manually instead.
%undefine __brp_python_bytecompile

BuildRequires:  python3-devel

# See the definition of requirements_test, which corresponds to the “test”
# extra, in setup.py; however, we do not generate BuildRequires from the “test”
# extra because most of the dependencies are for linting or coverage and would
# need to be patched out:
#   https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# run all unit tests
BuildRequires:  python3dist(pytest)
# use as a validator for exports
BuildRequires:  python3dist(ezdxf)

# Run tests in parallel:
BuildRequires:  python3dist(pytest-xdist)

# Command-line tools that are (optional) test dependencies:
#
# tests/test_export.py, tests/generic.py
# Meshlab Server Does Not Work With XVFB
# https://github.com/cnr-isti-vclab/meshlab/issues/237
# Upstream closed as WONTFIX
#BuildRequires:  /usr/bin/xvfb-run
#BuildRequires:  /usr/bin/meshlabserver
# tests/test_gltf.py
# Not yet packaged: https://github.com/KhronosGroup/glTF-Validator
#BuildRequires:  /usr/bin/gltf_validator

%global _description %{expand:
Trimesh is a pure Python library for loading and using triangular meshes with
an emphasis on watertight meshes. The goal of the library is to provide a fully
featured and well tested Trimesh object which allows for easy manipulation and
analysis, in the style of the Polygon object in the Shapely library.}

%description %{_description}


%package -n     python3-trimesh
Summary:        %{summary}
BuildArch:      noarch

Recommends:     python3-trimesh+easy = %{version}-%{release}
Suggests:       python3-trimesh+all = %{version}-%{release}

# A number of external command-line executables provide optional functionality.
# We choose to make these weak dependencies (Recommends). Hints (Suggests)
# would also be justifiable—although it should be noted that dnf does not do
# anything with hints. Any weak dependencies should also be BuildRequires so
# that their satisfiability is verified at build time; some may also enable
# additional tests.
#
# trimesh.exchange.binvox
# Cannot be packaged (closed-source): https://www.patrickmin.com/binvox/
#BuildRequires:  /usr/bin/binvox
#Recommends:     /usr/bin/binvox
# trimesh.interfaces.blender
%ifnarch %{ix86}
BuildRequires:  /usr/bin/blender
Recommends:     /usr/bin/blender
%endif
# trimesh.exchange.ply
%ifnarch s390x
# ExportTest.test_export fails with:
#   subprocess.CalledProcessError: Command '['/usr/bin/draco_encoder', '-qp',
#   '28', '-i', '/tmp/tmpd1uz557y.ply', '-o', '/tmp/tmpkbowi3es.drc']' died
#   with <Signals.SIGABRT: 6>.
# and stderr is:
#   terminate called after throwing an instance of 'std::bad_alloc'
#     what():  std::bad_alloc
# See also:
#   gtest failure on s390x
#   https://bugzilla.redhat.com/show_bug.cgi?id=2165173
# We conclude that draco is not necessarily usable on this platform.
BuildRequires:  /usr/bin/draco_decoder
Recommends:     /usr/bin/draco_decoder
BuildRequires:  /usr/bin/draco_encoder
Recommends:     /usr/bin/draco_encoder
%endif
# “openscad”: trimesh.interfaces.scad
# Library would also recognize “OpenSCAD”
%ifnarch %{ix86}
BuildRequires:  /usr/bin/openscad
Recommends:     /usr/bin/openscad
%endif
# trimesh.interfaces.vhacd
# Library would also recognize “vhacd” or “testVHACD”
#
# VHACD 4.0 not working through trimesh interface + dirty fix
# https://github.com/mikedh/trimesh/issues/1788
#BuildRequires:  /usr/bin/TestVHACD
#Recommends:     /usr/bin/TestVHACD

# This probably should be in [easy] extra but isn’t in the metadata at all; see
# README.rst and trimesh/ray/. However, it cannot be packaged until it supports
# the current version (3.x) of embree
# (https://github.com/scopatz/pyembree/issues/28).
#Recommends:     python3dist(pyembree)

%description -n python3-trimesh %{_description}


%if 0%{?fedora} > 38
%pyproject_extras_subpkg -n python3-trimesh easy all
%else
# We base these extras metapackages
# (https://fedoraproject.org/wiki/Changes/PythonExtras#Extras_metapackages)
# on the expansion of:
#
#   %%pyproject_extras_subpkg -n python3-trimesh easy all
#
# but add Provides/Obsoletes for the corresponding old subpackages to provide a
# clean upgrade path.

%package -n python3-trimesh+easy
Summary:        Metapackage for python3-trimesh: easy extras
BuildArch:      noarch

Requires:       python3-trimesh = %{version}-%{release}

Provides:       python3-trimesh-easy = %{version}-%{release}
Obsoletes:      python3-trimesh-easy < 3.9.20-4

%description -n python3-trimesh+easy
This is a metapackage bringing in easy extras requires for python3-trimesh.
It makes sure the dependencies are installed.

%files -n python3-trimesh+easy
%ghost %{python3_sitelib}/*.dist-info

%package -n python3-trimesh+all
Summary:        Metapackage for python3-trimesh: all extras
BuildArch:      noarch

Requires:       python3-trimesh = %{version}-%{release}

Provides:       python3-trimesh-all = %{version}-%{release}
Obsoletes:      python3-trimesh-all < 3.9.20-4

%description -n python3-trimesh+all
This is a metapackage bringing in all extras requires for python3-trimesh.
It makes sure the dependencies are installed.

%files -n python3-trimesh+all
%ghost %{python3_sitelib}/*.dist-info
%endif


# We elect not to build a documentation package, for the following reasons:
#
#  1. A (relatively simple) patch is required to build them offline without
#     pip-installing requirements from PyPI.
#  2. The documentation includes notebooks translated to HTML from .ipynb
#     using nbconvert.
#      a. Some conversions fail (wholly or on a per-cell basis, if continuing
#         on errors is requested) in architecture-dependent ways. This means
#         that the contents of the documentation package would depend on the
#         builder architecture, and it could not be noarch—an undesirable
#         situation.
#      b. An “HTML-ified” notebook contains a blob of JavaScript and other
#         web assets that is exceptionally difficult (at best, tedious) to
#         account for under current bundling guidelines.
#  3. Sphinx-generated HTML documentation is not suitable for packaging in
#     general—see https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for
#     discussion—and (because of the notebooks, if nothing else) the trimesh
#     documentation is not well-suited to building as a PDF instead of HTML.


%prep
%autosetup -n trimesh-%{version} -p1

# Patch out unavailable dependencies from “extras”:
#
# [all]
#   glooey: not yet packaged, https://github.com/kxgames/glooey; needs fonts
#           that are not currently packaged unbundled from its assets
sed -r -i "/^[[:blank:]]*'glooey',/d" setup.py
#   meshio: not yet packaged, https://github.com/nschloe/meshio
sed -r -i "/^[[:blank:]]*'meshio',/d" setup.py
#   python-fcl: not yet packaged; upstream is not compatible with the current
#               release of fcl,
#               https://github.com/BerkeleyAutomation/python-fcl/issues/19
sed -r -i "/^[[:blank:]]*'python-fcl',/d" setup.py
#   xatlas: not yet packaged, https://github.com/mworchel/xatlas-python;
#           depends on https://github.com/jpcy/xatlas, also not yet packaged
sed -r -i "/^[[:blank:]]*'xatlas',/d" setup.py

# Stub out unavailable pyinstrument test dependency; we don’t really need to do
# profiling anyway. Note that this does mean that API function
# trimesh.viewer.windowed.SceneViewer(…) will not work with “profile=True”.
#
# Packaging pyinstrument would be difficult due to a vue.js-based HTML
# renderer. Since guidelines forbid pre-built minified or compiled JS or CSS,
# this would have to be patched out, or the web asset pipeline would have to be
# somehow executed in the RPM build environment. (Or, of course, we can
# continue to do without pyinstrument.)
mkdir -p _stub
cat > _stub/pyinstrument.py <<'EOF'
class Profiler(object):
    def __enter__(self, *args, **kwds):
        return self

    def __exit__(self, *args, **kwds):
        return False

    def output_text(self, *args, **kwds):
        return """
Profiling output would be here if pyinstrument were available.
"""
EOF
sed -r -i "/'pyinstrument',/d" setup.py


%generate_buildrequires
%pyproject_buildrequires -x all


%build
%pyproject_wheel


%install
%pyproject_install
# Manual byte-compile, to skip that one troublesome “.py” template file:
find '%{buildroot}%{python3_sitelib}/trimesh' -type f \
    -name '*.py' ! -name 'blender_boolean.py' |
  while read -r pyfile
  do
    %py_byte_compile %{__python3} "${pyfile}"
  done
# Cannot handle skipping byte-compilation for blender_boolean.py:
#pyproject_save_files trimesh


%check
while read -r t
do
  k="${k-}${k+ and }not ($(sed -r 's/::/ and /' <<<"${t}"))"
done < <(sed -r '/^[[:blank:]]*($|#)/d' <<'EOF'
# Two new failures in tests/test_boolean.py with Blender 3.5.0
# https://github.com/mikedh/trimesh/issues/1894
BooleanTest::test_boolean
BooleanTest::test_multiple

%ifnarch x86_64
# CacheTest.test_hash fails, or may fail, because xxhash is not faster than CRC
# and/or MD5.
#
# This is not as intended, and upstream might or might not care, but it’s only
# a performance defect, so we just skip the test here.
CacheTest::test_hash
%endif

%ifarch s390x
# Several test failures remain on s390x. For now, we choose to skip these tests
# rather than excluding the architecture, even though they certainly represent
# real defects.
#
# https://github.com/mikedh/trimesh/issues/1351
# https://github.com/mikedh/trimesh/files/7385479/test-failures.log
GLTFTest::test_export_custom_attributes
OBJTest::test_vertex_color
PermutateTest::test_permutate
PlyTest::test_face_attributes
PlyTest::test_uv_export
PlyTest::test_vertex_attributes
%endif

# 32-bit problems:
# https://github.com/mikedh/trimesh/issues/690
# https://github.com/mikedh/trimesh/files/7389423/test-failures.log

# E           TypeError: Cannot cast array data from dtype('int64') to
#                        dtype('int32') according to the rule 'safe'
%if 0%{?__isa_bits} == 32
BinvoxTest::test_load_save_invariance
BoundsTest::test_bounding_egg
ContainsTest::test_inside
EncodingTest::test_composite
EncodingTest::test_dense
EncodingTest::test_flat
EncodingTest::test_flipped
EncodingTest::test_reshape
EncodingTest::test_transpose
NearestTest::test_coplanar_signed_distance
PrimitiveTest::test_cyl_buffer
RayTests::test_contain_single
RayTests::test_contains
RayTests::test_on_edge
RayTests::test_on_vertex
RleTest::test_brle_encode_decode
RleTest::test_brle_length
RleTest::test_brle_logical_not
RleTest::test_brle_to_dense
RleTest::test_brle_to_rle
RleTest::test_rle_encode_decode
SampleTest::test_sample_volume
SubdivideTest::test_loop_correct
VoxelGridTest::test_local
VoxelGridTest::test_roundtrip
%endif

# Either MemoryError or numpy.core._exceptions._ArrayMemoryError:
%if 0%{?__isa_bits} == 32
GLTFTest::test_basic
GLTFTest::test_merge_buffers
MutateTests::test_not_mutated_cube
SubDivideTest::test_subdivide
SceneTests::test_scene
%endif
EOF
)

export PYTHONPATH="${PWD}/_stub:%{buildroot}%{python3_sitelib}"
%pytest -v -k "${k-}" -n auto


%files -n python3-trimesh
%license LICENSE.md
%doc README.md
# %%pyproject_save_files cannot handle skipping byte-compilation for
# blender_boolean.py, so we list files manually:
%{python3_sitelib}/trimesh
%{python3_sitelib}/trimesh-%{version}.dist-info


%changelog
%autochangelog

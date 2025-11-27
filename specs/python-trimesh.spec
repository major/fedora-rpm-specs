%bcond blender 1
%bcond skimage 1

Name:           python-trimesh
Version:        4.10.0
Release:        %autorelease
Summary:        Import, export, process, analyze and view triangular meshes

# The entire source is (SPDX) MIT, except:
#   - trimesh/transformations.py is BSD-3-Clause
# Additionally, the following are under the same (SPDX) MIT license as the
# overall source, but with a different copyright statement:
#   - trimesh/viewer/trackball.py
License:        MIT AND BSD-3-Clause
URL:            https://trimsh.org
Source0:        https://github.com/mikedh/trimesh/archive/%{version}/trimesh-%{version}.tar.gz
# Man page hand-written for Fedora in groff_man(7) format based on --help
# output and on the docstring of trimesh.__main__.main
Source1:        trimesh.1

BuildSystem:            pyproject
# With v4, [all] = [easy,recommend,test,test_more,deprecated].
BuildOption(generate_buildrequires): -x easy,recommend,test,test_more

# The combination of an arched package with only noarch binary packages makes
# it easier for us to detect arch-dependent test failures, since the tests will
# always be run on every platform, and easier for us to skip failing tests if
# necessary, since we can be sure that %%ifarch macros work as expected.
#
# Since the package still contains no compiled machine code, we still have no
# debuginfo.
%global debug_package %{nil}

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Turn off automatic python byte-compilation. One .py file,
# trimesh/resources/templates/blender_boolean.py, is actually a *template for a
# Python source* rather than an *actual Python source*, and trying to
# byte-compile it will break the build. We will byte-compile manually instead.
%undefine __brp_python_bytecompile

BuildRequires:  python3-devel
BuildRequires:  tomcli

# Run tests in parallel:
BuildRequires:  %{py3_dist pytest-xdist}

# Command-line tools that are (optional) test dependencies:
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
Recommends:     python3-trimesh+recommend = %{version}-%{release}

# The source trimesh-4.10.0/trimesh/viewer/trackball.py is copied from an
# unspecified version of pyrender.
Provides:       bundled(python3dist(pyrender))

# The [recommends] extra was renamed to [recommend] for v4.
Obsoletes:      python3-trimesh+recommends < 4.0.0~~dev0-1
# In v4, the [all] extra became the same as [easy,recommend,test]. Since we
# don’t want to package the [test] extra, we no longer package [all]. If any
# package depends on it (unlikely), the dependency should be changed to
# [easy,recommend], and it should be suggested to upstream that this is really
# what they needed anyway.
Obsoletes:      python3-trimesh+all < 4.0.0~~dev0-1

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
%if %{with blender}
# trimesh.interfaces.blender
# Since 5.0.0, Blender doesn’t support big-endian architectures.
BuildRequires:  (/usr/bin/blender or python3(s390-64))
Recommends:     (/usr/bin/blender or python3(s390-64))
%endif
# trimesh.graph
BuildRequires:  /usr/bin/dot
Recommends:     /usr/bin/dot
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
BuildRequires:  /usr/bin/openscad
Recommends:     /usr/bin/openscad

# This probably should be in the [easy] extra but isn’t in the metadata at all;
# see README.rst and trimesh/ray/. However, it cannot be packaged until it
# supports the current version (3.x) of embree
# (https://github.com/scopatz/pyembree/issues/28).
#Recommends:     python3dist(pyembree)

%description -n python3-trimesh %{_description}


# We skip packaging the “deprecated” extra, since we no longer wish to maintain
# python-openctm. We therefore cannot package the “all” extra, either.
%pyproject_extras_subpkg -n python3-trimesh -a easy
# Note that the "recommend" extra does have an arch-dependent dependency.
%pyproject_extras_subpkg -n python3-trimesh recommend


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


%prep -a
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

    def print(self, *args, **kwds):
        return self.output_text(*args, **kwds)
EOF

# Patch out unavailable dependencies from extras:

# easy extra:
#   embreex: not packaged, https://github.com/mikedh/embreeX; this would
#            require version 2.x of embree, which was once available in a
#            compat package (https://src.fedoraproject.org/rpms/embree2) but
#            was retired; the current version was 4.x.
#   manifold3d: not yet packaged, https://github.com/elalish/manifold/
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.easy' '(embreex|manifold3d)\b.*'

# recommend extra:
#   pyglet: incompatible version 2.x, beginning with F41. See “Path to
#           supporting Pyglet 2?” https://github.com/mikedh/trimesh/issues/2155
#   manifold3d: not yet packaged, https://github.com/elalish/manifold/
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.recommend' '(pyglet|manifold3d)\b.*'
%if %{without skimage}
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.recommend' 'scikit-image\b.*'
%endif
%ifarch s390x
# The python-cascadio package is currently ExcludeArch: s390x
# python-cascadio: Tests for cascadio fail on s390x, wrong endianness
# https://bugzilla.redhat.com/show_bug.cgi?id=2298452
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.recommend' 'cascadio\b.*'
%endif

# test extra:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#   pytest-cov: linters/coverage/etc.
#   pyinstrument: not packaged; see “stub” workaround in %%prep
#   ruff: linters/coverage/etc.
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.test' '(pytest-cov|pyinstrument|ruff)\b.*'

# test_more extra:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#   coveralls: linters/coverage/etc.
#   pyright: linters/coverage/etc.
#   xatlas: not yet packaged, https://github.com/mworchel/xatlas-python;
#           depends on https://github.com/jpcy/xatlas, also not yet packaged
#   pytest-beartype: linters/coverage/etc.
#   pymeshlab: not yet packaged
#   triangle: nonfree license
#   marimo: not yet packaged
tomcli set pyproject.toml lists delitem \
    'project.optional-dependencies.test_more' \
    '(coveralls|pyright|xatlas|pytest-beartype|pymeshlab|triangle|marimo)\b.*'


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

install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 -D '%{SOURCE1}'


%check
# We cannot use %%pyproject_check_import without %%pyproject_save_files.

while read -r t
do
  k="${k-}${k+ and }not ($(sed -r 's/::/ and /' <<<"${t}"))"
done < <(sed -r '/^[[:blank:]]*($|#)/d' <<'EOF'
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
# Regressions in test_boolean.py with Blender 4.2.0
# https://github.com/mikedh/trimesh/issues/2267
# Fixed in trimesh 4.4.7, except on s390x:
# https://github.com/mikedh/trimesh/issues/2267#issuecomment-2302365583
# https://github.com/mikedh/trimesh/issues/2267#issuecomment-2414122193
test_boolean
test_multiple
test_multiple_difference
%endif

# This has been observed failing on at least x86_64, ppc64le, and s390x.
# https://github.com/mikedh/trimesh/issues/1351#issuecomment-2964820046
# https://github.com/mikedh/trimesh/issues/1351#issuecomment-3016671094
test_data_model

# This test fails if it doesn’t finish within 30 seconds, and executing it in
# parallel with other tests tends to slow it down too much. We exclude it here,
# then run it serially on its own.
test_obb_mesh_large

# Hangs flakily since 4.10.0; cannot reproduce in a git checkout
# tests/test_primitives.py::test_primitives
# (Unfortunately, there are other test called test_primitives that this will
# also skip.)
test_primitives
EOF
)

export PYTHONPATH="${PWD}/_stub:%{buildroot}%{python3_sitelib}"
%pytest -v -k "${k-}" -n auto
%pytest -v -k 'test_obb_mesh_large'


%files -n python3-trimesh
%license LICENSE.md
%doc README.md
# %%pyproject_save_files cannot handle skipping byte-compilation for
# blender_boolean.py, so we list files manually:
%{python3_sitelib}/trimesh
%{python3_sitelib}/trimesh-%{version}.dist-info

%{_bindir}/trimesh
%{_mandir}/man1/trimesh.1*


%changelog
%autochangelog

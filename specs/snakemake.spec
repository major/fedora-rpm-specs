# Work around a series of circular test dependencies:
#
# python-snakemake-interface-scheduler-plugins
# │￪ python-snakemake-interface-report-plugins
# ￬│ ￬￪   ⬐───╮
# snakemake → python-snakemake-interface-executor-plugins⬎
#   ￪￪￪ │ ⬑────────────────────python-snakemake-executor-plugin-cluster-generic
#   │││ ↳python-snakemake-interface-storage-plugins─────────────────╮
#   │││                                           ￬────────────────╮│
#   ││╰────────────────────────python-snakemake-storage-plugin-http││
#   │╰─────────────────────────python-snakemake-storage-plugin-s3🠔─╯│
#   ╰──────────────────────────python-snakemake-storage-plugin-fs🠔──╯
#
# A good build order is:
#
#   1. BOOTSTRAP: python-snakemake-interface-common
#      python-snakemake-interface-executor-plugins,
#      python-snakemake-interface-storage-plugins,
#      python-snakemake-interface-report-plugins
#   2. BOOTSTRAP: snakemake
#   3. python-snakemake-executor-plugin-cluster-generic,
#      python-snakemake-storage-plugin-http,
#      python-snakemake-storage-plugin-s3,
#      python-snakemake-storage-plugin-fs
#   4. snakemake, python-snakemake-interface-executor-plugins,
#      python-snakemake-interface-storage-plugins,
#      python-snakemake-interface-report-plugins
#      python-snakemake-interface-scheduler-plugins
%bcond bootstrap 0
%bcond tests %{without bootstrap}
# Run tests that require network access? This only makes sense for local mock
# builds in combination with --enable-network.
%bcond network_tests 0
# Almost all of the conda tests require network access, but there are also
# other failures that are not straightforward to understand.
%bcond conda_tests 0
%bcond gcs_tests 1

Name:           snakemake
Version:        9.11.6
%global srcversion %(echo '%{version}' | cut -d '^' -f 1)
Release:        %autorelease
Summary:        Workflow management system to create reproducible and scalable data analyses

# The primary license for Snakemake is MIT; web assets contribute a variety of
# other licenses.
#
# Apache-2.0 AND BSD-2-Clause AND BSD-3-CLause AND ISC AND MIT AND MIT-0:
# - src/snakemake/assets/data/vega/vega.js
#
# BSD-3-Clause AND MIT:
# - src/snakemake/assets/data/vega-lite/vega-lite.js
#
# BSD-3-Clause AND ISC AND MIT:
# - src/snakemake/assets/data/vega-embed/vega-embed.js
#
# MIT:
# - All Snakemake code unless otherwise noted
# - heroicons: It is unclear if anything derived from heroicons is actually
#   present in the package, but upstream carries a copy of its license file, so
#   we mention the possibility.
# - src/snakemake/assets/data/prop-types/prop-types.min.js
# - src/snakemake/assets/data/tailwindcss/tailwind.css
#
# == License breakdown: src/snakemake/assets/data/vega/vega.js ==
#
# The primary license for npm(vega) is BSD-3-Clause. The bundle contains:
#
# Apache-2.0:
# - apache-commons-math, from which an implementation of erfinv is derived
# BSD-2-Clause:
# - npm(esprima), bundled as a copied, derived, or adapted snippet
# BSD-3-Clause:
# - npm(vega) and various npm(vega-*) libraries
# - npm(d3-contour), bundled as a copied, derived, or adapted snippet
# - npm(d3-regression), bundled as a copied, derived, or adapted snippet
# - npm(science), bundled as a copied, derived, or adapted snippet
# - npm(shapefile), bundled as a copied, derived, or adapted snippet
# ISC:
# - various npm(d3-*) libraries
# - npm(delaunator)
# - npm(quickselect)
# - npm(topojson-client)
# ISC AND MIT:
# - npm(d3-geo) (MIT is due to some code being derived from GeographicLib)
# - npm(d3-geo-projection) (MIT is due to some code being derived from
#   https://github.com/scijs/integrate-adaptive-simpson)
# MIT:
# - npm(@types/estree)
# - npm(hashlru), bundled as a copied, derived, or adapted snippet
# - npm(regression), bundled as a copied, derived, or adapted snippet
# MIT-0:
# - npm(fabric), bundled as a copied, derived, or adapted snippet
#
# == License breakdown: src/snakemake/assets/data/vega-lite/vega-lite.js ==
#
# The primary license for npm(vega-lite) is BSD-3-Clause. The bundle contains:
#
# BSD-3-Clause:
# - npm(vega-lite) and various npm(vega-*) libraries
# MIT:
# - npm(@types/clone)
# - npm(@types/estree)
# - npm(clone)
# - npm(fast-deep-equal)
# - npm(fast-json-stable-stringify)
# - npm(hashlru), bundled as a copied, derived, or adapted snippet
# - npm(json-stringify-pretty-compact)
#
# == License breakdown: src/snakemake/assets/data/vega-embed/vega-embed.js ==
#
# The primary license for npm(vega-embed) is BSD-3-Clause. The bundle contains:
#
# BSD-3-Clause:
# - npm(vega-embed) and various npm(vega-*) libraries
# ISC:
# - npm(semver)
# MIT:
# - npm(fast-json-patch)
# - npm(json-stringify-pretty-compact)
License:        %{shrink:
                Apache-2.0 AND
                BSD-2-Clause AND
                BSD-3-Clause AND
                ISC AND
                MIT AND
                MIT-0
                }
URL:            https://snakemake.readthedocs.io/en/stable/index.html
%global forgeurl https://github.com/snakemake/snakemake
# We could use the PyPI sdist, which already contains the HTML report assets,
# but we would lose at least the vim extensions and changelog, and we would
# have to nontrivially modify the sdist to remove a CC0-1.0-licensed polyfill
# before uploading it to the lookaside cache, so doing so would not be
# meaningfully easier than using the GitHub archive with an additional source
# for the assets.
Source0:        %{forgeurl}/archive/v%{version}/snakemake-%{version}.tar.gz
# The assets for HTML reports are normally downloaded in setup.py when creating
# the sdist. We use a script, Source2, executed with no arguments (implicitly
# relying on the spec file in the same directory) to download the assets,
# modify them as necessary, and pack them into an additional source archive.
Source1:        snakemake-%{version}-assets.tar.zst
Source2:        get_assets

# Downstream-only: adjust the asset metadata in the sources, including
# checksums, for any adjustments that happened in the get_assets script.
#
# When the get_assets script unpacks and patches Source0 in order to use it to
# download assets, it skips this patch, because we need to first fetch the
# original assets in order to then modify them. The signal for this behavior is
# the substring "modified-assets" in the patch name.
Patch:          snakemake-9.1.1-modified-assets.patch

BuildSystem:            pyproject
# Generate BR’s for all supported extras to ensure they do not FTI
BuildOption(generate_buildrequires): -x reports
BuildOption(install):   -l snakemake
BuildOption(check):     %{shrink:
                        -e '*.tests*'
                        %{?!with_gcs_tests:-e 'snakemake.executors.google_lifesciences_helper'}
                        }

BuildArch:      noarch

BuildRequires:  help2man

# Snakemake uses (unversioned) "python" as the default remote execution
# command. Because remote hosts could be Windows machines, and those are likely
# to lack "python3.exe" (see https://github.com/python/cpython/issues/99185),
# we didn’t try to convince upstream to change this. Instead, we (reluctantly)
# just make sure that our own Snakemake installations are compatible by
# depending on python-unversioned-command.
BuildRequires:  python-unversioned-command
Requires:       python-unversioned-command

BuildRequires:  vim-filesystem
Requires:       vim-filesystem

# Required for snakemake.script.RScript, snakemake.notebook.RJupyterNotebook
# (Some of the tests in tests/tests_using_conda.py require this.)
BuildRequires:  R-core
Recommends:     R-core

Provides:       vim-snakemake = %{version}-%{release}

# Regarding pre-compiled/pre-minified JavaScript, see:
# - https://pagure.io/fesco/issue/3177
# - https://pagure.io/packaging-committee/pull-request/1370
# Regarding CSS, see:
# - https://pagure.io/fesco/issue/3269
# - https://pagure.io/packaging-committee/pull-request/1402

# Styles from Pygments are bundled in generated HTML reports (thus the presence
# of a Pygments license file), but the styles come from the system
# python3-pygments package and are not actually bundled in this package.

# tailwind.css 3.4.16 is src/snakemake/assets/data/tailwindcss/tailwind.css,
# but we do not normally treat CSS frameworks as bundled dependencies, and it
# is not clear how we should name a virtusl Provides if we added one.

# src/snakemake/assets/data/react/react.production.min.js
Provides:       bundled(npm(react)) = 18.2.0
# src/snakemake/assets/data/react/react-dom.production.min.js
Provides:       bundled(npm(react-dom)) = 18.2.0

# src/snakemake/assets/data/vega/vega.js
Provides:       bundled(npm(vega)) = 5.21.0
# Bundled in src/snakemake/assets/data/vega/vega.js as dependencies:
# For versions of vega-* packages, see:
# https://github.com/vega/vega/blob/v5.21.0/packages
Provides:       bundled(npm(vega-crossfilter)) = 4.0.5
Provides:       bundled(npm(vega-dataflow)) = 5.7.4
Provides:       bundled(npm(vega-encode)) = 4.8.3
Provides:       bundled(npm(vega-event-selector)) = 3.0.0
Provides:       bundled(npm(vega-expression)) = 5.0.0
Provides:       bundled(npm(vega-force)) = 4.0.7
Provides:       bundled(npm(vega-format)) = 1.0.4
Provides:       bundled(npm(vega-functions)) = 5.12.1
Provides:       bundled(npm(vega-geo)) = 4.3.8
Provides:       bundled(npm(vega-hierarchy)) = 4.0.9
Provides:       bundled(npm(vega-label)) = 1.1.0
Provides:       bundled(npm(vega-loader)) = 4.4.1
Provides:       bundled(npm(vega-parser)) = 6.1.4
Provides:       bundled(npm(vega-projection)) = 1.4.5
Provides:       bundled(npm(vega-regression)) = 1.0.9
Provides:       bundled(npm(vega-runtime)) = 6.1.3
Provides:       bundled(npm(vega-scale)) = 7.1.1
Provides:       bundled(npm(vega-scenegraph)) = 4.9.4
Provides:       bundled(npm(vega-statistics)) = 5.3.1
Provides:       bundled(npm(vega-time)) = 2.0.4
Provides:       bundled(npm(vega-transforms)) = 4.9.5
Provides:       bundled(npm(vega-typings)) = 0.22.0
Provides:       bundled(npm(vega-util)) = 1.17.0
Provides:       bundled(npm(vega-view)) = 5.10.1
Provides:       bundled(npm(vega-view-transforms)) = 4.5.8
Provides:       bundled(npm(vega-voronoi)) = 4.1.5
Provides:       bundled(npm(vega-wordcloud)) = 4.1.3
# For these, see notes in src/snakemake/assets/__init__.py.
Provides:       bundled(npm(@types/estree)) = 0.0.50
Provides:       bundled(npm(d3-array)) = 2.12.1
Provides:       bundled(npm(d3-color)) = 2.0.0
Provides:       bundled(npm(d3-delaunay)) = 5.2.0
Provides:       bundled(npm(d3-dispatch)) = 2.0.0
Provides:       bundled(npm(d3-dsv)) = 2.0.0
Provides:       bundled(npm(d3-force)) = 2.1.1
Provides:       bundled(npm(d3-format)) = 2.0.0
Provides:       bundled(npm(d3-geo)) = 2.0.2
Provides:       bundled(npm(d3-geo-projection)) = 3.0.0
Provides:       bundled(npm(d3-hierarchy)) = 2.0.0
Provides:       bundled(npm(d3-interpolate)) = 2.0.1
Provides:       bundled(npm(d3-path)) = 2.0.0
Provides:       bundled(npm(d3-quadtree)) = 2.0.0
Provides:       bundled(npm(d3-scale)) = 3.3.0
Provides:       bundled(npm(d3-shape)) = 2.1.0
Provides:       bundled(npm(d3-time)) = 2.1.1
Provides:       bundled(npm(d3-time-format)) = 3.0.0
Provides:       bundled(npm(d3-timer)) = 2.0.0
Provides:       bundled(npm(delaunator)) = 4.0.1
Provides:       bundled(npm(topojson-client)) = 3.1.0
# Present in src/snakemake/assets/data/vega/vega.js in the form of copied,
# derived, or adapted snippets. See notes in src/snakemake/assets/__init__.py.
# Implementation of erfinv is based on:
Provides:       bundled(apache-commons-math) = 3.6.1
# Expression parser is based on:
Provides:       bundled(esprima) = 2.2.0
Provides:       bundled(fabric) = 2.4.5
Provides:       bundled(npm(d3-contour)) = 1.3.2
Provides:       bundled(npm(d3-regression)) = 1.2.1
Provides:       bundled(npm(hashlru)) = 1.0.4
Provides:       bundled(npm(quickselect)) = 2.0.0
Provides:       bundled(npm(regression)) = 2.0.1
Provides:       bundled(npm(science)) = 1.9.3
Provides:       bundled(npm(shapefile)) = 0.6.2

# src/snakemake/assets/data/vega-lite/vega-lite.js
Provides:       bundled(npm(vega-lite)) = 5.2.0
# NOTE: Some of the following virtual Provides are commented out. These are
# correct, and need to be considered when determining the license of
# vega-lite.js, but they do not need to be repeated in the spec file because
# they duplicate virtual Provides from vega.js.
#
# Bundled in src/snakemake/assets/data/vega-lite/vega-lite.js as dependencies:
# See notes in src/snakemake/assets/__init__.py.
Provides:       bundled(npm(@types/clone)) = 2.1.1
Provides:       bundled(npm(clone)) = 2.1.2
Provides:       bundled(npm(fast-deep-equal)) = 3.1.3
Provides:       bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides:       bundled(npm(json-stringify-pretty-compact)) = 3.0.0
# See notes in src/snakemake/assets/__init__.py, as well as dependencies in
# https://github.com/vega/vega-lite/blob/v5.2.0/package.json, and for versions,
# see https://github.com/vega/vega-lite/blob/v5.2.0/yarn.lock; these correspond
# to those associated with vega 5.2.1.
#Provides:       bundled(npm(@types/estree)) = 0.0.50
#Provides:       bundled(npm(vega-event-selector)) = 3.0.0
#Provides:       bundled(npm(vega-expression)) = 5.0.0
#Provides:       bundled(npm(vega-util)) = 1.17.0
# Present in src/snakemake/assets/data/vega-lite/vega-lite.js in the form of
# copied, derived, or adapted snippets. See notes in
# src/snakemake/assets/__init__.py.
#Provides:       bundled(npm(hashlru)) = 1.0.4

# src/snakemake/assets/data/vega-embed/vega-embed.js
Provides:       bundled(npm(vega-embed)) = 6.20.8
# NOTE: Some of the following virtual Provides are commented out. These are
# correct, and need to be considered when determining the license of
# vega-embed.js, but they do not need to be repeated in the spec file because
# they duplicate virtual Provides from vega.js and/or vega-lite.js.
#
# Bundled in src/snakemake/assets/data/vega-embed/vega-embed.js as
# dependencies:
# See notes in src/snakemake/assets/__init__.py.
Provides:       bundled(npm(fast-json-patch)) = 3.1.0
#Provides:       bundled(npm(json-stringify-pretty-compact)) = 3.0.0
Provides:       bundled(npm(semver)) = 7.3.5
# See notes in src/snakemake/assets/__init__.py, as well as dependencies in
# https://github.com/vega/vega-embed/blob/v6.20.8/package.json, and for
# versions, see https://github.com/vega/vega-embed/blob/v6.20.8/yarn.lock;
# these correspond to those associated with vega 5.2.1.
Provides:       bundled(npm(vega-interpreter)) = 1.0.4
Provides:       bundled(npm(vega-schema-url-parser)) = 2.2.0
Provides:       bundled(npm(vega-themes)) = 2.10.0
Provides:       bundled(npm(vega-tooltip)) = 0.28.0
#Provides:       bundled(npm(vega-util)) = 1.17.0
# Present in src/snakemake/assets/data/vega-embed/vega-embed.js in the form of
# copied, derived, or adapted snippets. See notes in
# src/snakemake/assets/__init__.py.
#Provides:       bundled(npm(hashlru)) = 1.0.4
# _areEquals() is based on:
#Provides:       bundled(npm(fast-deep-equal)) = 3.1.3

# It is unclear if anything derived from heroicons is actually present in the
# package, but upstream carries a copy of its license file, so we dutifully add
# the virtual Provides, just in case we have missed something.
Provides:       bundled(npm(heroicons)) = 1.0.3

# src/snakemake/assets/data/prop-types/prop-types.min.js
Provides:       bundled(npm(prop-types)) = 15.7.2

# We no longer build Sphinx-generated PDF documentation. Beginning with 8.2.3,
# this would require patching out sphinxawesome-theme from docs/conf.py. It’s
# possible but tedious.
Obsoletes:      snakemake-doc < 8.2.1-2
# Removed in 9.6.0; keep the Obsoletes through Fedora 45.
Obsoletes:      snakemake+messaging < 9.6.1-1

%if %{with tests}
# For several tests (either apptainer or singularity-ce should work):
BuildRequires:  (apptainer or singularity-ce)
%if %{with conda_tests}
# We need this for test_jupyter_notebook*, even if we are not running tests
# that have conda in their names. When the conda_tests bcond is enabled, this
# is also needed for tests/tests_using_conda.py.
BuildRequires:  conda
# For test_conda_pin_file, test_conda_named, test_conda_function
BuildRequires:  ripgrep
# For test_script_xsh
BuildRequires:  xonsh
%endif
# For test_env_modules:
BuildRequires:  environment-modules
# For test_filegraph and test_env_modules, which use dot:
BuildRequires:  graphviz
# For test_github_issue1158:
BuildRequires:  strace
# For test_benchmark and test_benchmark_jsonl:
BuildRequires:  stress-ng

# See test-environment.yml for a listing of test dependencies, along with a lot
# of other cruft.
BuildRequires:  %{py3_dist boto3}
BuildRequires:  %{py3_dist pandas}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-mock}
BuildRequires:  %{py3_dist snakemake-executor-plugin-cluster-generic}
BuildRequires:  %{py3_dist snakemake-storage-plugin-http}
BuildRequires:  %{py3_dist snakemake-storage-plugin-fs}
BuildRequires:  %{py3_dist snakemake-storage-plugin-s3}
%endif
# For import-testing snakemake.gui
BuildRequires:  %{py3_dist flask}
%if %{with gcs_tests}
# For import-testing snakemake.executors.google_lifesciences_helper:
BuildRequires:  %{py3_dist google-cloud-storage}
%endif

%global _description %{expand:
The Snakemake workflow management system is a tool to create reproducible and
scalable data analyses. Workflows are described via a human readable, Python
based language. They can be seamlessly scaled to server, cluster, grid and
cloud environments, without the need to modify the workflow definition.
Finally, Snakemake workflows can entail a description of required software,
which will be automatically deployed to any execution environment.}

%description %_description


# No metapackage for “pep” extra because the following are not packaged:
#   - python3-eido
#   - python3-peppy
# Therefore, also no metapakge for “all” extra
%pyproject_extras_subpkg -n snakemake reports


%prep
%autosetup -n snakemake-%{version} -p1
%setup -q -T -D -a 1 -c -n snakemake-%{version}

# Copy and rename nano and vim extensions readmes for use in the main
# documentation directory.
for editor in nano vim
do
  cp -vp "misc/${editor}/README.md" "README-${editor}.md"
done

# The CDN URL for tailwind.css does not deliver a file with a stable checksum,
# so upstream has not recorded a checksum in src/snakemake/assets/__init__.py.
# A consequence of this is that setup.py will *always* re-download
# tailwind.css, even if it is already present, when building an sdist or
# bdist/wheel. Of course, this is not acceptable in an offline build, so we
# record the actual checksum of the tailwind.css file we are packaging.
cat >> src/snakemake/assets/__init__.py <<EOF

# Fedora patch: Upstream does not record a checksum for tailwind.css because
# they report that the CDN URL may serve trivially different copies. Since we
# package a copy of the file, we record the checksum of the actual packaged
# file.
Assets.spec["tailwindcss/tailwind.css"].sha256 = "$(
  sha256sum -b src/snakemake/assets/data/tailwindcss/tailwind.css |
    awk '{print $1}'
)"
EOF


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{srcversion}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{srcversion}'


%install -a
# Fix shebangs (no /usr/env shebangs)
%py3_shebang_fix %{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}

# Remove shebangs from non-executable scripts. The Python script is executable
# in the source tree but will be installed without executable permissions.
sed -r -i '1{/^#!/d}' \
    %{buildroot}%{python3_sitelib}/snakemake/executors/jobscript.sh \
    %{buildroot}%{python3_sitelib}/snakemake/executors/google_lifesciences_helper.py

# Mark license files in the asset bundle.
sed -r -i 's@^.*/(LICEN[CS]E|NOTICE)[^/]*$@%%license &@' %{pyproject_files}

# We wait until %%install to generate the man page so that we can use the
# proper script entry point. The generated man page is not perfect, but it is
# good enough to be useful.
install -d %{buildroot}%{_mandir}/man1
PATH="${PATH-}:%{buildroot}%{_bindir}" \
    PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    help2man --no-info --name='%{summary}' snakemake \
    > %{buildroot}%{_mandir}/man1/snakemake.1

# Install nano syntax highlighting
install -t '%{buildroot}%{_datadir}/nano' -D -m 0644 -p \
    misc/nano/syntax/snakemake.nanorc

# Install vim syntax highlighting
install -d '%{buildroot}%{_datadir}/vim/vimfiles'
cp -vrp misc/vim/* '%{buildroot}%{_datadir}/vim/vimfiles'
find '%{buildroot}%{_datadir}/vim/vimfiles' \
    -type f -name 'README.*' -print -delete


%check -a
%if %{with tests}
%if %{without network_tests}
# The following require network access (at least DNS) and pass if it is
# available.
k="${k-}${k+ and }not test_ancient"
k="${k-}${k+ and }not test_dynamic_container"
k="${k-}${k+ and }not test_github_issue78"
k="${k-}${k+ and }not test_issue1083"
k="${k-}${k+ and }not test_issue3361_pass"
k="${k-}${k+ and }not test_keep_local"
k="${k-}${k+ and }not test_modules_prefix"
k="${k-}${k+ and }not test_report_after_run"
k="${k-}${k+ and }not test_retrieve"
k="${k-}${k+ and }not test_shell_exec"
%endif

# These use the s3_storage test fixture, which sets up a server on the local
# loopback interface. For some reason, this does not seem to work in mock, with
# or without network access enabled. It is very likely that this is a quirk of
# the build environment rather than a real issue.
k="${k-}${k+ and }not test_default_storage"
k="${k-}${k+ and }not test_default_storage_local_job"
k="${k-}${k+ and }not test_output_file_cache_storage"
k="${k-}${k+ and }not test_storage"

# The following requires cwltool,
# https://github.com/common-workflow-language/cwltool, which is not packaged.
k="${k-}${k+ and }not test_cwl_singularity"

# The following requires polars, which is not packaged.
k="${k-}${k+ and }not test_params_pickling"
k="${k-}${k+ and }not test_validate"

# The following require the “pep” extra. They might also require network
# access.
k="${k-}${k+ and }not test_modules_peppy"
k="${k-}${k+ and }not test_pep_pathlib"
k="${k-}${k+ and }not test_peppy"

%if %{without conda_tests}
# All of these try to call conda info --json. We might experiment with making
# conda an unconditional BuildRequires, or with enabling the conda_tests bcond
# and filtering out the tests we cannot run, but we should wait for:
#
# F43FailsToInstall: python3-conda
# https://bugzilla.redhat.com/show_bug.cgi?id=2371696
k="${k-}${k+ and }not test_jupyter_notebook"
k="${k-}${k+ and }not test_jupyter_notebook_nbconvert"
k="${k-}${k+ and }not test_jupyter_notebook_draft"
%endif

# Flaky; so far, we have not attempted to understand or report these.
#
# FAILED ../tests/tests.py::test_update_flag - AssertionError: wrong result
# produced for file 'test.txt':
# ------found------
# foo
# -----expected-----
# foo
# bar
# -----------------
k="${k-}${k+ and }not test_update_flag"
# FAILED ../tests/tests.py::test_queue_input_dryrun -
# snakemake_interface_common.exceptions.WorkflowError: At least one job did not
# complete successfully.
# (produces no other useful output)

# Hangs on s390x; we have not attempted to understand or report this, although
# it would be nice to do so. For simplicity, we just skip it on all
# architectures.
k="${k-}${k+ and }not test_github_issue1158"

# Workaround for Python path issues
cd src/

# See discussion in https://github.com/snakemake/snakemake/issues/2961
# regarding running individual tests explicitly rather than letting pytest
# discover them freely, and see the “Running the full test suite” section in
# docs/project_info/contributing.rst for the list of tests that should be run.
#   - tests/test_api.py requires network access and S3 credentials
%pytest -v -k "${k-}" ${ignore-} \
    ../tests/tests.py \
%if %{with conda_tests}
    ../tests/tests_using_conda.py \
%endif
    ../tests/test_expand.py \
    ../tests/test_io.py \
    ../tests/test_schema.py \
    ../tests/test_linting.py \
    ../tests/test_executor_test_suite.py \
    ../tests/test_internals.py
%endif


%files -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%doc README-nano.md
%doc README-vim.md

%{_bindir}/snakemake
%{_mandir}/man1/snakemake.1*

# This is not owned by the filesystem package, and there is no nano-filesystem
# subpackage, so we co-own the directory to avoid depending on nano.
%dir %{_datadir}/nano/
%{_datadir}/nano/snakemake.nanorc

%{_datadir}/vim/vimfiles/ftdetect/snakemake.vim
%{_datadir}/vim/vimfiles/ftplugin/snakemake/
%{_datadir}/vim/vimfiles/syntax/snakemake.vim


%changelog
%autochangelog

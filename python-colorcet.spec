# F39FailsToInstall: python3-bokeh
# https://bugzilla.redhat.com/show_bug.cgi?id=2220137
%bcond examples 0

# We should package a commit corresponding to a release tag unless there is a
# compelling reason to do otherwise. Normally this would mean referencing the
# tag corresponding to the packaged version. However, packaging as a snapshot
# ensures that we never forget to update the commit hash, which is used to
# build the colorcet/.version file (imitating the upstream PyPI release
# process).
%global pypi_version 3.0.1
%global commit 809e2919d86241948b743fea741501f31674805a
%global snapdate 20221003

%global shortcommit %(c='%{commit}'; echo "${c:0:7}")

Name:           python-colorcet
Version:        %{pypi_version}^%{snapdate}git%{shortcommit}
Release:        %autorelease
Summary:        Collection of perceptually uniform colormaps

License:        CC-BY-4.0
URL:            https://github.com/holoviz/colorcet
# The PyPI archive lacks the Sphinx documentation sources, but since this
# documentation requires nbsite (which is not packaged) and specifically
# targets HTML output (which will not be suitable for packaging—see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion), we have
# no use for the documentation anyway.
#
# It also lacks the file tox.ini for testing, but we need to skip linting and
# tests with dependency issues, so we don’t use it anyway.
#
# It also lacks the baseline images for testing with pytest-mpl: that is enough
# to convince us to switch to the GitHub archive.
Source:         %{url}/archive/%{commit}/colorcet-%{commit}.tar.gz

BuildArch:      noarch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires:  python3-devel
# Strictly speaking, the build dependency on pyct should include its [build]
# extra; see https://github.com/holoviz/colorcet/pull/76.
BuildRequires:  %{py3_dist pyct[build]}

%global common_description %{expand:
Colorcet is a collection of perceptually uniform colormaps for use with Python
plotting programs like bokeh, matplotlib, holoviews, and datashader based on
the set of perceptually uniform colormaps created by Peter Kovesi at the Center
for Exploration Targeting.}

%description %{common_description}


%package -n python3-colorcet
Summary:        %{summary}

Obsoletes:      python3-colorcet+examples < 3.0.1^20221003git809e291-7

%description -n python3-colorcet %{common_description}


%if %{with examples}
# We don’t create a metapackage for the “all” extra because it includes several
# extras (“tests”, “tests_extra”, “doc”, “build”) that are only suitable for
# development. Only the “examples” extra really makes sense for packaging.
%pyproject_extras_subpkg -n python3-colorcet examples
%endif


%prep
%autosetup -n colorcet-%{commit}

# nbsmoke is not packaged, so we cannot run tests that use it
sed -r -i '/\bnbsmoke\b/d' setup.py
# holoviews is not packaged, so we cannot run examples that use it
sed -r -i '/\bholoviews\b/d' setup.py
# Don’t pull in dependencies for linting, PyPI uploading, or coverage analysis.
sed -r -i '/\b(flake8|pytest-cov)\b/d' setup.py

# Imitate the PyPI release process.
cat > colorcet/.version <<'EOF'
{"git_describe": "v%{pypi_version}-0-g%{shortcommit}", "version_string": "%{pypi_version}"}
EOF


%generate_buildrequires
# We want the “all” extra minus the “doc” extra:
%pyproject_buildrequires -x tests%{?with_examples:,examples},tests_extra,build


%build
%pyproject_wheel

# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
# Since the documentation uses nbsite, which explicitly targets HTML, it’s
# unlikely we could package satisfactory and guideline-compliant documentation
# even if python3dist(nbsite) were packaged.


%install
%pyproject_install
%pyproject_save_files colorcet
# The command-line tool is not particularly useful, as it only copies examples
# from one place to another. The other commands from pyct, which are supposed
# to fetch data, aren’t set up to do anything useful. We choose not to package
# it. If there is some need for it in the future, see
# https://github.com/holoviz/colorcet/pull/76.
rm -vf '%{buildroot}%{_bindir}/colorcet'


%check
# Based loosely on https://github.com/holoviz/colorcet/raw/v%%{pypi_version}/tox.ini
# commands: unit
%pytest colorcet
# commands: unit_extra
# Test the repository in the source tree so that tests have baseline images:
PYTHONPATH="${PWD}" %pytest colorcet --mpl colorcet/tests
# We cannot run the “examples” test command because nbsmoke is not packaged.


%files -n python3-colorcet -f %{pyproject_files}
%license LICENSE.txt
%doc README.md


%changelog
%autochangelog

%bcond_without tests

Name:       python-pybids
Version:    0.19.0
Release:    %autorelease
Summary:    Interface with datasets conforming to BIDS

# The entire source is MIT, except:
#   - The Versioneer-generated bids/_version.py 0.28, is Unlicense. (It simply
#     says “This file is released into the public domain,” but the full
#     Versioneer documentation makes it clear that it is actually under the
#     same Unlicense terms as Versioneer (Fedora: python-versioneer) itself.
#     https://github.com/python-versioneer/python-versioneer/tree/0.28#license)
#   - We presume other test datasets (bids/tests/data/*/) are under the overall
#     MIT license, unless evidence to the contrary comes to light.
#
# In the python3-pybids+test subpackage:
#
#   - The following test datasets (content) are PDDL-1.0:
#       bids/tests/data/ds005/
#       bids/tests/data/ds005_conflict/
#
# We refrain from including the bids-examples/ submodule
# (https://github.com/bids-standard/bids-examples/) because many of the
# datasets therein have unspecified licenses. A small number of tests are
# skipped as a result.
License:        MIT AND Unlicense
URL:            https://bids.neuroimaging.io
Source0:        https://github.com/bids-standard/pybids/archive/%{version}/pybids-%{version}.tar.gz

BuildArch:      noarch

# tests fail on 32 bit systems, plus:
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  git-core
BuildRequires:  hardlink
BuildRequires:  python3-devel
# Unbundled
BuildRequires:  %{py3_dist inflect}

%global _description %{expand:
PyBIDS is a Python library to centralize interactions with datasets conforming
BIDS (Brain Imaging Data Structure) format. For more information about BIDS
visit https://bids.neuroimaging.io.}

%description %{_description}


# We cannot package the “model_reports” extra because python-altair is not
# packaged.
%pyproject_extras_subpkg -n python3-pybids plotting


%package -n python3-pybids
Summary:    Interface with datasets conforming to BIDS
Obsoletes:      python-pybids-doc < 0.15.5-13
# unbundled
Requires:  %{py3_dist inflect}

%description -n python3-pybids %{_description}


%package -n python3-pybids+test
%global test_summary Tests and test extras for PyBIDS
Summary:        %{test_summary}

# See comment above base package License tag for licensing breakdown.
#
# The CC0-1.0 file _version.py does not appear in this subpackage.
License:        MIT AND PDDL-1.0

Requires:       python3-pybids = %{version}-%{release}

%global test_description %{expand: \
These are the tests for python3-pybids. This package:

• Provides the “bids.tests” package
• Makes sure the “test” extra dependencies are installed}

%description -n python3-pybids+test %{test_description}


# Upstream duplicates all extras with singular and plural names.
# Based loosely on: rpm -E '%%pyproject_extras_subpkg -n python3-pybids tests'
%package -n python3-pybids+tests
Summary:        %{test_summary}

# This has no files of its own, so none of the non-MIT licenses apply.
License:        MIT

# This metapackage is basically an alias for python3-pybids+test. We build it
# as a separate subpackage rather than adding a virtual Provides so that we can
# benefit from generators to add Provides like python3dist(pybids[tests]).
Requires:       python3-pybids+test = %{version}-%{release}

%description -n python3-pybids+tests %{test_description}


%prep
%autosetup -n pybids-%{version} -S git

# loosen formulaic dep: one test fails, reported upstream
# https://github.com/bids-standard/pybids/issues/1000
sed -i 's/formulaic .*"/formulaic"/' pyproject.toml

# Remove bundled inflect
rm -rf src/bids/external
sed -r -i.backup 's/from.*external (import)/\1/' src/bids/layout/layout.py

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/^([[:blank:]]*)"(pytest-cov|coverage)\b/\1# "\2/' pyproject.toml

# Not currently packaged: python-altair. This patches it out of *all* extras,
# currently “test” and “model_reports”, but we neither package nor generate
# BR’s from “model_reports” since we do not have altair.
sed -r -i 's/^([[:blank:]]*)"(altair)\b/\1# "\2/' pyproject.toml

# Remove bogus executable bits for non-script files
find src/bids doc -type f -perm /0111 -execdir chmod -v a-x '{}' '+'

# Drop test dependency on `s3fs`
sed -r -i '/s3fs/d' pyproject.toml

# Commit everything and tag to allow Versioneer to set the version.
# Make sure this is the last step in prep.
git add --all
git commit -m "[Fedora] Apply downstream changes"
git tag %{version}


%generate_buildrequires
%pyproject_buildrequires -x test,plotting


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l bids
# Save space by hardlinking duplicate test data files (of nonzero size).
hardlink -c -v '%{buildroot}%{python3_sitelib}/bids/tests/data/'


%check
%if %{with tests}
# temporarily disable failing tests
# https://github.com/bids-standard/pybids/issues/1000
k="${k-}${k+ and }not test_split"
# test_remote_bids.py requires network
%pytest -v \
    ${k+-k } "${k-}" \
    --ignore src/bids/layout/tests/test_remote_bids.py
%else
%pyproject_check_import
%endif


%files -n python3-pybids -f %{pyproject_files}
%doc README.md
%{_bindir}/pybids
%exclude %{python3_sitelib}/bids/tests/


%files -n python3-pybids+test
%{python3_sitelib}/bids/tests/
%ghost %{python3_sitelib}/*.dist-info


%files -n python3-pybids+tests
%ghost %{python3_sitelib}/*.dist-info


%changelog
%autochangelog

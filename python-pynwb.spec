# backwards compatibility tests
%bcond test_backwards         1
# example tests
%bcond test_example           1
# example tests with ros3 streaming
# Internet access required (automatically disabled without it)
%bcond test_example_ros3      0
# integration tests
%bcond test_integration       1
# unit tests for pynwb package
%bcond test_pynwb             1
# ros3 streaming tests
# Internet access required (automatically disabled without it)
%bcond test_ros3              0
# example tests and validation tests on example NWB files
%bcond test_validate_examples 0
# tests on pynwb.validate
%bcond test_validation_module 1

Name:           python-pynwb
Version:        2.5.0
Release:        %autorelease
Summary:        Package for working with Neurodata stored in the NWB format

# The entire source is BSD-3-Clause-LBNL, except:
#
# Unlicense:
#   - versioneer.py, a bundled and amalgamated copy of python3dist(versioneer),
#     is not distributed in the binary RPMs, but the _version.py it generates
#     is, and shares the same license
License:        BSD-3-Clause-LBNL AND Unlicense
URL:            https://github.com/NeurodataWithoutBorders/pynwb
# Use the pypi tar because GitHub tar does not include the required git-submodules
Source:         %{pypi_source pynwb}

# Fix warnings from tests
# https://github.com/NeurodataWithoutBorders/pynwb/pull/1778
#
# Rebased on 2.5.0 (except with setup.cfg replaced with the reformatted one
# from the PyPI sdist); contents of .github/ and docs/ removed from the patch
# so it applies to the PyPI sdist, which lacks them.
Patch:          0001-Fix-warnings-from-tests-1778.patch

BuildArch:      noarch

%global desc %{expand:
PyNWB is a Python package for working with NWB files. It provides a high-level
API for efficiently working with Neurodata stored in the NWB format.
https://pynwb.readthedocs.io/en/latest/}

%description %{desc}

%package -n python3-pynwb
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-pynwb %{desc}

%prep
%autosetup -n pynwb-%{version} -p1

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's@"coverage", "run", "-p"@"%{python3}"@' \
    tests/validation/test_validate.py

sed -r -i 's/==.*//' requirements.txt | tee requirements-unpinned.txt
#sed -i -e "s/h5py>.*'/h5py'/" -e "s/numpy>.*'/numpy'/" -e "s/pandas>.*'/pandas'/" setup.py

# TODO: Why does this happen? It seems like it is an issue with our test
# environment rather than a real bug.
#
# AssertionError: "<frozen runpy>:128:
#     RuntimeWarning: 'pyn[151 chars]ur\n" != ''
# - <frozen runpy>:128: RuntimeWarning: 'pynwb.validate' found in sys.modules
#     after import of package 'pynwb', but prior to execution of
#     'pynwb.validate'; this may result in unpredictable behaviour
sed -r -i '1{s/^/from unittest import skip\n/}' \
    tests/validation/test_validate.py
for n in \
    test_validate_file_cached \
    test_validate_file_cached_extension \
    test_validate_file_cached_extension_pass_ns \
    test_validate_file_cached_ignore \
    test_validate_file_list_namespaces_core \
    test_validate_file_list_namespaces_extension
do
  sed -r -i \
      "s/^([[:blank:]]*)(def $n\()/\1@skip('Re-import issues')\n\1\2/" \
      tests/validation/test_validate.py
done

%generate_buildrequires
%pyproject_buildrequires requirements-unpinned.txt

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pynwb

%check
# See skips added in %%prep.
PYTHONPATH='%{buildroot}%{python3_sitelib}' '%{python3}' ./test.py \
%if %{with test_backwards}
    --backwards \
%endif
%if %{with test_example}
    --example \
%endif
%if %{with test_example_ros3}
    --example-ros3 \
%endif
%if %{with test_integration}
    --integration \
%endif
%if %{with test_pynwb}
    --pynwb \
%endif
%if %{with test_ros3}
    --ros3 \
%endif
%if %{with test_validate_examples}
    --validate-examples \
%endif
%if %{with test_validation_module}
    --validation-module \
%endif
    --verbose

%files -n python3-pynwb -f %{pyproject_files}
%license license.txt
%doc README.rst

%changelog
%autochangelog

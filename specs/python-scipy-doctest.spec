Name:           python-scipy-doctest
Version:        1.7.1
Release:        %autorelease
Summary:        Configurable, whitespace-insensitive, floating-point-aware doctest helpers

License:        BSD-3-Clause
URL:            https://github.com/scipy/scipy_doctest
Source:         %{pypi_source scipy_doctest}

# Undo the pin of scipy <= 1.4.1 after scipy 1.5.2 is out.
# (This should have been 1.14.1 and 1.15.2, respectively.)
# https://github.com/scipy/scipy_doctest/issues/184
#
# MAINT : stop upper capping scipy
# https://github.com/scipy/scipy_doctest/pull/187
# Rebased on v1.7.1.
Patch:          scipy-doctest-1.7.1-scipy-1.15.patch

BuildSystem:            pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install):   -l scipy_doctest
# We *can* smoke-test imports from the test suite, but we do not *want* to.
BuildOption(check):     -e scipy_doctest.tests*

BuildArch:      noarch

%global common_description %{expand:
This project extends the standard library doctest module to allow flexibility
and easy customization of finding, parsing and checking code examples in
documentation.

Can be used either as drop-in doctest replacement or through the pytest
integration. Uses a floating-point aware doctest checker by default.}

%description %{common_description}


%package     -n python3-scipy-doctest
Summary:        %{summary}

%description -n python3-scipy-doctest %{common_description}


%check -a
# The lowest-friction way to run tests is using the installed package:
export PYTHONPATH='%{buildroot}%{python3_sitelib}'

# See test steps in .github/workflows/pip.yml in upstream git. We run only a
# subset of these tests. In particular, we try to avoid running doctests that
# belong to other packages, like scipy or pooch, since these are more likely to
# be brittle.

echo '==== Self-test with SciPy and MPL ====' 1>&2
%pytest --pyargs '%{buildroot}%{python3_sitelib}/scipy_doctest' -k "${k-}" -v
# Ideally, setting PYTEST_ADDOPTS to '-p no:cacheprovider' would prevent the
# creation of this cache directory, but it does not, so we just clean it up
# after the fact.
rm -rv '%{buildroot}%{python3_sitelib}/scipy_doctest/tests/.pytest_cache'

echo '==== Self-test CLI with SciPy and MPL ====' 1>&2
f='scipy_doctest/tests/finder_cases.py'
%{py3_test_envvars} %{python3} -m scipy_doctest \
    "%{buildroot}%{python3_sitelib}/${f}" -vv

echo '==== Test testfile CLI ====' 1>&2
f='scipy_doctest/tests/scipy_ndimage_tutorial_clone.rst'
%{py3_test_envvars} %{python3} -m scipy_doctest \
    "%{buildroot}%{python3_sitelib}/${f}" -v

echo '==== Test pytest plugin ====' 1>&2
for f in \
    'scipy_doctest/tests/module_cases.py' \
    'scipy_doctest/tests/stopwords_cases.py' \
    'scipy_doctest/tests/local_file_cases.py'
do
  %pytest "%{buildroot}%{python3_sitelib}/${f}" --doctest-modules -v
done


%files -n python3-scipy-doctest -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog

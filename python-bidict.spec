Name:           python-bidict
Version:        0.22.1
Release:        2%{?dist}
Summary:        Bidirectional mapping library for Python

License:        MPL-2.0
URL:            https://bidict.readthedocs.io
Source:         https://github.com/jab/bidict/archive/v%{version}/bidict-%{version}.tar.gz

# Fixes failure in test_abstract_bimap_init_fails
#
# Test with python3.12 (beta)
# https://github.com/jab/bidict/commit/073870807772d5c3ca837a9ed1450c47eec9388d
#
# Rebased on v0.22.1.
Patch:          0001-Test-with-python3.12-beta.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Forward declarations for all the custom interpreted text roles that Sphinx
defines and that are used below. This helps Sphinx-unaware tools (e.g.
rst2html, PyPI's and GitHub's renderers, etc.}

%description %{_description}

%package -n     python3-bidict
Summary:        %{summary}

%description -n python3-bidict %{_description}

%prep
%autosetup -n bidict-%{version} -p1
# Curate the list of test dependencies.
# - We don’t need to pull in documentation dependencies.
# - https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
# - We don’t need to run benchmarks.
# - The pytest-icdiff plugin is not packaged, and is purely aesthetic.
sed -r -i 's/"(pytest-(cov|benchmark))\b/# &/' pyproject.toml
# Since we have patched out pytest-benchmark, this would not be recognized.
sed -r -i '/--benchmark-disable/d' pytest.ini
# SPECPARTS dir in %%_builddir/%%buildsubdir is leaking to setuptools package
# discovery
# https://github.com/rpm-software-management/rpm/issues/2532
rm -rf SPECPARTS

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files bidict

%check
# We don’t need to run benchmarks.
rm -vf tests/test_microbenchmarks.py
PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTEST_XDIST_AUTO_NUM_WORKERS=%{_smp_build_ncpus} \
    %{python3} ./run_tests.py

%files -n python3-bidict -f %{pyproject_files}
%doc CHANGELOG.rst README.rst

%changelog
* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 06 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.22.1-1
- Update to 0.22.1 (fix RHBZ#2157231)
- Run tests via the included run_tests.py script (including all doctests)
- Fix Python 3.12 test failure (fix RHBZ#2190400, fix RHBZ#2220129)

* Thu Jul 06 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.22.0-7
- Port to pyproject-rpm-macros
- Stop skipping tests that would succeed
- Update License to SPDX

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.22.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.22.0-2
- Rebuilt for Python 3.11

* Thu Mar 24 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.22.0-1
- Update to latest upstream release 0.22.0 (closes rhbz#2067604)

* Wed Jan 26 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.4-1
- Update to latest upstream release 0.21.4 (closes rhbz#2016795)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Sep 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.3-1
- Update to latest upstream release 0.21.3 (closes rhbz#2001344)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.21.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 08 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.21.2-1
- Initial package for Fedora

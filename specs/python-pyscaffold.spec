%bcond tests 1

Name:           python-pyscaffold
Version:        4.6
Release:        %autorelease
Summary:        Template tool for putting up the scaffold of a Python project

# The entire source is MIT, except for the template files under
# pyscaffold.templates, which are 0BSD.
License:        MIT and 0BSD
URL:            https://pyscaffold.org/
Source0:        %{pypi_source pyscaffold}
# Man page written by hand in groff_man(7) format for Fedora based on --help
# output. Note that help2man(1) could autogenerate a decent man page if needed:
#   help2man --no-info --output=putup.1 putup
# but the hand-written one is better-formatted and contains better
# cross-references.
Source1:        putup.1

# Downstream-only: do not run coverage analysis
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch:          PyScaffold-4.5-no-coverage.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
# Needs vim (vim-enhanced) or vi (vim-minimal); we choose the lighter-weight BR
BuildRequires:  vim-minimal
BuildRequires:  python-unversioned-command
%endif

%global common_description %{expand:
PyScaffold is a project generator for bootstrapping high quality Python
packages, ready to be shared on PyPI and installable via pip. It is easy to use
and encourages the adoption of the best tools and practices of the Python
ecosystem, helping you and your team to stay sane, happy and productive. The
best part? It is stable and has been used by thousands of developers for over
half a decade!}

%description
%{common_description}


%package -n python3-pyscaffold
Summary:        %{summary}

# Removed in F43; can drop Obsoletes after F45 EOL
Obsoletes:      python-pyscaffold-doc < 4.6-5

%description -n python3-pyscaffold
%{common_description}


# We do not package the “all” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-markdown) >= 0.4
#   python3dist(pyscaffoldext-custom-extension) >= 0.6
#   python3dist(pyscaffoldext-dsproject) >= 0.5
#   python3dist(pyscaffoldext-django) >= 0.1.1
#   python3dist(pyscaffoldext-cookiecutter) >= 0.1
#   python3dist(pyscaffoldext-travis) >= 0.3
#
# We do not package the “md” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-markdown) >= 0.4
#
# We do not package the “ds” extra as a metapackage, because it has the
# following dependencies not currently packaged:
#
#   python3dist(pyscaffoldext-dsproject) >= 0.5


%prep
%autosetup -n pyscaffold-%{version} -p1

# Correct all shebangs in tests and templates
%py3_shebang_fix tests

# Cannot install “all” extra for testing
sed -r -i 's/^([[:blank:]]*)(all)\b/\1# \2/' tox.ini

# Relax the upper bound of the platformdirs dependency
sed -r -i '/\bplatformdirs\b/ s/<4/<5/' setup.cfg


%generate_buildrequires
# Missing dependencies for “all”, “md”, and “ds” extras
%pyproject_buildrequires %{?with_tests:-t}


%build
%pyproject_wheel


%install
%pyproject_install
# setup.py does not install the template files
install -p -m 0644 \
    -t '%{buildroot}/%{python3_sitelib}/pyscaffold/templates' \
    src/pyscaffold/templates/*.template
%pyproject_save_files -l pyscaffold
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 '%{SOURCE1}'


%check
%if %{with tests}
# skip tests that need network access
k="${k-}${k+ and }not test_inplace_update"
k="${k-}${k+ and }not test_piptools_works_with_pyscaffold"
k="${k-}${k+ and }not test_update_version_3_0_to_3_1"
k="${k-}${k+ and }not test_update_version_3_0_to_3_1_pretend"
k="${k-}${k+ and }not test_install_packages"
k="${k-}${k+ and }not test_api_with_venv"
k="${k-}${k+ and }not test_cli_with_venv"
k="${k-}${k+ and }not test_pipenv_works_with_pyscaffold"
# We should be able to write:
#   %%tox -- -- -k "${k-}" …
# but for some reason this does not successfully collect any tests.
#
# While upstream explicitly supports running tests in parallel, we observe a
# race condition causing flaky failures in test_get_log_level in practice.
%pytest -k "${k-}" -rs \
    --ignore=tests/test_install.py \
    --ignore=tests/system/test_common.py
%endif


%files -n python3-pyscaffold -f %{pyproject_files}
%doc CHANGELOG.rst
%doc CONTRIBUTING.rst
%doc README.rst

%{_bindir}/putup
%{_mandir}/man1/putup.1*


%changelog
%autochangelog

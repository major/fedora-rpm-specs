Name:           python-pytest-subtests
Version:        0.14.2
Release:        %autorelease
Summary:        Support for unittest subTest() and subtests fixture

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pytest-subtests
Source:         %{pypi_source pytest_subtests}

BuildSystem:            pyproject
BuildOption(install):   -l pytest_subtests

# Don’t depend on pytest-xdist on RHEL/ELN, since it’s unwanted there. Keep the
# dependency in Fedora because it enables several integration tests.
#
# (For similar reasons, we don’t pass -t to %%pyproject_buildrequires and we
# run tests via %%pytest directly instead of via %%tox: tox is unwanted in
# RHEL/ELN, and the benefit of using it in this package is small.)
%if %{undefined rhel}
BuildRequires:  python3dist(pytest-xdist)
%endif

BuildArch:      noarch

%description
pytest-subtests unittest subTest() support and subtests fixture.


%package -n     python3-pytest-subtests
Summary:        %{summary}

%description -n python3-pytest-subtests
%{summary}.


%check -a
%pytest -rs -v tests


%files -n python3-pytest-subtests -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog

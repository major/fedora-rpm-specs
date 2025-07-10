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
BuildOption(generate_buildrequires): -t

BuildArch:      noarch

%description
pytest-subtests unittest subTest() support and subtests fixture.


%package -n     python3-pytest-subtests
Summary:        %{summary}

%description -n python3-pytest-subtests
%{summary}.


%check -a
%tox -- -- -rs -v tests


%files -n python3-pytest-subtests -f %{pyproject_files}
%doc CHANGELOG.rst
%doc README.rst


%changelog
%autochangelog

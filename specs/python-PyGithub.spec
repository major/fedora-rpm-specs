Name:           python-PyGithub
Version:        2.6.1
Release:        %autorelease
Summary:        Python library to work with the Github API
License:        LGPL-3.0-or-later
URL:            https://github.com/PyGithub/PyGithub
# github tarball (unlike PyPI one) contains tests
Source:         %{url}/archive/v%{version}/PyGithub-%{version}.tar.gz
BuildArch:      noarch

%global _description %{expand:
A Python library implementing the full Github API v3.}

%description %{_description}

%package -n     python3-pygithub
Summary:        %{summary}
BuildRequires:  python3-devel

Provides:       python3-github = %{version}-%{release}
Obsoletes:      python3-github < 1.25.2-2
Provides:       python3-PyGithub = %{version}-%{release}
Obsoletes:      python3-PyGithub < 1.29-8

%description -n python3-pygithub %{_description}

%prep
%autosetup -p 1 -n PyGithub-%{version}

# Remove linter(s) from test requirements
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i '/pytest-cov/d' requirements/test.txt

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires requirements/test.txt

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l github

%check
%pytest -v

%files -n python3-pygithub -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

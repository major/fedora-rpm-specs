# Created by pyp2rpm-3.3.0
%global pypi_name gitlab

Name:           python-%{pypi_name}
Version:        4.4.0
Release:        %autorelease
Summary:        Interact with GitLab API

License:        LGPLv3
URL:            https://github.com/python-gitlab/python-gitlab
Source0:        https://files.pythonhosted.org/packages/source/p/python-gitlab/python-gitlab-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

# drop the -doc package. To much effort to keep working
Provides:  python-%{pypi_name}-doc = %{version}-%{release}
Obsoletes: python-%{pypi_name}-doc <= 3.3.0

%description
Interact with GitLab API

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Interact with GitLab API

%package -n python-%{pypi_name}-doc
Summary:        Python gitlab documentation
%description -n python-%{pypi_name}-doc
Documentation for gitlab

%prep
%autosetup -p1 -n python-%{pypi_name}-%{version}

# Relax some dependencies
sed -i 's/requests==.*/requests/'                    requirements.txt
sed -i 's/requests-toolbelt==.*/requests-toolbelt/'  requirements.txt
sed -i 's/pytest==.*/pytest/'       requirements-lint.txt requirements-test.txt
sed -i 's/PyYaml==.*/PyYaml/'       requirements-lint.txt requirements-test.txt
sed -i 's/responses==.*/responses/' requirements-lint.txt requirements-test.txt
sed -i 's/wheel==.*/wheel/'         requirements-test.txt
sed -i 's/coverage==.*/coverage/'   requirements-test.txt
sed -i 's/setuptools==.*/setuptools/' requirements-test.txt
sed -i 's/pytest-cov==.*/pytest-cov/' requirements-test.txt
sed -i 's/build==.*/build/'         requirements-test.txt

# not available in rawhide 11 Aug 2022
sed -i 's/pytest-console-scripts.*//' requirements-test.txt
sed -i 's/pytest-github-actions-annotate-failures.*//' requirements-test.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files gitlab

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_bindir}/gitlab
%doc README.rst

%changelog
%autochangelog

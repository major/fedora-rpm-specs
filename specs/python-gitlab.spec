# Created by pyp2rpm-3.3.0
%global pypi_name gitlab

Name:           python-%{pypi_name}
Version:        8.0.0
Release:        %autorelease
Summary:        Interact with GitLab API

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://github.com/python-gitlab/python-gitlab
Source0:        %{pypi_source python_gitlab}
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
%autosetup -p1 -n python_%{pypi_name}-%{version}

# Relax some dependencies
sed -i 's/pytest==9\.*/pytest>=8.4.2,<10/'             requirements-lint.txt requirements-test.txt
sed -i 's/wheel==0\.*/wheel>=0.45.0,<1.0/'             requirements-test.txt

# not available in rawhide 11 Aug 2022
sed -i 's/pytest-console-scripts.*//'                  requirements-test.txt
sed -i 's/pytest-github-actions-annotate-failures.*//' requirements-test.txt

# coverage disabled
sed -i 's/pytest-cov.*//'                              requirements-test.txt
sed -i 's/coverage.*//'                                requirements-test.txt

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

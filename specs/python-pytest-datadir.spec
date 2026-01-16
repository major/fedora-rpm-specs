Name:           python-pytest-datadir
Version:        1.8.0
Release:        %autorelease
Summary:        Pytest plugin for test data directories and files
License:        MIT
URL:            https://github.com/gabrielcnr/pytest-datadir
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/pytest-datadir-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -t
BuildOption(install):                -l pytest_datadir

BuildRequires:  %{py3_dist docutils}

%global _desc %{expand:This package contains a pytest plugin for manipulating test data directories
and files.}

%description
%_desc

%package     -n python3-pytest-datadir
Summary:        %{summary}

%description -n python3-pytest-datadir
%_desc

%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'

%build -a
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html

%check
%tox

%files -n python3-pytest-datadir -f %{pyproject_files}
%doc AUTHORS CHANGELOG.html README.md

%changelog
%autochangelog

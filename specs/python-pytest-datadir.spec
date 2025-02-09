Name:           python-pytest-datadir
Version:        1.6.1
Release:        %autorelease
Summary:        Pytest plugin for test data directories and files
License:        MIT
URL:            https://github.com/gabrielcnr/pytest-datadir
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/pytest-datadir-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist docutils}

%global _desc %{expand:
This package contains a pytest plugin for manipulating test data
directories and files.}

%description %_desc

%package     -n python3-pytest-datadir
Summary:        %{summary}

%description -n python3-pytest-datadir %_desc

%prep
%autosetup -n pytest-datadir-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires -t

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel
rst2html --no-datestamp CHANGELOG.rst CHANGELOG.html

%install
%pyproject_install
%pyproject_save_files -l pytest_datadir

%check
%tox

%files -n python3-pytest-datadir -f %{pyproject_files}
%doc AUTHORS CHANGELOG.html README.md

%changelog
%autochangelog

%bcond_without tests

# Pull from GitHub (prerquisite for Packit)
%global forgeurl https://github.com/willu47/amply

%global _description %{expand:
Amply allows you to load and manipulate AMPL data as Python data
structures.

Amply only supports a specific subset of the AMPL syntax:

> set declarations
> set data statements
> parameter declarations
> parameter data statements}

Name:           python-amply
Version:        0.1.6
Release:        %autorelease
Summary:        A Python package for AMPL/GMPL datafile parsing
%forgemeta
License:        EPL-1.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description %_description

%package -n python3-amply
Summary:        %{summary}

%description -n python3-amply %_description

%prep
%forgeautosetup

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files amply

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pytest

%files -n python3-amply -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

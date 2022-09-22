%bcond_without tests

%global _description %{expand:
Amply allows you to load and manipulate AMPL data as Python data
structures.

Amply only supports a specific subset of the AMPL syntax:

> set declarations
> set data statements
> parameter declarations
> parameter data statements}

Name:           python-amply
Version:        0.1.5
Release:        %autorelease
Summary:        A Python package for AMPL/GMPL datafile parsing

License:        EPL-1.0
URL:            https://github.com/willu47/amply
Source0:        %{pypi_source amply}

BuildArch:      noarch

%description %_description

%package -n python3-amply
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-amply %_description

%prep
%autosetup -n amply-%{version}

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files amply

%check
%pytest

%files -n python3-amply -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

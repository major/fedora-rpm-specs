%global srcname voluptuous

Name:      python-%{srcname}
Version:   0.16.0
Release:   %autorelease
Summary:   Python data validation library

License:   BSD-3-Clause
URL:       http://github.com/alecthomas/voluptuous
Source0:   %{pypi_source}
BuildArch: noarch

%global _description %{expand:
Voluptuous, despite the name, is a Python data validation library. It is 
primarily intended for validating data coming into Python as JSON, YAML, etc.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
BuildRequires: python3-devel
BuildRequires: %{py3_dist setuptools}
BuildRequires: %{py3_dist pytest}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files voluptuous

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md
%license COPYING

%changelog
%autochangelog

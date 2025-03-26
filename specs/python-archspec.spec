%global srcname archspec

Name:           python-%{srcname}
Version:        0.2.5
Release:        %autorelease
Summary:        A library to query system architecture

License:        Apache-2.0 OR MIT
URL:            https://github.com/archspec/archspec
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-jsonschema

%global _description %{expand:
Archspec aims at providing a standard set of human-understandable labels for
various aspects of a system architecture like CPU, network fabrics, etc. and
APIs to detect, query and compare them.

This project grew out of Spack and is currently under active development. At
present it supports APIs to detect and model compatibility relationships among
different CPU microarchitectures.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -p1 -n %{srcname}-%{version}
rm -rf archspec/json/.git*


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
%pytest -v


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.*
%{_bindir}/archspec


%changelog
%autochangelog

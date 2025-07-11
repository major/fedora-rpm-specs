Name:           python-confuse
Version:        2.0.1
Release:        9%{?dist}
Summary:        A Python module for handling YAML configuration files

License:        MIT
URL:            https://github.com/beetbox/confuse
Source0:        %{url}/archive/v%{version}/confuse-%{version}.tar.gz
Patch0:         python-confuse-py314.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%global _description %{expand:
Confuse is a configuration library for Python that uses YAML. It takes care of
defaults, overrides, type checking, command-line integration, environment
variable support, human-readable errors, and standard OS-specific locations.}

%description %{_description}

%package -n python3-confuse
Summary:        %{summary}

%description -n python3-confuse %{_description}

%prep
%autosetup -p1 -n confuse-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files confuse

%check
%pytest

%files -n python3-confuse -f %{pyproject_files}
%license LICENSE
%doc README.rst

%autochangelog

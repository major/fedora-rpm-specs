Summary:        Python function for condensing JSON using replacement strings
Name:           python-condense-json
Version:        0.1.3
Release:        %autorelease
License:        Apache-2.0
URL:            https://pypi.python.org/project/condense-json/
Source:         %{pypi_source condense_json}
Patch:          python-condense-json-0.1.3-toml.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
%global _description \
Python function for condensing JSON using replacement strings

%description %{_description}

%package     -n python3-condense-json
Summary:        %{summary}
%description -n python3-condense-json %{_description}

%prep
%autosetup -p1 -n condense_json-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l condense_json

%check
%pytest

%files -n python3-condense-json -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

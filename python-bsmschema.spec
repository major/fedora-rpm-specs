Name:           python-bsmschema
Summary:        BIDS Stats Models Schema
Version:        0.1.0
Release:        %autorelease

License:        Apache-2.0
URL:            https://github.com/bids-standard/stats-models
Source:         %{pypi_source bsmschema}

BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
This package contains a Pydantic description of the BIDS Stats Models format,
which can be used as a schema validator or generate JSON schema for independent
validation.}

%description %{common_description}


%package -n     python3-bsmschema
Summary:        %{summary}

%description -n python3-bsmschema %{common_description}


%prep
%autosetup -n bsmschema-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l bsmschema


%check
# Upstream does not provide a test suite.
%pyproject_check_import


%files -n python3-bsmschema -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog

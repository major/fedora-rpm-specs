Name:           python-datanommer-models
Version:        1.5.0
Release:        %autorelease
Summary:        SQLAlchemy models for datanommer

License:        GPL-3.0-or-later
URL:            https://github.com/fedora-infra/datanommer
Source:         %{pypi_source datanommer_models}

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies
#BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(pytest-postgresql)

%global _description %{expand:
SQLAlchemy models for datanommer. }

%description %_description

%package -n python3-datanommer-models
Summary:        %{summary}

%description -n python3-datanommer-models %_description


%prep
%autosetup -p1 -n datanommer_models-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L datanommer


# The tests suites requires the messaging schema that are currently not packaged
# in Fedora. We can try to make the %%pytest macro running later when they are available.
%check
%pyproject_check_import -t


%files -n python3-datanommer-models -f %{pyproject_files}
%doc README.*
%doc NEWS.*
%license LICENSE

%changelog
%autochangelog

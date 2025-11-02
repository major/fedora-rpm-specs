%global pypi_name serpent

Name:           python-%{pypi_name}
Version:        1.42
Release:        %autorelease
Summary:        Serialization based on ast.literal_eval

License:        MIT
URL:            https://github.com/irmen/Serpent
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Serpent is a simple serialization library based on ast.literal_eval. Because
it only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network
for instance) and de-serialize it there.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-attrs
BuildRequires:  python3-pytz
BuildRequires:  pytest

%description -n python3-%{pypi_name}
Serpent is a simple serialization library based on ast.literal_eval. Because
it only serializes literals and recreates the objects using ast.literal_eval(),
the serialized data is safe to transport to other machines (over the network
for instance) and de-serialize it there.
%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

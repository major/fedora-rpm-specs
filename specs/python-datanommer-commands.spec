Name:           python-datanommer-commands
Version:        1.4.3
Release:        2%{?dist}
Summary:        Console commands for datanommer

License:        GPL-3.0-or-later
URL:            https://pypi.org/project/datanommer.commands
Source:         %{pypi_source datanommer_commands}

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies
#BuildRequires:  python3dist(pytest)
#BuildRequires:  python3dist(pytest-postgresql)

%global _description %{expand:
Console commands for datanommer. }

%description %_description

%package -n python3-datanommer-commands
Summary:        %{summary}

%description -n python3-datanommer-commands %_description


%prep
%autosetup -p1 -n datanommer_commands-%{version}


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


%files -n python3-datanommer-commands -f %{pyproject_files}
%doc README.*
%license LICENSE
%{_bindir}/datanommer-create-db
%{_bindir}/datanommer-dump
%{_bindir}/datanommer-extract-users
%{_bindir}/datanommer-latest
%{_bindir}/datanommer-stats


%changelog
%autochangelog

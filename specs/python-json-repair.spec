Name:           python-json-repair
Version:        0.56.0
Release:        %autorelease
Summary:        A package to repair broken JSON strings

License:        MIT
URL:            https://github.com/mangiucugna/json_repair/
Source:         %{pypi_source json_repair}

BuildSystem:    pyproject
BuildOption(install):  -l json_repair
BuildOption(generate_buildrequires): -x schema

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
This simple package can be used to fix an invalid json string. To know all
cases in which this package will work, check out the unit test. }

%description %_description

%package -n     python3-json-repair
Summary:        %{summary}

%description -n python3-json-repair %_description

%pyproject_extras_subpkg -n python3-json-repair schema


%check
%pyproject_check_import

%files -n python3-json-repair -f %{pyproject_files}
%{_bindir}/json_repair

%changelog
%autochangelog

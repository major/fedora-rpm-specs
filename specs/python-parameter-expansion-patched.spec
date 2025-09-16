%global pypi_name parameter-expansion-patched

Name:           python-%{pypi_name}
Version:        0.3.1
Release:        %autorelease
Summary:        POSIX Parameter Expansion in Python

License:        Apache-2.0
URL:            https://github.com/aboutcode-org/parameter_expansion_patched
Source:         %{pypi_source}
# Update project references
# https://github.com/aboutcode-org/parameter_expansion_patched/commit/3f6a1ddfc25d199c8be9699d4edbbce3787c6699
Patch:          0001-Update_link_references_of_ownership_from_nexB_to_aboutcode-org.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
This is an experimental Python library to enable POSIX parameter expansion in a
string. It supports also a subset of Bash parameter expansion.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
sed -i 's|version = "0.0.0" |version = "%{version}" |' pyproject.toml
for lib in src/parameter_expansion/pe.py; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files parameter_expansion

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

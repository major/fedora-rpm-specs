Name:           python-bases
Version:        0.3.0
Release:        %autorelease
Summary:        Python library for general Base-N encodings

License:        MIT
URL:            https://github.com/hashberg-io/bases
Source:         %{pypi_source bases}

BuildSystem:    pyproject
BuildOption(install):  --assert-license bases

BuildArch:      noarch
BuildRequires:  python3-devel
# tests
BuildRequires:  python3-pytest
BuildRequires:  python3-base58

%global _description %{expand:
Bases provides a customisable, parametric implementation of several common
styles of Base-N encoding, covering all cases appearing in the multibase
specification (except for proquints).}

%description %_description

%package -n     python3-bases
Summary:        %{summary}

%description -n python3-bases %_description

%check -a
%pytest

%files -n python3-bases -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

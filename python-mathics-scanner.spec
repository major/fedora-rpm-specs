%global srcname Mathics_Scanner

Name:           python-mathics-scanner
Version:        1.3.0
Release:        %autorelease
Summary:        Character Tables and Tokenizer for Mathics and the Wolfram Language

License:        GPL-3.0-only
URL:            https://mathics.org
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package provides character tables and a tokenizer for Mathics and the
Wolfram Language.}

%description %_description

%package -n     python3-mathics-scanner
Summary:        %{summary}
Recommends:     python3dist(mathics_scanner[full]) = %{version}-%{release}

%description -n python3-mathics-scanner %_description

%pyproject_extras_subpkg -n python3-mathics-scanner full

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x full

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mathics_scanner

%check
%pytest

%files -n python3-mathics-scanner -f %{pyproject_files}
%license COPYING.txt
%doc README.rst CHANGES.rst AUTHORS.txt ChangeLog
%{_bindir}/mathics-generate-json-table

%changelog
%autochangelog

Name:           python-railroad-diagrams
Version:        3.0.1
Release:        %autorelease
Summary:        Library to generate railroad diagrams
License:        MIT
URL:            https://github.com/tabatkins/railroad-diagrams

# Upstream doesn't do tags: https://github.com/tabatkins/railroad-diagrams/issues/91
%global commit c3a16b9dcb06f5d0ae2260f8414136917871d4c5
%global forgeurl %url
%forgemeta
%global distprefix %{nil}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Railroad diagrams are a way of visually representing a grammar in a form that is
more readable than using regular expressions or BNF. They can easily represent
any context-free grammar, and some more powerful grammars.}

%description %_description

%package -n python3-railroad-diagrams
Summary:        %{summary}

%description -n python3-railroad-diagrams %_description

%prep
%forgesetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Here, "railroad" is the name of the importable module.
%pyproject_save_files railroad

%check
%python3 railroad.py >/dev/null

%files -n python3-railroad-diagrams -f %{pyproject_files}
%doc README.md
%doc README-py.md

%changelog
%autochangelog

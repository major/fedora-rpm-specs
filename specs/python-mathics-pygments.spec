%global forgeurl https://github.com/Mathics3/Mathics3-pygments
Version:        10.0.0
%global tag     %{version}
%forgemeta

Name:           python-mathics-pygments
Release:        %autorelease
Summary:        Mathematica/Wolfram Language Lexer for Pygments

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This package provides a lexer and highlighter for Mathematica/Wolfram
Language source code using the pygments engine.}

%description %_description

%package -n     python3-mathics-pygments
Summary:        %{summary}

%description -n python3-mathics-pygments %_description

%prep
%autosetup -n Mathics3-pygments-%{version}
# Remove shebang from non-executable script
sed -i '1{\@^#!/usr/bin/env python@d}' mathics_pygments/generate/build_pygments_tables.py

%generate_buildrequires
%pyproject_buildrequires -x dev

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mathics_pygments

%check
%pytest

%files -n python3-mathics-pygments -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGES.rst

%changelog
%autochangelog

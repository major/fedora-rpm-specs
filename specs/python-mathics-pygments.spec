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
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%global _description %{expand:
This package provides a lexer and highlighter for Mathematica/Wolfram
Language source code using the pygments engine.}

%description %_description

%package -n     python%{python3_pkgversion}-mathics-pygments
Summary:        %{summary}

%description -n python%{python3_pkgversion}-mathics-pygments %_description

%prep
%autosetup -n Mathics3-pygments-%{version}
# Relax/rename the dependency on Mathics3_Scanner to use Fedora's package name and version
sed -i 's/"Mathics3_Scanner>=10.0.0"/"mathics-scanner>=1.3.0"/' pyproject.toml
sed -i 's/Mathics3_Scanner>=10.0.0/mathics-scanner>=1.3.0/' requirements.txt

# Remove shebang from non-executable script
sed -i '1{\@^#!/usr/bin/env python@d}' mathics_pygments/generate/build_pygments_tables.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files mathics_pygments

%check
%pytest

%files -n python%{python3_pkgversion}-mathics-pygments -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGES.rst

%changelog
%autochangelog

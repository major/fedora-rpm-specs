Name:           python-uc-micro-py
Version:        2.0.0
Release:        %autorelease
Summary:        Micro subset of Unicode data files for linkify-it.py projects

License:        MIT
URL:            https://github.com/tsutsu3/uc.micro-py
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/uc.micro-py-%{version}.tar.gz

BuildArch:      noarch
BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install): -l uc_micro

%global _description %{expand:Micro subset of Unicode data files for linkify-it.py projects.  This is a
Python port of uc.micro (https://github.com/markdown-it/uc.micro).}

%description
%_description

%package     -n python3-uc-micro-py
Summary:        Micro subset of Unicode data files for linkify-it.py projects

%description -n python3-uc-micro-py
%_description

%prep
%autosetup -n uc.micro-py-%{version}

# Do not run coverage tools in RPM builds
sed -i 's/, "coverage", "pytest-cov"//' pyproject.toml

%check
%pytest -v

%files -n python3-uc-micro-py -f %{pyproject_files}
%doc CHANGELOG.md README.md

%changelog
%autochangelog

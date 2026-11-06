# On PyPI the package is called 'three-merge'. However, the installed
# module is called 'three_merge', making this messy (sigh).

Name:           python-three_merge
Version:        0.1.1
Release:        %autorelease
Summary:        Simple library for merging two strings with respect to a base one

%global forgeurl https://github.com/spyder-ide/three-merge
%forgemeta

# SPDX
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
Simple Python library to perform a 3-way merge between strings, based on 
diff-match-patch. This library performs merges at a character level, as 
opposed to most VCS systems, which opt for a line-based approach.}

%description
%_description

%package -n     python3-three_merge
Summary:        %{summary}
# Add Provides based on the canonical project name (see comment at top)
%py_provides python3-three-merge

%description -n python3-three_merge
%_description

%prep
%forgeautosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l three_merge

%check
%pyproject_check_import
%pytest -v

%files -n python3-three_merge -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog

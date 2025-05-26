# Use forge macros to pull from GitHub
%global forgeurl https://github.com/python-rope/rope

Name:           python-rope
Version:        1.13.0
Release:        %autorelease
Summary:        Python Code Refactoring Library
%global tag %{version}
%forgemeta
License:        LGPL-3.0-or-later
URL:            %forgeurl
Source:         %forgesource
# Fix tests failing with Python 3.13
# https://github.com/python-rope/rope/issues/801
Patch:          %forgeurl/pull/809.patch

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Rope is the world’s most advanced open source Python refactoring
library (yes, I totally stole that tagline from Postgres).

Most Python syntax up to Python 3.10 is supported. Please file bugs and
contribute patches if you encounter gaps.}

%description %_description


%package -n python3-rope
Summary:        %summary

%description -n python3-rope %_description


%package -n python-rope-doc
Summary:        %summary documentation
Requires:       python3-rope = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python-rope-doc %{expand:
Documentation for %{summary}.}


%prep
%forgeautosetup -p1

# Remove linter from dev requirements
sed -i '/pytest-cov/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l rope


%check
%pytest -r fEs


%files -n python3-rope -f %{pyproject_files}
%doc docs/README.md *.md


%files -n python-rope-doc
%doc docs/*.rst README.rst


%changelog
%autochangelog

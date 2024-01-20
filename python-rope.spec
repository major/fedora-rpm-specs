# Use forge macros to pull from GitHub
%global forgeurl https://github.com/python-rope/rope

Name:           python-rope
Version:        1.12.0
Release:        %autorelease
Summary:        Python Code Refactoring Library
%global tag %{version}
%forgemeta
License:        LGPL-3.0-or-later
URL:            %forgeurl
Source:         %forgesource

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


%generate_buildrequires
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
%if 0%{?fc38}
%pyproject_save_files rope
%else
%pyproject_save_files -l rope
%endif


%check
# 1.12.0: pytest fails in
# ropetest/contrib/autoimporttest.py::AutoImportTest::test_search_submodule
# unit and some pytest warnings
# https://github.com/python-rope/rope/issues/749
k="${k-}${k+ and }not (AutoImportTest and test_search_submodule)"
%pytest -v -k "${k-}"


%files -n python3-rope -f %{pyproject_files}
%if 0%{?fc38}
%license COPYING
%endif
%doc docs/README.md *.md


%files -n python-rope-doc
%doc docs/*.rst README.rst


%changelog
%autochangelog

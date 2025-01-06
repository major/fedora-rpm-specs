%global srcname          pydoctor
%global forgeurl         https://github.com/twisted/%{srcname}
%global pydoctor_version 24.11.1
%global tag              %{pydoctor_version}
%global date             20241208
%forgemeta

Name:           python-%{srcname}
Version:        %{pydoctor_version}
Release:        %autorelease
Summary:        API documentation generator that works by static analysis
License:        MIT AND BSD-3-Clause AND OFL-1.1
# BSD-3-Clause
# pydoctor/astutils.py
# OFL-1.1 
# pydoctor/themes/readthedocs/fonts/*
# MIT
# pydoctor/*

URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(sphinx-rtd-theme)
# Test depdendencies
BuildRequires:  gcc
BuildRequires:  python3-pytest
BuildRequires:  python3-docutils
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-hypothesis
BuildRequires:  python3-beautifulsoup4
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest-subtests

%{?python_enable_dependency_generator}

%description
This is pydoctor, a standalone API documentation generator that works by 
static analysis.

It was written primarily to replace epydoc for the purposes of the Twisted 
project as epydoc has difficulties with zope.interface. If you are looking 
for a successor to epydoc after moving to Python 3, pydoctor might be the 
right tool for your project as well.

pydoctor puts a fair bit of effort into resolving imports and computing 
inheritance hierarchies and, as it aims at documenting Twisted, knows about 
zope.interface's declaration API and can present information about which 
classes implement which interface, and vice versa.


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
%{description}


%prep
%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel
%make_build docs


%install
%pyproject_install
%pyproject_save_files %{srcname} -l


%check
%pyproject_check_import -t
# Reported upstream
# https://github.com/twisted/pydoctor/issues/796
k="${k-}${k+ and }not (test_cyclic_imports_base_classes)"
# Timestamp error
k="${k-}${k+ and }not (test_main_project_name_guess)"
k="${k-}${k+ and }not (test_main_return_zero_on_warnings)"
k="${k-}${k+ and }not (test_main_return_non_zero_on_warnings)"
k="${k-}${k+ and }not (test_main_symlinked_paths)"
k="${k-}${k+ and }not (test_main_source_outside_basedir)"
k="${k-}${k+ and }not (test_make_intersphix)"
k="${k-}${k+ and }not (test_index_symlink)"
k="${k-}${k+ and }not (test_index_hardlink)"
k="${k-}${k+ and }not (test_apidocs_help)"
k="${k-}${k+ and }not (test_htmlbaseurl_option_all_pages)"
# Requires network
k="${k-}${k+ and }not (test_main_project_name_option)"
k="${k-}${k+ and }not (test_unquote_naughty_quoted_strings)"

%pytest -k "${k-}"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst CONTRIBUTING.rst
%{_bindir}/pydoctor


%changelog
%autochangelog
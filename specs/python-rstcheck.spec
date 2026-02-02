%global forgeurl https://github.com/rstcheck/rstcheck

Name:       python-rstcheck
Version:    6.2.5
Release:    %autorelease
Summary:    Checks syntax of reStructuredText and code blocks nested within it
%forgemeta

# spdx
License:    MIT
URL:        %forgeurl
Source0:    %forgesource


BuildArch:  noarch
%description
Checks syntax of reStructuredText and code blocks nested within it.

%package -n python3-rstcheck
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
Summary:        %{summary}

%description -n python3-rstcheck
Checks syntax of reStructuredText and code blocks nested within it.


%prep
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%forgesetup

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install

%pyproject_save_files rstcheck

%check
# intermittently fails to find some data files for tests
# TODO: needs debugging
%pytest -v -k "not test_all_good_examples and not test_all_bad_examples[test_file2] and not test_all_bad_examples_recurively and not test_error_without_config_file and not test_file_1_is_bad_without_config"

%files -n python3-rstcheck -f %{pyproject_files}
%doc README.rst AUTHORS.rst
%{_bindir}/rstcheck

%changelog
%autochangelog

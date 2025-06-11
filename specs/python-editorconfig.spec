# The tests are stored in a separate repository, which is normally accessed
# as a git submodule.
%global tests_commit 895b3a65d0d823dbd0acf2bc402376381995d1b1

Name:           python-editorconfig
Version:        0.17.1
Release:        %autorelease
Summary:        EditorConfig File Locator and Interpreter for Python

# See COPYING: the overall license is BSD-2-Clause, but the following files are derived
# from the Python standard library under the PSF-2.0 license:
#   - editorconfig/fnmatch.py
#   - editorconfig/ini.py
License:        BSD-2-Clause AND PSF-2.0
URL:            https://github.com/editorconfig/editorconfig-core-py
Source0:        %{url}/archive/v%{version}/editorconfig-core-py-%{version}.tar.gz
%global tests_url https://github.com/editorconfig/editorconfig-core-test
Source1:        %{tests_url}/archive/%{tests_commit}/editorconfig-core-test-%{tests_commit}.tar.gz

BuildSystem:            pyproject
BuildOption(install):   -l editorconfig

BuildArch:      noarch

BuildRequires:  tomcli

# For tests:
BuildRequires:  cmake

%global common_description %{expand:
EditorConfig Python Core provides the same functionality as the EditorConfig C
Core.}

%description %{common_description}


%package     -n python3-editorconfig
Summary:        %{summary}

# Dropped without replacement for F43+; we can remove the Obsoletes in F45.
Obsoletes:      python-editorconfig-doc < 0.17.1-2

%description -n python3-editorconfig %{common_description}


%package        doc
Summary:        Documentation for python-editorconfig

%description    doc %{common_description}


%prep
%setup -q -n editorconfig-core-py-%{version}
rm -vrf tests
%setup -q -n editorconfig-core-py-%{version} -T -D -b 1
mv ../editorconfig-core-test-%{tests_commit}/ tests/

# Remove overly-strict setuptools minimum version bound. Each new release
# requires an extremely current setuptools because the version bound is
# automatically bumped by renovate automation; the bound  does not necessarily
# reflect the actual minimum version that will work correctly.
tomcli set pyproject.toml lists replace build-system.requires \
    'setuptools>.*' 'setuptools'


%build -a
# This prepares for testing.
%cmake -DPYTHON_EXECUTABLE='%{python3}'


%install -a
# The command-line tool would conflict with the one from the C version of
# EditorConfig. It could be installed under a different name, if anyone ever
# reports a need for it.
rm '%{buildroot}%{_bindir}/editorconfig'


%check -a
export %{py3_test_envvars}
%ctest


%files -n python3-editorconfig -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog

%global srcname   enrich
%global pkgname   python-enrich
%global forge_url https://github.com/pycontribs/%{srcname}
%global common_description %{expand:
rich library functionality with a set of changes that were not accepted
to rich itself.
}

%bcond_without tests

Name:           %{pkgname}
Version:        1.2.7
%forgemeta
Release:        %autorelease
Summary:        Enrich adds few missing features to the wonderful rich library
URL:            %{forge_url}
Source:         %{pypi_source}
License:        MIT
BuildArch:      noarch
patch:          0001-remove-unsuported-pytest-option.patch
patch:          0002_remove_pytest_plus_dependency.patch
# Backport of:
# Remove mock from test dependencies (#46)
# https://github.com/pycontribs/enrich/commit/6a21526fed438cdcd3ee0f9be27d8348293adcee
Patch:          remove-python-mock.patch
# https://bugzilla.redhat.com/show_bug.cgi?id=2248708
# Backport of:
# Update build-system requirement for setuptools-scm to >=7.0.0 (#45)
# https://github.com/pycontribs/enrich/commit/6a21526fed438cdcd3ee0f9be27d8348293adcee
Patch:          remove-setuptools-scm-git-archive.patch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %{common_description}

%package -n python3-%{srcname}
Summary: %summary

%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests: -x test}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with tests}
%check
PYTHONPATH=src %{python3} -m pytest src/enrich/test -v -k "not test_rich_console_ex"
%endif

%files -n python3-%{srcname}
%license LICENSE
%{python3_sitelib}/enrich/
%{python3_sitelib}/enrich-%{version}.dist-info/

%changelog
%autochangelog

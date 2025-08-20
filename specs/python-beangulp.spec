%global srcname beangulp

%bcond check 1

Name:           python-%{srcname}
Version:        0.2.0
Release:        %autorelease
Summary:        Importers Framework for Beancount

License:        GPL-2.0-only
URL:            https://github.com/beancount/beangulp
# PyPI tarball doesn't include test artifacts
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%if %{with check}
# Not packaged yet
# BuildRequires:  python3dist(petl)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
beangulp provides a framework for importing transactions into a Beancount
ledger from account statements and other documents and for managing documents.}

%description %_description

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description

%prep
%autosetup -p1 -n %{srcname}-%{version}

# petl isn't packaged yet
rm beangulp/{petl_utils,petl_utils_test}.py

# Installed without executable permissions, so the shebang is useless
# (and contains prohibited /usr/bin/env anyway):
sed -r -i '1{/^#!/d}' beangulp/file_type_testdata/example.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

# Remove spurious directories
rm -r %{buildroot}%{python3_sitelib}/{examples,tools}

%check
%if %{with check}
# Skip broken test
%pytest -v --deselect beangulp/tests/testing.rst::testing.rst
%else
%pyproject_check_import
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

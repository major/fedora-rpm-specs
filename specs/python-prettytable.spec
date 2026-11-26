# not available on RHEL
%bcond lf %{undefined rhel}

%global pypi_name prettytable

Name:           python-%{pypi_name}
Version:        3.19.0
Release:        %autorelease
Summary:        Python library to display tabular data in tables

License:        BSD-3-Clause
URL:            https://github.com/jazzband/prettytable
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  sed
BuildRequires:  python3dist(pytest)
%if %{with lf}
BuildRequires:  python3dist(pytest-lazy-fixtures)
%endif
BuildRequires:  python3dist(wcwidth)


%description
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.

%package -n python3-%{pypi_name}
Summary:	Python library to display tabular data in tables

%description -n python3-%{pypi_name}
PrettyTable is a simple Python library designed to make it quick and easy to
represent tabular data in visually appealing ASCII tables. It was inspired by
the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for
selection of which columns are to be printed, independent alignment of columns
(left or right justified or centred) and printing of "sub-tables" by specifying
a row range.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^*!\//, 1d' src/prettytable/*.py
%if %{without lf}
sed -i -e 's/from pytest_lazy_fixtures import lf/lf = str/' tests/test_prettytable.py
%endif

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files prettytable

%check
%pytest %{!?with_lf:-k 'not TestBuildEquivalence and not TestMultiPattern'}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md CHANGELOG.md

%changelog
%autochangelog

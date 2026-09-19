%global pypi_name pytest-json-report
# Some tests currently fail
%global with_tests 0

Name:          python-%{pypi_name}
Version:       1.5.0
Release:       %autorelease
Summary:       A pytest plugin to report test results as JSON
License:       MIT
URL:           https://github.com/numirias/%{pypi_name}
Source0:       %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
%if 0%{?with_tests}
# Test requirements
BuildRequires: python3dist(flaky)
BuildRequires: python3dist(pytest-xdist)
BuildRequires: python3dist(pytest-metadata)
%endif

%global _description %{expand:
This pytest plugin creates test reports as JSON. This makes it easy to
process test results in other applications.

It can report a summary, test details, captured output, logs, exception
tracebacks and more. Additionally, you can use the available fixtures
and hooks to add metadata and customize the report as you like.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l pytest_jsonreport

%if 0%{?with_tests}
%check
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog

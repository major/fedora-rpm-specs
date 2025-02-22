%bcond tests    1

Name:           python-ddt
Version:        1.7.2
Release:        %autorelease
Summary:        Python library to multiply test cases
License:        MIT
URL:            https://github.com/datadriventests/ddt
Source:         %{pypi_source ddt}
BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-pyyaml
BuildRequires:  python3-six
%if %{undefined el10}
# aiounittest is not yet available for EL10
# https://bugzilla.redhat.com/show_bug.cgi?id=2346738
BuildRequires:  python3-aiounittest
%endif
%endif

%global common_description %{expand:
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.}


%description %{common_description}


%package -n python3-ddt
Summary:        %{summary}


%description -n python3-ddt %{common_description}


%prep
%autosetup -n ddt-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ddt


%check
%if %{with tests}
# skip tests that require aiounittest on EL10
%pytest %{?el10:--ignore test/test_async.py}
%else
%pyproject_check_import
%endif


%files -n python3-ddt -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog

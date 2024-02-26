# Created by pyp2rpm-3.3.5
%global pypi_name hypothesmith

%global common_description %{expand:
Hypothesis strategies for generating Python programs, something like CSmith.}

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.3.3
Release:        %autorelease
Summary:        Hypothesis strategies for generating Python programs

License:        MPL-2.0
URL:            https://github.com/Zac-HD/hypothesmith
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
# rm -rf %{pypi_name}.egg-info
# Tox configuration is passing unsupported arguments to pytest
# rm tox.ini

%generate_buildrequires
%pyproject_buildrequires %{?with_tests: -r deps/test.in}


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files %{pypi_name}


%if %{with tests}
%check
%pytest
%endif


%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md


%changelog
%autochangelog

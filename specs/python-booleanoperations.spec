# We disable tests due to missing python test dep fontPens, which is required
# for *all* tests, not just a subset.
%bcond tests 0

Name:           python-booleanoperations
Version:        0.10.0
Release:        %autorelease
Summary:        Boolean operations on paths

License:        MIT
URL:            https://github.com/typemytype/booleanOperations
Source:         %{url}/archive/%{version}/booleanOperations-%{version}.tar.gz

BuildArch:      noarch

%global common_description %{expand:
Boolean operations on paths based on a super fast polygon clipper library by
Angus Johnson.}

%description %{common_description}

%package -n python3-booleanoperations
Summary:        %{summary}

%description -n python3-booleanoperations %{common_description}

%prep
%autosetup -n booleanOperations-%{version}

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_buildrequires %{?with_tests:-x test}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l booleanOperations

%check
%pyproject_check_import
%if %{with tests}
%pytest -v
%endif

%files -n python3-booleanoperations -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

%global srcname  pytest-cov
%global slugname pytest_cov
%global forgeurl https://github.com/pytest-dev/%{srcname}

%global common_description %{expand:
This plugin produces coverage reports. Compared to just using coverage run this
plugin does some extras:

  • Subprocess support: you can fork or run stuff in a subprocess and will get
    covered without any fuss.
  • Xdist support: you can use all of pytest-xdist’s features and still get
    coverage.
  • Consistent pytest behavior. If you run coverage run -m pytest you will have
    slightly different sys.path (CWD will be in it, unlike when running
    pytest).

All features offered by the coverage package should work, either through
pytest-cov’s command line options or through coverage’s config file.
}

# During python mass rebuild we need to build python-pytest-cov without
# tests because some dependencies are not yet available
%bcond_without tests

Name:           python-%{srcname}
Version:        5.0.0
%forgemeta
Release:        %autorelease
Summary:        Coverage plugin for pytest
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description %{common_description}

%package -n python3-%{srcname}
Summary: %{summary}
%description -n python3-%{srcname} %{common_description}

%prep
%forgeautosetup -p1
# The “hunter” testing dependency (https://github.com/ionelmc/python-hunter) is
# not packaged, but it also does not seem to be used.
sed -r -i '/^[[:blank:]]*.hunter.,[[:blank:]]*$/d' setup.py

%generate_buildrequires
%pyproject_buildrequires -r %{?with_tests:-x testing}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{slugname}

%if %{with tests}
%check
k="$(awk 'NR>1 {pre=" and " } { printf "%snot %s", pre, $0 }' <<EOF
test_append_coverage_subprocess
test_central_subprocess
test_cleanup_on_sigterm
test_dist_missing_data
test_dist_subprocess_collocated
test_dist_subprocess_not_collocated
test_subprocess_with_path_aliasing
EOF
)"
%pytest -k "${k}"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc *.rst
%{python3_sitelib}/%{srcname}.pth

%changelog
%autochangelog

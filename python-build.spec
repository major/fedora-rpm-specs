%global pypi_name build

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        %autorelease
Summary:        A simple, correct PEP517 package builder

License:        MIT
URL:            https://github.com/pypa/build
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros >= 0-41

%description
A simple, correct PEP517 package builder.


%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
A simple, correct PEP517 package builder.


%pyproject_extras_subpkg -n python3-%{pypi_name} virtualenv


%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# deprecated python3-toml is not needed on Python 3.11+
# upstream: https://github.com/pypa/build/pull/563
sed -Ei '/\btoml\b/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test,virtualenv

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
# The skipped tests require internet
%pytest -k "not (test_build_package or \
                 test_build_package_via_sdist or \
                 test_output[via-sdist-isolation] or \
                 test_output[wheel-direct-isolation] or \
                 test_wheel_metadata[True] or \
                 test_wheel_metadata_isolation or \
                 test_with_get_requires or \
                 test_build_sdist or \
                 test_build_wheel[from_sdist] or \
                 test_build_wheel[direct])"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/pyproject-build

%changelog
%autochangelog

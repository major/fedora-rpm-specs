Name:           python-multidict
Version:        6.3.0
Release:        %autorelease
Summary:        MultiDict implementation

License:        Apache-2.0
URL:            https://github.com/aio-libs/multidict
Source:         %{pypi_source multidict}

BuildRequires:  gcc

%global _description %{expand:
Multidict is dict-like collection of key-value pairs where key might occur more
than once in the container.}

%description %_description

%package -n python3-multidict
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-cython
BuildRequires:  python3-pytest

%description -n python3-multidict %_description

%prep
%autosetup -n multidict-%{version}
sed -e "/--cov/d" \
    -e "/-p pytest_cov/d" \
    -i pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l multidict

%check
# circular import tests fail in mock
# benchmark tests require pytest_codspeed which isn't packaged yet
%pytest \
    --verbose \
    --ignore tests/test_circular_imports.py \
    --ignore tests/test_multidict_benchmarks.py \
    --ignore tests/test_views_benchmarks.py \
    tests

%files -n python3-multidict -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

%global pypi_name filetype

Name:           python-%{pypi_name}
Version:        1.2.0
Release:        %autorelease
Summary:        Infer file type and MIME type of any file/buffer

License:        MIT
URL:            https://github.com/h2non/filetype.py
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pyproject-rpm-macros
Buildrequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Small and dependency free Python package to infer file type and MIME type
checking the magic numbers signature of a file or buffer.

%generate_buildrequires
%pyproject_buildrequires -r

%prep
%setup -q -n %{pypi_name}.py-%{version}
sed -i -e '/^#!\//, 1d' examples/*.py
rm -rf examples/__init__.py
# Remove deprecated universal wheel option if present
[ -f setup.cfg ] && sed -i '/^\[bdist_wheel\]/,/^\[/ s/^universal\s*=.*$//' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
rm -rf %{buildroot}%{python3_sitelib}/examples

%check
%pytest -v tests --ignore tests/test_benchmark.py \
  -k "not test_guess_memoryview and not test_guess_extension_memoryview \
    and not test_guess_mime_memoryview and not test_guess_zstd"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst History.md examples
%license LICENSE
%{_bindir}/%{pypi_name}

%autochangelog

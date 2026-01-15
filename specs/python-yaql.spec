%global pypi_name yaql

# Disable docs building as it doesn't support recent sphinx
%global with_docs 0

Name:           python-%{pypi_name}
Version:        3.2.0
Release:        %autorelease
Summary:        Yet Another Query Language

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source:         %pypi_source

BuildArch:      noarch

%description
YAQL library has a out of the box large set of commonly used functions.

%package -n     python3-%{pypi_name}
Summary:        YAQL library has a out of the box large set of commonly used functions.

%description -n python3-%{pypi_name}
YAQL library has a out of the box large set of commonly used functions.

%if 0%{?with_docs}
# Documentation package
%package -n python-%{pypi_name}-doc
Summary:        Documentation for YAQL library

%description -n python-%{pypi_name}-doc
Documentation for YAQL library
%endif

%prep
%autosetup -n %{pypi_name}-%{version} -p1

sed -i '/sphinx-build/ s/-W//' tox.ini

%generate_buildrequires
%if 0%{?with_docs}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%if 0%{?with_docs}
# generate html docs
%tox -e docs
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
mv %{buildroot}/%{_bindir}/%{pypi_name} %{buildroot}/%{_bindir}/python3-%{pypi_name}

pushd %{buildroot}%{_bindir}
for i in %{pypi_name}-{3,%{?python3_version}}; do
    ln -sf  python3-%{pypi_name} $i
    ln -sf  python3-%{pypi_name} %{pypi_name}
done
popd

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc doc/source/readme.rst README.rst
%{_bindir}/python3-%{pypi_name}
%{_bindir}/%{pypi_name}-3*
%{_bindir}/%{pypi_name}

%if 0%{?with_docs}
%files -n python-%{pypi_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%changelog
%autochangelog

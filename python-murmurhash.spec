%global pypi_name murmurhash

Name:           python-%{pypi_name}
Version:        1.0.10
Release:        3%{?dist}
Summary:        Cython bindings for MurmurHash2

License:        MIT
URL:            https://github.com/explosion/murmurhash
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Cython bindings for MurmurHash2

%package -n     python3-%{pypi_name}
Summary:        Cython bindings for MurmurHash2

%description -n python3-%{pypi_name}
Cython bindings for MurmurHash2

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove random *.h
rm -rf include/msvc9/stdint.h

%generate_buildrequires
%pyproject_buildrequires requirements.txt

%build
%pyproject_wheel

%check
pushd %{buildroot}/%{python3_sitearch}
%pytest -p no:cacheprovider %{pypi_name}/tests
popd

%install
%pyproject_install

# E: zero-length /usr/lib64/python3.12/site-packages/murmurhash/__init__.pxd
rm %{buildroot}%{python3_sitearch}/%{pypi_name}/__init__.pxd

# remove local murmurhash/ headers
rm -rf %{buildroot}%{python3_sitearch}/%{pypi_name}/include

# remove tests
rm -rf %{buildroot}/%{python3_sitearch}%{pypi_name}/tests

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}.dist-info

%changelog
* Thu Jan 4 2024 Tom Rix <trix@redhat.com> - 1.0.10-3
- remove tests from install

* Wed Jan 3 2024 Tom Rix <trix@redhat.com> - 1.0.10-2
- remove pypi_version
- change requirements
- Add check

* Sat Dec 16 2023 Tom Rix <trix@redhat.com> - 1.0.10-1
- Initial package.

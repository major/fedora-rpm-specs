%global pypi_name pkginfo2

Name:           python-%{pypi_name}
Version:        30.0.0
Release:        %autorelease
Summary:        API for querying the distutils metadata written in the PKG-INFO file

License:        MIT
URL:            https://github.com/nexB/pkginfo2
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%global common_description %{expand:
This package provides an API for querying the distutils metadata written in the
PKG-INFO file inside a source distriubtion (an sdist) or a binary distribution
or a wheel (e.g., created by running bdist_egg).  It can also query the EGG-INFO
directory of an installed distribution, and the *.egg-info stored in a
"development checkout" (e.g, created by running setup.py develop), or the
*.dist-info from an as-installed package.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for python-%{pypi_name}
# BSD-2-Clause: Sphinx javascript
License:        MIT AND BSD-2-Clause
BuildArch:      noarch
Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       bundled(js-doctools)
Provides:       bundled(js-language_data)
Provides:       bundled(js-searchtools)

%description -n python-%{pypi_name}-doc
%{common_description}

This package is providing the documentation for %{pypi_name}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
sphinx-build-3 -b html docs/ html
# remove the sphinx-build-3 leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.txt README.txt TODO.txt
%license LICENSE.txt
%{_bindir}/pkginfo2

%files -n python-%{pypi_name}-doc
%doc html

%changelog
%autochangelog

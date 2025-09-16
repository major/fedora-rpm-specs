%global pypi_name packageurl-python

Name:           python-%{pypi_name}
Version:        0.17.5
Release:        %autorelease
Summary:        Python implementation of the package url spec

License:        MIT
URL:            https://github.com/package-url/packageurl-python
Source:         %url/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global common_description %{expand:
A parser and builder for purl aka. Package URLs for Python 2 and 3. See
https://github.com/package-url/purl-spec for details.}

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{common_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rfv thirdparty/

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files packageurl

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc AUTHORS.rst CHANGELOG.rst CONTRIBUTING.rst README.rst
%license mit.LICENSE

%changelog
%autochangelog

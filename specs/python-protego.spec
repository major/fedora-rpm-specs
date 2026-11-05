%global pkg_name protego
%global pypi_name protego
%global desc %{expand:
Protego is a pure-Python `robots.txt` parser with support for modern
conventions.}

Name:		python-protego
Version:	0.7.0
Release:	%autorelease
Summary:	Pure-Python robots.txt parser with support for modern conventions

License:	BSD-3-Clause
URL:		https://github.com/scrapy/protego
Source0:	%{pypi_source}

BuildArch:	noarch
BuildRequires:	python3dist(pytest)


%description
%{desc}

%package -n python3-%{pkg_name}
Summary:	%{summary}



%description -n python3-%{pkg_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/protego
%{python3_sitelib}/protego-*.dist-info

%changelog
%autochangelog

%global pypi_name pysodium

Name:           python-%{pypi_name}
Version:        0.7.18
Release:        %autorelease
Summary:        A Python libsodium wrapper

License:        BSD-2-Clause
URL:            https://github.com/stef/pysodium
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  pkgconfig(libsodium)
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%global _description %{expand:
This is a very simple wrapper around libsodium masquerading as nacl.}

%description
%{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Requires:       libsodium

%description -n python3-%{pypi_name}
%{_description}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-%{pypi_name}
%doc AUTHORS README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}*.dist-info
%{python3_sitelib}/%{pypi_name}

%changelog
%autochangelog

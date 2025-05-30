%global pypi_name scanless

Name:           %{pypi_name}
Version:        2.2.1
Release:        %autorelease
Summary:        Online port scan scraper

License:        Unlicense
URL:            https://github.com/vesche/scanless
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3-%{pypi_name} = %{version}-%{release}

%description
scanless is a Python 3 command-line utility and library for using websites
that can perform port scans on your behalf.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
scanless is a Python 3 command-line utility and library for using websites
that can perform port scans on your behalf.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n %{pypi_name}
%{_bindir}/%{pypi_name}

%files -n python3-%{pypi_name}
%doc README.md
%{_bindir}/scanless
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog

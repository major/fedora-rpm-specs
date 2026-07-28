%global pypi_name colorlog
%global desc "colorlog.ColoredFormatter is a formatter for use with Python's logging module that outputs records using terminal colors."

Name:           python-%{pypi_name}
Version:        6.12.0
Release:        %autorelease
Summary:        Colored formatter for the Python logging module

License:        MIT
URL:            https://github.com/borntyping/python-colorlog
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%generate_buildrequires
%pyproject_buildrequires

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%{pytest} -v

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}*.dist-info/

%changelog
%autochangelog

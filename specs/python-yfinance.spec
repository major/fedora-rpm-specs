%global         srcname     yfinance
%global         forgeurl    https://github.com/ranaroussi/%{srcname}
Version:        0.2.51
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Yahoo! Finance market data downloader

License:        Apache-2.0
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Ever since Yahoo! finance decommissioned their historical data API, many
programs that relied on it to stop working.

yfinance aims to solve this problem by offering a reliable, threaded,
and Pythonic way to download historical market data from Yahoo! finance.}

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}


%prep
%forgeautosetup

# Remove the python shebang from non-executable files.
sed -i '1{\@^#!/usr/bin/env python@d}' yfinance/*.py

# Allow an older version of requests.
sed -i 's/requests>=2.31/requests>=2.28/' requirements.txt setup.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install

# A sample executable is included but it does not seem to work. It's not needed
# for the package since this is a python library meant to be used by other
# python executables.
rm -vf %{buildroot}%{_bindir}/sample

%pyproject_save_files yfinance


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog

%global         srcname     yfinance
%global         forgeurl    https://github.com/ranaroussi/%{srcname}
Version:        1.5.1
%global         tag         %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Download market data from Yahoo! Finance API

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
find yfinance -name "*.py" -exec sed -i -e '1{\@^#!/usr/bin/env python@d}' {} +

# curl_cffi is not packaged in Fedora, but is optional and falls back to requests.
sed -i '/curl_cffi/d' requirements.txt
sed -i "s/'curl_cffi>=0.15',//" setup.py

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
%license LICENSE.txt
%doc README.md


%changelog
%autochangelog

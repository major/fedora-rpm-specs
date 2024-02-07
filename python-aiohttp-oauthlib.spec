Name:           python-aiohttp-oauthlib
Version:        0.1.0
Release:        2%{?dist}
Summary:        This library is a port of requests-oauthlib for aiohttp

License:        ISC
URL:            https://git.sr.ht/~whynothugo/aiohttp-oauthlib
Source:         %{pypi_source aiohttp-oauthlib}

BuildArch:      noarch

BuildRequires:  python3-devel
Requires:       python3-aiohttp

%global _description %{expand:
This library is a port of requests-oauthlib for aiohttp}

%description %_description

%package -n python3-aiohttp-oauthlib
Summary:        %{summary}

%description -n python3-aiohttp-oauthlib %_description


%prep
%autosetup -p1 -n aiohttp-oauthlib-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files aiohttp_oauthlib


%check
%pyproject_check_import


%files -n python3-aiohttp-oauthlib -f %{pyproject_files}
%doc README.*


%changelog
* Tue Dec 20 2022 David Kaufmann <astra@ionic.at> - 0.1.0-1
- Initial version

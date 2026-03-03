Name:           python-truststore
Version:        0.10.1
Release:        %autorelease
Summary:        Verify certificates using native system trust stores

License:        MIT
URL:            https://github.com/sethmlarson/truststore
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/truststore-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
# tests
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pyopenssl)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-httpserver)
BuildRequires:  python3dist(urllib3)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(trustme)

%global _description %{expand:
Truststore is a library which exposes native system certificate stores
(ie "trust stores") through an ssl.SSLContext-like API. This means that
Python applications no longer need to rely on certifi as a root certificate
store. Native system certificate stores have many helpful features compared
to a static certificate bundle like certifi:

- Automatically update certificates as new CAs are created and removed
- Fetch missing intermediate certificates
- Check certificates against certificate revocation lists (CRLs) to avoid
  monster-in-the-middle (MITM) attacks
- Managed per-system rather than per-application by a operations/IT team
- PyPI is no longer a CA distribution channel

Right now truststore is a stand-alone library that can be installed globally in
your application to immediately take advantage of the benefits in Python 3.10+.
Truststore has also been integrated into pip 24.2+ as the default method for
verifying HTTPS certificates (with a fallback to certifi).}

%description %_description

%package -n     python3-truststore
Summary:        %{summary}

%description -n python3-truststore %_description


%prep
%autosetup -p1 -n truststore-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l truststore


%check
%pyproject_check_import
# asyncio tests have deprecation warning
#pytest -m "not internet" --no-flaky-report 

%files -n python3-truststore -f %{pyproject_files}


%changelog
%autochangelog

%bcond tests 1

Name:           python-httpx
Version:        0.27.2
Release:        %autorelease
Summary:        Next-generation HTTP client for Python

License:        BSD-3-Clause
URL:            https://github.com/encode/httpx
Source0:        %{url}/archive/%{version}/httpx-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
%if %{with tests}
# See the Optional charset auto-detection group in requirements.txt:
BuildRequires:  %{py3_dist chardet}
# See the Tests & Linting group in requirements.txt:
BuildRequires:  %{py3_dist cryptography}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist trio}
BuildRequires:  %{py3_dist trustme}
BuildRequires:  %{py3_dist uvicorn}
BuildRequires:  %{py3_dist zstandard}
%endif
BuildRequires:  help2man

%global _description %{expand:
HTTPX is a fully featured HTTP client library for Python 3. It includes an
integrated command line client, has support for both HTTP/1.1 and HTTP/2, and
provides both sync and async APIs.}


%description %{_description}

%package -n     python3-httpx
Summary:        %{summary}

%description -n python3-httpx %{_description}
HTTPX is a fully featured HTTP client for Python, which provides sync and
async APIs, and support for both HTTP/1.1 and HTTP/2.

%pyproject_extras_subpkg -n python3-httpx brotli http2 socks

%pyproject_extras_subpkg -n python3-httpx cli
%{_bindir}/httpx
%{_mandir}/man1/httpx.1*

%prep
%autosetup -n httpx-%{version}

%generate_buildrequires
%pyproject_buildrequires -x brotli,cli,http2,socks

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l httpx
install -d '%{buildroot}%{_mandir}/man1'
PYTHONPATH='%{buildroot}%{python3_sitelib}' \
    PATH="${PATH-}:%{buildroot}%{_bindir}" \
    PYTHONDONTWRITEBYTECODE=1 \
    help2man --no-info --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/httpx.1' httpx

%check
%pyproject_check_import
%if %{with tests}
# These require network access (DNS)
k="${k-}${k+ and }not test_async_proxy_close"
k="${k-}${k+ and }not test_sync_proxy_close"

# ResourceWarning in test_write_timeout[trio] with trio >=0.27
# https://github.com/encode/httpx/discussions/3498
k="${k-}${k+ and }not test_write_timeout[trio]"

%pytest -k "${k-}" -v
%endif

%files -n python3-httpx -f %{pyproject_files}
%doc CHANGELOG.md
%doc README.md
%license LICENSE.md

%changelog
%autochangelog


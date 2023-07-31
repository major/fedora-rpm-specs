%global commit      0e96f88704a940ed8eda7299a27f2c9dbb6fcf09
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global common_description %{expand:
Falcon is a minimalist ASGI/WSGI framework for building mission-critical REST
APIs and microservices, with a focus on reliability, correctness, and
performance at scale.  When it comes to building HTTP APIs, other frameworks
weigh you down with tons of dependencies and unnecessary abstractions. Falcon
cuts to the chase with a clean design that embraces HTTP and the REST
architectural style.}


Name:           python-falcon
Version:        4.0.0~^2.%{shortcommit}
Release:        %autorelease
Summary:        Fast ASGI+WSGI framework for building data plane APIs at scale
License:        Apache-2.0
URL:            https://falconframework.org
Source:         https://github.com/falconry/falcon/archive/%{commit}/falcon-%{shortcommit}.tar.gz

# downstream-only patch to remove bundled library
Patch:          0001-Use-system-mimeparse.patch

BuildRequires:  gcc


%description %{common_description}


%package -n python3-falcon
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools pip wheel cython}
# requirements/tests
BuildRequires:  %{py3_dist pytest pyyaml requests testtools}
BuildRequires:  %{py3_dist pytest-asyncio httpx aiofiles websockets}
BuildRequires:  %{py3_dist cbor2 msgpack mujson ujson python-mimeparse}


%description -n python3-falcon %{common_description}


%prep
%autosetup -p 1 -n falcon-%{commit}
rm -rf falcon/vendor


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files falcon


%check
# skip tests that fail on python 3.12
%pytest -k 'not test_client_disconnect_early and not test_ws_http_error_or_status_response and not test_ws_http_error_or_status_error_handler' tests


%files -n python3-falcon -f %{pyproject_files}
%doc README.rst
%{_bindir}/falcon-bench
%{_bindir}/falcon-inspect-app
%{_bindir}/falcon-print-routes


%changelog
%autochangelog

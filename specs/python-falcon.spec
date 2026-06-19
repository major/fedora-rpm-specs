Name:           python-falcon
Epoch:          1
Version:        4.3.1
Release:        %autorelease
Summary:        ASGI+WSGI framework for building data plane APIs
License:        Apache-2.0
URL:            https://falconframework.org
Source:         %{pypi_source falcon}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global common_description %{expand:
Falcon is a minimalist ASGI/WSGI framework for building mission-critical REST
APIs and microservices, with a focus on reliability, correctness, and
performance at scale.  When it comes to building HTTP APIs, other frameworks
weigh you down with tons of dependencies and unnecessary abstractions.  Falcon
cuts to the chase with a clean design that embraces HTTP and the REST
architectural style.}


%description %{common_description}


%package -n python3-falcon
Summary:        %{summary}


%description -n python3-falcon %{common_description}


%prep
%autosetup -p 1 -n falcon-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l falcon


%check
# based on testenv:mintest in tox.ini
%pytest tests -k 'not slow'


%files -n python3-falcon -f %{pyproject_files}
%doc README.rst
%{_bindir}/falcon-bench
%{_bindir}/falcon-inspect-app
%{_bindir}/falcon-print-routes


%changelog
%autochangelog

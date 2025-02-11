%global forgeurl https://github.com/aio-libs/janus

Version:        1.2.0

%forgemeta

Name:           python-janus
Release:        %autorelease
Summary:        Thread-safe asyncio-aware queue for Python

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
# Testing requirements to avoid extra checks
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)

%global _description %{expand:
Mixed sync-async queue, supposed to be used for communicating between classic
synchronous (threaded) code and asynchronous (in terms of asyncio) one.

Like Janus god the queue object from the library has two faces: synchronous and
asynchronous interface.

Synchronous is fully compatible with standard queue, asynchronous one follows
asyncio queue design.}

%description %_description

%package -n python3-janus
Summary:        %{summary}

%description -n python3-janus %_description


%prep
%forgesetup


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files janus


%check
# Ignore benchmarks (requires `pytest-codspeed`, which is not packaged for Fedora)
%pytest --ignore=tests/test_benchmarks.py


%files -n python3-janus -f %{pyproject_files}
%doc CHANGES.rst README.rst


%changelog
%autochangelog

%if 0%{?fedora}
%{?python_enable_dependency_generator}
%endif

%global desc Implements support for python plugins in Nvim. Also works as a library for\
connecting to and scripting Nvim processes through its msgpack-rpc API.

%bcond check 1
%bcond sphinx 1

Name:           python-neovim
Version:        0.5.2
Release:        %autorelease
License:        Apache-2.0
Summary:        Python client to Neovim
URL:            https://github.com/neovim/pynvim
Source0:        https://github.com/neovim/pynvim/archive/%{version}/pynvim-%{version}.tar.gz
Patch0:         https://github.com/neovim/pynvim/pull/584.patch#/pynvim-fix-asyncio.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
%if %{with check}
BuildRequires:  neovim
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(greenlet)
BuildRequires:  python3dist(msgpack)
%endif

%if %{with sphinx}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
%endif

%description
%{desc}

%package -n python%{python3_pkgversion}-neovim
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-neovim}
Requires:       neovim
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-greenlet
Requires:       python%{python3_pkgversion}-msgpack
%endif

%description -n python%{python3_pkgversion}-neovim
%{desc}

%if %{with sphinx}
%package doc
Summary:        Documentation for %{name}

%description doc
%{desc}

This package contains documentation in HTML format.
%endif

%prep
%autosetup -n pynvim-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%if %{with sphinx}
pushd docs
make html
rm -f _build/html/.buildinfo
popd
%endif

%install
%pyproject_install

%if %{with check}
%check
# The broadcast test doesn't work, see
# https://github.com/neovim/pynvim/issues/585
%tox run -- -- -k 'not test_broadcast'
%endif

%files -n python%{python3_pkgversion}-neovim
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%if %{with sphinx}
%files doc
%license LICENSE
%doc docs/_build/html
%endif

%changelog
%autochangelog

%global srcname hpack

%global common_description %{expand:
HTTP/2 Header Encoding for Python This module contains a pure-Python
HTTP/2 header encoding (HPACK) logic for use in Python programs that implement
HTTP/2. It also contains a compatibility layer that automatically enables the
use of nghttp2 if it's available.}

Name:           python-%{srcname}
Version:        4.1.0
Release:        %autorelease
Summary:        Pure-Python HPACK header compression

License:        MIT
URL:            http://hyper.rtfd.org
VCS:            https://github.com/python-hyper/hpack
Source0:        %vcs/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)

%description %{common_description}

%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{common_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{common_description}

This is the documentation package for %{name}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
# Upstream uses tox to call pytest.  If we used it we'd have to patch out
# pytest-xdist, pytest-cov, and coverage related pytest flags.  Instead, we'll
# just call pytest directly.
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=${PWD} sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%if %{with check}
%check
%pytest -k 'not test_get_by_index_out_of_range'
%endif

%files -n python3-%{srcname} -f %{pyproject_files}

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog

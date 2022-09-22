%global srcname hyperframe

%global common_description %{expand:
Pure-Python HTTP/2 framing This library contains the HTTP/2
framing code used in the hyper project. It provides a pure-Python codebase
that is capable of decoding a binary stream into HTTP/2 frames. This library is
used directly by hyper and a number of other projects to provide HTTP/2 frame
decoding logic.}

Name:           python-%{srcname}
Version:        6.0.1
Release:        %autorelease
Summary:        HTTP/2 framing layer for Python

License:        MIT
URL:            https://github.com/python-hyper/hyperframe/
Source0:        %url/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
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
# pytest-xdist, pytest-cov, and coverage related pytest flags. Instead, we'll
# just call pytest directly.
%pyproject_buildrequires

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog

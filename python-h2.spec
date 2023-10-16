%global srcname h2

%global common_description %{expand:
HTTP/2 Protocol Stack This repository contains a pure-Python
implementation of a HTTP/2 protocol stack. It's written from the ground up to
be embeddable in whatever program you choose to use, ensuring that you can
speak HTTP/2 regardless of your programming paradigm.}

Name:           python-h2
Version:        4.1.0
Release:        %autorelease
Summary:        HTTP/2 State-Machine based protocol implementation

License:        MIT
URL:            https://hyper-h2.readthedocs.io
VCS:            https://github.com/python-hyper/h2
Source0:        %vcs/archive/v%{version}/%{srcname}-%{version}.tar.gz
# downstream only patch
Patch0:         0001-Fedora-tox-adjustments.patch
# repr() changes in Python 3.11
Patch1:         0001-Fix-repr-checks-for-Python-3.11.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
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
%pyproject_buildrequires -t

%build
%pyproject_wheel

# generate html docs
PYTHONPATH=$PWD/build/lib.%{python3_platform}-cpython-%{python3_version_nodots} sphinx-build docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%tox

%files -n python3-%{srcname} -f %{pyproject_files}

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog

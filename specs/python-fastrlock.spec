Name:           python-fastrlock
Version:        0.8.3
Release:        %autorelease
Summary:        Fast, re-entrant optimistic lock implemented in Cython

License:        MIT
URL:            https://github.com/scoder/fastrlock
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(wheel)

%global _description %{expand:
This is a C-level implementation of a fast, re-entrant, optimistic
lock for CPython. It is a drop-in replacement for threading.RLock.
FastRLock is implemented in Cython and also provides a C-API for
direct use from Cython code via from fastrlock cimport rlock or
from cython.cimports.fastrlock import rlock.}

%description %_description

%package -n     python3-fastrlock
Summary:        %{summary}

%description -n python3-fastrlock %_description

%prep
%autosetup -p1 -n fastrlock-%{version}

# So we do not have to keep up with a license for something we don't use.
rm appveyor_env.cmd

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l fastrlock

%check
%pyproject_check_import
%tox

%files -n python3-fastrlock -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog

%global pkgname pygit2

Name:           python-%{pkgname}
Version:        1.17.0
Release:        %autorelease
Summary:        Python bindings for libgit2

License:        GPL-2.0-only WITH GCC-exception-2.0
URL:            https://www.pygit2.org/
Source0:        https://github.com/libgit2/pygit2/archive/v%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz
# mock (by default) and koji builds never have network access, but testing
# that capability through a DNS resolution is not always accurate.
# Forcefully disable all network tests to avoid unnecessary build failures.
Patch:          python-pygit2-network-tests.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  (libgit2-devel >= 1.9.0 with libgit2-devel < 1.10.0)

%description
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.


%package -n     python3-%{pkgname}
Summary:        Python 3 bindings for libgit2
%{?python_provide:%python_provide python3-%{pkgname}}
BuildRequires:  python3-pytest

%description -n python3-%{pkgname}
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.

The python3-%{pkgname} package contains the Python 3 bindings.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  python3-sphinx_rtd_theme

%description    doc
Documentation for %{name}.


%prep
%autosetup -n %{pkgname}-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

make -C docs html


%install
%pyproject_install
find %{_builddir} -name '.buildinfo' -print -delete


%check
# This is horrible, but otherwise pytest does not use pygit2 from site-packages
rm -f pygit2/__init__.py
# https://github.com/libgit2/pygit2/issues/812
%ifarch ppc64 s390x
  PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-%{python3_version} -v || :
%else
  PYTHONPATH=%{buildroot}%{python3_sitearch} py.test-%{python3_version} -v
%endif


%files -n python3-%{pkgname}
%license COPYING
%doc README.md
%{python3_sitearch}/%{pkgname}-*.dist-info/
%{python3_sitearch}/%{pkgname}/

%files doc
%license COPYING
%doc docs/_build/html/*


%changelog
%autochangelog

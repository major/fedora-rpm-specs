%global pkgname pygit2

Name:           python-%{pkgname}
Version:        1.12.2
Release:        %autorelease
Summary:        Python bindings for libgit2

License:        GPLv2 with linking exception
URL:            https://www.pygit2.org/
Source0:        https://github.com/libgit2/pygit2/archive/v%{version}.tar.gz#/%{pkgname}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  (libgit2-devel >= 1.6.0 with libgit2-devel < 1.7.0)

%description
pygit2 is a set of Python bindings to the libgit2 library, which implements
the core of Git.


%package -n     python3-%{pkgname}
Summary:        Python 3 bindings for libgit2
%{?python_provide:%python_provide python3-%{pkgname}}
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

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


%build
%py3_build

make -C docs html


%install
%py3_install
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
%doc README.rst
%{python3_sitearch}/%{pkgname}-*.egg-info/
%{python3_sitearch}/%{pkgname}/

%files doc
%license COPYING
%doc docs/_build/html/*


%changelog
%autochangelog

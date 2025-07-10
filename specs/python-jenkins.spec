%global srcname jenkins

Name:           python-%{srcname}
Version:        1.8.2
Release:        %autorelease
Summary:        Python bindings for the remote Jenkins API

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://python-jenkins.readthedocs.org/en/latest
Source0:        https://opendev.org/jjb/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires:  %{_bindir}/sphinx-build
BuildArch:      noarch

%description
Python Jenkins is a library for the remote API of the Jenkins continuous
integration server. It is useful for creating and managing jobs as well as
build nodes.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-kerberos
BuildRequires:  python%{python3_pkgversion}-mock
BuildRequires:  python%{python3_pkgversion}-multi_key_dict
BuildRequires:  python%{python3_pkgversion}-multiprocess
BuildRequires:  python%{python3_pkgversion}-pbr >= 0.8.2
BuildRequires:  python%{python3_pkgversion}-requests
BuildRequires:  python%{python3_pkgversion}-requests-mock
BuildRequires:  python%{python3_pkgversion}-six >= 1.3.0
BuildRequires:  python%{python3_pkgversion}-testscenarios
BuildRequires:  python%{python3_pkgversion}-testtools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-multi_key_dict
Requires:       python%{python3_pkgversion}-pbr >= 0.8.2
Requires:       python%{python3_pkgversion}-requests
Requires:       python%{python3_pkgversion}-six >= 1.3.0
%endif

%if 0%{?!rhel} || 0%{?rhel} >= 8
Recommends:     python%{python3_pkgversion}-kerberos
%endif

%description -n python%{python3_pkgversion}-%{srcname}
Python Jenkins is a library for the remote API of the Jenkins continuous
integration server. It is useful for creating and managing jobs as well as
build nodes.


%prep
%autosetup -p1 -n %{name}

# Remove env from __init__.py
sed -i '1{s|^#!/usr/bin/env python||}' jenkins/__init__.py


%generate_buildrequires
export PBR_VERSION=%{version}

%pyproject_buildrequires


%build
export PBR_VERSION=%{version}

%pyproject_wheel

PYTHONDONTWRITEBYTECODE=1 \
  PYTHONPATH=$PWD \
  %make_build -C doc html man
rm doc/build/html/.buildinfo


%install
export PBR_VERSION=%{version}

%pyproject_install

install -D -m0644 -p doc/build/man/pythonjenkins.1 %{buildroot}%{_mandir}/man1/pythonjenkins.1


%check
%{__python3} -m testtools.run discover tests


%files -n python%{python3_pkgversion}-%{srcname}
%doc README.rst doc/build/html
%license COPYING
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/python_jenkins-%{version}.dist-info/
%{_mandir}/man1/pythonjenkins.1.*


%changelog
%autochangelog

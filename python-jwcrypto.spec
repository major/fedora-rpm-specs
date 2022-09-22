%if 0%{?fedora} || 0%{?rhel} > 7
# Enable python3 build by default
%bcond_without python3
%else
%bcond_with python3
%endif

%if 0%{?fedora} > 31 || 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

%global srcname jwcrypto

Name:           python-%{srcname}
Version:        1.4.2
Release:        %autorelease
Summary:        Implements JWK, JWS, JWE specifications using python-cryptography

License:        LGPLv3+
URL:            https://github.com/latchset/%{srcname}
Source0:        https://github.com/latchset/%{srcname}/releases/download/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
%if 0%{?with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-cryptography >= 2.3
BuildRequires:  python2-pytest
BuildRequires:  python2-deprecated
%endif

%if 0%{?with_python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-cryptography >= 2.3
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-deprecated
%endif

%description
Implements JWK, JWS, JWE specifications using python-cryptography


%if 0%{?with_python2}
%package -n python2-%{srcname}
Summary:        Implements JWK,JWS,JWE specifications using python-cryptography
Requires:       python2-cryptography >= 2.3
Requires:       python2-deprecated
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Implements JWK, JWS, JWE specifications using python-cryptography
%endif


%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Implements JWK, JWS, JWE specifications using python-cryptography
Requires:       python%{python3_pkgversion}-cryptography >= 2.3
Requires:       python%{python3_pkgversion}-deprecated
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
Implements JWK, JWS, JWE specifications using python-cryptography
%endif


%prep
%setup -q -n %{srcname}-%{version}


%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif


%check
%if 0%{?with_python2}
%{__python2} -bb -m pytest %{srcname}/test*.py
%endif
%if 0%{?with_python3}
%{__python3} -bb -m pytest %{srcname}/test*.py
%endif


%install
%if 0%{?with_python2}
%py2_install
%endif
%if 0%{?with_python3}
%py3_install
%endif

rm -rf %{buildroot}%{_docdir}/%{srcname}
%if 0%{?with_python2}
rm -rf %{buildroot}%{python2_sitelib}/%{srcname}/tests{,-cookbook}.py*
%endif
%if 0%{?with_python3}
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/tests{,-cookbook}.py*
rm -rf %{buildroot}%{python3_sitelib}/%{srcname}/__pycache__/tests{,-cookbook}.*.py*
%endif


%if 0%{?with_python2}
%files -n python2-%{srcname}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}-py%{python2_version}.egg-info
%endif

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info
%endif


%changelog
%autochangelog

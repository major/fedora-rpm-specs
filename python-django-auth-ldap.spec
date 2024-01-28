%if 0%{?rhel}
# RHEL does not ship openldap-server :(
%bcond_with check
%else
%bcond_without check
%endif

%global srcname django-auth-ldap

Name:           python-%{srcname}
Version:        4.1.0
Release:        8%{?dist}
Summary:        Django LDAP authentication backend

License:        BSD
URL:            https://pypi.org/project/django-auth-ldap
Source:         %{pypi_source}

BuildArch:      noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	pyproject-rpm-macros
BuildRequires:	%{py3_dist setuptools}
BuildRequires:	%{py3_dist setuptools-scm}
BuildRequires:	python%{python3_pkgversion}-setuptools_scm+toml
BuildRequires:	%{py3_dist pip}
BuildRequires:	%{py3_dist wheel}
BuildRequires:	%{py3_dist django} >= 2.2
BuildRequires:	%{py3_dist python-ldap} >= 3.1
BuildRequires:	%{py3_dist tox-current-env}
%if %{with check}
BuildRequires:  /usr/bin/ldapadd
BuildRequires:  /usr/sbin/slapd
%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{summary}.

%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with check}
%check
%tox
%endif

%files -n python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/django_auth_ldap/
%{python3_sitelib}/django_auth_ldap-%{version}.dist-info/

%changelog
* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 4.1.0-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 4.1.0-2
- Rebuilt for Python 3.11

* Sat Jun 11 2022 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0 (rhbz #2094373 and #2048088)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Jul 11 2021 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.4.0-1
- Update to 2.4.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 11 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.0-1
- Initial package

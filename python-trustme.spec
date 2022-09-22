%global srcname trustme
%global common_description %{expand:
You wrote a cool network client or server.  It encrypts connections using TLS.
Your test suite needs to make TLS connections to itself.  Uh oh.  Your test
suite probably doesn't have a valid TLS certificate.  Now what?  trustme is a
tiny Python package that does one thing: it gives you a fake certificate
authority (CA) that you can use to generate fake TLS certs to use in your
tests.  Well, technically they are real certs, they are just signed by your CA,
which nobody trusts.  But you can trust it.  Trust me.}

%bcond_without  tests

%if %{defined fedora}
%bcond_without  docs
%endif


Name:           python-%{srcname}
Version:        0.9.0
Release:        3%{?dist}
Summary:        #1 quality TLS certs while you wait, for the discerning tester
License:        MIT or ASL 2.0
URL:            https://github.com/python-trio/trustme
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  %{py3_dist pytest pyopenssl service-identity}
%endif


%description -n python3-%{srcname} %{common_description}


%if %{with docs}
%package -n python-%{srcname}-doc
Summary:        Documentation for %{name}
BuildRequires:  %{py3_dist sphinx sphinxcontrib-trio}


%description -n python-%{srcname}-doc
Documentation for %{name}.
%endif


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel

%if %{with docs}
sphinx-build-3 docs/source html
%endif


%install
%pyproject_install
%pyproject_save_files %{srcname}


%if %{with tests}
%check
%if %{defined el8}
# The upstream test suite uses cryptography's rfc4514_string method, which
# wasn't added until version 2.5.  RHEL 8 currently only provides version 2.3.
# https://cryptography.io/en/latest/changelog/?highlight=rfc4514_string#v2-5
%pytest --verbose -k "not (test_ca_custom_names or test_issue_cert_custom_names)"
%else
%pytest --verbose
%endif
%endif


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst


%if %{with docs}
%files -n python-%{srcname}-doc
%license LICENSE LICENSE.MIT LICENSE.APACHE2
%doc html
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.9.0-2
- Rebuilt for Python 3.11

* Thu Jan 27 2022 Carl George <carl@george.computer> - 0.9.0-1
- Latest upstream
- Resolves: rhbz#1993357

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Jul 24 2021 Carl George <carl@george.computer> - 0.8.0-1
- Latest upstream
- Resolves: rhbz#1969634

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.10

* Fri Mar 19 2021 Charalampos Stratakis <cstratak@redhat.com> - 0.7.0-1
- Update to 0.7.0 (rhbz#1927133)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 14 2020 Carl George <carl@george.computer> - 0.6.0-5
- Add doc subpackage

* Wed Oct 07 2020 Carl George <carl@george.computer> - 0.6.0-4
- Remove explicit run time requires in favor of automatically generated ones

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Carl George <carl@george.computer> - 0.6.0-1
- Latest upstream

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Carl George <carl@george.computer> - 0.5.2-1
- Latest upstream

* Tue Apr 16 2019 Carl George <carl@george.computer> - 0.5.1-1
- Latest upstream

* Fri Feb 22 2019 Carl George <carl@george.computer> - 0.5.0-1
- Latest upstream

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 13 2018 Carl George <carl@george.computer> - 0.4.0-1
- Initial package

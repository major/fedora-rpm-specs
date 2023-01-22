Name:           python-certifi
Version:        2022.09.24
Release:        2%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPL-2.0
URL:            https://certifi.io/
Source:         https://github.com/certifi/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          certifi-2022.09.24-use-system-cert.patch

BuildArch:      noarch

# Require the system certificate bundle (/etc/pki/tls/certs/ca-bundle.crt)
BuildRequires: ca-certificates

BuildRequires:  python3-devel

# Run upstream tests
BuildRequires: python3-pytest

%description
Certifi is a carefully curated collection of Root Certificates for validating
the trustworthiness of SSL certificates while verifying the identity of TLS
hosts. It has been extracted from the Requests project.

Please note that this Fedora package does not actually include a certificate
collection at all. It reads the system shared certificate trust collection
instead. For more details on this system, see the ca-certificates package.

%package -n python3-certifi
Summary:        %{summary}
Requires:       ca-certificates

%description -n python3-certifi
Certifi is a carefully curated collection of Root Certificates for validating
the trustworthiness of SSL certificates while verifying the identity of TLS
hosts. It has been extracted from the Requests project.

Please note that this Fedora package does not actually include a certificate
collection at all. It reads the system shared certificate trust collection
instead. For more details on this system, see the ca-certificates package.

This package provides the Python 3 certifi library.


%prep
%autosetup -p1

# Remove bundled Root Certificates collection
rm -rf certifi/*.pem


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files certifi


%check
# sanity check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
test $(%{__python3} -m certifi) == /etc/pki/tls/certs/ca-bundle.crt
test $(%{__python3} -c 'import certifi; print(certifi.where())') == /etc/pki/tls/certs/ca-bundle.crt
%{__python3} -c 'import certifi; print(certifi.contents())' > contents
diff --ignore-blank-lines /etc/pki/tls/certs/ca-bundle.crt contents
# upstream tests
%pytest -v


%files -n python3-certifi -f %{pyproject_files}
%doc README.rst


%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.09.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 14 2022 Karolina Surma <ksurma@redhat.com> - 2022.09.24-1
- Update to 2022.09.24

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.10.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2021.10.8-2
- Rebuilt for Python 3.11

* Tue Feb 08 2022 Major Hayden <major@redhat.com> - 2021.10.8-1
- Update to 2021.10.8.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 2020.12.5-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Joel Capitao <jcapitao@redhat.com> - 2020.12.5-1
- Update to 2020.12.5

* Tue Nov 10 2020 Joel Capitao <jcapitao@redhat.com> - 2020.11.8-1
- Update to 2020.11.8

* Thu Aug 13 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2020.6.20-1
- Update to 2020.6.20

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.4.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Miro Hrončok <mhroncok@redhat.com> - 2020.4.5.1-1
- Update to 2020.4.5.1 (#1843713)

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 2018.10.15-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.10.15-8
- Remove Python 2 subpackage (#1770744)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.10.15-7
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.10.15-6
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018  <jdennis@redhat.com> - 2018.10.15-3
- Resolves: rhbz#1659132 Incorrect location used for system certs
  where() now returns /etc/pki/tls/certs/ca-bundle.crt

* Fri Nov 02 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 2018.10.15-2
- Update spec to use %%pypi_source macro

* Tue Oct 23 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 2018.10.15-1
- Update to release: 2018.10.15
- Update patch to point to system certificates

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.26-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2016.9.26-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.26-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Oct 14 2017 williamjmorenor@gmail.com - 2016.9.26-6
- Fix path of .pem file
  Thanks to @carlwgeorge
  See: https://src.fedoraproject.org/rpms/python-certifi/pull-request/1

* Thu Oct 12 2017 williamjmorenor@gmail.com - 2016.9.26-5
- If fedora path to use current ca-certificates
- If epel7 follow proper file to .pem file

* Thu Oct 12 2017 Carl George <carl@george.computer> - 2016.9.26-4
- EPEL compatibility
- Include license
- Move ca-certificates requirement to subpackages

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.9.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Dec 28 2016 Adam Williamson <awilliam@redhat.com> - 2016.9.26-1
- New release 2016.9.26

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2015.04.28-10
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.04.28-9
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.04.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.04.28-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Sep 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> - 2015.04.28-6
- Update python macros
- Include subpackages for Python2 and Python3

* Thu Jul 09 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-5
- rebuilt

* Wed Jul 08 2015 William Moreno Reyes  <williamjmorenor at gmail.com> 
- 2015.04.28-4
- Initial Import of #1232433

* Mon Jul 06 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-3
- Remove shebang

* Thu Jul 02 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-2
- Remove bundle cacert.pem

* Tue Jun 16 2015 William Moreno Reyes <williamjmorenor at gmail.com> 
- 2015.04.28-1
- Initial packaging

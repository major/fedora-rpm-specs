%global srcname pysaml2

Name:           python-%{srcname}
Version:        7.1.2
Release:        1%{?dist}
Summary:        Python implementation of SAML Version 2
License:        ASL 2.0
URL:            https://github.com/IdentityPython/%{srcname}

%global gittag v%{version}



Source0: https://github.com/IdentityPython/%{srcname}/archive/%{gittag}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
PySAML2 is a pure python implementation of SAML2. It contains all
necessary pieces for building a SAML2 service provider or an identity
provider.  The distribution contains examples of both.  Originally
written to work in a WSGI environment there are extensions that allow
you to use it with other frameworks.



%package -n python3-%{srcname}
Summary: Python implementation of SAML Version 2
Conflicts:  python2-%{srcname} < 4.5.0-6
%{?python_provide:%python_provide python3-%{srcname}}

Requires: python3-requests >= 1.0.0
Requires: python3-future
Requires: python3-cryptography >= 3.1
Requires: python3-pytz
Requires: python3-pyOpenSSL
Requires: python3-dateutil
Requires: python3-defusedxml
Requires: python3-six
Requires: python3-xmlschema >= 1.2.1
Requires: xmlsec1
Requires: xmlsec1-openssl

BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-defusedxml
# To run  unit tests
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-requests >= 1.0.0
BuildRequires:  python3-future
BuildRequires:  python3-cryptography >= 3.1
BuildRequires:  python3-pytz
BuildRequires:  python3-pyOpenSSL
BuildRequires:  python3-dateutil
BuildRequires:  python3-defusedxml
BuildRequires:  python3-six
BuildRequires:  python3-xmlschema >= 1.2.1
BuildRequires:  python3-pymongo
BuildRequires:  python3-responses
BuildRequires:  xmlsec1
BuildRequires:  xmlsec1-openssl


%description -n python3-%{srcname}
PySAML2 is a pure python implementation of SAML2. It contains all
necessary pieces for building a SAML2 service provider or an identity
provider.  The distribution contains examples of both.  Originally
written to work in a WSGI environment there are extensions that allow
you to use it with other frameworks.


%package doc
Summary: Documentation for Python implementation of SAML Version 2

%description doc
Documentation for Python implementation of SAML Version 2.

%prep
%autosetup -n %{srcname}-%{version} -S git
sed -i '/argparse/d' setup.py

# Avoid non-executable-script rpmlint while maintaining timestamps
find src -name \*.py |
while read source; do
  if head -n1 "$source" | grep -F '/usr/bin/env'; then
    touch --ref="$source" "$source".ts
    sed -i '/\/usr\/bin\/env python/{d;q}' "$source"
    touch --ref="$source".ts "$source"
    rm "$source".ts
  fi
done
# special case for parse_xsd generated file which have lines like:
#!!!! 'NoneType' object has no attribute 'py_class'
source="src/saml2/schema/wsdl.py"
touch --ref="$source" "$source".ts
sed -i '1,3{d;q}' "$source"
touch --ref="$source".ts "$source"
rm "$source".ts

%build

%py3_build

# drop alabaster Sphinx theme, not packaged in Fedora yet
#sed -i '/alabaster/d' docs/conf.py
# generate html docs
export PYTHONPATH=./src
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install

%py3_install

%check
%pytest

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{_bindir}/parse_xsd2.py
%{_bindir}/make_metadata.py
%{_bindir}/mdexport.py
%{_bindir}/merge_metadata.py
%{python3_sitelib}/saml2
%{python3_sitelib}/*.egg-info

%files doc
%license LICENSE
%doc html

%changelog
* Thu Aug 04 2022 Alfredo Moralejo <amoralej@redhat.com> - 7.1.2-1
- Update to 7.1.2

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 7.0.1-5
- Rebuilt for Python 3.11

* Fri Jan 28 2022 Kai A. Hiller <V02460@gmail.com> - 7.0.1-4
- Add missing requires for xmlsec1 and xmlsec1-openssl

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 21 2021 Alfredo Moralejo <amoralej@redhat.com> - 7.0.1-2
- Use importlib.resources in python >= 3.7  (rhbz#2008668)

* Fri Sep 24 2021 Joel Capitao <jcapitao@redhat.com> - 7.0.1-1
- Update to 7.0.1 (rhbz#1290944)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jul 30 2020 Yatin Karel <ykarel@redhat.com> - 6.1.0-1
- Update to 6.1.0 (rhbz#1290944)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-11
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 11 2019 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-6
- Subpackage python2-pysaml2 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.5.0-3
- Rebuilt for Python 3.7

* Wed Jun  6 2018  <jdennis@redhat.com> - 4.5.0-2
- Resolves: rhbz#1582254 - re-enable python2 support

* Fri May 18 2018  <jdennis@redhat.com> - 4.5.0-1
- upgrade to current upstream
- enforce Python packaging standards

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.2-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jason Joyce <jjoyce@redhat.com> - 3.0.2-7
- security fix for entity expansion issue - CVE-2016-10149

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-5
- Rebuild for Python 3.6

* Sun Nov 13 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.2-4
- fix pycrypto dependency

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 05 2015 Alan Pevec <alan.pevec@redhat.com> 3.0.2-1
- Update to 3.0.2

* Wed Jul 15 2015 Alan Pevec <apevec@redhat.com> - 3.0.0-1
- update to upstream release 3.0.0

* Thu Jun 18 2015 Alan Pevec <apevec@redhat.com> - 3.0.0-0.3.git40603ae
- include unreleased fix for https://github.com/rohe/pysaml2/issues/202
- review feedback
- fix rpmlint errors

* Tue Mar 31 2015 Alan Pevec <apevec@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Mon Feb 16 2015 Dan Prince - 2.3.0-1
- Initial package.

%global pypi_name PyNLPl
%global pkg_name pynlpl

Name:           python-%{pkg_name}
Version:        1.2.7
Release:        14%{?dist}
Summary:        A Python library for Natural Language Processing

License:        GPLv3
URL:            https://github.com/proycon/%{pkg_name}
Source0:        https://github.com/proycon/%{pkg_name}/archive/v%{version}.tar.gz#/%{pkg_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-lxml >= 2.2
BuildRequires:  python3-httplib2 >= 0.6
BuildRequires:  python3-rdflib

# Required to build docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-twisted

%description
PyNLPl, pronounced as ‘pineapple’, is a Python library for Natural Language
Processing. It contains various modules useful for common, and less common,
NLP tasks. PyNLPl can be used for basic tasks such as the extraction of
n-grams and frequency lists, and to build simple language model. There are
also more complex data types and algorithms. Moreover, there are parsers for
file formats common in NLP (e.g. FoLiA/Giza/Moses/ARPA/Timbl/CQL). There are
also clients to interface with various NLP specific servers. PyNLPl most
notably features a very extensive library for working with FoLiA XML (Format
for Linguistic Annotation).

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Requires:       python3-lxml >= 2.2
Requires:       python3-httplib2 >= 0.6
Requires:       python3-setuptools
Requires:       python3-numpy
Requires:       python3-rdflib
%description -n python3-%{pkg_name}
PyNLPl, pronounced as ‘pineapple’, is a Python library for Natural Language
Processing. It contains various modules useful for common, and less common,
NLP tasks. PyNLPl can be used for basic tasks such as the extraction of
n-grams and frequency lists, and to build simple language model. There are
also more complex data types and algorithms. Moreover, there are parsers for
file formats common in NLP (e.g. FoLiA/Giza/Moses/ARPA/Timbl/CQL). There are
also clients to interface with various NLP specific servers. PyNLPl most
notably features a very extensive library for working with FoLiA XML (Format
for Linguistic Annotation).

%package doc
Summary:        PyNLPl documentation
%description doc
Documentation for PyNLPl library.


%prep
%autosetup -n %{pkg_name}-%{version}
# Fix shebangs.
find -type f -exec sed -i '1s=^#!\s\?/usr/bin/env python=#!%{__python3}=' {} +


%build
%py3_build
# Generate html docs
export PYTHONPATH=$PYTHONPATH:../:../../
sphinx-build docs html
# Remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
# Exclude folia.py, folia_benchmark.py and fql.py tests
# as they download external resources from Github
rm %{pkg_name}/tests/{folia*,fql}.py
# Run tests
%{__python3} setup.py test -s %{pkg_name}.tests


%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{_bindir}/pynlpl-computepmi
%{_bindir}/pynlpl-sampler
%{_bindir}/pynlpl-makefreqlist
%{python3_sitelib}/%{pkg_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE
%doc html


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.2.7-13
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.7-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.7-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Iryna Shcherbina <shcherbina.iryna@gmail.com> - 1.2.7-1
- Update to 1.2.7

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.11-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.11-1
- Update to 1.1.11
- Drop Python 2 subpackage

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 4 2017 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.2-1
- Update to version 1.1.2

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-2
- Rebuild for Python 3.6

* Mon Dec 12 2016 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.1-1
- Update to version 1.1.1

* Wed Nov 2 2016 Iryna Shcherbina <ishcherb@redhat.com> - 1.0.9-1
- Initial package

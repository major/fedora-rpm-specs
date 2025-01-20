%global modname sieve

Name:             python-sieve
Version:          0.1.9
Release:          35%{?dist}
Summary:          XML Comparison Utils

License:          MIT
URL:              https://pypi.python.org/pypi/sieve
Source0:          https://pypi.python.org/packages/source/s/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:        noarch


BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-six
BuildRequires:    python3-lxml
BuildRequires:    python3-markupsafe
BuildRequires:    python3-wheel

%global _description\
Ripped from FormEncode and strainer just to support Pythons 2 and 3.\
Intended for use in your webapp test suites.\
\
Example usage::\
\
    >>> from sieve.operators import eq_xml, in_xml\
    >>> a = "<foo><bar>Value</bar></foo>"\
    >>> b = """\
    ... <foo>\
    ...     <bar>\
    ...         Value\
    ...     </bar>\
    ... </foo>\
    ... """\
    >>> eq_xml(a, b)\
    True\
    >>> c = "<html><body><foo><bar>Value</bar></foo></body></html"\
    >>> in_xml(a, c)  # 'needle' in a 'haystack'\
    True\


%description %_description

%package -n python3-sieve
Summary:        XML Comparison Utils

Requires:   python3-six
Requires:   python3-lxml
Requires:   python3-markupsafe

%description -n python3-sieve
Ripped from FormEncode and strainer just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

Example usage::

    >>> from sieve.operators import eq_xml, in_xml 
    >>> a = "<foo><bar>Value</bar></foo>" 
    >>> b = """ 
    ... <foo> 
    ...     <bar>
    ...         Value 
    ...     </bar> 
    ... </foo> 
    ... """
    >>> eq_xml(a, b)
    True 
    >>> c = "<html><body><foo><bar>Value</bar></foo></body></html"
    >>> in_xml(a, c)  # 'needle' in a 'haystack'
    True

%prep
%setup -q -n %{modname}-%{version}

rm -rf %{modname}.egg-info



%build
%{__python3} setup.py build


%install
%{__python3} setup.py install -O1 --skip-build --root=%{buildroot}


%check
# check disabled, only deprecated nose is supported
#%%{__python3} setup.py test


%files -n python3-%{modname}
%doc LICENSE.txt README.rst
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}-*



%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.1.9-33
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.1.9-29
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.1.9-26
- Rebuilt for Python 3.11

* Thu Apr 21 2022 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.1.9-25
- Remove check, because there is support only for deprecated nose package

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.9-22
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 07 2020 Ján ONDREJ (SAL) <ondrejj(at)salstar.sk> - 0.1.9-20
- BuildRequire setuptools explicitly

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-18
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 08 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-16
- Subpackage python2-sieve has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-15
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.1.9-12
- Use the py2 version of the macros

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.9-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.1.9-7
- Python 2 binary package renamed to python2-sieve
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.9-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1.9-1
- Update to upstream 0.1.9 to fix tracebacks with some xml fragments

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 13 2014 Ralph Bean <rbean@redhat.com> - 0.1.6-12
- Fixed with_python3 conditional.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 03 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-7
- Move python3 requirements into the correct section.

* Tue Oct 30 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-6
- Bump release to get around a koji hiccup again.

* Mon Oct 22 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-5
- Bump release to get around a koji hiccup.

* Tue Sep 25 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-4
- Added requirement on python3-six back in since that package has been split.

* Mon Sep 24 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-3
- Removed upstream egg-info in prep section.

* Fri Jun 22 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-2
- Fix to python-six dependencies.  (no python3-six)

* Fri Jun 22 2012 Ralph Bean <rbean@redhat.com> - 0.1.6-1
- Initial package for Fedora

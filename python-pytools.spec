%global srcname pytools

Name:           python-%{srcname}
Version:        2022.1.14
Release:        3%{?dist}
Summary:        Collection of tools for Python

License:        MIT
URL:            https://pypi.python.org/pypi/pytools
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description \
Pytools is a big bag of things that are "missing" from the Python standard\
library. This is mainly a dependency of my other software packages, and is\
probably of little interest to you unless you use those. If you're curious\
nonetheless, here's what's on offer:\
\
  * A ton of small tool functions such as `len_iterable`, `argmin`,\
    tuple generation, permutation generation, ASCII table pretty printing,\
    GvR's mokeypatch_xxx() hack, the elusive `flatten`, and much more.\
  * Michele Simionato's decorator module\
  * A time-series logging module, `pytools.log`.\
  * Batch job submission, `pytools.batchjob`.\
  * A lexer, `pytools.lex`.

%description %{_description}


%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(typing-extensions)


%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}
rm -vrf *.egg-info

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst PKG-INFO
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2022.1.14-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.14-1
- Update to 2022.1.14 (fixes rhbz#2156422)

* Tue Nov 22 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.13-1
- Update to 2022.1.13 (fixes rhbz#2144223)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.12-1
- Update to 2022.1.12 (fixes rhbz#2101154)

* Fri Jun 24 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.11-1
- Update to 2022.1.11 (fixes rhbz#2099966)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.1.9-2
- Rebuilt for Python 3.11

* Sat May 21 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.9-1
- Update to 2022.1.9

* Fri May 20 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.8-1
- Update to 2022.1.8

* Fri May 13 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.7-1
- Update to 2022.1.7

* Fri Mar 18 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.2-1
- Update to 2022.1.2

* Thu Mar 17 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2022.1.1-1
- Update to 2022.1.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2021.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 04 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.9-1
- Update to 2021.2.9

* Mon Aug 16 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.8-1
- Update to 2021.2.8

* Wed Aug 04 2021 Frantisek Zatloukal <fzatlouk@redhat.com> - 2021.2.7-1
- Update to the latest upstream - 2021.2.7
- Clean up specfile a bit

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2019.1-10
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2019.1-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2019.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2019.1-1
- Update to 2019.1

* Tue Aug 21 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.5.2-4
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.5.2-2
- Rebuilt for Python 3.7

* Sun Jul 01 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2018.5.2-1
- Update to 2018.5.2

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.2-2
- Rebuilt for Python 3.7

* Mon Mar 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2018.2-1
- Update to 2018.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.6-1
- Update to 2017.6

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2017.4-1
- Update to 2017.4

* Sat Jul 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 2017.3-1
- Update to 2017.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2016.2.6-2
- Rebuild for Python 3.6

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2016.2.6-1
- Update to 2016.2.6

* Mon Oct 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2016.2.4-1
- Update to 2016.2.4
- Fixes in spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.1.2-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2015.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2015.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 05 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2015.1.2-1
- Update to 2015.1.2
- Update python macroses
- Add python3 subpackage
- Update for new python packaging guidelines

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 8-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 09 2009 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> 8-2
- Spec file cleanup

* Wed Apr 08 2009 Ramakrishna Reddy Yekulla <ramkrsna@fedoraproject.org> 8-1
- Initial RPM release

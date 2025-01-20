%global pypi_name cssutils
%global srcname cssutils

%bcond_without tests

Name:           python-%{srcname}
Summary:        CSS Cascading Style Sheets library for Python
Version:        2.11.1
Release:        3%{?dist}

License:        LGPL-3.0-or-later
URL:            https://github.com/jaraco/cssutils
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
# Tests BuildRequires
BuildRequires:  python3dist(more-itertools)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(mypy)
BuildRequires:  ruff
BuildRequires:  python3dist(cssselect)
BuildRequires:  python3dist(jaraco-test)

%global _description \
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not\
any rendering facilities.

%description %{_description}

%package doc
Summary:        Documentation for %{name}

%description doc
%{summary}.

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}
A Python package to parse and build CSS Cascading Style Sheets. DOM only, not\
any rendering facilities.

%prep
%autosetup -p1 -n cssutils-%{version}
# jaraco.test module not yet in Fedora
rm -f cssutils/tests/test_property.py cssutils/tests/test_selector.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files *utils

%if %{with tests}
%check
%pytest -k "not test_parseUrl and not encutils and not website.logging"
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.rst
%{_bindir}/csscapture
%{_bindir}/csscombine
%{_bindir}/cssparse

%files doc
%doc examples/

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 23 2024 Kevin Fenzi <kevin@scrye.com> - 2.11.1-1
- Update to 2.11.1. Fixes rhbz#2252065

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.6.0-7
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 28 2023 Michel Alexandre Salim <salimma@fedoraproject.org> - 2.6.0-4
- Drop manual BRs and deprecated use of %%python_provide
- Use SPDX license identifier

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 12 2022 Kevin Fenzi <kevin@scrye.com> - 2.6.0-1
- Update to 2.6.1. Fixes rhbz#2106407

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 21 2022 Parag Nemade <pnemade AT redhat DOT com> - 2.4.2-1
- Update to 2.4.2 version

* Mon Jun 20 2022 Python Maint <python-maint@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.11

* Sat May 28 2022 Kevin Fenzi <kevin@scrye.com> - 2.4.0-1
- Update to 2.4.0. Fixes rhbz#2057228

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Parag Nemade <pnemade AT redhat DOT com> - 2.3.0-1
- Update to 2.3.0
- Disable for now failing tests

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.10

* Sat Mar 27 2021 Kevin Fenzi <kevin@scrye.com> - 2.2.0-1
- Update to 2.2.0. New upstream. rhbz#1936952

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 23 2019 Kevin Fenzi <kevin@scrye.com> - 1.0.2-5
- Drop python2 subpackages.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Kevin Fenzi <kevin@scrye.com> - 1.0.2-1
- Update to 1.0.2. Fixes bug #1649872

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-10
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-6
- Rebuild for Python 3.6

* Sat Aug 27 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.0.1-5
- Fixes in packaging
- Run test suite
- Don't distribute test suite
- Cleanups

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sun Mar 06 2016 Kevin Fenzi <kevin@scrye.com> - 1.0.1-3
- Create python2 and python3 subpackages. Fixes bug #1310629

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 26 2015 Kevin Fenzi <kevin@scrye.com> - 1.0.1-1
- Update to 1.0.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Kevin Fenzi <kevin@scrye.com> - 0.9.9-1
- Update to 0.9.9

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 12 2011 Kevin Fenzi <kevin@tummy.com> - 0.9.7-1
- Update to final 0.9.7

* Sun Sep 12 2010 Kevin Fenzi <kevin@tummy.com> - 0.9.7-0.0.b3
- Update to 0.9.7 beta 3

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Feb 25 2010 Matthias Saou <http://freshrpms.net/> 0.9.6-1
- Update to 0.9.6.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.5.1-4
- Rebuild for Python 2.6

* Fri Oct 10 2008 Matthias Saou <http://freshrpms.net/> 0.9.5.1-3
- Add missing python-setuptools BR, split off doc sub-package (mschwendt).

* Thu Oct  9 2008 Matthias Saou <http://freshrpms.net/> 0.9.5.1-2
- Update license, group, add python-setuptools requirement (mschwendt).

* Tue Aug 19 2008 Matthias Saou <http://freshrpms.net/> 0.9.5.1-1
- Update to 0.9.5.1.

* Fri Aug  8 2008 Matthias Saou <http://freshrpms.net/> 0.9.5-1
- Update to 0.9.5 final.

* Tue Jul 15 2008 Matthias Saou <http://freshrpms.net/> 0.9.5b2-0.2.rc2
- Convert CRLF end of lines.
- Patch out #!/... magic from python files meant to be included and not run.

* Tue Jul 15 2008 Matthias Saou <http://freshrpms.net/> 0.9.5b2-0.1.rc2
- Initial RPM release.


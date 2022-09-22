Name:          python-appdirs
Version:       1.4.4
Release:       7%{?dist}
Summary:       Python module for determining platform-specific directories

License:       MIT
URL:           https://github.com/ActiveState/appdirs
Source:        %{pypi_source appdirs}

BuildArch:     noarch

BuildRequires: python3-devel

%description
A small Python module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".


%package -n python3-appdirs
Summary:        %{summary}

%description -n python3-appdirs
A small Python 3 module for determining appropriate " + " platform-specific
directories, e.g. a "user data dir".


%prep
%autosetup -n appdirs-%{version}
sed -i -e '1{\@^#!/usr/bin/env python@d}' appdirs.py


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files appdirs


%check
# upstream's tox.ini just wraps this command with no extra deps
# we don't use %%tox here to avoid a dependency loop: tox->platformdirs->appdirs
%{python3} setup.py test


%files -n python3-appdirs -f %{pyproject_files}
%doc README.rst CHANGES.rst


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.4.4-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 1.4.4-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 10 2020 Yatin Karel <ykarel@redhat.com> - 1.4.4-1
- Update to 1.4.4 (#1834175)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-12
- Subpackage python2-appdirs has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Sep 02 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-11
- Reduce Python 2 build time dependencies

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.3-7
- Get python2 package back

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.3-6
- Drop python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4.3-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.4.3-1
- Update to 1.4.3

* Mon Feb 13 2017 Charalampos Stratakis <cstratak@redhat.com> - 1.4.0-10
- Rebuild as wheel

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Aug 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-4
- Update to new packaging guidelines

* Sun Aug 02 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-3
- Use modern python rpm macros

* Mon Jul 27 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-2
- Include CHANGES.rst in doc
- use python2-devel in BR instead of python-devel
- run tests

* Fri May 08 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-1
- Initial package

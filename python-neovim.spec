%if 0%{?fedora}
%{?python_enable_dependency_generator}
%endif

%global desc Implements support for python plugins in Nvim. Also works as a library for\
connecting to and scripting Nvim processes through its msgpack-rpc API.

%bcond_without check

# EPEL7 Sphinx is too old, disable doc building by default
%if 0%{?el7}
%bcond_with sphinx
%else
%bcond_without sphinx
%endif

Name:           python-neovim
Version:        0.4.3
Release:        8%{?dist}

License:        ASL 2.0
Summary:        Python client to Neovim
URL:            https://github.com/neovim/pynvim
Source0:        https://github.com/neovim/pynvim/archive/%{version}/pynvim-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with check}
BuildRequires:  neovim
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(greenlet)
BuildRequires:  python3dist(msgpack)
%endif

%if 0%{?el7}
BuildRequires:  python-devel
BuildRequires:  python-setuptools
%endif

%if %{with sphinx}
BuildRequires:  python%{python3_pkgversion}-sphinx
BuildRequires:  python%{python3_pkgversion}-sphinx_rtd_theme
%endif

%description
%{desc}

%if 0%{?el7}
%package -n python2-neovim
Summary:        %{summary}
%{?python_provide:%python_provide python2-neovim}
Requires:       neovim
Requires:       python-greenlet
Requires:       python-trollius

%description -n python2-neovim
%{desc}
%endif

%package -n python%{python3_pkgversion}-neovim
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-neovim}
Requires:       neovim
%if %{undefined __pythondist_requires}
Requires:       python%{python3_pkgversion}-greenlet
Requires:       python%{python3_pkgversion}-msgpack
%endif

%description -n python%{python3_pkgversion}-neovim
%{desc}

%if %{with sphinx}
%package doc
Summary:        Documentation for %{name}

%description doc
%{desc}

This package contains documentation in HTML format.
%endif

%prep
%autosetup -n pynvim-%{version}

%build
%if 0%{?el7}
%py2_build
%endif
%py3_build

%if %{with sphinx}
pushd docs
make html
rm -f _build/html/.buildinfo
popd
%endif

%install
%if 0%{?el7}
%py2_install
%endif
%py3_install

%check
%py3_check_import pynvim
%if %{with check}
%pytest
%endif

%if 0%{?el7}
%files -n python2-neovim
%license LICENSE
%doc README.md
%{python2_sitelib}/*
%endif

%files -n python%{python3_pkgversion}-neovim
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%if %{with sphinx}
%files doc
%license LICENSE
%doc docs/_build/html
%endif

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.3-6
- Rebuilt for Python 3.11

* Wed Mar 23 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.4.3-5
- Enable tests
- Drop python-pytest-runner dependency

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.3-2
- Rebuilt for Python 3.10

* Mon Apr 19 2021 Andreas Schneider <asn@redhat.com> - 0.4.3-1
- resolves: #1773192 - Update to version 0.4.3
  o https://github.com/neovim/pynvim/releases/tag/0.4.3

* Mon Mar 15 2021 Andreas Schneider <asn@redhat.com> - 0.4.2-1
- Update to version 0.4.2
  o https://github.com/neovim/pynvim/releases/tag/0.4.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Andreas Schneider <asn@redhat.com> - 0.4.1-1
- Update to version 0.4.1
  * https://github.com/neovim/pynvim/releases/tag/0.4.1

* Sun Nov 17 2019 Andreas Schneider <asn@redhat.com> - 0.4.0-1
- Update to version 0.4.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.3.2-2
- Merge spec with EPEL7 branch
- Fix missing Sphinx theme for F31 #1716511

* Mon Mar 11 2019 Andreas Schneider <asn@redhat.com> - 0.3.2-1
- Update to version 0.3.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 02 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.3.1-2
- Enable python dependency generator

* Wed Jan 02 2019 Andreas Schneider <asn@redhat.com> - 0.3.1-1
- Update to version 0.3.1

* Wed Sep 26 2018 Andreas Schneider <asn@redhat.com> - 0.2.6-4
- resolves: #1632298 - Remove python2 sub-packages

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.6-2
- Rebuilt for Python 3.7

* Thu May 03 2018 Andreas Schneider <asn@redhat.com> - 0.2.6-1
- resolves: #1574026 - Update to 0.2.6

* Mon Mar 12 2018 Filip Szymański <fszymanski@fedoraproject.org> - 0.2.4-1
- resolves: #1541621 - Update to 0.2.4
- Add -doc subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Dec 30 2017 Filip Szymański <fszymanski@fedoraproject.org> - 0.2.0-1
- resolves: #1511245 - Update to 0.2.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.1.13-3
- Use %%{python3_pkgversion} macro for EPEL compatibility
- special-case python2 greenlet dependency on EL7

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Filip Szymański <fszymanski at, fedoraproject.org> - 0.1.13-1
- Update to 0.1.13
- Use %%{summary} macro

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.12-4
- Rebuild for Python 3.6

* Wed Dec 07 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 0.1.12-3
- Add requires on python-trollius

* Mon Dec 05 2016 Filip Szymański <fszymanski at, fedoraproject.org> - 0.1.12-2
- Add python2- package

* Sun Dec 04 2016 Andreas Schneider <asn@redhat.com> - 0.1.12-1
- Initial release

%global pypi_name cotyledon

Name:           python-%{pypi_name}
Version:        1.7.3
Release:        25%{?dist}
Summary:        Cotyledon provides a framework for defining long-running services

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://cotyledon.readthedocs.io
Source0:        %{pypi_source}
Patch0:         remove-python-mock.patch
BuildArch:      noarch

%package -n python3-%{pypi_name}
Summary:        Cotyledon provides a framework for defining long-running services
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description -n python3-%{pypi_name}
Cotyledon provides a framework for defining long-running services.

%package doc
Summary:    Documentation for %{name}

%description doc
Cotyledon provides a framework for defining long-running services.

This package contains documentation in HTML format.

%description
Cotyledon provides a framework for defining long-running services.

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x test -x doc -x oslo

%build
%pyproject_wheel

export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build-3 -b html doc/source html
# Fix hidden-file-or-dir warnings
rm -rf html/.doctrees html/.buildinfo

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest ||:


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%files doc
%doc html

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7.3-24
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 1.7.3-22
- Rebuilt for Python 3.13

* Sat Jan 27 2024 Maxwell G <maxwell@gtmx.me> - 1.7.3-21
- Remove python3-mock test dependency

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 1.7.3-17
- Rebuilt for Python 3.12

* Tue May 30 2023 Joel Capitao <jcapitao@redhat.com> - 1.7.3-16
- Convert to pyproject macros
- Remove py2 bits

* Tue May 30 2023 Joel Capitao <jcapitao@redhat.com> - 1.7.3-15
- Remove testrepository dep

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.7.3-12
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.7.3-9
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.7.3-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.7.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Alfredo Moralejo <amoralej@redhat.com> - 1.7.3-1
- Update to 1.7.3.
- Remove python2 subpackages when building in Fedora.

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.6.7-9
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6.7-7
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6.7-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.7-5
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 08 2017 Pradeep Kilambi <pkilambi@redhat.com> - 1.6.7-1
- Rebase 1.6.7

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6.3-2
- Rebuild for Python 3.6

* Thu Dec  1 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.6.3-1
- Upstream 1.6.3

* Fri Sep 02 2016 Alan Pevec <apevec AT redhat.com> - 1.2.7-2
- python2 subpackage was missing

* Wed Aug 31 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.7-1
- Rebase to 1.2.7
- move sphinx-build to %%build
- move buildRequires/requires to python2-cotyledon 
- run python3 tests

* Fri Jul 15 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.5-3
- Add check section
- added new test dependencies
- fixed tests sub packages

* Thu Jul 14 2016 Pradeep Kilambi <pkilambi@redhat.com> - 1.2.5-2
- Fix source url

* Wed Jul 6 2016 Mehdi Abaakouk <sileht@redhat.com> - 1.2.5-1
- Initial package.

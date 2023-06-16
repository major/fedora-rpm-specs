
%global upstream_version 1.4

Name:           rpmdeplint
Version:        1.4
Release:        27%{?dist}
Summary:        Tool to find errors in RPM packages in the context of their dependency graph
License:        GPLv2+
URL:            https://pagure.io/rpmdeplint
Source0:        https://files.pythonhosted.org/packages/source/r/%{name}/%{name}-%{upstream_version}.tar.gz
Patch0:         0001-Hotfix-for-libdnf-in-Fedora-29.patch
Patch1:         0001-Silence-some-Deprecation-warnings.patch
Patch2:         0001-Decode-rpm_file-rpm.RPMTAG_ARCH-only-if-it-is-bytes.patch
BuildArch:      noarch

# The base package is just the CLI, which pulls in the rpmdeplint
# Python modules to do the real work.
Requires:       python3-%{name} = %{version}-%{release}

%description
Rpmdeplint is a tool to find errors in RPM packages in the context of their
dependency graph.


%package -n python3-%{name}
%{?python_provide:%python_provide python3-%{name}}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-pytest
BuildRequires:  python3-six
BuildRequires:  python3-rpm
BuildRequires:  python3-hawkey
BuildRequires:  python3-librepo
Requires:       python3-six
Requires:       python3-rpm
Requires:       python3-hawkey
Requires:       python3-librepo

%description -n python3-%{name}
Rpmdeplint is a tool to find errors in RPM packages in the context of their
dependency graph.

This package provides a Python 3 API for performing the checks.

%prep
%setup -q -n %{name}-%{upstream_version}

%patch0 -p1
%patch1 -p1
%patch2 -p1

rm -rf rpmdeplint.egg-info

%build
%py3_build

%install
%py3_install

%check
py.test-3 rpmdeplint -k "not TestDependencyAnalyzer"
# Acceptance tests do not work in mock because they require .i686 packages.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%files -n python3-%{name}
%license COPYING
%doc README.rst
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info

%changelog
* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.4-27
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.4-24
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.4-21
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4-18
- Add BR python3-setuptools

* Fri May 29 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-17
- Rebuilt for Python 3.9

* Fri May 29 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4-16
- Decode rpm_file[rpm.RPMTAG_ARCH] only if it is bytes (RHBZ#1693774)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4-15
- Rebuilt for Python 3.9

* Wed May 20 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4-14
- Silence some Deprecation warnings (RHBZ#1832171)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 2019 Frantisek Zatloukal <fzatlouk@redhat.com> - 1.4-9
- Update fix for F29+ to handle all g.problems occurences

* Wed May 29 2019 Miroslav Vadkerti <mvadkert@redhat.com> - 1.4-8
- Incorporate fix for F29+ from frantisekz - https://src.fedoraproject.org/rpms/rpmdeplint/pull-request/1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 07 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4-5
- Remove python2-rpmdeplint (#1634569)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.4-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 20 2017 Dan Callaghan <dcallagh@redhat.com> - 1.4-1
- upstream bug fix release 1.4:
  https://rpmdeplint.readthedocs.io/en/latest/CHANGES.html

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 21 2017 Dan Callaghan <dcallagh@redhat.com> - 1.3-2
- subpackage requirement should be versioned (RHBZ#1462047)

* Fri Apr 28 2017 Dan Callaghan <dcallagh@redhat.com> - 1.3-1
- upstream bug fix release 1.3:
  https://rpmdeplint.readthedocs.io/en/latest/CHANGES.html

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2-3
- Rebuild for Python 3.6

* Thu Oct 20 2016 Dan Callaghan <dcallagh@redhat.com> - 1.2-2
- split Python module into its own package, ship both Python 2 and
  Python 3 versions

* Mon Oct 17 2016 Dan Callaghan <dcallagh@redhat.com> - 1.2-1
- initial version

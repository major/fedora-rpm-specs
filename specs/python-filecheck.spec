%bcond_without check
%global pypi_name filecheck
%global commit a630efd71cc5ad791162a6809334364b8a1c9e8f
%global shortcommit %%(c=%{commit}; echo ${c:0:7})

%global desc Python port of LLVM's FileCheck, flexible pattern matching file verifier.

Name: python-%{pypi_name}
Version: 0.0.24
Release: 4%{?dist}
Summary: Flexible pattern matching file verifier
License: Apache-2.0
URL: https://github.com/mull-project/FileCheck.py
Source0: https://github.com/mull-project/FileCheck.py/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
# upstream testsuite includes only x86_64 reference binaries and Fedora llvm9.0 package doesn't include FileCheck
# https://bugzilla.redhat.com/show_bug.cgi?id=1939414
Patch0: %{name}-tests-x86_64.patch
# upstream testsuite measures code coverage
# that is discouraged in the packaging guidelines
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
Patch1: %{name}-no-coverage.patch
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-pip
BuildRequires: python3-hatchling
BuildRequires: sed
%if %{with check}
BuildRequires: %{_bindir}/invoke
BuildRequires: %{_bindir}/lit
BuildRequires: %{_bindir}/python
BuildRequires: python3-pytest
BuildRequires: gcc
%endif

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -p1 -n FileCheck.py-%{version}
sed -i -e '/#!.*python3/d' filecheck/filecheck.py

%build
%pyproject_wheel

%install
%pyproject_install

%if %{with check}
%check
# lit seems to overwrite PYTHONPATH, so inject the buildroot paths directly
if ! grep -q %{buildroot} tests/integration/tests/examples/lit-and-filecheck/lit.local.cfg ; then
cat << __EOF__ >> tests/integration/tests/examples/lit-and-filecheck/lit.local.cfg

config.environment['PYTHONPATH'] = '%{buildroot}%{python3_sitelib}'
config.environment['PATH'] = '${PATH}:%{buildroot}%{_bindir}'
__EOF__
fi
%{_bindir}/invoke -e test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%{python3_sitelib}/%{pypi_name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.0.24-2
- Rebuilt for Python 3.13

* Thu Mar 21 2024 Dominik Mierzejewski <dominik@greysector.net> 0.0.24-1
- update to 0.0.24
- drop obsolete patch
- use SPDX license identifier

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 21 2023 Dominik Mierzejewski <dominik@greysector.net> 0.0.23-4
- fix passing count as positional argument deprecated in Python 3.13 (resolves rhbz#2247032)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 0.0.23-2
- Rebuilt for Python 3.12

* Mon Feb 06 2023 Dominik Mierzejewski <dominik@greysector.net> 0.0.23-1
- update to 0.0.23 (resolves rhbz#2166793)
- drop obsolete patch

* Thu Feb 02 2023 Dominik Mierzejewski <dominik@greysector.net> 0.0.22-4
- backport upstream patch to limit build dependencies to poetry-core

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Miro Hrončok <mhroncok@redhat.com> - 0.0.22-2
- Enable testsuite due to fixed rhbz#2102736

* Thu Jul 28 2022 Dominik Mierzejewski <dominik@greysector.net> 0.0.22-1
- update to 0.0.22
- disable testsuite due to rhbz#2102736

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 0.0.18-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Dominik Mierzejewski <dominik@greysector.net> 0.0.18-1
- update to 0.0.18

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.17-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.0.17-3
- Rebuilt for Python 3.10

* Mon Mar 15 2021 Dominik Mierzejewski <dominik@greysector.net> 0.0.17-2
- enable testsuite
- drop shebang from module source
- run testsuite only on x86_64

* Sun Jan 24 2021 Dominik Mierzejewski <dominik@greysector.net> 0.0.17-1
- initial build

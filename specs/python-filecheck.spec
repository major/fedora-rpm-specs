%bcond_without check
%global pypi_name filecheck

%global desc Python port of LLVM's FileCheck, flexible pattern matching file verifier.

Name: python-%{pypi_name}
Version: 1.0.3
Release: 1%{?dist}
Summary: Flexible pattern matching file verifier
License: Apache-2.0
URL: https://github.com/AntonLydike/filecheck
Source0: https://github.com/AntonLydike/filecheck/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch: noarch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: python3-devel
%if %{with check}
BuildRequires: %{_bindir}/lit
BuildRequires: python3-pytest
%endif

%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%if %{with check}
%check
%pyproject_check_import
# lit seems to overwrite PYTHONPATH, so inject the buildroot paths directly
if ! grep -q %{buildroot} tests/filecheck/lit.local.cfg ; then
cat << __EOF__ >> tests/filecheck/lit.local.cfg

config.environment['PYTHONPATH'] = '%{buildroot}%{python3_sitelib}'
config.environment["PATH"] = (
    config.environment["PATH"] + ':' + '%{buildroot}%{_bindir}'
)

__EOF__
fi
%{_bindir}/lit -v tests/filecheck
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%{_bindir}/%{pypi_name}

%changelog
* Mon Apr 20 2026 Dominik Mierzejewski <dominik@greysector.net> - 1.0.3-1
- switch to new upstream
- clean up

* Sat Jan 17 2026 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_44_Mass_Rebuild

* Fri Sep 19 2025 Python Maint <python-maint@redhat.com> - 0.0.24-9
- Rebuilt for Python 3.14.0rc3 bytecode

* Fri Aug 15 2025 Python Maint <python-maint@redhat.com> - 0.0.24-8
- Rebuilt for Python 3.14.0rc2 bytecode

* Sat Aug 02 2025 Dominik Mierzejewski <dominik@greysector.net> 0.0.24-7
- use generate_buildrequires/pyproject_buildrequires

* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Mon Jun 23 2025 Python Maint <python-maint@redhat.com> - 0.0.24-5
- Rebuilt for Python 3.14

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

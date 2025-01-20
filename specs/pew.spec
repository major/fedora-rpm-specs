%bcond_without check

Name: pew
Version: 1.2.0
Release: 25%{?dist}
Summary: Tool to manage multiple virtualenvs written in pure Python

License: MIT
URL: https://github.com/berdario/pew
Source0: https://github.com/berdario/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: README.md

# This patch removes Python version management on Fedora.
#
# NOTE: This removes the pythonz-bd dependency which is not available in Fedora
# anymore.
# Furthermore, there is strong support upstream to either remove Pew's
# Python version management or replace it with pyenv:
# https://github.com/berdario/pew/issues/195.
Patch0: 0001-Remove-Python-version-management-on-Fedora.patch

# Backport PR #214:
# Support Python 3.8, 3.9 and 3.10, drop EOL Python versions (2.7, 3.4, 3.5),
# use GitHub Actions for CI
# https://github.com/berdario/pew/pull/214
#
# NOTE: This enables Pew to be used on recent Fedora versions.
Patch1: 0002-Remove-remaining-references-to-Python-2.6-3.2-and-3..patch
Patch2: 0003-Add-support-for-Python-3.8-and-3.9.patch
Patch3: 0004-Unify-Pipfile-and-requirements.txt-with-dependencies.patch
Patch4: 0005-Replace-Travis-CI-and-AppVeyor-with-GitHub-Actions.patch
Patch5: 0006-Drop-support-for-Python-2-Python-3.4-and-3.5.patch
Patch6: 0007-Replace-PyPy-with-PyPy-3.patch
Patch7: 0008-Remove-test-for-testing-virtualenv-relocatable.patch
Patch8: 0009-Replace-obsolete-pytest.yield_fixture-with-pytest.fi.patch
Patch9: 0010-Explicilty-import-distutils.sysconfig-subpackage-in-.patch
Patch10: 0011-Replace-easy_install-with-setuptools-in-test_lssitep.patch
Patch11: 0012-Rewrite-test_restore-to-delete-setuptools-to-break-t.patch
Patch12: 0013-Register-pytest.marker.shell-custom-marker.patch
Patch13: 0014-Temporarily-disable-test_create_in_symlink-test-in-t.patch
Patch14: 0015-Add-support-for-Python-3.10.patch

BuildArch: noarch

BuildRequires: python3-devel
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(virtualenv) >= 1.11
BuildRequires: python3dist(virtualenv-clone) >= 0.2.5

%if %{with check}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pip)
%endif

%{?python_provide:%python_provide python3-%{name}}

%description
Python Env Wrapper is a set of commands to manage multiple virtual
environments. Pew can create, delete and copy your environments, using a
single command to switch to them wherever you are, while keeping them in a
single (configurable) location.


%prep
%autosetup -p 1 -n %{name}-%{version}

# Rename the Fedora-specific README.md to avoid conflict with the upstream
# README.md.
# NOTE: The source file should stay named README.md so that Pagure renders it
# when one visits https://src.fedoraproject.org/rpms/pew.
cp -v %{SOURCE1} README.Fedora.md

# This script for shell completion can't be used for Fedora package
rm -rf %{name}/shell_config/complete_deploy

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pew

# Manually install shell completions scripts for Bash/Fish/Zsh.
install -m 0644 -p -D %{name}/shell_config/complete.bash %{buildroot}/%{bash_completions_dir}/pew
install -m 0644 -p -D %{name}/shell_config/complete.fish %{buildroot}/%{fish_completions_dir}/pew.fish
install -m 0644 -p -D %{name}/shell_config/complete.zsh %{buildroot}/%{zsh_completions_dir}/_pew

%check
%if %{with check}
# Temporarily disable tests failing with Python 3.12.
# For more details, see: https://github.com/pew-org/pew/issues/233.
k="not test_restore and not test_lssitepackages and not test_new_env_activated"
PATH=%{buildroot}%{_bindir}:$PATH \
PYTHONPATH=%{buildroot}%{python3_sitelib} \
%{pytest} "${k:+-k $k}" -v tests
%endif


%files -f %{pyproject_files}
%doc README.md README.Fedora.md
%{_bindir}/pew
%{bash_completions_dir}/pew
%{fish_completions_dir}/pew.fish
%{zsh_completions_dir}/_pew

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.0-23
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jul 24 2023 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.2.0-20
- Modernize SPEC file (use %%pyproject_* and %pytest macros)
- Use cp instead of mv for README.Fedora.md
- Install shell completion files for Bash/Fish/Zsh
- Temporarily disable tests failing with Python 3.12

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 04 2023 Python Maint <python-maint@redhat.com> - 1.2.0-18
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.2.0-15
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 01 2021 Tadej Janež <tadej.j@nez.si> - 1.2.0-13
- Backport upstream PR #214 to enable Pew to be used on recent Fedora versions
- Simplify applying patches and remove obsolete if statement

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.2.0-11
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 09 2020 Tadej Janež <tadej.j@nez.si> - 1.2.0-7
- Replace Python version glob with macro to support Python 3.10
- Drop conditionals for EOL Fedora releases

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Tadej Janež <tadej.j@nez.si> 1.2.0-1
- Update to 1.2.0 release
- Drop the tests-connection-marker-fix patch since it has been upstreamed
- Remove Python version management functionality in Fedora 30+
- Use automatic Python dependency generator
- Improve pytest call to not include the current working directory as suggested
  by Zbigniew Jędrzejewski-Szmek:
  https://bugzilla.redhat.com/show_bug.cgi?id=1720757#c1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Oct 13 2017 Michal Cyprian <mcyprian@redhat.com> - 1.1.2-1
- Initial package.

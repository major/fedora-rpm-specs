%bcond_without check

Name:           pre-commit
Version:        2.20.0
Release:        2%{?dist}
Summary:        Framework for managing and maintaining multi-language pre-commit hooks

License:        MIT
URL:            https://pre-commit.com
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with check}
# All of the tests for the following require network access, so we can avoid
# pulling in these dependencies for now.
#
# BuildRequires:  R-core
# BuildRequires:  conda
# BuildRequires:  dotnet-host
# BuildRequires:  dotnet-hostfxr-6.0
# BuildRequires:  dotnet-sdk-6.0
# BuildRequires:  golang-bin

# These BR’s would enable a few extra tests, but are inconveniently
# ExclusiveArch. If we wanted to conditionalize BR’s based on build
# architecture, we would have to make *this* package arched.
#
# BuildRequires:  swift-lang

BuildRequires:  cargo
BuildRequires:  git-core
BuildRequires:  lua-devel
BuildRequires:  luarocks
BuildRequires:  npm
BuildRequires:  nodejs
BuildRequires:  perl-CPAN
BuildRequires:  rubypick
BuildRequires:  rubygems

# Manually added to speed up the %%check section
BuildRequires:  python3dist(pytest-xdist)
%endif

%description
A framework for managing and maintaining multi-language pre-commit hooks.


%prep
%autosetup -p1
# Do not generate BR’s for coverage, linters, etc.:
sed -r '/^(covdefaults|coverage)\b/d' requirements-dev.txt |
  tee requirements-dev-filtered.txt


%generate_buildrequires
%pyproject_buildrequires -r %{?with_check:requirements-dev-filtered.txt}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pre_commit


%if %{with check}
%check
git init
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# For general discusson on test failures building distribution packages, see:
# https://github.com/pre-commit/pre-commit/issues/1183,
# https://github.com/pre-commit/pre-commit/issues/1202
#
# Require network access:
# See https://github.com/pre-commit/pre-commit/issues/1202
k="${k-}${k+ and }not test_additional_dependencies_roll_forward"
k="${k-}${k+ and }not test_additional_golang_dependencies_installed"
k="${k-}${k+ and }not test_additional_node_dependencies_installed"
k="${k-}${k+ and }not test_additional_ruby_dependencies_installed"
k="${k-}${k+ and }not test_additional_rust_cli_dependencies_installed"
k="${k-}${k+ and }not test_additional_rust_lib_dependencies_installed"
k="${k-}${k+ and }not test_conda_hook"
k="${k-}${k+ and }not test_conda_with_additional_dependencies_hook"
k="${k-}${k+ and }not test_dotnet_hook"
k="${k-}${k+ and }not test_golang_hook"
k="${k-}${k+ and }not test_golang_hook_still_works_when_gobin_is_set"
k="${k-}${k+ and }not test_golang_with_recursive_submodule"
k="${k-}${k+ and }not test_install_ruby_with_version"
k="${k-}${k+ and }not test_installs_without_links_outside_env"
k="${k-}${k+ and }not test_local_conda_additional_dependencies"
k="${k-}${k+ and }not test_local_golang_additional_dependencies"
k="${k-}${k+ and }not test_local_lua_additional_dependencies"
k="${k-}${k+ and }not test_local_perl_additional_dependencies"
k="${k-}${k+ and }not test_local_rust_additional_dependencies"
k="${k-}${k+ and }not test_r_hook"
k="${k-}${k+ and }not test_r_inline_hook"
k="${k-}${k+ and }not test_r_local_with_additional_dependencies_hook"
k="${k-}${k+ and }not test_r_with_additional_dependencies_hook"
k="${k-}${k+ and }not test_run_a_node_hook_default_version"
k="${k-}${k+ and }not test_run_ruby_hook_with_disable_shared_gems"
k="${k-}${k+ and }not test_run_versioned_node_hook"
k="${k-}${k+ and }not test_run_versioned_ruby_hook"
# Requires Python 2 (forbidden as a BR, obsolete)
k="${k-}${k+ and }not test_local_python_repo_python2"
k="${k-}${k+ and }not test_switch_language_versions_doesnt_clobber"
# Requires dart (not packaged):
k="${k-}${k+ and }not test_dart_hook"
k="${k-}${k+ and }not test_local_dart_additional_dependencies"
k="${k-}${k+ and }not test_local_dart_additional_dependencies_versioned"
# Does not work under (i.e., respect) an “external” PYTHONPATH
k="${k-}${k+ and }not test_installed_from_venv"
# Fails in koji but not local mock (hook exits with code 1, no useful output)
k="${k-}${k+ and }not test_run_a_ruby_hook"
%pytest -v -k "${k-}" -n %{_smp_build_ncpus}
%endif


%files -f %{pyproject_files}
%doc README.md CHANGELOG.md CONTRIBUTING.md
%{_bindir}/pre-commit
%{_bindir}/pre-commit-validate-config
%{_bindir}/pre-commit-validate-manifest


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 12 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.20.0-1
- Update to 2.20.0 (close RHBZ#2105849)

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.19.0-2
- Rebuilt for Python 3.11

* Sun May 15 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.19.0-1
- Update to 2.19.0

* Thu Mar 24 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.16.0-3
- Use pytest-env, now that it is packaged
- Skip tests more precisely/selectively
- Drop unnecessary BR on deprecated python-mock
- Port to pyproject-rpm-macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 2.16.0-1
- Update to version 2.16.0 (#2027887)

* Fri Oct 01 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 2.14.1-1
- Update to version 2.15.0 (#2000799)

* Wed Sep 01 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 2.14.1-1
- Upate to version 2.14.1 (#1990997)

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.13.0-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 03 2021 Aniket Pradhan <major AT fedoraproject DOT org> - 2.13.0-1
- Version update to 2.13.0
- Remove redundant dependency generator call
- Use pytest macro
- Remove unnecessary python-devel version requirement
- Removed the dependency for Fedora 31 or lower

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.11.1-2
- Rebuilt for Python 3.10

* Sun Mar 21 2021 Chedi Toueiti <chedi.toueiti@gmail.com> - 2.11.1-1
- Update to version 2.11.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Lumír Balhar <lbalhar@redhat.com> - 2.5.1-1
- Update to 2.5.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.0-2
- Rebuilt for Python 3.9

* Wed May 13 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.4.0-1
- Update to 2.4.0

* Thu Apr 23 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.3.0-1
- Update to 2.3.0

* Thu Mar 12 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.2.0-1
- Update to 2.2.0

* Mon Feb 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.1-1
- Update to 2.1.1

* Mon Feb 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 2.1.0-1
- Update to 2.1.0

* Mon Jan 20 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 1.21.0-1
- Update to 1.21.0
- Thanks Aniket Pradhan <major AT fedoraproject DOT org> for help with packaging
- Thanks Miro Hrončok <mhroncok@redhat.com> for help with packaging

* Sun Dec 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Thu Oct 24 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.18.3-8
- Update to 1.18.3

* Sat Mar 30 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 1.14.4-1
- Initial package

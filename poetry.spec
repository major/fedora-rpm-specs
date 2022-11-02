# To break circular dependency on poetry-plugin-export, when bootstrapping
# we don't BuildRequire runtime deps and we don't run tests.
%bcond bootstrap 0

%global common_description %{expand:
Poetry helps you declare, manage and install dependencies of Python
projects, ensuring you have the right stack everywhere.}

Name:           poetry
Summary:        Python dependency management and packaging made easy
Version:        1.2.1
Release:        3%{?dist}

License:        MIT

URL:            https://python-poetry.org/
Source0:        https://github.com/python-poetry/poetry/archive/%{version}/poetry-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

# The tests deps are only defined as part of poetry.dev-dependencies together with tox, pre-commit etc.
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  /usr/bin/python
BuildRequires:  %py3_dist pytest
BuildRequires:  %py3_dist pytest-mock
BuildRequires:  %py3_dist httpretty
BuildRequires:  %py3_dist virtualenv

Requires:       python3-poetry = %{version}-%{release}

%description %{common_description}


%package -n     python3-poetry
Summary:        %{summary}
%description -n python3-poetry %{common_description}


%prep
%autosetup -p1

# remove vendored dependencies
rm -r src/poetry/_vendor

# Allow newer requests-toolbelt version
# https://bugzilla.redhat.com/show_bug.cgi?id=2138636
# Merged upstream: https://github.com/python-poetry/poetry/pull/6924
sed -i 's/requests-toolbelt = "^0.9.1"/requests-toolbelt = ">=0.9.1,<0.11.0"/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires %{?with_bootstrap: -R}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files poetry

export PYTHONPATH=%{buildroot}%{python3_sitelib}
for i in bash,bash-completion/completions,poetry fish,fish/vendor_completions.d,poetry.fish zsh,zsh/site-functions,_poetry; do IFS=","
    set -- $i
    mkdir -p %{buildroot}%{_datadir}/$2
    # poetry leaves references to the buildroot in the completion files -> remove them
    %{buildroot}%{_bindir}/poetry completions $1 | sed 's|%{buildroot}||g' > %{buildroot}%{_datadir}/$2/$3
done

%if %{with bootstap}
%check
# don't use %%tox here because tox.ini runs "poetry install"
# test_lock_no_update: attempts a network connection to pypi
# test_export_exports_requirements_txt_file_locks_if_no_lock_file:
#    virtualenv: error: argument dest: the destination . is not write-able at /
# test_executor and test_editable_builder doesn't work with pytest7
#    upstream report: https://github.com/python-poetry/poetry/issues/4901
%pytest -k "not lock_no_update and \
not export_exports_requirements_txt_file_locks_if_no_lock_file and \
not executor and \
not editable_builder"
%endif


%files
%{_bindir}/poetry
# The directories with shell completions are co-owned
%{_datadir}/bash-completion/
%{_datadir}/fish/
%{_datadir}/zsh/


%files -n python3-poetry -f %{pyproject_files}
%license LICENSE
%doc README.md

# this is co-owned by poetry-core but we require poetry-core, so we get rid of it
# the file and its pycache might not be bit by bit identical
%exclude %dir %{python3_sitelib}/poetry
%pycached %exclude %{python3_sitelib}/poetry/__init__.py



%changelog
* Sun Oct 30 2022 Miro Hrončok <mhroncok@redhat.com> - 1.2.1-3
- Allow newer requests-toolbelt version
- Fixes: rhbz#2138636

* Fri Oct 07 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.2.1-2
- Update to 1.2.1
- Disable bootstrap bcond

* Fri Sep 30 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.2.1-1
- Update to 1.2.1
- Enable bootstrap bcond

* Mon Jul 25 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1.14-1
- Update to 1.1.14

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 1.1.13-2
- Rebuilt for Python 3.11

* Mon Mar 07 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1.13-1
- Update to 1.1.13
- Disable failing tests with pytest 7
- Fixes: rhbz#2059941

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1.12-1
- Update to 1.1.12

* Mon Nov 15 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1.11-1
- Update to 1.1.11

* Fri Oct 01 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.1.10
- Update to 1.1.10

* Tue Sep 07 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.8-1
- Update to 1.1.8

* Fri Sep 03 2021 Miro Hrončok <mhroncok@redhat.com> - 1.1.7-2
- Install Fish shell completions to /usr/share/fish/vendor_completions.d

* Wed Aug 18 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.7-1
- Update to 1.1.7

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Lumír Balhar <lbalhar@redhat.com> - 1.1.6-5
- Allow newer packaging version

* Tue Jun 15 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.6-4
- Backport upstream patch to fix error on Python 3.10+
- New empty projects created by poetry now have default dev dependency on pytest ^6.2
- to ensure compatibility with Python 3.10+
- Fixes: rhbz#1970361

* Wed Jun  9 2021 Dan Čermák <dan.cermak@cgc-instruments.com> - 1.1.6-3
- Install shell completion files

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.6-2
- Rebuilt for Python 3.10

* Thu Apr 15 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.6-1
- Update to 1.1.6

* Fri Mar 05 2021 Tomas Hrnciar <thrnciar@redhat.com> - 1.1.5-1
- Update to version 1.1.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 02 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.4-1
- Update to version 1.1.4.

* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 1.1.0-1
- Update to version 1.1.0.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.10-1
- Update to version 1.0.10.

* Sat Jul 04 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.9-1
- Update to version 1.0.9.
- Drop manual dependency generator enablement (it's enabled by default).

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-2
- Rebuilt for Python 3.9

* Sat Feb 29 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.5-1
- Update to version 1.0.5.

* Fri Feb 28 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.4-1
- Update to version 1.0.4.

* Wed Feb 05 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-2
- Hard-code dependency on python3-lockfile.

* Sun Feb 02 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-1
- Update to version 1.0.3.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.2-1
- Update to version 1.0.2.

* Fri Dec 13 2019 Fabio Valentini <decathorpe@gmail.com> - 1.0.0-1
- Update to version 1.0.0.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.17-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 26 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.17-4
- Relax dependency on cachy.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.17-3
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.12.17-2
- Add missing dependencies on lockfile and pip

* Sat Aug 10 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.17-1
- Update to version 0.12.17.

* Fri May 03 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.15-1
- Update to version 0.12.15.

* Fri Apr 26 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.14-1
- Update to version 0.12.14.

* Fri Apr 26 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.13-1
- Update to version 0.12.13.

* Fri Apr 12 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.12-1
- Update to version 0.12.12.

* Mon Jan 14 2019 Fabio Valentini <decathorpe@gmail.com> - 0.12.11-1
- Update to version 0.12.11.

* Wed Dec 12 2018 Fabio Valentini <decathorpe@gmail.com> - 0.12.10-1
- Initial package.


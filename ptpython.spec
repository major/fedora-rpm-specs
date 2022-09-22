%global common_description %{expand:
Ptpython is an advanced Python REPL built on top of the prompt_toolkit library.
It features syntax highlighting, multiline editing (the up arrow works),
autocompletion, mouse support, support for color schemes, support for bracketed
paste, both Vi and Emacs key bindings, support for double width (Chinese)
characters, and many other things.}

%if %{defined fedora}
%bcond_without ptipython
%endif

Name:           ptpython
Version:        3.0.20
Release:        3%{?dist}
Summary:        Python REPL build on top of prompt_toolkit
License:        BSD
URL:            https://github.com/prompt-toolkit/ptpython
Source0:        %pypi_source
BuildArch:      noarch


%description %{common_description}


%package -n ptpython3
Summary:        %{summary}
BuildRequires:  python3-devel
Suggests:       python3-ipython
Provides:       ptpython = %{version}-%{release}
%py_provides    python3-%{name}


%description -n ptpython3 %{common_description}


%prep
%autosetup
find -name \*.py | xargs sed -i -e '1 {/^#!\//d}'


%generate_buildrequires
%pyproject_buildrequires %{?with_ptipython:-x ptipython}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{name}
%if %{without ptipython}
rm %{buildroot}%{_bindir}/ptipython*
%endif


%check
%pyproject_check_import -e ptpython.contrib.asyncssh_repl %{!?with_ptipython:-e ptpython.ipython}


%files -n ptpython3 -f %{pyproject_files}
%doc CHANGELOG README.rst
%{_bindir}/ptpython
%{_bindir}/ptpython3
%{_bindir}/ptpython%{python3_version}


%if %{with ptipython}
%pyproject_extras_subpkg -n ptpython3 ptipython
%{_bindir}/ptipython
%{_bindir}/ptipython3
%{_bindir}/ptipython%{python3_version}
%endif


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.20-2
- Rebuilt for Python 3.11

* Fri Apr 08 2022 Carl George <carl@george.computer> - 3.0.20-1
- Latest upstream (resolves: rhbz#1855831)
- Convert to pyproject macros
- Add ptipython subpackage

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.2-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-2
- Rebuilt for Python 3.9

* Thu May 14 2020 Carl George <carl@george.computer> - 3.0.2-1
- Latest upstream rhbz#1760025
- Provide ptpython from ptpython3

* Tue Mar 24 2020 Carl George <carl@george.computer> - 2.0.6-1
- Update to 2.0.6

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 02 2018 Carl George <carl@george.computer> - 2.0.2-1
- Latest upstream
- Drop ptpython2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Carl George <carl@george.computer> - 0.41-7
- Add patch1 to fix Python 3.7 build (upstream #250)

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.41-6
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.41-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 28 2017 Carl George <carl@george.computer> - 0.41-3
- Re-rebuild for F27

* Mon Sep 25 2017 Carl George <carl@george.computer> - 0.41-2
- Require python2-jedi

* Thu Jul 27 2017 Carl George <carl@george.computer> - 0.41-1
- Latest upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Carl George <carl.george@rackspace.com> - 0.39-1
- Latest upstream
- Add patch0 to undo https://github.com/jonathanslenders/ptpython/commit/16e4e31

* Sat Mar 18 2017 Carl George <carl.george@rackspace.com> - 0.36-1
- Initial package.

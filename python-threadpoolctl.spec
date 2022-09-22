%bcond_without check

%global srcname threadpoolctl

Name: python-%{srcname}
Version: 3.1.0
Release: 5%{?dist}
Summary: Thread-pool Controls
License: BSD

URL: https://github.com/joblib/threadpoolctl
Source0: %{pypi_source}

BuildArch: noarch
BuildRequires:  python3-devel

%global _description %{expand:
Python helpers to limit the number of threads used in the 
threadpool-backed of common native libraries used for scientific computing 
and data science (e.g. BLAS and OpenMP).
Fine control of the underlying thread-pool size can be useful in 
workloads that involve nested parallelism so as to mitigate 
oversubscription issues.}     

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
# Testing
%if %{with check}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(scipy)
BuildRequires: python3dist(cython)
%endif

%description -n python3-%{srcname}
%_description

%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files threadpoolctl

%check
%if %{with check}
# test_architecture has a hardcoded list of architectures,
# instead of playing Whac-A-Mole by adding new and new, we skip it
%pytest -v -k 'not test_architecture and not test_command_line'
%else
%pyproject_check_import -t
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md multiple_openmp.md

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 25 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 3.1.0-4
- Skip command line tests for the momment

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.1.0-3
- Rebuilt for Python 3.11

* Mon Apr 25 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 3.1.0-2
- New upstream release (3.1.0)
- Rewrite spec whith new guidelines
- Add Koji's POWER9 and Z14 to the list of test architectures

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.9

* Thu May 21 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0.0-2
- Package approved

* Tue May 19 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 2.0.0-1
- Initial spec

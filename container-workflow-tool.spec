Name:           container-workflow-tool
Version:        1.2.0
Release:        7%{?dist}
Summary:        Tool for automation of rebuilding container images
License:        MIT
URL:            https://github.com/sclorg/%{name}
Source0:        https://github.com/sclorg/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       fedpkg

BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-flexmock

%py_provides python%{python3_pkgversion}-%{name}


%description
A python3 tool to make rebuilding container images easier by automating several
steps of the process.

%prep
%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files container_workflow_tool

# install man pages manually
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/cwt.1

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %{buildroot}%{_bindir}/cwt --help
%py3_check_import container_workflow_tool
%pytest -m "not distgit"


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/cwt
%{_mandir}/man1/cwt.1*


%changelog
* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 1.2.0-6
- Rebuilt for Python 3.12

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Zuzana Miklankova <zmiklank@redhat.com> - 1.2.0-1
- Rebase on 1.2.0

* Wed Sep 29 2021 Zuzana Miklankova <zmiklank@redhat.com> - 1.1.0-1
- Initial package

%global pypi_name widgetsnbextension

Name:           python-%{pypi_name}
Version:        4.0.4
Release:        1%{?dist}
Summary:        Interactive HTML widgets for Jupyter notebooks

License:        BSD
URL:            http://ipython.org
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python-jupyter-filesystem

%description
Interactive HTML widgets for Jupyter notebooks.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Requires:       python3dist(notebook) >= 4.4.1
Requires:       python-jupyter-filesystem

# sagemath included the files of this package
# https://bugzilla.redhat.com/show_bug.cgi?id=1856311
Conflicts:      sagemath-jupyter < 9.1-2

%description -n python3-%{pypi_name}
Interactive HTML widgets for Jupyter notebooks.

%prep
%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%py3_build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

# Move config file from /usr/etc to /etc
mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d/
mv {%{buildroot}%{_prefix}/etc,%{buildroot}%{_sysconfdir}}/jupyter/nbconfig/notebook.d/widgetsnbextension.json

%files -n python3-%{pypi_name} -f %{pyproject_files}
%{_datadir}/jupyter/nbextensions/jupyter-js-widgets/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/widgetsnbextension.json

%changelog
* Wed Dec 07 2022 Lumír Balhar <lbalhar@redhat.com> - 4.0.4-1
- Update to 4.0.4 (rhbz#2151509)

* Sat Sep 03 2022 Lumír Balhar <lbalhar@redhat.com> - 4.0.3-1
- Update to 4.0.3
Resolves: rhbz#2123851

* Mon Aug 22 2022 Lumír Balhar <lbalhar@redhat.com> - 4.0.2-1
- Update to 4.0.2
Resolves: rhbz#1977141

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.6.0-2
- Rebuilt for Python 3.11

* Wed Jun 08 2022 Lumír Balhar <lbalhar@redhat.com> - 3.6.0-1
- Update to 3.6.0
Resolves: rhbz#1977141

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.5.1-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Lumír Balhar <lbalhar@redhat.com> - 3.5.1-1
- Initial package.

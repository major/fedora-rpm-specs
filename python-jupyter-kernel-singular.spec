Name:           python-jupyter-kernel-singular
Version:        0.9.9
Release:        10%{?dist}
Summary:        Jupyter kernel for Singular

License:        GPLv2+
URL:            https://github.com/sebasguts/jupyter_kernel_singular
Source0:        %{url}/archive/v%{version}/jupyter_kernel_singular-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist pysingular}
BuildRequires:  %{py3_dist wheel}

%global _description %{expand:
This package contains a Jupyter kernel for Singular, to enable using
Jupyter as the front end for Singular.}

%description %_description

%package     -n python3-jupyter-kernel-singular
Summary:        Jupyter kernel for Singular
Requires:       python-jupyter-filesystem
Requires:       %{py3_dist ipykernel}
Requires:       %{py3_dist jupyter-client}
Requires:       %{py3_dist pysingular}

%description -n python3-jupyter-kernel-singular %_description

%prep
%autosetup -n jupyter_kernel_singular-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jupyter_kernel_singular

# We want /etc, not /usr/etc
mv %{buildroot}%{_prefix}%{_sysconfdir} %{buildroot}%{_sysconfdir}

%check
%pyproject_check_import

%files -n python3-jupyter-kernel-singular -f %{pyproject_files}
%doc README.md
%{_datadir}/jupyter/kernels/singular/
%{_datadir}/jupyter/nbextensions/singular-mode/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/singular-mode.json

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 0.9.9-9
- Add ipykernel BR
- Expand %%srcname and %%upname for clarity
- Use %%pyproject_save_files

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.9.9-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.9-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.9-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Jerry James <loganjerry@gmail.com> - 0.9.9-1
- Initial RPM

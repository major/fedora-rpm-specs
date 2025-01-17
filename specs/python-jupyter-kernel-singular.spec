Name:           python-jupyter-kernel-singular
Version:        0.9.9
Release:        18%{?dist}
Summary:        Jupyter kernel for Singular

License:        GPL-2.0-or-later
URL:            https://github.com/sebasguts/jupyter_kernel_singular
VCS:            git:%{url}.git
Source:         %{url}/archive/v%{version}/jupyter_kernel_singular-%{version}.tar.gz
# https://github.com/sebasguts/jupyter_kernel_singular/pull/13
Patch:          %{name}-imports.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist ipython}
BuildRequires:  %{py3_dist jupyter-client}
BuildRequires:  %{py3_dist pysingular}

%global _description %{expand:
This package contains a Jupyter kernel for Singular, to enable using
Jupyter as the front end for Singular.}

%description %_description

%package     -n python3-jupyter-kernel-singular
Summary:        Jupyter kernel for Singular
Requires:       python-jupyter-filesystem
Requires:       %{py3_dist ipykernel}
Requires:       %{py3_dist pysingular}

%description -n python3-jupyter-kernel-singular %_description

%prep
%autosetup -n jupyter_kernel_singular-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l jupyter_kernel_singular

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
* Wed Jan 15 2025 Jerry James <loganjerry@gmail.com> - 0.9.9-18
- Add patch to remove unused imports
- Assert that a license is installed

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 0.9.9-17
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Jerry James <loganjerry@gmail.com> - 0.9.9-14
- Stop building for 32-bit x86

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 0.9.9-13
- Rebuilt for Python 3.12

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.9.9-12
- Dynamically generate BuildRequires

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Oct 22 2022 Jerry James <loganjerry@gmail.com> - 0.9.9-11
- Add setuptools BR
- Convert License tag to SPDX

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

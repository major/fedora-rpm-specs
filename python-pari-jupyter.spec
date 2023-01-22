Name:           python-pari-jupyter
Version:        1.4.1
Release:        5%{?dist}
Summary:        Jupyter kernel for PARI/GP

License:        GPL-3.0-or-later
URL:            https://github.com/sagemath/pari-jupyter
Source0:        %{url}/archive/%{version}/pari-jupyter-%{version}.tar.gz
# Adapt to recent versions of pari
Patch0:         %{name}-pari.patch

BuildRequires:  gcc
BuildRequires:  pari-devel
BuildRequires:  pari-gp
BuildRequires:  pkgconfig(readline)
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist cython}
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}

%description
This package contains a Jupyter kernel for PARI/GP.

%package     -n python3-pari-jupyter
Summary:        Jupyter kernel for PARI/GP
Requires:       pari-gp
Requires:       python-jupyter-filesystem

%py_provides python3-PARIKernel

%description -n python3-pari-jupyter
This package contains a Jupyter kernel for PARI/GP.

%prep
%autosetup -n pari-jupyter-%{version} -p1

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install

# Move the config file to the right place
mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig
mv %{buildroot}%{_prefix}%{_sysconfdir}/jupyter/nbconfig/notebook.d \
   %{buildroot}%{_sysconfdir}/jupyter/nbconfig
rm -fr %{buildroot}%{_prefix}%{_sysconfdir}

%files -n python3-pari-jupyter
%doc README.html
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/gp-mode.json
%{_datadir}/jupyter/kernels/pari_jupyter/
%{_datadir}/jupyter/nbextensions/gp-mode/
%{python3_sitearch}/PARIKernel/
%{python3_sitearch}/pari_jupyter*

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.4.1-4
- Rebuild for pari 2.15.0
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 1.4.1-2
- Rebuilt for Python 3.11

* Tue Jan 25 2022 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Version 1.4.1
- Drop upstreamed -cython patch

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 13 2021 Jerry James <loganjerry@gmail.com> - 1.3.2-2
- Provide python3-PARIKernel
- Trim the -pari patch down to the essentials
- Provide URLs for upstream pull requests

* Wed Aug 11 2021 Jerry James <loganjerry@gmail.com> - 1.3.2-1
- Initial RPM

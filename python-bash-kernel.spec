Name:           python-bash-kernel
Version:        0.9.0
Release:        2%{?dist}
Summary:        Bash kernel for Jupyter
License:        BSD-3-Clause
URL:            https://github.com/takluyver/bash_kernel
Source0:        %{url}/archive/%{version}/bash_kernel-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  %{py3_dist docutils}
BuildRequires:  %{py3_dist flit-core}
BuildRequires:  %{py3_dist ipykernel}
BuildRequires:  %{py3_dist pexpect}
BuildRequires:  %{py3_dist pip}
BuildRequires:  %{py3_dist setuptools}
BuildRequires:  %{py3_dist wheel}

%description
This package contains a Jupyter kernel for bash.

%package -n python3-bash-kernel
Summary:        %{summary}
Requires:       bash
Requires:       python-jupyter-filesystem

%description -n python3-bash-kernel
This package contains a Jupyter kernel for bash.

%prep
%autosetup -n bash_kernel-%{version}

%build
%pyproject_wheel
rst2html --no-datestamp README.rst README.html

%install
%pyproject_install
%pyproject_save_files bash_kernel
cd bash_kernel
python3 install.py --prefix %{buildroot}%{_prefix}
cd -

%check
%pyproject_check_import

%files -n python3-bash-kernel -f %{pyproject_files}
%doc README.html
%license LICENSE
%{_datadir}/jupyter/kernels/bash/

%changelog
* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Jerry James <loganjerry@gmail.com> - 0.9.0-1
- Version 0.9.0

* Mon Aug 22 2022 Jerry James <loganjerry@gmail.com> - 0.8-1
- Version 0.8
- Convert License tag to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 0.7.2-4
- Minor spec file cleanups

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.7.2-4
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 0.7.2-1
- Initial RPM

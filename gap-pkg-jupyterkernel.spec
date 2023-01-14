# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%global py3_shebang_flags %(echo %py3_shebang_flags | sed s/s//)

%global pkgname  jupyterkernel
%global upname   JupyterKernel

Name:           gap-pkg-%{pkgname}
Version:        1.4.1
Release:        6%{?dist}
Summary:        Jupyter kernel written in GAP

License:        BSD-3-Clause
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/JupyterKernel/
Source0:        https://github.com/gap-packages/JupyterKernel/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-crypting
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-json
BuildRequires:  gap-pkg-uuid
BuildRequires:  gap-pkg-zeromqinterface
BuildRequires:  jupyter-notebook
BuildRequires:  %{py3_dist jupyter-client}

Requires:       gap-pkg-crypting
Requires:       gap-pkg-io
Requires:       gap-pkg-json
Requires:       gap-pkg-uuid
Requires:       gap-pkg-zeromqinterface
Requires:       python-jupyter-filesystem

%description
This package implements the Jupyter protocol in GAP.

%package doc
# The content is BSD-3-Clause.  The remaining licenses cover the various fonts
# embedded in PDFs.
# CM: Knuth-CTAN
# CM-Super: GPL-1.0-or-later
# Nimbus: AGPL-3.0-only
License:        BSD-3-Clause AND Knuth-CTAN AND GPL-1.0-or-later AND AGPL-3.0-only
Summary:        Jupyter kernel for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}

%build
export LC_ALL=C.UTF-8
gap makedoc.g

%install
mkdir -p %{buildroot}%{_bindir}
cp -p bin/jupyter-kernel-gap %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{gap_libdir}/pkg/%{upname}/doc
cp -a *.g demos gap tst %{buildroot}%{gap_libdir}/pkg/%{upname}
%gap_copy_docs -n %{upname}

mkdir -p %{buildroot}%{_datadir}/jupyter/kernels
cp -a etc/jupyter %{buildroot}%{_datadir}/jupyter/kernels/gap-4

mkdir -p %{buildroot}%{_datadir}/jupyter/nbextensions
cp -a etc/gap-mode %{buildroot}%{_datadir}/jupyter/nbextensions

mkdir -p %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d
cp -p etc/gap-mode.json %{buildroot}%{_sysconfdir}/jupyter/nbconfig/notebook.d

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_libdir};" tst/testall.g

%files
%doc README.md
%license COPYRIGHT.md LICENSE
%{_bindir}/jupyter-kernel-gap
%{_datadir}/jupyter/nbextensions/gap-mode/
%{_datadir}/jupyter/kernels/gap-4/
%config(noreplace) %{_sysconfdir}/jupyter/nbconfig/notebook.d/gap-mode.json
%{gap_libdir}/pkg/%{upname}/
%exclude %{gap_libdir}/pkg/%{upname}/demos/
%exclude %{gap_libdir}/pkg/%{upname}/doc/

%files doc
%docdir %{gap_libdir}/pkg/%{upname}/demos/
%docdir %{gap_libdir}/pkg/%{upname}/doc/
%{gap_libdir}/pkg/%{upname}/demos/
%{gap_libdir}/pkg/%{upname}/doc/

%changelog
* Thu Jan 12 2023 Jerry James <loganjerry@gmail.com> - 1.4.1-6
- Update for split GAP directories

* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 1.4.1-5
- Clarify license of the doc subpackage

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.4.1-5
- Update for gap 4.12.0

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.4.1-4
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Karolina Surma <ksurma@redhat.com> - 1.4.1-2
- Remove -s from Python shebang in `jupyter-kernel-gap` to
  let Jupyter see pip installed extensions

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- Version 1.4.1

* Thu Aug  5 2021 Jerry James <loganjerry@gmail.com> - 1.4.0-1
- Version 1.4.0
- Drop -setup patch since we no longer install with setup.py

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Mar  9 2019 Jerry James <loganjerry@gmail.com> - 1.3-1
- Initial RPM

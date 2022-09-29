%global pkgname  jupyterviz

Name:           gap-pkg-%{pkgname}
Version:        1.5.6
Release:        1%{?dist}
Summary:        Jupyter notebook visualization tools for GAP

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://nathancarter.github.io/%{pkgname}/
Source0:        https://github.com/nathancarter/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Update the python scripts for python 3
Patch0:         %{name}-python3.patch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-jupyterkernel
BuildRequires:  python3-devel

Requires:       gap-pkg-jupyterkernel

%description
This package adds visualization tools to GAP for use in Jupyter
notebooks.  These include standard line and bar graphs, pie charts,
scatter plots, and graphs in the vertices-and-edges sense.

%package doc
Summary:        Jupyter visualization tools for GAP documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
python3 extract_examples.py
gap makedoc.g

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g *.ipynb examples lib tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};%{gap_dir}" tst/testall.g

%files
%doc CHANGES README.md
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/*.ipynb
%exclude %{gap_dir}/pkg/%{pkgname}/doc/
%exclude %{gap_dir}/pkg/%{pkgname}/examples/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%docdir %{gap_dir}/pkg/%{pkgname}/examples/
%{gap_dir}/pkg/%{pkgname}/*.ipynb
%{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/examples/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.5.6-1
- Version 1.5.6
- Convert License tag to SPDX
- Update for gap 4.12.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- New upstream version

* Wed Mar 27 2019 Jerry James <loganjerry@gmail.com> - 1.5.0-1
- Initial RPM

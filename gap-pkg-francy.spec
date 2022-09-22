%global pkgname  francy

Name:           gap-pkg-%{pkgname}
Version:        1.2.4
Release:        8%{?dist}
Summary:        Framework for interactive discrete mathematics
BuildArch:      noarch

License:        MIT
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# The string returned by DrawSplash() can differ based on the order of some
# dict entries.  Only do a cursory check of the return value.
# See https://github.com/gap-packages/francy/pull/76
Patch0:         %{name}-test.patch

BuildRequires:  elinks
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-jupyterkernel
BuildRequires:  xdg-utils

Requires:       gap-pkg-jupyterkernel
Requires:       xdg-utils

%description
Francy is a package for GAP and provides a framework for Interactive
Discrete Mathematics.

Unlike xgap, Francy is not linked with any GUI framework and instead,
this package generates a semantic model that can be used to produce a
graphical representation using any other framework / language.

There is a JavaScript implementation of the graphical representation
that works on Jupyter, embedded in a Web page or as a Desktop Application
(e.g. using electron).

%package doc
Summary:        Francy documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

# Call xdg-open instead of open
sed -i.orig 's/"open "/"xdg-open "/' gap/canvas.gi
touch -r gap/canvas.gi.orig gap/canvas.gi
rm gap/canvas.gi.orig

%build
export LC_ALL=C.UTF-8
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{LICENSE,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/examples/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/examples/

%changelog
* Mon Jul 25 2022 Jerry James <loganjerry@gmail.com> - 1.2.4-8
- Add -test patch to fix the tests
- Invoke xdg-open instead of open
- BR elinks for the tests

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 1.2.4-1
- New upstream version

* Wed Mar 27 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- Initial RPM

%global pkgname singular

Name:           gap-pkg-%{pkgname}
Version:        2020.12.18
Release:        5%{?dist}
Summary:        GAP interface to Singular

License:        GPLv2+
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Adapt to changed output in Singular 4.2.x
# https://github.com/gap-packages/singular/issues/7
Patch0:         %{name}-test.patch

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-guava-doc
BuildRequires:  Singular

Requires:       gap-core
Requires:       Singular

%description
This package contains a GAP interface to the computer algebra system
Singular.

%package doc
Summary:        Singular documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-pkg-guava-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

# The Fedora version of Singular needs the explicit quit command.  Without it,
# we see this on stderr:
#
# fgets() failed with errno 5
# Input/output error
sed -i.orig 's/# WriteLine/WriteLine/' gap/singular.g
touch -r gap/singular.g.orig gap/singular.g
rm gap/singular.g.orig

# Fix encoding
iconv -f ISO8859-1 -t UTF-8 gap/todo > gap/todo.utf8
touch -r gap/todo gap/todo.utf8
mv -f gap/todo.utf8 gap/todo

%build
export LC_ALL=C.UTF-8
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/gap/todo
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{CHANGES.md,LICENSE,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES.md README.md gap/todo
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/lib/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/lib/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 28 2021 Jerry James <loganjerry@gmail.com> - 2020.12.18-3
- Add -test patch to adapt to Singular 4.2.x

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.12.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 21 2020 Jerry James <loganjerry@gmail.com> - 2020.12.18-1
- Version 2020.12.18
- Drop upstreamed -ref patch

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.10.01-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.10.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  2 2019 Jerry James <loganjerry@gmail.com> - 2019.10.01-1
- New upstream version

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2019.02.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun  8 2019 Jerry James <loganjerry@gmail.com> - 2019.02.22-1
- Initial RPM

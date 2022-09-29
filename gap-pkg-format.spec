%global pkgname format

Name:           gap-pkg-%{pkgname}
Version:        1.4.3
Release:        7%{?dist}
Summary:        Formations of finite solvable groups

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Add omitted bibliography file
# See https://github.com/gap-packages/format/pull/8
Patch0:         0001-Add-missing-bibliography.patch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  tth

Requires:       gap-core

%description
The package contains programs for computing with formations of finite
solvable groups and with various formation-theoretic subgroups.

%package doc
Summary:        Format documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p1

# There is no ext manual anymore
sed -i '/UseReferences.*ext/d' doc/manual.tex

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{gap_dir}/etc ../../etc
ln -s %{gap_dir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g grp htm lib tst %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};" tst/testall.g

%files
%doc README.md
%license LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/
%exclude %{gap_dir}/pkg/%{pkgname}/htm/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%docdir %{gap_dir}/pkg/%{pkgname}/htm/
%{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/htm/

%changelog
* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 1.4.3-7
- Update for gap 4.12.0
- Add patch to include missing bibliography file

* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 1.4.3-6
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar  5 2020 Jerry James <loganjerry@gmail.com> - 1.4.3-1
- Version 1.4.3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Jerry James <loganjerry@gmail.com> - 1.4.2-1
- Initial RPM

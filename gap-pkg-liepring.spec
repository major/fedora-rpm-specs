%global pkgname liepring

Name:           gap-pkg-%{pkgname}
Version:        2.8
Release:        1%{?dist}
Summary:        Database and algorithms for Lie p-rings

License:        GPL-2.0-or-later
BuildArch:      noarch
ExclusiveArch:  aarch64 ppc64le s390x x86_64 noarch
URL:            https://gap-packages.github.io/liepring/
Source0:        https://github.com/gap-packages/liepring/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-liering
BuildRequires:  gap-pkg-polycyclic
BuildRequires:  gap-pkg-singular
BuildRequires:  tth

Requires:       gap-pkg-liering
Requires:       gap-pkg-singular

%description
The main object of the LiePRing package is to provide access to the
nilpotent Lie rings of order p^n for p>2 and n<=7.

%package doc
# The content is GPL-2.0-or-later.  The remaining licenses cover the various
# fonts embedded in PDFs.
# AMS: OFL-1.1-RFN
# CM: Knuth-CTAN AND LicenseRef-Fedora-Public-Domain
# Nimbus: AGPL-3.0-only
# StandardSymL: GPL-1.0-or-later
License:        GPL-2.0-or-later AND Knuth-CTAN AND LicenseRef-Fedora-Public-Domain AND AGPL-3.0-only AND GPL-1.0-or-later
Summary:        LiePRing documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Fix paths
sed -i 's,\.\./\.\./\.\./,%{gap_dir}/,' doc/make_doc

%build
export LC_ALL=C.UTF-8
ln -s %{gap_dir}/doc ../../doc
cd doc
./make_doc
cd -
rm ../../doc

%install
mkdir -p %{buildroot}%{gap_dir}/pkg/%{pkgname}/doc
cp -a *.g gap htm lib tst VERSION %{buildroot}%{gap_dir}/pkg/%{pkgname}
%gap_copy_docs

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{gap_dir};%{gap_dir}" tst/testall.g

%files
%doc README.md
%license LICENSE
%{gap_dir}/pkg/%{pkgname}/
%exclude %{gap_dir}/pkg/%{pkgname}/doc/
%exclude %{gap_dir}/pkg/%{pkgname}/htm/
%exclude %{gap_dir}/pkg/%{pkgname}/lib/notes/
%exclude %{gap_dir}/pkg/%{pkgname}/lib/dim6/notes/
%exclude %{gap_dir}/pkg/%{pkgname}/lib/dim7/2gen/notes/
%exclude %{gap_dir}/pkg/%{pkgname}/lib/dim7/3gen/notes/
%exclude %{gap_dir}/pkg/%{pkgname}/lib/dim7/4gen/notes/
%exclude %{gap_dir}/pkg/%{pkgname}/lib/dim7/5gen/notes/

%files doc
%docdir %{gap_dir}/pkg/%{pkgname}/doc/
%docdir %{gap_dir}/pkg/%{pkgname}/lib/notes/
%docdir %{gap_dir}/pkg/%{pkgname}/lib/dim6/notes/
%docdir %{gap_dir}/pkg/%{pkgname}/lib/dim7/2gen/notes/
%docdir %{gap_dir}/pkg/%{pkgname}/lib/dim7/3gen/notes/
%docdir %{gap_dir}/pkg/%{pkgname}/lib/dim7/4gen/notes/
%docdir %{gap_dir}/pkg/%{pkgname}/lib/dim7/5gen/notes/
%{gap_dir}/pkg/%{pkgname}/doc/
%{gap_dir}/pkg/%{pkgname}/htm/
%{gap_dir}/pkg/%{pkgname}/lib/notes/
%{gap_dir}/pkg/%{pkgname}/lib/dim6/notes/
%{gap_dir}/pkg/%{pkgname}/lib/dim7/2gen/notes/
%{gap_dir}/pkg/%{pkgname}/lib/dim7/3gen/notes/
%{gap_dir}/pkg/%{pkgname}/lib/dim7/4gen/notes/
%{gap_dir}/pkg/%{pkgname}/lib/dim7/5gen/notes/

%changelog
* Thu Nov 10 2022 Jerry James <loganjerry@gmail.com> - 2.8-1
- Clarify license of the doc subpackage

* Sat Oct 22 2022 Jerry James <loganjerry@gmail.com> - 2.8-1
- Version 2.8
- Remove runtime dependency on the polycyclic package

* Tue Sep 27 2022 Jerry James <loganjerry@gmail.com> - 2.7-2
- Update for gap 4.12.0
- Convert License tag to SPDX

* Sat Aug  6 2022 Jerry James <loganjerry@gmail.com> - 2.7-1
- Version 2.7

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 12 2022 Jerry James <loganjerry@gmail.com> - 2.6-1
- Version 2.6
- Add dependencies on gap-pkg-polycyclic and gap-pkg-singular

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 19 2019 Jerry James <loganjerry@gmail.com> - 1.9.2-1
- Initial RPM

%global pkgname grpconst

Name:           gap-pkg-%{pkgname}
Version:        2.6.2
Release:        6%{?dist}
Summary:        Constructing groups of a given order

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gap-pkg-autpgrp
BuildRequires:  gap-pkg-irredsol
BuildRequires:  tth

Requires:       gap-pkg-autpgrp
Requires:       gap-pkg-irredsol

%description
This package contains GAP implementations of three different approaches
to constructing up to isomorphism all groups of a given order.

The FrattiniExtensionMethod constructs all soluble groups of a given
order.  On request it gives only those that are (or are not) nilpotent
or supersolvable or that do (or do not) have normal Sylow subgroups for
some given set of primes.  The program's output may be expressed in a
compact coded form, if desired.

The CyclicSplitExtensionMethod constructs all (necessarily soluble)
groups whose given orders are of the form p^n*q for different primes p
and q and which have at least one normal Sylow subgroup.  The method,
which relies upon having available a list of all groups of order p^n, is
often faster than the Frattini extension method for the groups to which
it applies.

The UpwardsExtensions method takes as its input a permutation group G
and positive integer s and returns a list of permutation groups, one for
each extension of G by a soluble group of order a divisor of s.  Usually
it is used for nonsoluble G only, since for soluble groups the above
methods are more efficient.

%package doc
Summary:        GrpConst documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/etc ../../etc
ln -s %{_gap_dir}/doc ../../doc
cd doc
./make_doc
cd -
rm -f ../../{doc,etc}

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{LICENSE,README}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/make_doc

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/htm/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/htm/

%changelog
* Tue Aug 16 2022 Jerry James <loganjerry@gmail.com> - 2.6.2-6
- Convert License tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb  1 2020 Jerry James <loganjerry@gmail.com> - 2.6.2-1
- Version 2.6.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Jerry James <loganjerry@gmail.com> - 2.6.1-1
- Initial RPM

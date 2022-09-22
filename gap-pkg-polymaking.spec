%global pkgname polymaking

Name:           gap-pkg-%{pkgname}
Version:        0.8.6
Release:        4%{?dist}
Summary:        GAP interface to polymake

License:        GPLv2+
URL:            https://gap-packages.github.io/polymaking/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

# Polymake is no longer available on 32-bit platforms
# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
BuildArch:      noarch
ExclusiveArch:  noarch aarch64 ppc64le s390x x86_64

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  polymake

Requires:       gap-core
Requires:       polymake

%description
This package provides a very basic GAP interface to polymake.

%package doc
Summary:        Polymaking documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Fix an undefined LaTeX command in the BibTeX file
sed -i 's/URL/url/' doc/polymaking.bib

# Fix a reference to the main GAP manual
sed -i 's/The \.gaprc file/The former .gaprc file/' doc/environment.xml

%build
export LC_ALL=C.UTF-8

# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
gap < makedoc.g
rm -fr ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{CHANGES,README}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/LICENSE
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8

# Produce less chatter while running the test
polymake --reconfigure - <<< exit;

# Now we can run the actual test.
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" tst/testall.g

%files
%doc CHANGES.md README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Jerry James <loganjerry@gmail.com> - 0.8.6-3
- Do not build on i386 due to unavailability of polymake

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jul 13 2021 Jerry James <loganjerry@gmail.com> - 0.8.6-1
- Version 0.8.6

* Wed Apr 14 2021 Jerry James <loganjerry@gmail.com> - 0.8.5-1
- Version 0.8.5

* Tue Apr 13 2021 Jerry James <loganjerry@gmail.com> - 0.8.4-1
- Version 0.8.4

* Mon Apr 12 2021 Jerry James <loganjerry@gmail.com> - 0.8.3-1
- Version 0.8.3
- Drop all patches; all have been upstreamed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 21 2020 Jerry James <loganjerry@gmail.com> - 0.8.2-5
- Rebuild for gap 4.11.0

* Wed Mar  4 2020 Jerry James <loganjerry@gmail.com> - 0.8.2-4
- Add -polymake4 patch

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr 27 2019 Jerry James <loganjerry@gmail.com> - 0.8.2-1
- New upstream version
- New URLs
- Drop upstreamed -output and -test patches

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 0.8.1-11
- Rebuild for gap 4.10.0
- Add a -doc subpackage
- Add the -test patch to use a more modern test method
- Add the -dims patch to adapt to recent versions of polymake

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 0.8.1-5
- Rebuild for gap 4.8.3

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 0.8.1-3
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source
- Add -output patch to fix misparsed polymake output

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jan 20 2015 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- Initial RPM

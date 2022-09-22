%global pkgname float

Name:           gap-pkg-%{pkgname}
Version:        1.0.3
Release:        3%{?dist}
Summary:        GAP access to mpfr, mpfi, mpc, fplll and cxsc

License:        GPL-2.0-or-later
URL:            https://gap-packages.github.io/float/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Remove atexit hack, not needed for non-coverage builds
Patch0:         %{name}-atexit.patch
# Fix infinitely recursive definitions to work as intended
# https://github.com/gap-packages/float/pull/81
Patch1:         %{name}-recursive.patch

BuildRequires:  cxsc-devel
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  gcc-c++
BuildRequires:  libmpc-devel
BuildRequires:  make
BuildRequires:  mpfi-devel
BuildRequires:  pkgconfig(fplll)
BuildRequires:  pkgconfig(mpfr)

Requires:       gap-core%{?_isa}

%description
This package implements floating-point numbers within GAP, with
arbitrary precision, based on the C libraries FPLLL, MPFR, MPFI, MPC
and CXSC.

%package doc
Summary:        FLOAT documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
BuildArch:      noarch

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version} -p0

# Do not override Fedora build flags
sed -i 's/-O3 -fomit-frame-pointer//;s/-O3/-O2/' configure

%build
export CPPFLAGS="-I %{_includedir}/cxsc"
%configure --with-gaproot=%{_gap_dir} --without-gcc-arch
%make_build

# Build the documentation
mkdir ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

%install
%make_install

# Match upstream
mv %{buildroot}%{_gap_dir}/pkg/%{pkgname} \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}

# We do not want the libtool archive
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/*/*.la

# Install the GAP files; we install test files for use by GAP's internal test
# suite runner.
cp -a *.g lib tst %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/{lib,tst}/Makefile*

# Install the documentation
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc
cp -p doc/*.{bib,css,html,js,lab,pdf,six,toc,txt,xml} \
      %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md THANKS
%license COPYING
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Wed Aug 17 2022 Jerry James <loganjerry@gmail.com> - 1.0.3-3
- Convert License tag to SPDX

* Sun Jul 24 2022 Jerry James <loganjerry@gmail.com> - 1.0.3-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Feb 16 2022 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3
- Add -recursive patch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 14 2021 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- Version 1.0.2
- Drop upstreamed -cxsc patch

* Fri Nov 26 2021 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Version 1.0.1

* Wed Nov 24 2021 Jerry James <loganjerry@gmail.com> - 1.0.0-1
- Version 1.0.0

* Mon Oct 18 2021 Jerry James <loganjerry@gmail.com> - 0.9.9-1
- Version 0.9.9
- License change from GPLv3+ to GPLv2+

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Dec 12 2020 Jerry James <loganjerry@gmail.com> - 0.9.1-11
- Rebuild for libfplll 5.4.0
- Add -cxsc patch to fix issues with cxsc and gcc 11

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  8 2020 Jerry James <loganjerry@gmail.com> - 0.9.1-9
- Rebuild for libfplll 5.3.3

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 0.9.1-8
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 0.9.1-6
- Rebuild for libfplll 5.3.2

* Thu Nov 28 2019 Jerry James <loganjerry@gmail.com> - 0.9.1-5
- Rebuild for libfplll 5.3.0

* Fri Oct 11 2019 Jerry James <loganjerry@gmail.com> - 0.9.1-4
- Rebuild for mpfr 4

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 0.9.1-2
- Rebuild for changed bin dir name in gap 4.10.1

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 0.9.1-1
- New upstream version
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 0.8.0-3
- Rebuild for libfplll 5.2.1 and mpfi 1.5.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 17 2017 Jerry James <loganjerry@gmail.com> - 0.8.0-1
- New upstream version (bz 1509755)
- Drop upstreamed float-instantiator patch
- Drop upstreamed testsuite fixups

* Thu Sep 28 2017 Jerry James <loganjerry@gmail.com> - 0.7.6-4
- Rebuild for libfplll 5.1.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May  9 2017 Jerry James <loganjerry@gmail.com> - 0.7.6-1
- New upstream version (bz 1449208)

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 0.7.5-2
- Rebuild for libfplll 5.x

* Mon Feb 20 2017 Jerry James <loganjerry@gmail.com> - 0.7.5-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul  1 2016 Jerry James <loganjerry@gmail.com> - 0.7.4-1
- Initial RPM

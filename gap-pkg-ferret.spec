%global pkgname ferret

Name:           gap-pkg-%{pkgname}
Version:        1.0.8
Release:        3%{?dist}
Summary:        Backtracking search in permutation groups

# YAPB++/simple_graph/gason is MIT
# YAPB++/source/library/fnv_hash.hpp is Public Domain
# However, none of those files are part of the final binary.
License:        MPL-2.0
URL:            https://gap-packages.github.io/ferret/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-atlasrep
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-ctbllib
BuildRequires:  gap-pkg-io
BuildRequires:  gap-pkg-tomlib
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

Requires:       gap-core%{?_isa}

%description
Ferret is a reimplementation of parts of Jeffery Leon's Partition
Backtrack framework in C++, with extensions including:

- Ability to intersect many groups simultaneously.
- Improved refiners based on orbital graphs.

This package currently supports:

- Group intersection.
- Stabilizing many structures including sets, sets of sets, graphs,
  sets of tuples and tuples of sets.

This package can be used by users in two ways:

- When the package is loaded many built-in GAP functions such as
  'Intersection' and 'Stabilizer' are replaced with more optimized
  implementations.  This requires no changes to existing code.

- The function 'Solve' provides a unified interface to accessing
  all the functionality of the package directly.

%package doc
Summary:        Ferret documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}-%{version}

# Update the atlas package name
sed -i 's/atlas/atlasrep/' tst/test_functions.g

%build
export LC_ALL=C.UTF-8
%configure --with-gaproot=%{_gap_dir}
%make_build

# Build the documentation
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version}
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -p bin/%{_gap_arch}/.libs/ferret.so \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -a doc lib tst *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Wed Aug 17 2022 Jerry James <loganjerry@gmail.com> - 1.0.8-3
- Convert License tag to SPDX

* Tue Jul 26 2022 Jerry James <loganjerry@gmail.com> - 1.0.8-3
- Rebuild due to changed binary dir name on s390x

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul  1 2022 Jerry James <loganjerry@gmail.com> - 1.0.8-1
- Version 1.0.8

* Wed Mar 30 2022 Jerry James <loganjerry@gmail.com> - 1.0.7-1
- Version 1.0.7
- Make the -doc subpackage noarch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Oct 26 2021 Jerry James <loganjerry@gmail.com> - 1.0.6-1
- Version 1.0.6

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 10 2021 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Version 1.0.5

* Tue Feb  9 2021 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- Version 1.0.4

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 27 2020 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3
- Replace GPLv2+ with MPLv2.0 in the License field

* Thu Apr 30 2020 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- Initial RPM

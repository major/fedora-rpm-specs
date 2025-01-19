Name:		lrcalc
Version:	2.1
Release:	11%{?dist}
License:	GPL-3.0-or-later
Summary:	Littlewood-Richardson Calculator
URL:		https://sites.math.rutgers.edu/~asbuch/lrcalc/
Source0:	https://sites.math.rutgers.edu/~asbuch/lrcalc/%{name}-%{version}.tar.gz
Source1:	lrcalc.module.in
Requires:	environment(modules)

BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	%{py3_dist cython}

%description
The "Littlewood-Richardson Calculator" is a package of C and Maple programs
for computing Littlewood-Richardson coefficients. The C programs form the
engine of the package, providing fast calculation of single LR coefficients,
products of Schur functions, and skew Schur functions. The Maple code mainly
gives an interface which makes it possible to use the C programs from Maple.
This interface uses the same notation as the SF package of John Stembridge,
to make it easier to use both packages at the same time.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n	python3-lrcalc
Summary:	Python interface to lrcalc
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description -n python3-lrcalc
Python interface to the Littlewood-Richardson Calculator.

%prep
%autosetup

%generate_buildrequires
cd python
%pyproject_buildrequires

%build
%configure --bindir=%{_libdir}/%{name} --enable-shared --disable-static
# Kill rpaths
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC=.g..|& -Wl,--as-needed|' \
    -i libtool

%make_build

# Build the python interface
sed -e "/libraries/i\                  extra_link_args=['-L$PWD/src/.libs']," \
    -e 's/long_description_type/long_description_content_type/' \
    -i python/setup.py
cd python
ln -s ../src lrcalc
%pyproject_wheel
cd -

%install
%make_install
rm %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_datadir}/%{name}

mkdir -p %{buildroot}%{_datadir}/modulefiles
sed 's#@BINDIR@#'%{_libdir}/%{name}'#g;' < %{SOURCE1} > \
    %{buildroot}%{_datadir}/modulefiles/%{name}-%{_arch} 

cd python
%pyproject_install
%pyproject_save_files lrcalc
cd -

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir}: make check

%files
%doc AUTHORS ChangeLog README
%license COPYING LICENSE
%{_libdir}/%{name}/
%{_libdir}/lib%{name}.so.2*
%{_datadir}/modulefiles/%{name}-%{_arch}

%files		devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%files -n	python3-lrcalc -f %{pyproject_files}

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Jan 14 2025 Jerry James <loganjerry@gmail.com> - 2.1-10
- Fix a typo in setup.py

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.1-9
- Rebuilt for Python 3.13

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.1-5
- Rebuilt for Python 3.12

* Fri Feb 24 2023 Jerry James <loganjerry@gmail.com> - 2.1-4
- Dynamically generate python BuildRequires

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Jerry James <loganjerry@gmail.com> - 2.1-3
- Convert License tag to SPDX
- Use %%pyproject_save_files

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1-2
- Rebuilt for Python 3.11

* Wed Jun  1 2022 Jerry James <loganjerry@gmail.com> - 2.1-1
- Version 2.1
- Drop upstreamed includes patch
- Add python3-lrcalc subpackage
- Minor spec file cleanups

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 11 2016 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.2-1
- Update do latest upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.6-7
- Require environment(modules), install into generic modulefiles location
- Use %%license
- Drop group

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.6-2.beta
- Rebuild with updated upstream tarball (#909510#c3).

* Fri Feb  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.1.6-1.beta
- Initial lrcalc spec.

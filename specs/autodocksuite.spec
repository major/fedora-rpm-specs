%global vname dist426

Name:		autodocksuite
Version:	4.2.6
Release:	24%{?dist}
Summary:	AutoDock is a suite of docking tools to study protein-ligand interaction

License:	GPL-2.0-or-later
URL:		http://autodock.scripps.edu/
Source0:	http://autodock.scripps.edu/downloads/autodock-registration/tars/%{vname}/%{name}-%{version}-src.tar.gz

BuildRequires:  gcc-c++
BuildRequires:	csh
BuildRequires: make

%description
AutoDock is a suite of automated docking tools. It is designed to predict \
how small molecules, such as substrates or drug candidates, bind to a \
receptor of known 3D structure. AutoDock 4 actually consists of two main \
programs: autodock performs the docking of the ligand to a set of grids \
describing the target protein; autogrid pre-calculates these grids. In \
addition to using them for docking, the atomic affinity grids can be \
visualized. This can help, for example, to guide organic synthetic chemists \
design better binders.

%prep
%setup -q -n src

%build

pushd autodock
%configure
make %{?_smp_mflags}
popd

pushd %{_builddir}/src/autogrid
%configure
make V=1 %{?_smp_mflags}

%install
make -C autodock install DESTDIR=%{buildroot}
make -C autogrid install DESTDIR=%{buildroot}

rm -f %{buildroot}/%{_bindir}/autodock4.omp

%files
%license autodock/COPYING
%{_bindir}/autodock4
%{_bindir}/autogrid4

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep  8 2022 Dave Love <loveshack@fedoraproject.org> - 4.2.6-18
- Use SPDX licence TAG

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.2.6-2
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 12 2015 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.6-1
- Update to version 4.2.6
- Removed -doc subpackage (user guide removed from src tarball)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 20 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.5.1-5
- Spec file optimizations/corrections

* Wed Feb 19 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.5.1-4
- Fixed spec file problems
- Removed ldconfig from post and postun
- Removed export CFLAGS

* Wed Feb 19 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.5.1-3
- Added Requires for -doc subpackage

* Tue Feb 18 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.5.1-2
- Fixed spec file errors
- Added files under doc and created -doc package

* Mon Feb 17 2014 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 4.2.5.1-1
- Initial package

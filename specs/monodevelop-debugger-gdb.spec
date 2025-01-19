# rpm does not currently pull debuginfo out of mono packages
%global debug_package %{nil}  

Summary:        MonoDevelop gdb Debugger Add-in
Name:           monodevelop-debugger-gdb
Version:        5.0.1
Release:        18%{?dist}
License:        MIT
Source:         http://download.mono-project.com/sources/%{name}/%{name}-%{version}-0.tar.bz2
URL:            http://www.monodevelop.com/
BuildRequires: make
BuildRequires:  mono-devel >= 2.6 monodevelop-devel >= 2.6 mono-addins-devel
Requires:       monodevelop >= 2.6 gdb
ExclusiveArch:  %{mono_arches}

# nunit2 fails to build on armv7hl. Mono crashes. see bug 1923663
# it is too much work to switch to nunit (version 3) at the moment.
ExcludeArch:    armv7hl

%description
Mono gdb Debugger Add-in for MonoDevelop.

%prep
%setup -q

%build
sed -i "s#dmcs#mcs#g" configure
./configure --prefix=%{_prefix} --bindir=%{_bindir} --datadir=%{_datadir} --libdir=%{_libdir}
# no parallel build support
make

%install
make install DESTDIR=%{buildroot}

%files
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Debugger/MonoDevelop.Debugger.Gdb*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 05 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 5.0.1-10
- disable arch armv7hl

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 22 2017 Claudio Rodrigo Pereyra Diaz <chkr@fedoraproject.org> - 5.0.1-1
- Update to 5.0.1-2
- Use mcs instead dmcs

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8.4-9
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.8.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun 09 2012 Christian Krause <chkr@fedoraproject.org> - 2.8.8.4-1
- Update to 2.8.8.4

* Wed Jan 04 2012 Christian Krause <chkr@fedoraproject.org> - 2.8.5-1
- Update to 2.8.5

* Mon Oct 31 2011 Christian Krause <chkr@fedoraproject.org> - 2.8.1-2
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Sun Oct 16 2011 Christian Krause <chkr@fedoraproject.org> - 2.8.1-1
- Update to 2.8.1

* Sun Oct 16 2011 Dan Horák <dan[at]danny.cz> - 2.6-2
- updated the supported arch list

* Mon Sep 12 2011 Christian Krause <chkr@fedoraproject.org> - 2.6-1
- Update to 2.6
- Minor spec file cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 19 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.4-1
- Bump to 2.4
- Alter BR and R to reflect 2.4

* Sun May 30 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.3.1-1
- Bump to 2.4 beta 2

* Tue May 18 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.3-1
- Bump to 2.4 beta

* Thu Mar 04 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2.1-2
- Spec file clean up
- Remove BR gdb, added R gdb

* Fri Feb 12 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2.1-1
- Bump to 2.2.1

* Sun Jan 24 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-2
- Fix URL and licence
- Fix build problems on x86_64

* Sun Jan 03 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.2-1
- Initial import

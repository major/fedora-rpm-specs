Name:           primer3
Version:        2.4.0
Release:        15%{?dist}
Summary:        PCR primer design tool
# Automatically converted from old format: BSD and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-2.0-or-later
URL:            http://primer3.sourceforge.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:  gcc-c++

%description
Primer3 is a widely used program for designing PCR primers (PCR = 
"Polymerase Chain Reaction"). PCR is an essential and ubiquitous 
tool in genetics and molecular biology. Primer3 can also design 
hybridization probes and sequencing primers.

PCR is used for many different goals. Consequently, primer3 has 
many different input parameters that you control and that tell 
primer3 exactly what characteristics make good primers for your goals.


%prep
%autosetup
chmod -x src/*
chmod +x src/primer3_config # causes permissions issue if removed
sed -i -e 's|CFLAGS  = $(CC_OPTS) $(O_OPTS)|CFLAGS  = $(CC_OPTS) $(O_OPTS) $(INIT_CFLAGS) -fpermissive|' src/Makefile
sed -i 's/\r//' settings_files/*
sed -i -e 's|/opt/primer3_config|/etc/primer3_config|' src/release_notes.txt src/thal_main.c src/primer3_boulder_main.c


%build
cd src
export INIT_CFLAGS="%{optflags}"
%make_build


%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 src/%{name}_core $RPM_BUILD_ROOT%{_bindir}/%{name}_core
install -p -m 0755 src/oligotm $RPM_BUILD_ROOT%{_bindir}/oligotm
install -p -m 0755 src/ntdpal $RPM_BUILD_ROOT%{_bindir}/ntdpal
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/primer3_config
cp -r src/primer3_config $RPM_BUILD_ROOT%{_sysconfdir}/


%check
pushd src
 %{?_with_tests:make test}
popd


%files
%doc README.md example settings_files/*
%license LICENSE
%{_bindir}/%{name}_core
%{_bindir}/oligotm
%{_bindir}/ntdpal
%{_sysconfdir}/primer3_config

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.4.0-14
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Filipe Rosset <rosset.filipe@gmail.com> - 2.4.0-1
- Update to 2.4.0 fixes rhbz#1509743 rhbz#1606905 and rhbz#1675685

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.3.7-3
-  Add BR on gcc-c++

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 10 2018 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.3.7-1
- Update to 2.3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.6-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec 23 2013 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.6-1
- Update to 2.3.6

* Thu Sep 05 2013 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.3.5-1
- Update to 2.3.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 26 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.3.4-1
- Update to 2.3.4

* Tue Mar 27 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.3.2-2
- Include the primer3_config folder RHBZ#821501
- Move primer3_config from /opt/ where upstream wants it to /etc where I want it

* Tue Mar 27 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.3.2-1
- Update to release 2.3.2

* Wed Feb 22 2012 Pierre-Yves Chibon <pingou@pingoured.fr> - 2.3.0-1
- Update to release 2.3.0

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 25 2010 pingou <pingou@pingoured.fr> - 2.2.3-1
- Update to 2.2.3
- Fix permission issue

* Sat Apr 24 2010 pingou <pingou@pingoured.fr> - 2.2.2-pre1
- Build version 2.2.2 beta

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 06 2008 pingou <pingoufc4@yahoo.fr> 1.1.4-5
- Remove headers, not needed

* Tue Aug 12 2008 pingou <pingoufc4@yahoo.fr> 1.1.4-4
- Change the check section to use conditionnality --with tests runs the test
-  defaults does not

* Mon Aug 11 2008 pingou <pingoufc4@yahoo.fr> 1.1.4-3
- Move the export to the build section
- Move the make test to the check section
- Set the binaries perms to 755

* Wed Aug 06 2008 pingou <pingoufc4@yahoo.fr> 1.1.4-2
- Keep the timestamp in the README.txt
- Change the CFLAG for the compilation
- Remove BR perl

* Thu Jul 24 2008 pingou <pingoufc4@yahoo.fr> 1.1.4-1
- First build for Fedora


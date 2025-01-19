%global modulesdir %%(pkg-config --variable=modulesdir libcrypto)

Summary: OpenSSL provider for IBMCA
Name: openssl-ibmca
Version: 2.4.1
Release: 6%{?dist}
License: Apache-2.0
URL: https://github.com/opencryptoki
Source0: https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# post GA fixes
Patch0: %{name}-%{version}-fixes.patch
Requires: libica >= 4.0.0
BuildRequires: make
BuildRequires: gcc
BuildRequires: libica-devel >= 4.0.0
BuildRequires: automake libtool
BuildRequires: openssl >= 3.0.5
BuildRequires: perl(FindBin)
ExclusiveArch: s390 s390x


%description
A dynamic OpenSSL provider for IBMCA crypto hardware on IBM Z machines
to accelerate cryptographic operations.


%prep
%autosetup -p1

./bootstrap.sh


%build
%configure --disable-engine --enable-provider --libdir=%{modulesdir} --with-libica-cex --with-libica-version=4
%make_build


%install
%make_install
rm -f %{buildroot}%{modulesdir}/*.la

# remove generated sample configs
rm -rf %{buildroot}%{_datadir}/%{name}


%check
make check


%files
%license LICENSE
%doc ChangeLog README.md
%doc src/provider/ibmca-provider-opensslconfig
%{modulesdir}/ibmca-provider.so
%{_mandir}/man5/ibmca-provider.5*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu May 23 2024 Dan Horák <dan@danny.cz> - 2.4.1-4
- add post GA fixes

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 21 2023 Dan Horák <dan@danny.cz> - 2.4.1-1
- updated to 2.4.1

* Thu Jul 27 2023 Dan Horák <dan@danny.cz> - 2.4.0-5
- switch to upstream fix for logging into /tmp

* Wed Jul 26 2023 Dan Horák <dan@danny.cz> - 2.4.0-4
- one more fix

* Wed Jul 26 2023 Dan Horák <dan@danny.cz> - 2.4.0-3
- add post GA fixes
- let provider log into /tmp

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 04 2023 Dan Horák <dan@danny.cz> - 2.4.0-1
- updated to 2.4.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Dan Horák <dan@danny.cz> - 2.3.1-4
- add post GA fixes

* Fri Jan 06 2023 Dan Horák <dan@danny.cz> - 2.3.1-3
- switch to building only the provider

* Fri Sep 30 2022 Dan Horák <dan@danny.cz> - 2.3.1-1
- updated to 2.3.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 19 2022 Dan Horák <dan@danny.cz> - 2.3.0-1
- updated to 2.3.0

* Mon Mar 21 2022 Dan Horák <dan@danny.cz> - 2.2.3-1
- updated to 2.2.3

* Mon Jan 31 2022 Dan Horák <dan@danny.cz> - 2.2.2-1
- updated to 2.2.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Dan Horák <dan@danny.cz> - 2.2.1-1
- updated to 2.2.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Dan Horák <dan@danny.cz> - 2.2.0-1
- updated to 2.2.0

* Wed May 12 2021 Dan Horák <dan@danny.cz> - 2.1.2-1
- updated to 2.1.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 12 2020 Dan Horák <dan@danny.cz> - 2.1.1-1
- updated to 2.1.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Dan Horák <dan@danny.cz> - 2.1.0-1
- updated to 2.1.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Dan Horák <dan@danny.cz> - 2.0.3-1
- updated to 2.0.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 13 2018 Dan Horák <dan@danny.cz> - 2.0.2-1
- updated to 2.0.2

* Thu Aug 23 2018 Dan Horák <dan@danny.cz> - 2.0.0-3
- run upstream test-suite during build

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Dan Horák <dan@danny.cz> - 2.0.0-1
- updated to 2.0.0

* Fri Feb 23 2018 Dan Horák <dan@danny.cz> - 1.4.1-1
- updated to 1.4.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Dan Horák <dan@danny.cz> - 1.4.0-2
- update engine filename
- spec cleanup

* Mon Sep 11 2017 Dan Horák <dan@danny.cz> - 1.4.0-1
- updated to 1.4.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 08 2017 Dan Horák <dan@danny.cz> - 1.3.1-1
- updated to 1.3.1 and OpenSSL 1.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Nov 05 2014 Dan Horák <dan@danny.cz> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Mar 19 2014 Dan Horák <dan[at]danny.cz - 1.2.0-8
- Set proper key signature flag (#1075474)

* Fri Mar 14 2014 Dan Horák <dan[at]danny.cz - 1.2.0-7
- Fix multilib conflict in sample config file (#1076423)
- Fixed message digest length definition in sha256 template (#1074976)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 20 2012 Dan Horák <dan[at]danny.cz - 1.2.0-3
- make the libica dependecies versioned
- fix segfaults in OFB mode (#749638)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 07 2011 Dan Horák <dan[at]danny.cz - 1.2.0-1
- update to 1.2.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 22 2010 Dan Horák <dhorak@redhat.com> - 1.1-2
- fixed opening of the libica library (#584765)
- Resolves: #584765

* Thu Mar  4 2010 Dan Horák <dhorak@redhat.com> - 1.1-1
- rebased to 1.1 instead of patching
- Resolves: #568847

* Thu Feb 18 2010 Dan Horák <dhorak@redhat.com> - 1.0.0-5
- added patch with port to libica 2.x API
- Related: #543948

* Wed Feb 10 2010 Dan Horák <dhorak@redhat.com> - 1.0.0-4
- added explicit dependency on libica, because it's dlopened
- Related: #543948

* Tue Jan 12 2010 Dan Horák <dhorak@redhat.com> - 1.0.0-3
- rebuild
- Related: #543948

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul  9 2009 Dan Horak <dan[at]danny.cz - 1.0.0-1
- update to final 1.0.0
- spec file cleanup

* Thu Jun 21 2007 Phil Knirsch <pknirsch@redhat.com> - 1.0.0rc2-1.el5.4
- Fixed several issues with failure of using ibmca engine (#227644)

* Tue Dec 12 2006 Phil Knirsch <pknirsch@redhat.com> - 1.0.0rc2-1.el5.3
- Added missing symlinks for libs (#215735)
- Added samle config file (#215735)

* Thu Nov 23 2006 Phil Knirsch <pknirsch@redhat.com> - 1.0.0rc2-1.el5.2
- Necessary fix so openssl finds the module properly (#215735)

* Thu May 11 2006 Phil Knirsch <pknirsch@redhat.com> - 1.0.0rc2
- Initial package.

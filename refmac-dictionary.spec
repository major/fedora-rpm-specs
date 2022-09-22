Name: refmac-dictionary
Summary: Refmac ligand dictionaries
Version: 5.41
Release: 17%{?dist}
License: LGPLv2+
URL: http://www2.mrc-lmb.cam.ac.uk/groups/murshudov/content/refmac/refmac.html
Source0: http://www2.mrc-lmb.cam.ac.uk/groups/murshudov/content/refmac/Dictionary/refmac_dictionary_v%{version}.tar.gz
BuildArch: noarch

%description
The refmac ligand dictionaries contain chemical information on a large
number of molecules, including the chemical structure of the ligand,
the tree-like structure, the links between ligands, and possible
modifications to them.  This information is stored in the mmCIF
format, which is used by a number of molecular viewing, refinement and
validation tools.

%prep
%setup -q -c
# stuff we don't want to redistribute/need
rm monomers/pdb_v2to3.py
rm monomers/pdb_alt_names.txt
rm monomers/dnarna_basepairs.txt
rm monomers/dnarna_basepairs_2.txt
rm -rf monomers/.bzr
rm monomers/t/TRP.cif~ monomers/g/GLU.cif~ monomers/h/HIS.cif~ monomers/g/GLN.cif~

# clear exec flag
chmod 644 monomers/docs/bug_fixes.html
chmod 644 monomers/primes.table monomers/primes.txt monomers/m/MO6.cif
chmod 644 monomers/f/FUC-A-L.cif
chmod 644 monomers/n/NAG-B-D.cif
chmod 644 monomers/m/MAN-B-D.cif
chmod 644 monomers/g/GLC-B-D.cif
chmod 644 monomers/d/DUM.cif
chmod 644 monomers/g/GAL-B-D.cif

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/%{name}-%{version}/data
cp -pr monomers %{buildroot}%{_datadir}/%{name}-%{version}/data

%files
%doc monomers/COPYING monomers/docs/bug_fixes.html
%{_datadir}/%{name}-%{version}

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.41-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 8 2013 Tim Fenn <tim.fenn@gmail.com> - 5.41-1
- update to 5.41
- update upstream URL

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 10 2012 Tim Fenn <tim.fenn@gmail.com> - 5.38-1
- update to 5.38

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Tim Fenn <fenn@stanford.edu> - 5.30-1
- update to 5.30

* Thu Apr 21 2011 Tim Fenn <fenn@stanford.edu> - 5.28-1
- update to 5.28

* Fri Feb 25 2011 Tim Fenn <fenn@stanford.edu> - 5.25-2
- add missing doc file

* Fri Feb 25 2011 Tim Fenn <fenn@stanford.edu> - 5.25-1
- update to 5.25

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Aug 08 2010 Tim Fenn <fenn@stanford.edu> - 5.21-1
- update to 5.21

* Tue Mar 09 2010 Tim Fenn <fenn@stanford.edu> - 5.18-1
- update to 5.18

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 19 2009 Tim Fenn <fenn@stanford.edu> - 5.12-1
- update to 5.12

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.04-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 17 2008 Tim Fenn <fenn@stanford.edu> - 5.04-2
- minor edit to description

* Wed Dec 10 2008 Tim Fenn <fenn@stanford.edu> - 5.04-1
- update to 5.04 (ccp4 6.1.0)

* Fri Nov 21 2008 Tim Fenn <fenn@stanford.edu> - 5.02-3
- change license to LGPLv2+

* Wed Nov 19 2008 Tim Fenn <fenn@stanford.edu> - 5.02-2
- edit buildroot macro
- add version to changelog

* Mon Nov 17 2008 Tim Fenn <fenn@stanford.edu>
- initial build

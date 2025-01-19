Name: pcapdiff
Version: 0.1
Release:  39%{?dist}
Summary: Compares packet captures, detects forged, dropped or mangled packets

License: GPL-2.0-or-later AND GPL-3.0-or-later
URL: http://www.eff.org/testyourisp/pcapdiff/
Source0: http://www.eff.org/files/pcapdiff-%{version}.tar.gz
Source1: pcapdiff.py
Source2: printpackets
Patch0: pcapdiff-python3.patch

BuildArch: noarch
BuildRequires: python3-devel
Requires: python3-pcapy

%description
Pcapdiff is a tool developed by the EFF to compare two packet captures and
identify potentially forged, dropped, or mangled packets. Two technically-
inclined friends can set up packet captures (e.g. tcpdump or Wireshark) on
their own computers and produce network traffic between their two computers 
over the Internet. Later, they can run pcapdiff on the two packet capture 
files to identify suspicious packets for further investigation. See 
Detecting packet injection: a guide to observing packet spoofing by ISPs 
and EFF's Test Your ISP Project for more background.

%prep
%setup -qn pcapdiff
%patch -P0 -p0

%build

%install
install -D -m 755 -p %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/pcapdiff
install -D -m 644 -p pcapdiff.py $RPM_BUILD_ROOT%{_datadir}/pcapdiff/pcapdiff.py
install -D -m 755 -p %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/printpackets
install -D -m 644 -p printpackets.py $RPM_BUILD_ROOT%{_datadir}/pcapdiff/printpackets.py
install -D -m 644 -p pcapdiff_helper.py $RPM_BUILD_ROOT%{_datadir}/pcapdiff/pcapdiff_helper.py


%files
%doc README COPYING.2 COPYING.3
%{_bindir}/pcapdiff
%{_bindir}/printpackets
%dir %{_datadir}/pcapdiff/
%{_datadir}/pcapdiff/*.py
#%{_datadir}/pcapdiff/*.pyc
#%{_datadir}/pcapdiff/*.pyo

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.1-34
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Gwyn Ciesla <gwync@protonmail.com> 0.1-26
- Eliminate final python 2 dep.

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.1-25
- Python 3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.1-22
- Fix shebang handling.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1-20
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.1-8
- recompiling .py files against Python 2.7 (rhbz#623344)

* Tue Mar 20 2010 Jon Ciesla <limb@jcomserv.net> - 0.1-7
- Fix for crash, BZ 557733.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.1-4
- Rebuild for Python 2.6

* Fri Feb 22 2008 Jon Ciesla <limb@jcomserv.net> - 0.1-3
- BZ 434582.

* Tue Dec 04 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-2
- Added python-devel BR to fix .pyc/.pyo issue.

* Fri Nov 30 2007 Jon Ciesla <limb@jcomserv.net> - 0.1-1
- create.

Name: cfdg
Version:  3.4.1
Release:  1%{?dist}
Summary: Context Free Design Grammar

License: GPL-2.0-or-later
URL: http://www.contextfreeart.org/

Source0: http://www.contextfreeart.org/download/ContextFreeSource%{version}.tgz
Patch0:  cfdg-nostrip.patch
BuildRequires: gcc-c++ libatomic libicu-devel
BuildRequires: libpng-devel bison flex
BuildRequires: make
BuildRequires: sed

%description
Context Free is a program that generates images from written instructions 
called a grammar. The program follows the instructions in a few seconds to 
create images that can contain millions of shapes.

%prep
%setup -qcn ContextFreeSource%{version}

%patch -P0 -p0

# Remove -march=native everywhere.
find -type f -print0 | xargs -0 sed -i 's/-march=native//g'

%build
pushd context-free%{version}
OPTFLAGS=$RPM_OPT_FLAGS make %{?_smp_mflags}
popd

%install
pushd context-free%{version}
install -D -m 755 cfdg %{buildroot}%{_bindir}/cfdg
popd

%files
%{_bindir}/cfdg
%license context-free%{version}/LICENSE.txt
%doc context-free%{version}/input/* context-free%{version}/README* context-free%{version}/ChangeLog

%changelog
* Wed Jan 08 2025 Gwyn Ciesla <gwync@protonmail.com> - 3.4.1-1
- 3.4.1

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 3.3-19
- Rebuild for ICU 74

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 3.3-15
- Rebuilt for ICU 73.2

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 3.3-14
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 3.3-12
- Rebuild for ICU 72

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 3.3-11
- Rebuilt for ICU 71.1

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 3.3-7
- Rebuild for ICU 69

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 3.3-6
- Rebuild for ICU 69

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 3.3-2
- Rebuild for ICU 67

* Mon Apr 13 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.3-1
- 3.3

* Tue Feb 11 2020 Gwyn Ciesla <gwync@protonmail.com> - 3.2-4
- Fix FTBFS.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 3.2-2
- Rebuild for ICU 65

* Tue Aug 06 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.2-1
- 3.2

* Wed Jul 31 2019 Gwyn Ciesla <gwync@protonmail.com> - 3.1-1
- 3.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-0.beta2.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0-0.beta2.7
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-0.beta2.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 20 2012 Jon Ciesla <limburgher@gmail.com> - 3.0-0.beta2.1
- Fix optflags, BZ 795104.

* Fri Feb 17 2012 Jon Ciesla <limburgher@gmail.com> - 3.0-0.beta2
- New upstream.

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 10 2011 Jon Ciesla <limb@jcomserv.net> - 2.2.2-3
- Rebuild for libpng 1.5.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 02 2011 Jon Ciesla <limb@jcomserv.net> - 2.2.2-1
- New upstream.

* Mon Jun 28 2010 Jon Ciesla <limb@jcomserv.net> - 2.2.1-2
- Fix for FTBFS, BZ 600013.

* Mon Oct 05 2009 Jon Ciesla <limb@jcomserv.net> - 2.2.1-1
- New upstream.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Jon Ciesla <limb@jcomserv.net> - 2.2-3
- Rebuild due to 505774.

* Fri Jun 12 2009 Ville Skyttä <ville.skytta at iki.fi> - 2.2-2
- Build with %%{optflags}.

* Mon Apr 27 2009 Jon Ciesla <limb@jcomserv.net> - 2.2-1
- 2.2, fixed licencing and gcc issues.
- Updated mktemp, optflag patches.

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 24 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-5
- Created modified tarball for licensing issue.

* Wed Oct 15 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-4
- Optflag fix.
- Added smp flags.
- Simplified install process.
- Retconned initial changelog entry.
- Fixed URL.

* Tue Oct 14 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-3
- Patched for mktemp error.

* Mon Aug 18 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-2
- Annotated patches, append CFLAGS for review.

* Tue Jun 17 2008 Jon Ciesla <limb@jcomserv.net> - 2.1-1
- Create.

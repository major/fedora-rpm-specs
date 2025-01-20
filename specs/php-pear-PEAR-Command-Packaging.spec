%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global pear_name PEAR_Command_Packaging

Name:           php-pear-PEAR-Command-Packaging
Version:        0.3.0
Release:        30%{?dist}
Summary:        Create RPM spec files from PEAR modules

# Automatically converted from old format: PHP - review is highly recommended.
License:        PHP-3.01
URL:            http://pear.php.net/package/PEAR_Command_Packaging
Source0:        http://pear.php.net/get/%{pear_name}-%{version}.tgz
Source1:        php-pear-PEAR-Command-Packaging-fedora-template-specfile
Patch0:         php-pear-PEAR-Command-Packaging-0.3.0-fedora-conventions.patch
# https://pear.php.net/bugs/19673 - Adaptation required for metadata_dir
Patch1:         php-pear-PEAR-Command-Packaging-0.3.0-metadata.patch
Patch2:         php-pear-PEAR-Command-Packaging-0.3.0-metadata2.patch

BuildArch:      noarch
BuildRequires:  php-pear

Requires:       php-pear(PEAR)
Requires(post): %{__pear}
Requires(postun): %{__pear}
Provides:       php-pear(%{pear_name}) = %{version}

%description
This command is an improved implementation of the standard PEAR "makerpm" 
command, and contains several enhancements that make it far more flexible. 
Similar functions for other external packaging mechanisms may be added at
a later date.

This package generate spec file closed to fedora PHP Guidelines:
http://fedoraproject.org/wiki/Packaging:PHP


%prep
%setup -q -c

cd %{pear_name}-%{version}
mv ../package.xml %{name}.xml

# Patches for Fedora conventions
%patch -P0 -p1 -b .fedora
# Patches for new Metadata location
%patch -P1 -p1 -b .metadata
%patch -P2 -p1 -b .metadata2


%build
# Empty build section, nothing required

%install
cd %{pear_name}-%{version}
rm -rf %{buildroot}
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

cp -p %{SOURCE1} %{buildroot}%{pear_datadir}/%{pear_name}/template.spec

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}



%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi

%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_datadir}/%{pear_name}
%{pear_testdir}/%{pear_name}
%{pear_phpdir}/PEAR/Command/Packaging.*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.0-29
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 17 2012 Remi Collet <remi@fedoraproject.org> - 0.3.0-6
- fix previous patch for metadata_dir

* Tue Oct 23 2012 Remi Collet <remi@fedoraproject.org> - 0.3.0-5
- take care of new metadata_dir option

* Sun Aug 19 2012 Remi Collet <remi@fedoraproject.org> - 0.3.0-4
- rebuilt for new pear_datadir

* Tue Aug 14 2012 Remi Collet <remi@fedoraproject.org> - 0.3.0-3
- rebuilt for new pear_testdir

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 16 2012 Remi Collet <remi@fedoraproject.org> - 0.3.0-1
- Update to 0.3.0

* Wed Jan 25 2012 Remi Collet <remi@fedoraproject.org> - 0.2.0-8
- clean fedora template
- fix Provides for non standard channel (missing channel name)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 24 2011 Remi Collet <Fedora@FamilleCollet.com> 0.2.0-6
- keep installed doc in %%{pear_docdir}
- define date.timezone during build

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 20 2010 Remi Collet <Fedora@FamilleCollet.com> 0.2.0-4
- fix missing pear in dep name (#536756)
- replace %%define by %%global in template
- requires php-common (rather than php) when needed (not used yet)
- apply patch in %%prep

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jul 19 2009 Remi Collet <Fedora@FamilleCollet.com> 0.2.0-2
- change %%{pear-name}.xml to %%{name}.xml

* Sat Jun 27 2009 Tim Jackson <rpm@timj.co.uk> 0.2.0-1
- Update to 0.2.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 28 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1.2-6
- fix license tag

* Sat Sep 23 2006 Tim Jackson <rpm@timj.co.uk> 0.1.2-5
- Remove "PEAR:" from Summary in spec and template.spec

* Sun Sep 10 2006 Tim Jackson <rpm@timj.co.uk> 0.1.2-4
- Shorten summary
- Remove unnecessary dep on php
- Bundle LICENSE file
- Rename template specfile source to keep rpmlint happy

* Sat Sep 09 2006 Tim Jackson <rpm@timj.co.uk> 0.1.2-3
- Update to conform with latest conventions in bug #198706
- Update in-built spec (for generation of other package specs) to (nearly)
  conform with latest spec conventions

* Mon Jul 03 2006 Tim Jackson <rpm@timj.co.uk> 0.1.2-2
- BR php-pear 1.4.9; 1.4.8 is broken
- Update to conform to proposed Fedora PHP packaging standards

* Wed Jun 28 2006 Tim Jackson <rpm@timj.co.uk> 0.1.2-1
- Update to 0.1.2
- Update fedora-conventions patch to patch Packaging.xml
- Update fedora-conventions patch for peardir/tests -> peardir/test
- Backport upstream patch to make Fedora conventions work properly

* Fri Jun 9 2006 Tim Jackson <rpm@timj.co.uk> 0.1.1-2
- Add Epoch to php-pear BR

* Thu May 18 2006 Tim Jackson <rpm@timj.co.uk> 0.1.1-1
- Update to 0.1.1
- XML description now in datadir/pear/.pkgxml (see bug #190252)
- Stop buildroot path ending up in output files

* Wed Mar 15 2006 Tim Jackson <rpm@timj.co.uk> 0.1.0-2
- Own data/PEAR_Command_Packaging dir
- Remove empty doc line
- Remove empty build section
- Replace cp with install

* Tue Mar 14 2006 Tim Jackson <rpm@timj.co.uk> 0.1.0-1
- Initial RPM build

%global date    20020801
%global baserelease 23

Name:           xhtml1-dtds
Version:        1.0
Release:        %{date}.%{baserelease}%{?dist}
Summary:        XHTML 1.0 document type definitions

# W3C Software License for DTDs etc:
# http://www.w3.org/Consortium/Legal/IPR-FAQ-20000620#DTD
# https://www.w3.org/Consortium/Legal/copyright-software-19980720
License:        W3C-19980720
URL:            http://www.w3.org/TR/2002/REC-xhtml1-%{date}/
# Source0 generated with Source99, see comments in the script
Source0:        %{name}-%{date}.tar.xz
Source1:        %{name}.catalog.xml
Source99:       %{name}-prepare-tarball.sh
Patch0:         %{name}-sgml-catalog.patch
Patch1:         %{name}-sgml-dcl.patch

BuildArch:      noarch
BuildRequires:  libxml2 >= 2.4.8
Requires:       libxml2 >= 2.4.8
Requires:       xml-common
Requires:       sgml-common
Requires(post): /usr/bin/xmlcatalog
Requires(preun): /usr/bin/xmlcatalog

%description
This provides the DTDs of the Second Edition of XHTML 1.0, a reformulation
of HTML 4 as an XML 1.0 application, and three DTDs corresponding to the
ones defined by HTML 4. The semantics of the elements and their attributes
are defined in the W3C Recommendation for HTML 4. These semantics provide
the foundation for future extensibility of XHTML.


%prep
%setup -q -n xhtml1-20020801
%patch -P0 -p0
%patch -P1 -p1
cp -p %{SOURCE1} DTD/catalog.xml


%build


%install
rm -rf $RPM_BUILD_ROOT

# Note: documentation is not shipped; the W3C Documentation License is not an
# acceptable one per Fedora licensing guidelines.

mkdir -p $RPM_BUILD_ROOT%{_datadir}/xml/xhtml/1.0
cp -p DTD/* $RPM_BUILD_ROOT%{_datadir}/xml/xhtml/1.0

# XML catalog:

xpkg() {
  xmlcatalog --noout --add "$1" "$2" \
    file://%{_datadir}/xml/xhtml/1.0/catalog.xml \
    $RPM_BUILD_ROOT%{_sysconfdir}/xml/%{name}-%{version}-%{release}.xml
}

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/xml
xmlcatalog --noout --create \
  $RPM_BUILD_ROOT%{_sysconfdir}/xml/%{name}-%{version}-%{release}.xml
xpkg delegatePublic "-//W3C//DTD XHTML 1.0 "
xpkg delegatePublic "-//W3C//ENTITIES Latin 1 for XHTML"
xpkg delegatePublic "-//W3C//ENTITIES Special for XHTML"
xpkg delegatePublic "-//W3C//ENTITIES Symbols for XHTML"
for i in xhtml1 2002/REC-xhtml1-%{date} ; do
  xpkg delegateSystem http://www.w3.org/TR/$i/DTD/
  xpkg delegateURI http://www.w3.org/TR/$i/DTD/
done
ln -s %{name}-%{version}-%{release}.xml \
  $RPM_BUILD_ROOT%{_sysconfdir}/xml/%{name}.xml

# SGML catalog:

mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sgml
cd $RPM_BUILD_ROOT%{_sysconfdir}/sgml
touch %{name}-%{version}-%{release}.soc
ln -s %{name}-%{version}-%{release}.soc %{name}.soc
cd -



%post
cd %{_sysconfdir}/xml
[ -e catalog ] || /usr/bin/xmlcatalog --noout --create catalog
/usr/bin/xmlcatalog --noout --add \
    nextCatalog %{name}-%{version}-%{release}.xml "" catalog >/dev/null
cd - >/dev/null
/usr/bin/xmlcatalog --sgml --noout --add \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
    %{_datadir}/xml/xhtml/1.0/xhtml.soc >/dev/null
:

%preun
/usr/bin/xmlcatalog --noout --del \
    %{name}-%{version}-%{release}.xml \
    %{_sysconfdir}/xml/catalog >/dev/null
/usr/bin/xmlcatalog --sgml --noout --del \
    %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
    %{_datadir}/xml/xhtml/1.0/xhtml.soc >/dev/null
:


%files
%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
%{_sysconfdir}/sgml/%{name}.soc
%{_sysconfdir}/xml/%{name}*.xml
%{_datadir}/xml/xhtml/


%changelog
* Fri Jul 25 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 23 2023 Ondrej Sloup <osloup@redhat.com> - 1.0-20020801.19
- Update license tag to the SPDX format

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 23 2021 Florian Weimer <fweimer@redhat.com> - 1.0-20020801.14
- Add %%baserelease to help future mass rebuilds

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-20020801.13.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul  2 2015 Ville Skyttä <ville.skytta@iki.fi> - 1.0-20020801.13
- Add %%{?dist} to release (#1237194)
- Compress tarball with xz

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-20020801.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Ville Skyttä <ville.skytta at iki.fi> - 1.0-20020801.3
- Prune nondistributable content from source tarball.

* Fri Dec 12 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.0-20020801.2
- Drop no longer needed upgrade quirks.

* Thu Feb 28 2008 Ville Skyttä <ville.skytta at iki.fi> - 1.0-20020801.1
- Major spec file rewrite (#226559), most visible changes:
- Various XML cataloguing improvements.
- Register to SGML catalogs in addition to XML.
- Install to %%{_datadir}/xml per the FHS.
- Sync with Fedora packaging guidelines.
- Silence post-install scriptlet.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0-7.1.1
- rebuild

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Jun  2 2004 Daniel Veillard <veillard@redhat.com> 1.0-7
- add BuildRequires: libxml2, fixes 125030

* Mon Feb 23 2004 Tim Waugh <twaugh@redhat.com>
- Use ':' instead of '.' as separator for chown.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Oct 21 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- add %%clean specfile target

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec 13 2002 Daniel Veillard <veillard@redhat.com> 1.0-4
- Prepare for inclusion, Prereq xml-common, fix the uninstall
  for upgrades of the package

* Thu Dec 12 2002 Daniel Veillard <veillard@redhat.com> 1.0-1
- Creation, based on Tim Waugh docbook-dtd package

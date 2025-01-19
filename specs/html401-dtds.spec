# Note to self: like is with the HTML 2.0 and 3.2 DTDs, HTML 4.0 and 4.01
# have the same public id to their ENTITIES files.  They are not exactly the
# same in 4.0 and 4.01, but the changes are in comments only, so no need
# use a hardcoded system id.  Well, until something installs another, and
# incompatible set of entities using the same public id anyway...

%define date     19991224

Name:            html401-dtds
Version:         4.01
Release:         %{date}.12%{?dist}.26
Summary:         HTML 4.01 document type definitions

# W3C Software License for DTDs etc:
# http://www.w3.org/Consortium/Legal/IPR-FAQ-20000620#DTD
License:         W3C
URL:             http://www.w3.org/TR/1999/REC-html401-%{date}/
# Source0 generated with Source99, see comments in the script
Source0:         %{name}-%{date}.tar.bz2
Source99:        %{name}-prepare-tarball.sh
Patch0:          %{name}-catalog.patch

BuildArch:       noarch
Requires:        sgml-common
Requires(post):  /usr/bin/install-catalog
Requires(preun): /usr/bin/install-catalog

%description
This package provides the three HTML 4.01 DTDs (strict, frameset, and
transitional).  The DTDs are required for processing HTML 4.01
document instances using SGML tools such as OpenSP, OpenJade, or
SGMLSpm.


%prep
%setup -q -n %{name}
%patch -P 0 -p1


%build


%install

install -dm 0755 %{buildroot}%{_datadir}/sgml/html/4.01
install -pm 0644 *.dtd *.cat *.ent *.decl %{buildroot}%{_datadir}/sgml/html/4.01

install -dm 0755 %{buildroot}%{_sysconfdir}/sgml
touch %{buildroot}%{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
ln -s %{name}-%{version}-%{release}.soc %{buildroot}%{_sysconfdir}/sgml/%{name}.soc


%post
/usr/bin/install-catalog --add \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null

%preun
/usr/bin/install-catalog --remove \
  %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc \
  %{_datadir}/sgml/html/4.01/HTML4.cat >/dev/null || :


%files
%ghost %{_sysconfdir}/sgml/%{name}-%{version}-%{release}.soc
%{_sysconfdir}/sgml/%{name}.soc
%{_datadir}/sgml/html/


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 21 2023 David Cantrell <dcantrell@redhat.com> - 4.01-19991224.12.22
- Minor spec file cleanups
- Verified the License tag carries an SPDX expression

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.01-19991224.12.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.12.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.12.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.12.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.12.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.12.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.12.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec  1 2011 Ville Skyttä <ville.skytta@iki.fi> - 4.01-19991224.12
- Add system entries to catalog.
- Drop specfile constructs no longer needed with Fedora or EL6+.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.01-19991224.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Ville Skyttä <ville.skytta@iki.fi> - 4.01-19991224.8
- Prune nondistributable content from source tarball.

* Mon Aug 13 2007 Ville Skyttä <ville.skytta@iki.fi> - 4.01-19991224.5
- Don't use %%{dist}.

* Mon Aug 13 2007 Ville Skyttä <ville.skytta@iki.fi> - 4.01-19991224.4
- Don't ship the docs, the W3C Documentation License is not an acceptable
  one per Fedora licensing guidelines.
- License: W3C

* Fri Sep 15 2006 Ville Skyttä <ville.skytta@iki.fi> - 4.01-19991224.3
- Rebuild.

* Tue Jun 20 2006 Ville Skyttä <ville.skytta@iki.fi> - 4.01-19991224.2
- Require install-catalog at post-install and pre-uninstall time (#181068).

* Sun Jun 18 2006 Ville Skyttä <ville.skytta@iki.fi> - 4.01-19991224.1
- Include specification date in release field (#181068).
- Make doc symlinks relative.

* Sat Feb 25 2006 Ville Skyttä <ville.skytta@iki.fi> - 4.01-0.3
- Improve description (#181068).
- Fold specification into main package as %%doc (#181068).

* Wed Jun 15 2005 Ville Skyttä <ville.skytta@iki.fi> - 4.01-0.2
- Rebuild for FC4.

* Sat Apr 16 2005 Ville Skyttä <ville.skytta@iki.fi> - 4.01-0.1
- Use -maxdepth before other options to find(1).

* Tue Jun 22 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:4.01-0.fdr.6
- Move files below %%{_datadir}/sgml/html/4.01, remove alternatives.
- Add non-versioned %%{_sysconfdir}/sgml/%%{name}.soc symlink.

* Sun Jun 20 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:4.01-0.fdr.5
- Add additional public id "aliases" for entities to SGML catalog as defined
  in ISO-HTML Annex B, http://purl.org/NET/ISO+IEC.15445/Users-Guide.html#DTD

* Sat Jun 19 2004 Ville Skyttä <ville.skytta@iki.fi> - 0:4.01-0.fdr.4
- Add DTDDECLs to SGML catalog.

* Sun Dec  7 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:4.01-0.fdr.3
- Use alternatives to install preferred HTML DTD location.

* Sat Dec  6 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:4.01-0.fdr.2
- Install dir directly under %%{_datadir}/sgml.
- Spec cleanups.

* Tue Dec  2 2003 Ville Skyttä <ville.skytta@iki.fi> - 0:4.01-0.fdr.1
- First build.

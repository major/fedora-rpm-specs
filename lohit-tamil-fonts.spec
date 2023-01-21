%global fontname lohit-tamil
%global fontconf 65-0-%{fontname}.conf
%global metainfo io.pagure.lohit.tamil.font.metainfo

Name:           %{fontname}-fonts
Version:        2.91.3
Release:        15%{?dist}
Summary:        Free truetype font for Tamil language

License:        OFL
URL:            https://pagure.io/lohit/
Source0:        https://pagure.io/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires: python3-devel
BuildRequires: make
Requires:       fontpackages-filesystem

%description
This package provides a free Tamil truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version}
mv 66-lohit-tamil.conf 65-0-lohit-tamil.conf


%build
make ttf %{?_smp_mflags}

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{fontconf} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{metainfo}.xml \
       %{buildroot}%{_datadir}/metainfo/%{metainfo}.xml

%_font_pkg -f %{fontconf} *.ttf

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README test-tamil.txt
%{_datadir}/metainfo/%{metainfo}.xml

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 17 2019 Vishal Vijayraghavan <vvijayra AT redhat DOT com> - 2.91.3-7
- Added CI tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.91.3-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.3-1
- Upstream new release 2.91.3
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.91.2-1
- Added  BuildRequires: python3-devel.
- Resolves: #1423909 - FTBFS in rawhide
- Upstream new release, migrated from fedorahosted.org to pagure.io.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.91.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 03 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.1-1
- Upstream release 2.91.1
- Resolves #1170137 - Lohit Tamil 2.91.0 hinting issues

* Mon Oct 27 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-2
- Added metainfo for gnome-software

* Tue Oct 14 2014 Pravin Satpute <psatpute@redhat.com> - 2.91.0-1
- Resolves 1152203 :- Upstream release 2.91.0
- Rewritten all Open type tables with supporting taml and tml2 tags.
- Renamed all the glyphs by following AGL syntax.
- Open type tables are available in .fea file and this time it is compiled with AFDKO.
- Reusing glyphs by "COPY REFERENCE"
- Added GRID FITTING table and auto-hinting by fontforge.
- Tested with Harfbuzz NG and Uniscribe (W8).
- Auto test module available with test files.


* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolves bug 829143

* Wed Jun 06 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream release 2.5.1

* Thu May 10 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.0-3
- Resolves bug 820478

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 10 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-7
- fixed bug 673419, asterisk character and rupee sign

* Thu Sep 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-6
- improved fixe to bug 629824, punctuations marks

* Fri Sep 10 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-5
- fixed bug 629824, punctuations mark size

* Mon Aug 23 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-4
- fixed bug 621445, conf file

* Mon Apr 19 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.5-3
- fixed bug 578039, conf file

* Sun Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-2
- fixed bug 548686, license field

* Tue Nov 24 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release

* Wed Nov 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- resolved rh bug 536724

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- updated specs

* Mon Sep 21 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release of 2.4.4
- updated url for upstream tarball
- added Makefile in upstream tar ball

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball

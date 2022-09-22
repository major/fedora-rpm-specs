%global fontname lohit-gujarati
%global fontconf 65-0-%{fontname}.conf
%global metainfo io.pagure.lohit.gujarati.font.metainfo

Name:           %{fontname}-fonts
Version:        2.92.4
Release:        14%{?dist}
Summary:        Free Gujarati font
License:        OFL
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge >= 20080429
BuildRequires:  fontpackages-devel
BuildRequires: python3-devel
BuildRequires: make
Requires:       fontpackages-filesystem
Obsoletes: lohit-fonts-common < %{version}-%{release}

%description
This package provides a free Gujarati truetype/opentype font.


%prep
%setup -q -n %{fontname}-%{version} 
mv 66-%{fontname}.conf 65-0-lohit-gujarati.conf

%build
make ttf %{?_smp_mflags}

%install

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

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README test-gujarati.txt
%{_datadir}/metainfo/%{metainfo}.xml

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Vishal Vijayraghavan <vvijayra AT redhat DOT com> - 2.92.4-7
- Added CI tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.92.4-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.92.4-1
- Upstream new release 2.91.5
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.92.3-1
- Added  BuildRequires: python2-devel.
- Resolves: #1423903 - FTBFS in rawhide
- Migrated from Fedorahosted.org to pagure.io

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.92.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.92.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Oct 20 2014 Pravin Satpute <psatpute@redhat.com> - 2.92.2-3
- Added metainfo for gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.92.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 03 2014 Pravin Satpute <psatpute@redhat.com> - 2.92.2-1
- Minor release 2.92.2 from upstream.

* Thu Dec 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.92.1-1
- Minor release 2.92.1 from upstream.

* Mon Dec 09 2013 Pravin Satpute <psatpute@redhat.com> - 2.92.0-1
- Beta release 2.92.0 from upstream (lohit2 project)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Fri Apr 12 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.2-3
- Resolved #950516

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.2-1
- Upstream release 2.5.2

* Mon Nov 19 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-4
- Corrected license

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 25 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-2
- Resolved bug #803192

* Mon Apr 23 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1-1
- Upstream new release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 07 2011 Pravin Satpute <psatpute@redhat.com> - 2.5.0-1
- Upstream new release with relicensing to OFL

* Tue Mar 29 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.5-1
- upstream new release
- fixed bug 682667, added rupee symbol

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 04 2011 Pravin Satpute <psatpute@redhat.com> - 2.4.4-4
- fixed bug 673413, rupee sign

* Fri Apr 16 2010 Pravin Satpute <psatpute@redhat.com> - 2.4.4-3
- fixed bug 578031, conf file

* Sun Dec 13 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-2
- fixed bug 548686, license field

* Wed Oct 28 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.4-1
- upstream release wuth bugfix 529637
- update in upstream url

* Fri Sep 25 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-2
- updated specs

* Fri Sep 11 2009 Pravin Satpute <psatpute@redhat.com> - 2.4.3-1
- first release after lohit-fonts split in new tarball



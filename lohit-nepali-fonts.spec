%global fontname lohit-nepali
%global fontconf 65-0-%{fontname}.conf
%global metainfo io.pagure.lohit.nepali.font.metainfo

Name:           %{fontname}-fonts
Version:        2.94.2
Release:        14%{?dist}
Summary:        Free TrueType fonts for Nepali language

License:        OFL
URL:            https://pagure.io/lohit
Source0:        https://releases.pagure.org/lohit/%{fontname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: fontforge
BuildRequires:  fontpackages-devel
BuildRequires: python3-devel
BuildRequires: make
Requires:       fontpackages-filesystem

%description
This package provides a free TrueType font for Nepali language.


%prep
%setup -q -n %{fontname}-%{version} 

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

%doc ChangeLog COPYRIGHT OFL.txt AUTHORS README test-nepali.txt
%{_datadir}/metainfo/%{metainfo}.xml

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 2019 Vishal Vijayraghavan <vvijayra AT redhat DOT com> - 2.94.2-7
- Added CI tests

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.94.2-4
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 30 2017 Pravin Satpute <psatpute@redhat.com> - 2.94.2-1
- Upstream new release 2.94.2
- Update metainfo file with latest specifications
- Changed location of metainfo to /usr/share/metainfo

* Tue Mar 14 2017 Pravin Satpute <psatpute@redhat.com> - 2.94.1-1
- Added  BuildRequires: python3-devel.
- Resolves: #1423907 - FTBFS in rawhide.
- Upstream new release, migrated from fedorahosted.org to pagure.io.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.94.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.94.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Oct 28 2014 Pravin Satpute <psatpute@redhat.com> - 2.94.0-3
- Added metainfo for gnome-software

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.94.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Pravin Satpute <psatpute@redhat.com> - 2.94.0-1
- Upstream release 2.94.0
- Positioning lookup clean-up.
- Improved grid fitting(GASP) table.
- Renamed anchors to DVAnchor.
- Using glyph reference (copy reference) instead of whole glyph points.
- Auto test integrated with Makefile ($make test).
- Resolved #32: "सर्व्हिस does not render correctly"
- Resolved #33: "improper rendering for word : "मञ्यांच्या""

* Mon Dec 30 2013 Pravin Satpute <psatpute@redhat.com> - 2.93.0-1
- Upstream release 2.93.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jan 31 2013 Pravin Satpute <psatpute@redhat.com> - 2.5.3-1
- Upstream release 2.5.3

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr 12 2012 Pravin Satpute <psatpute@redhat.com> - 2.5.1.1-1
- first release after lohit-devanagari split into nepali specific shapes

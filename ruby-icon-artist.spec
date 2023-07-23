Name:           ruby-icon-artist
Version:        0.1.92
Release:        26%{?dist}
Summary:        Supporting libraries for icon artists


License:        LGPLv2+
URL:            https://fedorahosted.org/echo-icon-theme/
Source0:        https://fedorahosted.org/released/echo-icon-theme/icon-artist-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  ruby
BuildRequires:  ruby-devel
Requires:       ruby(release)
Requires:       rubygem(git)
Requires:       inkscape
Requires:       icon-naming-utils
Provides:       ruby(icon-artist) = %{version}

%description
Supporting libraries for icon artist scripts. It contains support for
generating new icons from templates, exporting PNGs and SVGs from one canvas
SVG, creating new icon theme and managing icon theme buildsys.

%prep
%setup -q -n icon-artist-%{version}


%build
export CFLAGS="$RPM_OPT_FLAGS"
sed -i 's|CONFIG|RbConfig::CONFIG|' install.rb
sed -i 's|CONFIG\["sitelibdir"\]|CONFIG["vendorlibdir"]|' install.rb
sed -i '/include Config/d' install.rb

%install
rm -rf %{buildroot}
DESTDIR=%{buildroot} ./install.rb

%check


%files
%doc doc/*
%{ruby_vendorlibdir}/*
%{_datadir}/icon-artist


%changelog
* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.92-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.92-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 19 2015 Vít Ondruch <vondruch@redhat.com> - 0.1.92-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.92-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.92-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 21 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.1.92-7
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.92-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.92-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 06 2012 Martin Sourada <martin.sourada@gmail.com> - 0.1.92-4
- rebuilt

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.92-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.92-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Dec 05 2009 Martin Sourada <mso@fedoraproject.org> - 0.1.92-1
- New upstream release
- Workaround broken remote branches name detection by rubygem(git)
- Better icon name detection

* Thu Aug 13 2009 Martin Sourada <mso@fedoraproject.org> - 0.1.91-1
- New upstream release
- Patch upstreamed
- Add icon-naming-utils dependency

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 13 2009 Martin Sourada <mso@fedoraproject.org> - 0.1.90-2
- Backport fix for correct checking of icon name from git

* Thu Feb 05 2009 Martin Sourada <mso@fedoraproject.org> - 0.1.90-1
- Initial rpm packaging

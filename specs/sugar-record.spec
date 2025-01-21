Name:           sugar-record
Version:        201
Release:        11%{?dist}
Summary:        Recording tool for Sugar

License:        MIT
URL:            http://wiki.laptop.org/go/Record
Source0:        http://download.sugarlabs.org/sources/honey/Record/Record-%{version}.tar.bz2

BuildArch:      noarch
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:	gstreamer1-devel
BuildRequires:	gstreamer1-plugins-base-devel
BuildRequires:  sugar-toolkit-gtk3-devel
BuildRequires:  python3-devel

Requires:       sugar
Requires:       sugar-toolkit-gtk3
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good

%description
Record is the basic rich-media capture activity for the laptop. It 
lets you capture still images, video, and/or audio. It has a simple 
interface and works in both laptop and ebook mode. An interface for 
sharing pictures among multi XOs during a picture-taking session is
a hallmark of the Record activity

%prep
%autosetup -n Record-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build

%install
python3 ./setup.py install --prefix=%{buildroot}/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}/%{sugaractivitydir}/Record.activity/

%find_lang org.laptop.RecordActivity

%files -f org.laptop.RecordActivity.lang
%license COPYING
%doc NEWS
%{sugaractivitydir}/Record.activity/

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 201-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 201-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 201-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 201-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 201-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 201-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 201-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 201-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 201-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Ibiam Chihurumnaya <ibiamchihurumnaya@gmail.com> - 201-1
- v201

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 200.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 200.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 200.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 200.2-1
- Update to 200.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 200-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Peter Robinson <pbrobinson@fedoraproject.org> 200-1
- Update to 200, gtk3 and gstreamer1 support

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 102-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 102-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 102-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 102-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 102-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 25 2015 Peter Robinson <pbrobinson@fedoraproject.org> 102-1
- Update to 102

* Tue Jun 30 2015 Peter Robinson <pbrobinson@fedoraproject.org> 100-1
- Update to 100

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 99-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Peter Robinson <pbrobinson@fedoraproject.org> 99-5
- Add Requires sugar-toolkit

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 99-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 17 2013 Peter Robinson <pbrobinson@fedoraproject.org> 99-3
- Add gstreamer-python runtime dependency

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun  1 2013 Peter Robinson <pbrobinson@fedoraproject.org> 98-1
- Update to 99

* Mon May 20 2013 Peter Robinson <pbrobinson@fedoraproject.org> 99-1
- Update to 98

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Peter Robinson <pbrobinson@fedoraproject.org> 97-1
- New upstream 97 release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 96-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May  8 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 96-1
- New upstream 96 release

* Mon Mar 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 95-1
- New upstream 95 release

* Sat Mar 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 94-1
- New upstream 94 release

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 93-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Jul 23 2011 Peter Robinson <pbrobinson@gmail.com> - 93-1
- New upstream 93 release

* Mon Jun 13 2011 Peter Robinson <pbrobinson@gmail.com> - 92-1
- New upstream 92 release

* Sat May 21 2011 Peter Robinson <pbrobinson@gmail.com> - 91-1
- New upstream 91 release

* Sat May  7 2011 Peter Robinson <pbrobinson@gmail.com> - 90-1
- New upstream 90 release

* Mon Apr  4 2011 Peter Robinson <pbrobinson@gmail.com> - 87-1
- New upstream 87 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 66-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 66-4
- recompiling .py files against Python 2.7 (rhbz#623385)

* Tue Apr 20 2010 Peter Robinson <pbrobinson@gmail.com> - 66-3
- fix launch script

* Thu Apr  8 2010 Peter Robinson <pbrobinson@gmail.com> - 66-2
- fix build

* Thu Apr  8 2010 Peter Robinson <pbrobinson@gmail.com> - 66-1
- New upstream 66 release

* Sat Apr  3 2010 Peter Robinson <pbrobinson@gmail.com> - 65-1
- New upstream 65 release

* Sun Feb 21 2010 Sebastian Dziallas <sebastian@when.com> - 64-6
- Enable use of system library

* Thu Feb 18 2010 Sebastian Dziallas <sebastian@when.com> - 64-5
- Enable binary builds again

* Mon Dec 14 2009 Peter Robinson <pbrobinson@gmail.com> - 64-4
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 539221

* Sun Aug 16 2009 Fabian Affolter <fabian@bernewireless.net> - 64-3
- Readded noarch
- Removed duplicated docs 
- Removed pre-compiled parts

* Tue Aug 04 2009 Fabian Affolter <fabian@bernewireless.net> - 64-2
- Added gstreamer as a requirement and removed the embedded one
- Added debug_package

* Sat Jun 27 2009 Fabian Affolter <fabian@bernewireless.net> - 64-1
- Removed noarch
- Updated to new upstream version 64

* Sat Apr 25 2009 Fabian Affolter <fabian@bernewireless.net> - 62-1
- Added URL for source tarball
- Removed VCS checkout stuff
- Updated to new upstream version 62

* Sun Dec 14 2008 Fabian Affolter <fabian@bernewireless.net> - 60-1
- Updated to new upstream version 60

* Sun Oct 19 2008 Fabian Affolter <fabian@bernewireless.net> - 59-1
- Initial package for Fedora

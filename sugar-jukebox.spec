Name:		sugar-jukebox
Version:	36
Release:	7%{?dist}
Summary:	Media player activity for Sugar

License:	GPLv2+
URL:		http://wiki.laptop.org/go/Jukebox
Source0:	http://download.sugarlabs.org/sources/sucrose/fructose/Jukebox/Jukebox-%{version}.tar.bz2

BuildRequires:	gettext
BuildRequires:	gobject-introspection-devel
BuildRequires:	gstreamer1-devel
BuildRequires:	gstreamer1-plugins-base-devel
BuildRequires:	python3-devel
BuildRequires:	sugar-toolkit-gtk3-devel
BuildArch:	noarch
Requires:	sugar

%description
The jukebox activity is an audio/video player that will play
different kind of files bases on the installed gstreamer plugins.


%prep
%autosetup -n Jukebox-%{version}

sed -i 's/python/python3/' setup.py

%build
python3 ./setup.py build


%install
python3 ./setup.py install --prefix=$RPM_BUILD_ROOT/%{_prefix}
rm %{buildroot}%{_prefix}/share/applications/*.desktop || true

# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_3
%py_byte_compile %{python3} %{buildroot}%{_datadir}/{sugaractivitydir}/Jukebox.activity/

%find_lang org.laptop.sugar.Jukebox


%files -f org.laptop.sugar.Jukebox.lang
%license COPYING
%doc AUTHORS NEWS TODO
%{sugaractivitydir}/Jukebox.activity/


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 36-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 5 2020 Chihurumnaya Ibiam <ibiamchihurumnaya@gmail.com> 36-1
- New 36 release

* Thu Jan 30 2020 Peter Robinson <pbrobinson@fedoraproject.org> 35-1
- New 35 release

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 30 2019 Peter Robinson <pbrobinson@fedoraproject.org> 34-3
- Drop unneed python-unversioned-command

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 34-1
- New 34 release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 33-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 08 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 33-1
- New 33 release

* Sat Apr 29 2017 Kalpa Welivitigoda <callkalpa@gmail.com> - 32-7
- Fix FTBFS issue

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 32-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 32-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 04 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 32-1
- New 32 release

* Mon May 27 2013 Kalpa Welivitigoda <callkalpa@gmail.com> - 31-1
- New 31 release

* Tue Apr  9 2013 Peter Robinson <pbrobinson@fedoraproject.org> 30-1
- New 30 release

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Nov  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> 29-1
- New 29 release

* Sat Oct 13 2012 Peter Robinson <pbrobinson@fedoraproject.org> 28-1
- New 28 release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct  2 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 23-1
- New 23 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@fedoraproject.org> - 20-1
- New 20 release

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 19-2
- recompiling .py files against Python 2.7 (rhbz#623376)

* Mon May 24 2010 Sebastian Dziallas <sebastian@when.com> - 19-1
- New upstream release

* Wed Feb 17 2010 Sebastian Dziallas <sebastian@when.com> - 18-1
- New upstream release

* Wed Dec 23 2009 Sebastian Dziallas <sebastian@when.com> - 13-1
- New upstream release

* Mon Dec 14 2009 Peter Robinson <pbrobinson@fedoraproject.org> - 11-3
- Add buildreq gettext to fix build issues on F-12/rawhide - fixes # 538871

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 16 2009 Sebastian Dziallas <sebastian@when.com> - 11-1
- update to version 11

* Mon Apr 06 2009 Sebastian Dziallas <sebastian@when.com> - 8-1
- update to version 8

* Wed Mar 04 2009 Sebastian Dziallas <sebastian@when.com> - 7-1
- update to version 7

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec 18 2008 Sebastian Dziallas <sebastian@when.com> - 6-1
- update to version 6

* Mon Nov 24 2008 Sebastian Dziallas <sebastian@when.com> - 5-3
- use git checkout script

* Wed Nov 19 2008 Sebastian Dziallas <sebastian@when.com> - 5-2
- modify build section and source path

* Thu Nov 13 2008 Sebastian Dziallas <sebastian@when.com> - 5-1
- update to version 5

* Tue Nov 11 2008 Sebastian Dziallas <sebastian@when.com> - 4-1
- update to version 4

* Wed Oct 22 2008 Sebastian Dziallas <sebastian@when.com> - 3-1
- Initial Packaging

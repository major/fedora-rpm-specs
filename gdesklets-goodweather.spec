Name:           gdesklets-goodweather
Version:        0.31
Release:        18%{?dist}
Summary:        Themeable weather and condition display for gdesklet

License:        GPL+
URL:            http://www.gdesklets.de
Source0:        http://www.gdesklets.info/archive/GoodWeather_08-0.31.tar.gz
Patch1: 	weather.patch
Patch2:		__init__.py.patch
# fix handling of current day 
Patch3:		goodweather-xml.patch

BuildArch:      noarch

BuildRequires:  python
Requires:       gdesklets

%description

Themeable weather and condition display for gdesklets. Displays the current
conditions along with a 5 day forcast

%prep
%setup -q -n GoodWeather-08
#Switch to GoodWeather directory
cd Sensors/GoodWeather
%patch1 -p0 -b .weather
%patch2 -p0 -b .__init__.py
%patch3 -p0 -b .goodweather-xml

%build


%install
rm -rf $RPM_BUILD_ROOT
#need to install the sensor first
#%{__python} Install_GoodWeather_Sensor.bin --nomsg $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors/ > /dev/null
#rm -rf $RPM_BUILD_ROOT%{_datadir}/gdesklets/Sensors/GoodWeather/weather.com/small_icons/.pics

#install the display now
rm -f Displays/GoodWeather/Install_GoodWeather_Sensor.bin
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/GoodWeather/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Sensors/GoodWeather/
#install -p -m644 -D Displays/GoodWeather/GoodWeather.display $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/GoodWeather/GoodWeather.display
#install -p -m644 -D Displays/GoodWeather/gfx/bg-bar.png $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/GoodWeather/gfx/bg-bar.png
#install -p -m644 -D Displays/GoodWeather/gfx/bg-left.png $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/GoodWeather/gfx/bg-left.png
#install -p -m644 -D Displays/GoodWeather/gfx/bg-right.png $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/GoodWeather/gfx/bg-right.png
#install -p -m644 -D Displays/GoodWeather/gfx/bg-weather.png $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/GoodWeather/gfx/bg-weather.png
cp -pr Sensors/GoodWeather/* $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Sensors/GoodWeather/.
cp -rp Displays/GoodWeather/* $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Displays/GoodWeather/.
rm -rf $RPM_BUILD_ROOT/%{_datadir}/gdesklets/Sensors/GoodWeather/{__init__.py.__init__.py*,*goodweather-xml,weather.py.weather,weather.com/small_icons/.pics}

%files
%doc README INSTALL
%{_datadir}/gdesklets/Displays/GoodWeather/
%{_datadir}/gdesklets/Sensors/GoodWeather/


%changelog
* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org>
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 28 2014 Luya Tshimbalanga <luya@fedoraproject.org> - 0.31-16
- Restored some deleted files (rhbz #1069113)

* Tue Feb 25 2014 Luya Tshimbalanga <luya@fedoraproject.org> - 0.31-15
- Removal of unnecessary files (rhbz #1069113)

* Sat Feb 22 2014 Luya Tshimbalanga <luya@fedoraproject.org> - 0.31-13
- Patch for handling xml tag for current day (rhbz #1057375)
- Few spec clean up

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 14 2011 Luya Tshimbalanga <luya@fedoraproject.org> - 0.31-8
- Removal of some odd py files and .weather

* Mon Nov 07 2011 Luya Tshimbalanga <luya@fedoraproject.org> - 0.31-7
- Patch for load data failure thanks to Corinna Vinschen (rhbz #674291)
- Updated upstream url
 
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 0.31-5
- recompiling .py files against Python 2.7 (rhbz#623305)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.31-2
- Rebuild for Python 2.6

* Sat Aug 2 2008 Tyler Owen <tyler.l.owen@gmail.com> - 0.31-1
- Fixed license tag to specify a version
- Upgrade to 08-0.31

* Thu Nov 15 2007 Tyler Owen <tyler.l.owen@gmail.com> - 0.3-3
- Updated License to match new Fedora scheme
- Updated files section

* Sat Jul 07 2007 Tyler Owen <tyler.l.owen@gmail.com> - 0.3-2
- Added Python to Requires
- Added -p option to install to preserve timestamps
- Fixed missing directory ownership issues

* Sun Jun 24 2007 Tyler Owen <tyler.l.owen@gmail.com> - 0.3-1
- Initial Packaging for Fedora

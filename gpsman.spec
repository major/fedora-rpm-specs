Name:           gpsman
Version:        6.4.1
Release:        23%{?dist}
Summary:        A GPS manager

License:        GPLv2+
URL:            http://www.ncc.up.pt/gpsman/wGPSMan_4.html
Source0:        http://www.ncc.up.pt/gpsman/gpsmanhtml/gpsman-%{version}.tgz
#man files for the utils, stolen from debian
Source1:        mou2gmn.1
Source2:        mb2gmn.1
Source3:        gpsman.desktop
Source4:        gpsman-icon.png
#fix location of files in executable
Patch0:         gpsman-sourcedir.patch

BuildArch:      noarch

BuildRequires:  desktop-file-utils
Requires:       tk
Requires:       tkimg

%description
GPS Manager (GPSMan) is a graphical manager of GPS data that makes possible
the preparation, inspection and edition of GPS data in a friendly environment.

GPSMan supports communication and real-time logging with both Garmin and
Lowrance receivers and accepts real-time logging information in NMEA 0183
from any GPS receiver.

%prep
%setup -q
%patch0 -p1

#make sure all files are utf-8
recode()
{
  iconv -f "$2" -t utf-8 < "$1" > "${1}_"
  mv -f "${1}_" "$1"
}
for f in `find manual/html -name *.html`
 do recode $f iso-8859-15
done
recode manual/html/info/WPs.txt iso-8859-15


%build
#no build needed


%install
rm -rf $RPM_BUILD_ROOT
#manual install
install -D -m 0755 gpsman.tcl $RPM_BUILD_ROOT%{_bindir}/gpsman
install -Dd gmsrc $RPM_BUILD_ROOT%{_datadir}/gpsman
for f in `find gmsrc/ -type f -maxdepth 1`
 do install -D -m 0644 $f $RPM_BUILD_ROOT%{_datadir}/gpsman/`echo $f | cut -d '/' -f2`
done
install -Dd gmsrc/gmicons $RPM_BUILD_ROOT%{_datadir}/gpsman/gmicons
for f in `find gmsrc/gmicons/ -type f -name *.gif`
 do install -D -m 0644 $f $RPM_BUILD_ROOT%{_datadir}/gpsman/gmicons/`echo $f | cut -d '/' -f3`
done
install -D -m 0644 man/man1/gpsman.1 $RPM_BUILD_ROOT%{_mandir}/man1/gpsman.1
#utils
install -D -m 0755 util/mb2gmn.tcl $RPM_BUILD_ROOT%{_bindir}/mb2gmn
install -D -m 0755 util/mou2gmn.tcl $RPM_BUILD_ROOT%{_bindir}/mou2gmn
#man files
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/mb2gmn.1
install -D -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man1/mou2gmn.1
# desktop file and icon
mkdir -p   ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
install -m 644 %{SOURCE4} \
  ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/
desktop-file-install --vendor="" \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
  %{SOURCE3}


%files
%doc LICENSE
%doc manual/GPSMandoc.pdf manual/html
%{_bindir}/*
%{_datadir}/gpsman
%{_mandir}/man?/*
%attr(0644,root,root) %{_datadir}/applications/%{name}.desktop
%attr(0644,root,root) %{_datadir}/pixmaps/*


%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 07 2010 Lucian Langa <cooly@gnome.eu.org> - 6.4.1-1
- misc cleanups
- new upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 08 2008 Sindre Pedersen Bjørdal <sindrepb@fedoraproject.org> - 6.4-1
- New upstream release

* Thu Aug 14 2008 Lucian Langa <cooly@gnome.eu.org> - 6.3.2-4
- fix reuirements
- misc cleanups

* Tue Feb 26 2008 Steve Conklin <sconklin at redhat dot com> - 6.3.2-3
- rpmlint clean up

* Sun Dec 09 2007 Robert 'Bob' Jensen <bob@bobjensen.com> - 6.3.2-2
- rpmlint clean up

* Sun Dec 09 2007 Sindre Pedersen Bjørdal - 6.3.2-1
- Initial build

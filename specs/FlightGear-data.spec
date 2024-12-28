Name:           FlightGear-data
Summary:        FlightGear base scenery and data files
Version:        2020.3.19
Release:        7%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
Source0:        https://sourceforge.net/projects/flightgear/files/release-2020.3/FlightGear-%{version}-data.txz
URL:            http://www.flightgear.org/
BuildArch:      noarch
Obsoletes:      fgfs-base < 1.9.0-1

# Fix for rhbz#2331176
BuildRequires:  ImageMagick

%description
This package contains the base scenery for FlightGear and must be
installed

%prep
%setup -q -n fgdata

%build

%install
install -d $RPM_BUILD_ROOT%{_datadir}/flightgear
cp -alf *  $RPM_BUILD_ROOT%{_datadir}/flightgear

# cleanup temporary files and fix permissions
find $RPM_BUILD_ROOT/%{_datadir}/flightgear -name '*#*' -exec rm {} \;
find $RPM_BUILD_ROOT/%{_datadir}/flightgear -type f -exec chmod 644 {} \;

# fix wrong eol encoding on some doc files
for f in Docs/FGShortRef.css Docs/README.kln89.html Docs/FGShortRef.html \
        Docs/README.submodels Docs/README.yasim Docs/README.xmlparticles
do
        sed -i 's/\r//' $RPM_BUILD_ROOT/%{_datadir}/flightgear/$f
done

# remove unwanted data
for d in Aircraft/c172/Panels/Textures/.xvpics \
        Textures/Runway/.xvpics .gitignore
do
        rm -rf $RPM_BUILD_ROOT/%{_datadir}/flightgear/$d
done

# fix files not in utf-8
for f in Thanks Docs/README.xmlparticles Aircraft/c172p/Models/Immat/immat.xml
do
        path=$RPM_BUILD_ROOT/%{_datadir}/flightgear/$f
        iconv -f iso-8859-1 -t utf-8 -o ${path}.utf8 $path
        mv -f ${path}.utf8 ${path}
done

# put documentation and license in the proper location
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
for f in COPYING AUTHORS NEWS README Thanks Docs
do
        mv $RPM_BUILD_ROOT/%{_datadir}/flightgear/$f \
                $RPM_BUILD_ROOT/%{_docdir}/%{name}
done

# Fix for rhbz#2331176
file=$RPM_BUILD_ROOT/%{_datadir}/flightgear/Aircraft/Generic/Effects/null_bumpspec.png
magick $file -resize 2 $file

%files
%doc %{_docdir}/%{name}
%{_datadir}/flightgear

%changelog
* Thu Dec 26 2024 Fabrice Bellet <fabrice@bellet.info> - 2020.3.19-7
- Fix for rhbz#2331176

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2020.3.19-6
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 21 2023 Fabrice Bellet <fabrice@bellet.info> - 2020.3.19-1
- new upstream release

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 21 2023 Fabrice Bellet <fabrice@bellet.info> - 2020.3.18-1
- new upstream release

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 26 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.17-1
- new upstream release

* Thu Oct 20 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.16-1
- new upstream release

* Mon Oct 03 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.14-1
- new upstream release

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Mar 31 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.13-1
- new upstream release

* Fri Feb 04 2022 Fabrice Bellet <fabrice@bellet.info> - 2020.3.12-1
- new upstream release

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 01 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.11-1
- new upstream release

* Mon Jul 26 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.10-1
- new upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 16 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.9-1
- new upstream release

* Tue Mar 30 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.8-1
- new upstream release

* Mon Mar 22 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.7-1
- new upstream release

* Mon Jan 25 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.6-1
- new upstream release

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Fabrice Bellet <fabrice@bellet.info> - 2020.3.5-1
- new upstream release

* Tue Dec 01 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.4-1
- new upstream release

* Sun Nov 29 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.3-1
- new upstream release

* Mon Nov 09 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.2-1
- new upstream release

* Thu Oct 29 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.3.1-1
- new upstream release

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.3-1
- new upstream release

* Sat May 23 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.2-1
- new upstream release

* Tue May 12 2020 Fabrice Bellet <fabrice@bellet.info> - 2020.1.1-1
- new upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2019.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jul 29 2019 Fabrice Bellet <fabrice@bellet.info> - 2019.1.1-1
- new upstream release

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fabrice Bellet <fabrice@bellet.info> - 2018.3.2-1
- new upstream release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Dec 07 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.3.1-1
- new upstream release

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2018.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.2.2-1
- new upstream release

* Thu May 24 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.2.1-1
- new upstream release

* Sun Apr 08 2018 Fabrice Bellet <fabrice@bellet.info> - 2018.1.1-1
- new upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.3.1-1
- new upstream release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2017.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Tom Callaway <spot@fedoraproject.org> - 2017.2.1-1
- update to 2017.2.1

* Wed Apr 05 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.3-1
- new upstream release

* Fri Mar 03 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.2-1
- new upstream release

* Thu Feb 23 2017 Fabrice Bellet <fabrice@bellet.info> - 2017.1.1-1
- new upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2016.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 06 2017 Fabrice Bellet <fabrice@bellet.info> - 2016.4.4-1
- new upstream release

* Tue Dec 06 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.3-1
- new upstream release

* Fri Nov 25 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.2-1
- new upstream release

* Mon Nov 21 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.4.1-1
- new upsream release

* Wed Sep 14 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.3.1-1
- new upstream release

* Thu May 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.2.1-1
- new upstream release

* Mon May  9 2016 Tom Callaway <spot@fedoraproject.org> - 2016.1.2-1
- update to 2016.1.2

* Fri Feb 19 2016 Fabrice Bellet <fabrice@bellet.info> - 2016.1.1-1
- new upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2.gitd5d5508
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 Fabrice Bellet <fabrice@bellet.info> - 3.7.0-1.gitd5d5508
- Update to 3.7.0 + fixes from git

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 19 2015 Fabrice Bellet <fabrice@bellet.info> - 3.4.0-2
- Remove FG_SCENERY from Nasal allowed directories
- Modernize spec

* Tue Feb 17 2015 Fabrice Bellet <fabrice@bellet.info> - 3.4.0-1
- new upstream release

* Fri Oct 17 2014 Fabrice Bellet <fabrice@bellet.info> - 3.2.0-1
- new upstream release

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 01 2014 Fabrice Bellet <fabrice@bellet.info> - 3.0.0-2
- fix the package owning the data directory

* Fri Feb 21 2014 Fabrice Bellet <fabrice@bellet.info> - 3.0.0-1
- new upstream release

* Sun Sep 22 2013 Fabrice Bellet <fabrice@bellet.info> - 2.12.0-1
- new upstream release
- update path for documentation

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 18 2013 Fabrice Bellet <fabrice@bellet.info> - 2.10.0-1
- new upstream release

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 11 2012 Fabrice Bellet <fabrice@bellet.info> 2.8.0-1
- new upstream release

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Feb 19 2012 Fabrice Bellet <fabrice@bellet.info> 2.6.0-1
- new upstream release

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Sep 05 2011 Fabrice Bellet <fabrice@bellet.info> 2.4.0-1
- new upstream release
- the data directory name is now in lowercase

* Wed Apr 20 2011 Tom Callaway <spot@fedoraproject.org> - 2.0.0-3
- fix utf8 encoding on Aircraft/c172p/Models/Immat/immat.xml (default plane)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 26 2010 Fabrice Bellet <fabrice@bellet.info> 2.0.0-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 06 2009 Fabrice Bellet <fabrice@bellet.info> 1.9.0-1
- new upstream release

* Mon Jan  7 2008 Fabrice Bellet <fabrice@bellet.info> 1.0.0-1
- new upstream release

* Sun Sep 23 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.11-0.2.pre1
- update License tag

* Wed Jun 27 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.11-0.1.pre1
- new upstream (pre-)release

* Sat Apr  7 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-3
- use sed instead of dos2unix to correct end-of-line encoding

* Mon Apr  2 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-2
- Move documentation and license to a better place and mark it as %%doc
- Fix wrong end-of-line encoding in some doc files

* Tue Mar 20 2007 Fabrice Bellet <fabrice@bellet.info> 0.9.10-1
- Initial packaging

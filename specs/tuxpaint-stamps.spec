Name:           tuxpaint-stamps
Version:        2020.05.29
Release:        13%{?dist}
Summary:        Extra stamp files for tuxpaint
License:        GPL-1.0-or-later AND GFDL-1.1-or-later AND CC-BY-SA-2.0 AND CC-BY-SA-2.5 AND CC-BY-SA-3.0 AND LicenseRef-Fedora-Public-Domain
URL:            http://www.tuxpaint.org/
Source0:        https://downloads.sourceforge.net/tuxpaint/%{name}/2020-05-29/%{name}-%{version}.tar.gz
Patch0:         python3.patch
Patch1:         indent.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  python3-devel
Requires:       tuxpaint

%description
This package is a collection of 'rubber stamps' for Tux Paint's "Stamp" tool.

%prep
%setup -q
# note need to update this if version is something other than a date
sed -i "s/VER_DATE=\`date +\"%%Y.%%m.%%d\"\`/VER_DATE=\`date +%{version}\`/" Makefile
%patch -P 0 -p0
%patch -P 1 -p0
%py3_shebang_fix .

%build
(cd po && sh ./createpo.sh)
(cd po && ./createtxt.sh)

%install
install -d $RPM_BUILD_ROOT%{_datadir}/tuxpaint/stamps
make install-all PREFIX=$RPM_BUILD_ROOT%{_prefix}
# Register as an add-on to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!--
Copyright 2016 Colin B. Macdonald

Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.
-->
<!--
BugReportURL: https://sourceforge.net/p/tuxpaint/feature-requests/172/
SentUpstream: 2016-06-02
-->
<component type="addon">
  <id>tuxpaint-stamps</id>
  <extends>tuxpaint.desktop</extends>
  <name>Tuxpaint Stamps</name>
  <summary>"Rubber stamp" images of animals, plants, vehicles, and many more</summary>
  <url type="homepage">http://tuxpaint.org/</url>
  <metadata_license>FSFAP</metadata_license>
</component>
EOF

pushd po
for file in *.po ; do
    loc=`echo $file | sed -e 's/tuxpaint-stamps-\(.*\).po/\1/'`
    mkdir -p $RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES
    msgfmt -o $RPM_BUILD_ROOT%{_datadir}/locale/$loc/LC_MESSAGES/tuxpaint-stamps.mo $file
done
popd

# License is bad on this file, Creative Commons Sampling Plus 1.0 is non-free.
rm -rf $RPM_BUILD_ROOT%{_datadir}/tuxpaint/stamps/vehicles/emergency/firetruck.ogg

%find_lang %{name}


%files -f %{name}.lang
%doc docs/*.txt
%lang(el) %doc docs/el
%lang(es) %doc docs/es
%lang(fr) %doc docs/fr
%lang(hu) %doc docs/hu
%defattr(0644,root,root,0755)
%{_datadir}/tuxpaint/stamps/*
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Gwyn Ciesla <gwync@protonmail.com> - 2020.05.29-10
- Drop dependency on 2to3

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 2020.05.29-8
- Convert to SPDX license.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.05.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 31 2020 Gwyn Ciesla <gwync@protonmail.com> - 2020.05.29-1
- 2020.05.29

* Wed Feb 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 2019.09.01-1
- 2018.09.01

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2014.08.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2014.08.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2014.08.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Colin B. Macdonald <cbm@m.fsf.org> - 2014.08.23-5
- Replace unversioned python calls with python2 (#1601256)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2014.08.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2014.08.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 09 2017 Colin B. Macdonald <cbm@m.fsf.org> - 2014.08.23-2
- Fix versioning patch in Makefile and Source0 URL

* Tue Nov 07 2017 Gwyn Ciesla <limburgher@gmail.com> - 2014.08.23-1
- 2014.08.23

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2009.06.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2009.06.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jun 03 2016 Colin B. Macdonald <cbm@m.fsf.org> - 2009.06.28-10
- Add a .metainfo.xml file for GUI package managers

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2009.06.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.06.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.06.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.06.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.06.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.06.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.06.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.06.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Jon Ciesla <limb@jcomserv.net> - 2009.06.28-1
- New upstream, fix FTBFS BZ 631086.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008.06.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2008.06.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 2008.06.30-1
- fix license tag
- update to 2008.06.30.

* Sat Jul 07 2007 Steven Pritchard <steve@kspei.com> 2007.07.01-1
- Update to 2007.07.01.

* Tue Oct 24 2006 Steven Pritchard <steve@kspei.com> 2006.10.21-1
- Update to 2006.10.21.
- Remove a little extra whitespace in the spec.
- Just include docs/*.txt.
- Use version macro in Source0 URL.
- Use "install-all" target.

* Mon Aug 28 2006 Wart <wart at kobold dot org> 2005.11.25-1
- Initial Fedora Extras package

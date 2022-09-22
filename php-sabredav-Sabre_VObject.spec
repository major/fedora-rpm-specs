%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}
%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%global gh_commit   c3ebe643fd1037b656ebcc149e3fd3d38938fe58
%global gh_short    %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner    fruux
%global gh_project  sabre-vobject
%global pear_name   Sabre_VObject
%global channelname pear.sabredav.org
%global reldate     2015-01-21

Name:           php-sabredav-Sabre_VObject
Version:        2.1.7
Release:        15%{?dist}
Summary:        An intuitive reader for iCalendar and vCard objects

License:        BSD
URL:            http://sabre.io/
# https://github.com/fruux/sabre-dav/issues/336
# Please update PEAR channel
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}.tar.gz
Source1:        %{name}.xml

BuildArch:      noarch
BuildRequires:  php-pear(PEAR)
BuildRequires:  php-channel(%{channelname})

Requires(post): %{__pear}
Requires(postun): %{__pear}

Requires:       php-mbstring
Requires:       php-pear(PEAR)
Requires:       php-channel(%{channelname})
Requires:       php-pear(%{channelname}/Sabre) >= 1.0.0

Provides:       php-pear(%{pear_name}) = %{version}
Provides:       php-pear(%{channelname}/%{pear_name}) = %{version}


%description
SabreDAV VObject plugin.

%prep
%setup -q -n %{gh_project}-%{gh_commit}

sed -e 's/@VERSION@/%{version}/' \
    -e 's/@RELDATE@/%{reldate}/' \
    %{SOURCE1} >%{name}.xml
mv lib/Sabre Sabre

# Check version
extver=$(sed -n "/VERSION/{s/.* '//;s/'.*$//;p}" Sabre/VObject/Version.php)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream version is ${extver}, expecting %{version}.
   exit 1
fi

# Check files
touch error.lst
for fic in $(find Sabre/VObject -type f)
do
  grep $fic %{name}.xml || echo -$fic >> error.lst
done

for fic in $(grep '<file' %{name}.xml | sed -e 's/.*name="//' -e 's/".*//')
do
  [ -f $fic ] || echo +$fic >> error.lst
done

if [ -s error.lst ]; then
  : Error in %{name}.xml
  cat error.lst
  exit 1
fi


%build
# Empty build section, most likely nothing required.


%install
%{__pear} install --nodeps --packagingroot %{buildroot} %{name}.xml

# Clean up unnecessary files
rm -rf %{buildroot}%{pear_metadir}/.??*

# Install XML package description
mkdir -p %{buildroot}%{pear_xmldir}
install -pm 644 %{name}.xml %{buildroot}%{pear_xmldir}


%post
%{__pear} install --nodeps --soft --force --register-only \
    %{pear_xmldir}/%{name}.xml >/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    %{__pear} uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi


%files
%doc %{pear_docdir}/%{pear_name}
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Sabre/VObject


%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 06 2015 Adam Williamson <awilliam@redhat.com> - 2.1.7-1
- update to 2.1.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Remi Collet <remi@fedoraproject.org> 2.1.4-1
- update to 2.1.4
- sources from github
- fix upstream URL

* Wed Feb 12 2014 Joseph Marrero <jmarrero@fedoraproject.org> 2.1.3-1
- update to 2.1.3
* Tue Sep 03 2013 Joseph Marrero <jmarrero@fedoraproject.org> 2.1.0-1
- update to 2.1.0
- use our own package.xml created by Remi Collet as upstream doesn't use pear anymore
* Wed Oct 31 2012 Joseph Marrero <jmarrero@fedoraproject.org> 1.3.5-2
- specified php version as pointed out by phpci
* Tue Oct 23 2012 Joseph Marrero <jmarrero@fedoraproject.org> 1.3.5-1
- update to latest version
- remove uncesary changes of directory
- change define to global
- fix documentation directory
- Fix description
* Thu Aug 30 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.3.4-1
- update
* Fri Apr 06 2012 Felix Kaechele <heffer@fedoraproject.org> - 1.3.1-1
- initial package

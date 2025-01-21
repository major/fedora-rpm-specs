# version we want to build against
%global vdr_version 2.6.3
# Set vdr_version based on Fedora version
%if 0%{?fedora} >= 42
%global vdr_version 2.7.2
%elif 0%{?fedora} >= 40
%global vdr_version 2.6.9
%endif

Name:           vdr-epg2vdr
Version:        1.2.16
Release:        12%{?dist}
Summary:        A plugin to retrieve EPG data from a mysql database into VDR

License:        GPL-1.0-or-later
URL:            https://github.com/horchi/vdr-plugin-epg2vdr
Source0:        %url/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/kfb77/vdr-plugin-epg2vdr/commit/0f5caa2739a1adf5669c128df96cf0b102a2cb34.diff
Patch0:         %{name}-EventID.diff

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  sqlite-devel
BuildRequires:  openssl-devel
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  libuuid-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  imlib2-devel
BuildRequires:  vdr-devel >= %{vdr_version}
BuildRequires:  python3-devel
BuildRequires:  jansson-devel
BuildRequires:  libarchive-devel
Requires:       vdr(abi)%{?_isa} = %{vdr_apiversion}

%description 
This plugin is used to retrieve EPG data into the VDR. The EPG data 
was loaded from a mysql database. 

 
%prep
%autosetup -p1 -n vdr-plugin-epg2vdr-%{version}
iconv -f iso-8859-1 -t utf-8 README > README.utf8 ; mv README.utf8 README
# disable AUX patch
sed -i -e 's|WITH_AUX_PATCH = 1|#WITH_AUX_PATCH = 1|' Make.config

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build

%install
%make_install
# fix the perm
chmod 0755 %{buildroot}/%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc HISTORY* README*
%config(noreplace) %{vdr_configdir}/plugins/epg2vdr/epg.dat
%{vdr_plugindir}/libvdr-*.so.%{vdr_apiversion}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 11 2024 Dominik Mierzejewski <dominik@greysector.net> - 1.2.16-11
- rebuild for tinyxml2

* Tue Oct 22 2024 Richard W.M. Jones <rjones@redhat.com> - 1.2.16-10
- Rebuild for Jansson 2.14
  (https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/3PYINSQGKQ4BB25NQUI2A2UCGGLAG5ND/)

* Wed Oct 09 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-9
- Rebuilt for new VDR API version 2.7.2
- Add %%{name}-EventID.diff for vdr 2.7.x

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.16-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 15 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-7
- Rebuilt for new VDR API version 2.6.9

* Thu Jul 11 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-6
- Rebuilt for new VDR API version 2.6.8

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.16-5
- convert license to SPDX

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.16-4
- Rebuilt for Python 3.13

* Fri Apr 12 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-3
- Rebuilt for new VDR API version

* Fri Jan 26 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-2
- Rebuilt for new VDR API version

* Sun Jan 21 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.16-1
- Update to 1.2.16

* Fri Jan 05 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.2.15-2
- Rebuilt for new VDR API versionA
- Add BR gettext for rawhide

* Tue Oct 17 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.15-1
- Update to 1.2.15

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 1.2.14-2
- Rebuilt for Python 3.12

* Wed Feb 15 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.14-1
- Update to 1.2.14

* Sun Feb 12 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.13-1
- Update to 1.2.13

* Wed Jan 25 2023 Martin Gansser <martinkg@fedoraproject.org> - 1.2.12-1
- Update to 1.2.12

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 24 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.9-1
- Update to 1.2.9
- Add vps.epg2vdr.patch

* Wed Dec 14 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.8-4
- Rebuilt for new VDR API version

* Thu Dec 01 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.8-3
- Rebuilt for new VDR API version

* Sun Sep 25 2022 Rich Mattes <richmattes@gmail.com> - 1.2.8-2
- Rebuild for tinyxml2-9.0.0

* Thu Aug 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.8-1
- Update to new github address
- Update to 1.2.8

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.2.7-2
- Rebuilt for Python 3.11

* Sat Apr 30 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.7-1
- Update to 1.2.7

* Sat Feb 12 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.6-1
- Update to 1.2.6

* Fri Feb 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-4
- Rebuilt for new VDR API version

* Fri Jan 28 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-3
- Changing python to python3 in Make.config

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.5-1
- Update to 1.2.5

* Mon Jan 03 2022 Martin Gansser <martinkg@fedoraproject.org> - 1.2.3-1
- Update to 1.2.3

* Fri Dec 31 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1
- Update to 1.2.0

* Thu Dec 30 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.118-8
- Rebuilt for new VDR API version
- Add vdr-epg2vdr-2.5.4.patch

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.1.118-7
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.118-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.118-5
- Rebuilt for new VDR API version

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.118-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 03 2021 Martin Gansser <martinkg@fedoraproject.org> - 1.1.118-3
- Rebuilt for new VDR API version

* Wed Oct 21 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.118-2
- Rebuilt for new VDR API version

* Tue Sep 22 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.118-1
- Update to 1.1.118

* Fri Aug 28 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.117-2
- Rebuilt for new VDR API version

* Wed Aug 19 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.117-1
- Update to 1.1.117

* Tue Aug 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.116-1
- Update to 1.1.116

* Mon Aug 17 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.115-1
- Update to 1.1.115
- Add %%{name}-epg.patch

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.113-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Mar 23 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.113-1
- Update to 1.1.113

* Fri Mar 13 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.112-1
- Update to 1.1.112

* Sun Mar 01 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.111-1
- Update to 1.1.111

* Mon Feb 24 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.110-1
- Update to 1.1.110

* Tue Feb 18 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.109-1
- Update to 1.1.109

* Sun Feb 16 2020 Martin Gansser <martinkg@fedoraproject.org> - 1.1.107-1
- Update to 1.1.107

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.106-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 24 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.106-2
- Update to 1.1.106

* Sun Dec 15 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.104-2
- Update to 1.1.104

* Thu Dec 05 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.103-2
- Add %%{name}-gcc10-include.patch

* Tue Dec 03 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.103-1
- Update to 1.1.103

* Thu Nov 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.102-1
- Update to 1.1.102

* Mon Nov 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.101-2
- Add %%{name}-py38.patch

* Mon Nov 04 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.101-1
- Update to 1.1.101

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.98-6
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.98-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.98-4
- Add if condition for f31 with BR python3-devel

* Tue Jun 18 2019 Martin Gansser <martinkg@fedoraproject.org> - 1.1.98-3
- Rebuilt for new VDR API version

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.98-1
- Update to 1.1.98

* Thu Sep 27 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.97-1
- Update to 1.1.97

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.96-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 18 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.96-2
- Rebuilt for vdr-2.4.0

* Fri Apr 13 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.96-1
- Update to 1.1.96

* Sun Mar 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.95-1
- Update to 1.1.95

* Sun Mar 11 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.94-1
- Update to 1.1.94

* Sat Mar 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.93-1
- Update to 1.1.93

* Fri Mar 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.92-1
- Update to 1.1.92

* Tue Feb 27 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.91-1
- Update to 1.1.91
- Switched to BR python2-devel according to Fedora Packaging guidelines for Python

* Mon Feb 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.86-1
- Update to 1.1.86

* Fri Feb 16 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.84-1
- Update to 1.1.84

* Sat Feb 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.83-1
- Update to 1.1.83

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.81-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 31 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.81-1
- Update to 1.1.81

* Sun Jan 28 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.80-1
- Update to 1.1.80

* Thu Jan 25 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.79-1
- Update to 1.1.79

* Tue Jan 23 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.78-2
- Rebuilt for new tinyxml2 6.0.0

* Mon Jan 15 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.78-1
- Update to 1.1.78

* Thu Sep 21 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.73-5
- Use mariadb-connector-c-devel instead of mariadb-devel only for f28,
  fixes (BZ#1493661).

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.73-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.73-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.73-2
- Add %%{name}-mariadb-fix-build.patch fixes (BZ#1298505).

* Thu Jun 29 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.73-1
- Update to 1.1.73

* Mon Jun 12 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.68-1
- Update to 1.1.68

* Sat Jun 10 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.66-1
- Update to 1.1.66

* Fri Jun 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.64-1
- Update to 1.1.64

* Tue May 23 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.61-1
- Update to 1.1.61
- disable AUX patch in Make.config

* Mon May 08 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.60-1
- Update to 1.1.60

* Sat May 06 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.59-1
- Update to 1.1.59

* Thu May 04 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.58-1
- Update to 1.1.58

* Fri Mar 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.56-1
- Update to 1.1.56

* Fri Mar 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.55-1
- Update to 1.1.55
- Add BR tinyxml2-devel

* Wed Mar 22 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.52-1
- Update to 1.1.52

* Sun Mar 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.49-1
- Update to 1.1.49

* Fri Mar 17 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.48-1
- Update to 1.1.48

* Thu Mar 16 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.47-1
- Update to 1.1.47

* Thu Mar 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.46-1
- Update to 1.1.46

* Tue Feb 28 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.41-1
- Update to 1.1.41

* Mon Feb 27 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.40-1
- Update to 1.1.40

* Fri Feb 24 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.39-1
- Update to 1.1.39

* Tue Feb 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.38-1
- Update to 1.1.38

* Tue Feb 14 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.36-1
- Update to 1.1.36

* Fri Feb 10 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.34-1
- Update to 1.1.34

* Thu Feb 09 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.33-1
- Update to 1.1.33

* Wed Feb 08 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.32-1
- Update to 1.1.32

* Mon Feb 06 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.30-1
- Update to 1.1.30

* Wed Feb 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.27-1
- Update to 1.1.27

* Fri Jan 20 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.26-1
- Update to 1.1.26

* Mon Jan 16 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.24-1
- Update to 1.1.24

* Wed Jan 11 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.23-1
- Update to 1.1.23

* Sat Jan 07 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.21-1
- Update to 1.1.21

* Tue Jan 03 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.1.20-1
- Update to 1.1.20

* Thu Dec 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.19-1
- Update to 1.1.19

* Wed Nov 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.16-1
- Update to 1.1.16

* Wed Nov 02 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.15-1
- Update to 1.1.15

* Tue Nov 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.14-1
- Update to 1.1.14

* Tue Nov 01 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.13-1
- Update to 1.1.13

* Sun Oct 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.11-1
- Update to 1.1.11

* Thu Oct 20 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.10-1
- Update to 1.1.10

* Wed Oct 19 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.9-1
- Update to 1.1.9

* Fri Aug 26 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.6-1
- Update to 1.1.6

* Fri Jul 08 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.3-1
- Update to 1.1.3

* Mon Jul 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Sun Mar 27 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.3.47-1
- Update to 0.3.47
- Added BR python-devel
- Added BR jansson-devel
- Added BR libarchive-devel

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-7.20150203gitb2fe603
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.13-6.20151112gitb2fe603
- rebuild for new git release

* Wed Oct 21 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.13-5.20151021gitec38f0c
- rebuild for new git release

* Tue Oct 20 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.13-4.20151020git87802bc
- rebuild for new git release

* Sun Oct 11 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.13-3.20151011git0500f75
- rebuild for new git release

* Sat Oct 10 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.13-2.20151010git4906742
- rebuild for new git release

* Fri Oct 09 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.13-1.20151009git9add629
- Update to 0.1.13

* Sun Aug 30 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.12-4.20150203git5776628
- Rebuilt

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.12-3.20150203git5776628
- Rebuilt for GCC 5 C++11 ABI change

* Thu Feb 19 2015 Ville Skyttä <ville.skytta@iki.fi> - 0.1.12-2.20150203git5776628
- Rebuild

* Tue Feb 03 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.12-1.20150203git5776628
- Update to 0.1.12
- Mark license files as %%license where available

* Thu Jan 01 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.1.11-1.20141228git45ae8b4
- Update to 0.1.11

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.10-6.20140612git9b92181
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 12 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.10-5.20140612git9b92181
- rebuild for new git release

* Mon May 26 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.10-4.20140526gitd264ad8
- rebuild for new git release

* Fri May 16 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.10-3.20140516gita569a6e
- rebuild for new git release

* Thu May 15 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.10-2.20140515gitcaeef79
- rebuild for new git release

* Tue May 13 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.10-1.20140513git9479831
- rebuild for new git release 0.1.10

* Sat May 10 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.9-1.20140510gitd8382ba
- rebuild for new git release
- added Fedora %%optflags for CFLAGS and CXXFLAGS
- Add BR libcurl-devel
- Add BR libxslt-devel
- Add BR libxml2-devel
- Add BR libjpeg-turbo-devel
- Add BR imlib2-devel

* Wed May 07 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.8-1.20140507git866f08d
- rebuild for new git release

* Sat May 03 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-5.20130322git324f392
- fixed description

* Fri May 02 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-4.20130322git324f392
- Fix patch path
- Fix bogus date in %%changelog
- Fix comments

* Thu May 01 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-3.20130322git324f392
- added permission fix to solve unstripped-binary-or-object warning

* Fri Apr 25 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-2.20130322git324f392
- corrected version numbering in %%changelog
- added CXXFLAGS
- added openssl-devel as requirement
- added mariadb-devel as requirement
- added libuuid-devel as requirement

* Fri Apr 25 2014 Martin Gansser <martinkg@fedoraproject.org> - 0.1.0-1.20130322git324f392
- rebuild for initial release

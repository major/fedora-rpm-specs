
%define snap 20111102git

Name:    kio-upnp-ms
Version: 1.0.0
Release: 26.%{snap}%{?dist}
Summary: UPnP mediaserver kio slave

License: GPLv2+
URL:	 https://projects.kde.org/projects/playground/base/kio-upnp-ms
# git clone git://anongit.kde.org/kio-upnp-ms
# git archive --prefix=kio-upnp-ms-%{version}/ master | gzip > ../kio-upnp-ms-%{version}-%{snap}.tar.gz
%if 0%{?snap:1}
Source0: kio-upnp-ms-%{version}-%{snap}.tar.gz
%else
Source0: http://download.kde.org/stable/kio-upnp-ms/%{version}/src/kio-upnp-ms-%{version}.tar.gz
%endif

Source1: SOLID_UPNP.sh

BuildRequires:	kdelibs4-devel
BuildRequires:	herqq-devel
BuildRequires: make

# apparently requires both cagibi and SOLID_UPNP backend, the latter is disabled
# by default due to #754530, #758008, kde#259472
Requires: cagibi

%description
This is the UPnP MediaServer KIO-slave for the KDE platform. It supports both
browse and search based MediaServers and is able to perform various tasks on
them, including running queries, listing directories and files and allowing
KDE based applications transparent access to them. Being used for Amarok UPnP
support, the slave features many developer friendly features which allow
faster speed or easier handling while compromising on user-friendliness when
used “under the hood”.

Functionality requires some user-intervention to re-enable the SOLID_UPNP 
backend, which is disabled in fedora by default due to many crashes 
( see https://bugs.kde.org/show_bug.cgi?id=259472 ).  To re-enable, set
SOLID_UPNP=1 environment variable, or copy the sample SOLID_UPNP.sh to
$HOME/.kde/env/
to do it for you.


%prep
%setup -q

install -m644 %{SOURCE1} .


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

rm -fv %{buildroot}%{_kde4_includedir}/kio/upnp-ms-types.h


%files
%doc COPYING README* TODO
%doc SOLID_UPNP.sh 
%{_kde4_libdir}/kde4/kio_upnp_ms.so
%{_kde4_datadir}/kde4/services/kio_upnp_ms.protocol


%changelog
* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.0.0-7.20111102git
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 07 2013 Rex Dieter <rdieter@fedoraproject.org> 1.0.0-4.20111102git
- don't directly reference %%docdir in %%description (#993814)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2.20111102git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 14 2012 Rex Dieter <rdieter@fedoraproject.org>  1.0.0-1.20111102git
- 20111102 git snapshot

* Thu Apr 19 2012 Rex Dieter <rdieter@fedoraproject.org> 0.8.0-1
- 0.8.0

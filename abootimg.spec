%global gitrev ff8e759
%global checkout 20110830git%{gitrev}

Name:           abootimg
Version:        0.6
Release:        25.%{checkout}%{?dist}
Summary:        Tool for manipulating Android boot images

License:        GPLv2+
URL:            https://gitorious.org/ac100/abootimg
# git clone git://gitorious.org/ac100/abootimg.git
# cd abootimg ; git archive --format=tar --prefix=abootimg-%%{version}-%%{checkout}/ %%{gitrev} | gzip > abootimg-%%{version}-%%{checkout}.tar.gz
Source0:        abootimg-%{version}-%{checkout}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=856241
# Fix man page typos. Sent upstream
Patch0:         abootimg.1.patch

BuildRequires:  gcc
BuildRequires:  libblkid-devel

%description
abootimg is used to manipulate block devices or files with the special 
partition format defined by the Android Open Source Project.


%prep
%setup -q -n abootimg-%{version}-%{checkout}
%patch0 -p1 -b .mantypo


%build
echo "#define VERSION_STR \"%{version}\"" > version.h
gcc ${RPM_OPT_FLAGS} -DHAS_BLKID -lblkid abootimg.c -o abootimg


%install
install -D abootimg ${RPM_BUILD_ROOT}/%{_bindir}/abootimg
install -D -m 644 -p debian/abootimg.1 ${RPM_BUILD_ROOT}/%{_mandir}/man1/abootimg.1


%files
%{_bindir}/abootimg
%{_mandir}/man1/*
%doc Changelog LICENSE README



%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-25.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-24.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-23.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-22.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-21.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-20.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-19.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-18.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-17.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-16.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-15.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-14.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-13.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-12.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-11.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-10.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-9.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-8.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-7.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 11 2012 Yanko Kaneti <yaneti@declera.com> 0.6-6.20110830gitff8e759
- Fix man page typos. Filip Holec , bug 856241

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-4.20110830gitff8e759
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Yanko Kaneti <yaneti@declera.com> 0.6-3.20110830gitff8e759
- Preserve man page timestamp on install.

* Wed Nov 16 2011 Yanko Kaneti <yaneti@declera.com> 0.6-2.20110830gitff8e759
- Fixed a typo pointed by the first review.

* Tue Aug 30 2011 Yanko Kaneti <yaneti@declera.com> 0.6-1.20110830gitff8e759
- Attempt at packaging.

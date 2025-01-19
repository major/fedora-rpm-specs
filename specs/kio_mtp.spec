%define git_commit c418634
%define snap 20141221

Name:           kio_mtp
Version:        0.75
Release:        33.%{snap}git%{git_commit}%{?dist}
Summary:        An MTP KIO slave for KDE

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://projects.kde.org/projects/playground/base/kio-mtp
# use releaseme
Source0:        kio-mtp-%{version}-%{snap}.tar.xz

## upstreamable patches
# use kio-mtp4 locale catalog so as to not conflict with kio-mtp from kio-extras-5+
Patch1: kio-mtp-catalog.patch

BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  libmtp-devel
BuildRequires: make

# short-lived subpkg
Obsoletes: kio_mtp-common < 0.75-10

%description
Provides KIO Access to MTP devices using the mtp:/// protocol.


%prep
%setup -n kio-mtp-%{version}

%patch -P1 -p1 -b .catalog

for po in po/*/*.po ; do
pushd $(dirname $po)
mv kio_mtp.po kio_mtp4.po
popd
done


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
make install/fast  DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang kio_mtp4


%files -f kio_mtp4.lang
%doc README LICENCE
%{_kde4_libdir}/kde4/kio_mtp.so
%{_kde4_datadir}/kde4/services/mtp.protocol
%{_kde4_datadir}/kde4/apps/konqueror/dirtree/remote/mtp-network.desktop
%{_kde4_datadir}/kde4/apps/solid/actions/solid_mtp.desktop
%{_kde4_datadir}/kde4/apps/remoteview/mtp-network.desktop


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-33.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.75-32.20141221gitc418634
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-31.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-30.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-29.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-28.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-27.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-26.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-25.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-24.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-23.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-22.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-21.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-20.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-19.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-18.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-17.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-16.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-15.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-14.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.75-13.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-12.20141221gitc418634
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.75-11.20141221gitc418634
- Rebuilt for GCC 5 C++11 ABI change

* Tue Apr 07 2015 Rex Dieter <rdieter@fedoraproject.org> 0.75-10.20141221gitc418634
- use non-conflicting kio_mtp4 catalog instead

* Fri Apr 03 2015 Rex Dieter <rdieter@fedoraproject.org> 0.75-9.20141221gitc418634
- omit -common, Requires: kio-extras-mtp-common (f22+, plasma5)

* Fri Apr 03 2015 Rex Dieter <rdieter@fedoraproject.org> 0.75-8.20141221gitc418634
- -common subpkg, fix conflicts with kio-extras (#1208601)

* Sat Jan 10 2015 Rex Dieter <rdieter@fedoraproject.org> 0.75-7.20141221gitc418634 
- 20141221 snapshot, include translations, .spec cleanup

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-6.20131020git2063e75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-5.20131020git2063e75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 26 2013 Jan Grulich <jgrulich@redhat.com> - 0.75-4.20131020git2063e75
- update git snapshot

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.75-3.20130323gitcc6b195
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Jan Grulich <jgrulich@redhat.com> - 0.75-2.20130323gitcc6b195
- update git snapshot

* Tue Mar 26 2013 Jan Grulich <jgrulich@redhat.com> - 0.75-1.20130323git1bcd508
- update git snapshot

* Mon Mar 11 2013 Jan Grulich <jgrulich@redhat.com> - 0.70-5.20130311git7de86ba
- fix versioning

* Mon Mar 11 2013 Jan Grulich <jgrulich@redhat.com> - 0.70-4.20130311git7de86ba
- update git snapshot

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.70-3.20121225gitfae62fc
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 25 2012 Jan Grulich <jgrulich@redhat.com> - 0.70-2.20121225gitfae62fc
- Add LICENCE file
- Remove %%clean
- Change name

* Fri Dec 21 2012 Jan Grulich <jgrulich@redhat.com> - 0.70-1.20121221gitccaa6d1
- Initial package
- Based on git snapshot ccaa6d1da2d6c04134dd35fbdd6bbf5dd0b86572

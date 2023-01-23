Name:       spin-kickstarts
Version:    0.36.0
Release:    0.4%{?dist}
License:    GPLv2+
Summary:    Kickstart files and templates for creating your own Fedora Spins
URL:        https://pagure.io/fedora-kickstarts
Source0:    https://pagure.io/fedora-kickstarts/archive/%{version}/fedora-kickstarts-%{version}.tar.gz
BuildArch:  noarch
BuildRequires: make
Requires:   fedora-kickstarts

%description
A number of kickstarts you can use to create customized (Fedora) Spins

%package -n fedora-kickstarts
Summary:    Official Fedora Spins
Requires:   spin-kickstarts = %{version}-%{release}

%description -n fedora-kickstarts
Kickstarts used to compose the official Fedora Spins (see
http://spins.fedoraproject.org/ for a full list)

%package -n custom-kickstarts
Summary:    Kickstart files for Custom Spins (not official)
Requires:   spin-kickstarts = %{version}-%{release}
Requires:   fedora-kickstarts = %{version}-%{release}

%description -n custom-kickstarts
Unofficial spins (remixes) brought to us by several contributors

%package -n l10n-kickstarts
Summary:    Localized kickstarts for localized spins
Requires:   fedora-kickstarts = %{version}-%{release}
Requires:   custom-kickstarts = %{version}-%{release}

%description -n l10n-kickstarts
Localized versions of kickstarts for localized spins

%prep
%setup -q -n fedora-kickstarts-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT/usr

%files
%doc COPYING README.md AUTHORS
%dir %{_datadir}/%{name}/

%files -n fedora-kickstarts
%{_datadir}/%{name}/*.ks*
%{_datadir}/%{name}/snippets/

%files -n custom-kickstarts
%dir %{_datadir}/%{name}/custom/
%{_datadir}/%{name}/custom/*.ks
%{_datadir}/%{name}/custom/*.js
%doc %{_datadir}/%{name}/custom/README

%files -n l10n-kickstarts
%dir %{_datadir}/%{name}/l10n/
%{_datadir}/%{name}/l10n/*.ks
%doc %{_datadir}/%{name}/l10n/README

%changelog
* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.36.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 27 2021 Kevin Fenzi <kevin@scrye.com> - 0.36.0-0.1
- Release for rawhide pre f36

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-0.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-0.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.31.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 18 2019 Kevin Fenzi <kevin@scrye.com> - 0.31.0-0.1
- Make a spin kickstarts for f31 rawhide.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Kevin Fenzi <kevin@scrye.com> - 0.30.0-1
- Update to 0.30.0 to kick off the 30 cycle in rawhide.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.29.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 24 2018 Kevin Fenzi <kevin@scrye.com> - 0.29.1-1
- Update to 0.29.0 for rawhide.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 30 2017 Kevin Fenzi <kevin@scrye.com> - 0.27.1-1
- 0.27.1 version for final f27 release. Fixes bug #1506050

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 01 2017 Kevin Fenzi <kevin@scrye.com> - 0.27.0-1
- Initial version for f27

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Aug 04 2016 Bruno Wolff III <bruno@wolff.to> - 0.26.0-1
- Build initial rawhide / f26 version

* Fri Jun 24 2016 Bruno Wolff III <bruno@wolff.to> - 0.25.0-2
- Change spec to refer to new upstream location on pagure.io

* Sun Jun 12 2016 Bruno Wolff III <bruno@wolff.to> - 0.25.0-1
- Keep rawhide ahead of f24
- README moved to README.md

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Kalev Lember <klember@redhat.com> - 0.24.3-1
- Update to 0.24.3
- Install missing snippets/packagekit-cached-metadata.ks (#1276987)

* Sat Oct 31 2015 Bruno Wolff III <bruno@wolff.to> - 0.24.2-1
- Keep ahead of f23

* Tue Oct 20 2015 Bruno Wolff III <bruno@wolff.to> - 0.24.1-1
- Keep ahead of f23

* Sat Jul 25 2015 Bruno Wolff III <bruno@wolff.to> - 0.24.0-1
- Astronomy Lab is a new spin

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 30 2015 Bruno Wolff III <bruno@wolff.to> - 0.23.3-1
- dvd and cd were removed from file names

* Wed Apr 22 2015 Bruno Wolff III <bruno@wolff.to> - 0.23.1
- Keep up with f22 beta

* Tue Mar 03 2015 Bruno Wolff III <bruno@wolff.to> - 0.23.0
- Initial f23 build
- Keep up with f22 alpha

* Fri Nov 28 2014 <bruno@wolff.to> - 0.22.2-1
- Up to date rawhide version roughly sync'd with the f21 final version

* Sat Oct 11 2014 <bruno@wolff.to> - 0.22.1-1
- Get an up to date copy sync'd with f21 beta

* Sun Jul 13 2014 <bruno@wolff.to> - 0.22.0-1
- Initial f22 build

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Dec 21 2013 <bruno@wolff.to> - 0.21.6-1
- Keep up with f20 version

* Wed Nov 27 2013 <bruno@wolff.to> - 0.21.5-1
- Keep up with f20 version

* Sat Nov 02 2013 <bruno@wolff.to> - 0.21.4-1
- Keep up with f20 version

* Tue Oct 08 2013 <bruno@wolff.to> - 0.21.3-1
- Keep up with f20 version

* Sat Aug 31 2013 <bruno@wolff.to> - 0.21.2-1
- Fix updates and testing repo urls - bz 1003032

* Tue Aug 20 2013 <bruno@wolff.to> - 0.21.1-1
- Get a rawhide build after the branch
- This version will use rawhide repos

* Tue Aug 20 2013 <bruno@wolff.to> - 0.20.17-1
- Switch over to branched repos

* Tue Aug 20 2013 <bruno@wolff.to> - 0.20.16-1
- Get an up to date build at branch time

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 04 2013 Bruno Wolff III <bruno@wolff.to> 0.20.15-1
- Pick up fix for broken repo include files

* Sat Jun 29 2013 Bruno Wolff III <bruno@wolff.to> 0.20.14-1
- Stop maintaining the spec file upstream
- Upstream has changed the way repo commands are handled
- The NEWS file was dropped
- One kickstart file was meant to be used after running sed and ended in .ks.in

* Thu May 23 2013 Bruno Wolff III <bruno@wolff.to> 0.20.4-1
- Pick up changes for getting spins under size limits
- Pick up various fixes for other issues

* Mon May 06 2013 Bruno Wolff III <bruno@wolff.to> 0.20.3-1
- Add missing ks files to Makefile.am - bz 959911

* Wed May 01 2013 Bruno Wolff III <bruno@wolff.to> 0.20.2-1
- New ks file for Mate desktop
- Keep up with f19

* Fri Mar 15 2013 Bruno Wolff III <bruno@wolff.to> 0.20.1-1
- Initial package for f20

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> -
 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 30 2013 Luya Tshimbalanga <luya@fedoraproject.org> 0.19.2-1
- Design Suite ks renamed as fedora-live-design-suite

* Sat Oct 06 2012 Bruno Wolff III <bruno@wolff.to> 0.19.1-1
- Meego ks has been dropped
- Initial package for f19

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun 15 2012 Bruno Wolff III <bruno@wolff.to> 0.18.1-1
- Initial package for f18 rawhide
- Switch back to rawhide repos until branch
- Include Russian localization ks files

* Sun Feb 12 2012 Bruno Wolff III <bruno@wolff.to> 0.17.1-1
- Rebuild post branch to build from branch repos

* Tue Oct 25 2011 Bruno Wolff III <bruno@wolff.to> 0.17.0-1
- Initial build of f17 version
- Use rawhide repo by default for live images

* Sat Oct 15 2011 Bruno Wolff III <bruno@wolff.to> 0.16.2-1
- Get an up to date version now that we are near f16 final freeze

* Sat Aug 06 2011 Bruno Wolff III <bruno@wolff.to> 0.16.1-1
- Update for F16 branch

* Fri May 20 2011 Bruno Wolff III <bruno@wolff.to> 0.16.0-1
- Initial F16 build

* Fri Apr 01 2011 Bruno Wolff III <bruno@wolff.to> 0.15.4-1
- Enough has changed that it seems worth doing a new beta build

* Wed Mar 16 2011 Bruno Wolff III <bruno@wolff.to> 0.15.3-1
- Early beta build to facilitate testing
- The alternate KDE ks file has been added to the package

* Mon Feb 14 2011 Bruno Wolff III <bruno@wolff.to> 0.15.2-1
- Rebuild to point to branched release

* Mon Feb 07 2011 Bruno Wolff III <bruno@wolff.to> 0.15.1-1
- Pre-alpha release rebuild

* Sun Oct 31 2010 Bruno Wolff III <bruno@wolff.to> 0.15.0-1
- Now that F14 is gold, we want a separate rawhide package.
- Includes most stuff from F14, minus some last minute space cutting changes.

* Tue Jul 27 2010 Bruno Wolff III <bruno@wolff.to> 0.14.1-1
- Get a snapshot of kickstarts just prior to f14 branch

* Mon Jun 07 2010 Bruno Wolff III <bruno@wolff.to> 0.14.0-1
- New release for F14
- Add some documentation about how rebuild package from git repo
- Change custom kickstarts to use ../ to refer to included kickstarts

* Sun Jul 05 2009 Jeroen van Meeuwen <kanarip a fedoraunity.org> 0.11.4-1
- Fix repos in fedora-install-fedora.ks (#505262)

* Sun May 31 2009 Jeroen van Meeuwen <kanarip a fedoraunity.org> 0.11.3-1
- New release
- Removed developer spin from the mix

* Wed Mar 04 2009 Jeroen van Meeuwen <kanarip a fedoraunity.org> 0.11.1-1
- Added de_CH localized spins

* Mon Feb 23 2009 Jeroen van Meeuwen <kanarip a fedoraunity.org> 0.11.0-2
- Remove fedora-livecd-desktop-default.ks

* Sat Nov 29 2008 Jeroen van Meeuwen <kanarip a fedoraunity.org> 0.11.0-1
- Point fedora-live-base.ks repos to f-10
- Remove sysprof from fedora-livedvd-developer.ks
- Latest and final rebuild for Fedora 10

* Sat Nov 08 2008 Jeroen van Meeuwen <kanarip a fedoraunity.org> 0.10.2-1
- Package updates to kickstarts into F-10 package

* Fri Nov 07 2008 Jeroen van Meeuwen <kanarip a fedoraunity.org> 0.10.1-1
- Second build for review #448072

* Fri May 23 2008 Jeroen van Meeuwen <kanarip a fedoraunity.org> 0.01-1
- Initial packaging

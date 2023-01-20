Name:           audex
Version:        0.79
Release:        18%{?dist}
Summary:        Audio ripper
License:        GPLv3+
URL:            https://userbase.kde.org/Audex

Source0:        http://downloads.sourceforge.net/project/%{name}/src/%{name}-%{version}.tar.xz
Patch0:         audex-fixbuild.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  kdelibs4-devel
BuildRequires:  libkcddb-devel
BuildRequires:  libkcompactdisc-devel
BuildRequires:  cdparanoia-devel
BuildRequires: make

%description
audex is a new audio grabber tool for CD-ROM drives based on KDE 4. 
Although it is still under development, it is published as
a beta version. It is being tested by some testers and this program
may change on the way to its first stable 1.0-release.

%prep
%setup -qn %{name}-%{version}

%patch0 -p1 -b .fixbuild

%build
# get lots of c++11 warnings, particularly literal/string warnings, so
# don't use c++11 mode for now -- rex
%if 0%{?fedora} > 24
export CXXFLAGS="%{optflags} -std=gnu++98 -Wno-c++11-compat"
%endif

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform} V=1

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name}

desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications/kde4 \
    --add-category X-AudioVideoImport \
    %{buildroot}%{_datadir}/applications/kde4/audex.desktop

%files -f %{name}.lang
%doc README.md
%license LICENCE
%{_kde4_bindir}/audex
%{_kde4_appsdir}/solid/actions/audex-rip-audiocd.desktop
%{_kde4_datadir}/applications/kde4/audex.desktop
%{_kde4_iconsdir}/hicolor/*/apps/audex.*
%{_kde4_appsdir}/audex/

%changelog
* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.79-7
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 0.79-4
- fix FTBFS, .spec cosmetics/cleanup

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.79-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.79-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Roland Wolters <wolters.liste@gmx.net> 0.79-1
- Update to 0.79-1

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-0.9.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-0.8.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-0.7.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-0.6.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 11 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.74-0.5.beta1
- Add patch to fix FTBFS

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-0.4.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Rex Dieter <rdieter@fedoraproject.org> 0.74-0.3.beta1
- audex-0.74-0.2.beta1.fc17 is FTBFS (#824767)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.74-0.2.beta1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 29 2011 Roland Wolters <wolters.liste@gmx.net> 0.74-0.1.beta1
- Rebuilt for 0.74-0.1.beta1

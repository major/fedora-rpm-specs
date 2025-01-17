Name:           xmountains
Version:        2.11
Release:        3%{?dist}
Summary:        A fractal terrain generator

# SPDX confirmed
License:        HPND
URL:            https://spbooth.github.io/xmountains/
Source0:        https://github.com/spbooth/xmountains/archive/v%{version}/%{name}-%{version}.tar.gz
Source11:        xscreensaver-xmountains.xml
Source12:        xscreensaver-xmountains.conf
# Need report to the upstream
# Fix for C23
Patch0:         xmountains-2.11-c23.patch

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  xorg-x11-xbitmaps
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libX11-devel
BuildRequires:  imake

%description
Xmountains is a fractal terrain generator written by Stephen Booth.

%package         xscreensaver
Summary:         XScreenSaver integration support
Requires(post): xscreensaver-base
Requires:        xscreensaver-base
Requires:        %{name} = %{version}-%{release}
BuildArch:       noarch

%description     xscreensaver
This package adds XScreenSaver integration.


%prep
%setup -q
%patch -P0 -p1 -b .c23

%global optflags %optflags -Werror=implicit-function-declaration

%build
xmkmf
make %{?_smp_mflags} CCOPTIONS="$RPM_OPT_FLAGS -DANSI"

%install
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	%{nil}
make install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -p" \
	INSTMANFLAGS="-m 0644" \
	%{nil}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/xscreensaver/{config,hacks.conf.d}
install -cpm 0644 %{SOURCE11} $RPM_BUILD_ROOT%{_datadir}/xscreensaver/config/xmountains.xml
install -cpm 0644 %{SOURCE12} $RPM_BUILD_ROOT%{_datadir}/xscreensaver/hacks.conf.d/xmountains.conf

%post xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks
fi

%postun xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ]; then
    %{_sbindir}/update-xscreensaver-hacks || :
fi

%files
%doc	README
%license	copyright.h
%{_bindir}/xmountains
%{_mandir}/man1/xmountains.1x*

%files xscreensaver
%{_datadir}/xscreensaver/*/*

%changelog
* Wed Jan 15 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.11-3
- Port to C23

* Wed Jan 15 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.11-2
- use C17 for now

* Wed Jan 15 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.11-1
- 2.11

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-8.D20170103git3ba444a4f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 22 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.9-7.D20170103git3ba444a4f7
- SPDX migration

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-6.D20170103git3ba444a4f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.9-5.D20170103git3ba444a4f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4.D20170103git3ba444a4f7.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4.D20170103git3ba444a4f7.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4.D20170103git3ba444a4f7.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4.D20170103git3ba444a4f7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4.D20170103git3ba444a4f7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-4.D20170103git3ba444a4f7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Feb  2 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.9-4.D20170103git3ba444a4f7
- Compile with -Werror=implicit-function-declaration
- Support gcc10 -fno-common

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3.D20170103git3ba444a4f7.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3.D20170103git3ba444a4f7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3.D20170103git3ba444a4f7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-3.D20170103git3ba444a4f7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 2.9-3.D20170103git3ba444a4f7
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.9-2.D20170103git3ba444a4f7.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.9-2.D20170103git3ba444a4f7
- Add xscreensaver integration

* Fri Dec  8 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.9-1.D20170103git3ba444a4f7
- Update to 2.9
- Upstream switched to github, using it

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.8-3
- F-17: rebuild against gcc47

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Nov  6 2009 Ian Weller <ian@ianweller.org> - 2.8-1
- 2.8

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 19 2008 Ian Weller <ianweller@gmail.com> 2.7-3
- License correction
- Removed redundant doc identifier
- Honored Fedora specific compilation flags
- Fixed permissions on man page

* Wed Mar 19 2008 Ian Weller <ianweller@gmail.com> 2.7-2
- Added some (should-be) obvious BuildRequires

* Wed Mar 19 2008 Ian Weller <ianweller@gmail.com> 2.7-1
- First package build.

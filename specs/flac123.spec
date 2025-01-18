#global snapshot 1
%global OWNER flac123
%global PROJECT flac123
%global commit d969f2cc94a6b0ff623c2a64081a3d67b624a39d
%global commitdate 20230811
%global gittag v2.1.1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		flac123
Version:	2.1.1%{?snapshot:^%{commitdate}git%{shortcommit}}
Release:	5%{?dist}
Summary:	Command-line program for playing FLAC audio files

License:	GPL-2.0-or-later
URL:		https://github.com/flac123/flac123
%if 0%{?snapshot}
Source0:	https://github.com/%{OWNER}/%{PROJECT}/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0:	https://github.com/%{OWNER}/%{PROJECT}/archive/%{gittag}/%{name}-%{version}.tar.gz
%endif
BuildRequires:	gcc
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	intltool
BuildRequires:	make
BuildRequires:	libao-devel
BuildRequires:	flac-devel
BuildRequires:	libogg-devel
BuildRequires:	popt-devel

%description
flac123 is a command-line program for playing FLAC audio files.

FLAC (Free Lossless Audio Codec) is an open format for losslessly
compressing audio data.  Grossly oversimplified, FLAC is similar to
Ogg Vorbis, but lossless.

flac123 implements mpg123's 'Remote Control' interface via option -R.
This is useful if you're writing a frontend to flac123 which needs a
consistent, reliable interface to control playback.


%prep
%if 0%{?snapshot}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif


%build
#aclocal && autoconf && automake --add-missing
%configure
%make_build


%install
%make_install


%files
%doc AUTHORS BUGS ChangeLog NEWS README*
%license COPYING
%{_bindir}/flac123
%{_mandir}/man1/flac123.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Sep 12 2023 Charles R. Anderson <cra@alum.wpi.edu> - 2.1.1-1
- Update to 2.1.1 from new github upstream
- Use SPDX license identifer
- Bring up to date with latest packaging guidelines

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 14 2022 Florian Weimer <fweimer@redhat.com> - 0.0.12-23
- Port to C99

* Tue Sep 13 2022 Michel Alexandre Salim <salimma@fedoraproject.org> - 0.0.12-22
- Rebuilt for flac 1.4.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 08 2020 Charles R. Anderson <cra@alum.wpi.edu> - 0.0.12-17
- BR make

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Feb 18 2018 Charles R. Anderson <cra@wpi.edu> - 0.0.12-11
- Add BR gcc
- Remove Group: and rm -rf in install section

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.12-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Charles R. Anderson <cra@wpi.edu> - 0.0.12-1
- update to 0.0.12
- use correct Sourceforge source URL
- update description

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Sep 02 2010 Rakesh Pandit <rakesh@fedoraproject.org> - 0.0.11-9
- Bump for libao

* Fri Jun 04 2010 Charles R. Anderson <cra@wpi.edu> - 0.0.11-8
- fix Source0 URL since SourceForge moved the downloads again

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 18 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.0.11-5
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.11-4
- Autorebuild for GCC 4.3

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.11-3
- BR popt-devel

* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 0.0.11-2
- Rebuild for selinux ppc32 issue.

* Tue Jul 12 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.11-1
- Bump to 0.0.11, this fixes #246322 and adds flac 1.1.4 support
- Remove flac 1.1.3 patch, it's not needed anymore
* Mon Feb 26 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.9-6
- Add fixed patch to really make build work against flac 1.1.3
* Mon Feb 26 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.9-3
- Add patch to make build work against flac 1.1.3
* Thu Feb 15 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.9-2
- Rebuild against new libflac
* Mon Dec 11 2006 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 0.0.9-1
- Initial build

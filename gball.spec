Name:		gball
Version:	2.0
Release:	18%{?dist}
Summary:	The Console Ball and Racket Game

License:	GPLv3+
URL:		http://sites.google.com/site/mohammedisam2000/home/projects
Source0:	%{url}/%{name}-%{version}.tar.gz

#Requires:	gnudos
BuildRequires:  gcc
BuildRequires:	gnudos-devel
BuildRequires: make

%description
GBall is a simple yet nice implementation of the well known ball and 
racket game. It is designed to run under the GNU/Linux console 
(including terminal emulators). The aim of the game is simple: control 
your racket and move it around to bounce the ball and hit all the bricks.
If the ball hits a wall, it will bounce. If it fell down the screen without
bouncing on the racket, you lose.
The game includes many levels with an option to play levels randomly.
The game also has a high score board.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

install -m 0644 -p -D info/gball.info* %{buildroot}%{_infodir}/gball.info

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
%{_docdir}/gball

%license COPYING

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Mohammed Isam <mohammed_isam1984@yahoo.com> - 2.0-12
- Bugfixes

* Thu Feb 27 2020 Mohammed Isam <mohammed_isam1984@yahoo.com> - 2.0-11
- Bugfixes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 2.0-1
- Added '9' & '0' keys to control game speed
- Fixed a bug in collision detection logic
- Added more levels

* Tue Oct 13 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.2-1
- Added commandline '--level' option
- Fixed black background

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 28 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-2
- Fixed spec file issues

* Sun Apr 26 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-1
- Fixed spec file issues

* Wed Nov 19 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-1
- First release

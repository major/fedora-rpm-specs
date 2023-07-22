Name:		gosnake
Version:	2.0
Release:	18%{?dist}
Summary:	The Console Snake Game

License:	GPLv3+
URL:		http://sites.google.com/site/mohammedisam2000/home/projects
Source0:	http://sites.google.com/site/mohammedisam2000/home/projects/%{name}-%{version}.tar.gz

Requires:	gnudos
BuildRequires:  gcc
BuildRequires:	gnudos-devel
BuildRequires: make

%description
GoSnake is a simple yet nice implementation of the well known snake game.
It is designed to run under the GNU/Linux console (including terminal
emulators). The aim of the game is simple: control your snake and move 
it around to eat food without hitting walls, or colliding with itself.
The game includes many levels with an option to play levels randomly, 
and a high score board.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

install -m 0644 -p -D info/gosnake.info* %{buildroot}%{_infodir}/gosnake.info

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
%{_docdir}/gosnake

#%%doc AUTHORS README COPYING ChangeLog
%license COPYING

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Mohammed Isam <mohammed_isam1984@yahoo.com> 2.0-11
- Bug fixes

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
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

* Tue Dec 01 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 2.0-1
- Bug fixes
- Added more levels

* Tue Oct 13 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.2-1
- Added commandline '--level' option
- Fixed black background

* Mon Jun 29 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-1
- Corrected license issue

* Wed Nov 19 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-1
- First release

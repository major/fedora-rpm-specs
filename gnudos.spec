Name:		gnudos
Version:	1.11
Release:	17%{?dist}
Summary:	The GnuDOS library for GNU/Linux

License:	GPLv3+
URL:		http://sites.google.com/site/mohammedisam2000/home/projects
Source0:	http://sites.google.com/site/mohammedisam2000/home/projects/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires: make


%description
GnuDOS is a library of functions for use under the GNU/Linux console/xterm. 
It provides 3 core components and 2 utility programs. The core components 
are Kbd (for keyboard handling), Screen (for screen handling) and Dialogs (for 
drawing dialogs and input boxes). The utility programs are: prime (the console 
file manager) and mino (the console text editor).

GnuDOS is a group of utilities that were designed to introduce new users to 
the GNU system. The tools included in the library have a look-and-feel 
familiar to users of MS-DOS like systems. The aim is to provide users 
accustomed to such systems a gentle way to learn how to use the GNU 
operating system.


%package devel
Summary: Development files for the GnuDOS library
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains files necessary to develop programs using the GnuDOS 
corelib library of functions.


%prep
%setup -q

%build
%set_build_flags
# For declarations of fcloseall and strcasestr.
CFLAGS="$CFLAGS -D_GNU_SOURCE"
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete

install -m 0644 -p -D info/gnudos.info* %{buildroot}%{_infodir}/gnudos.info
install -m 0644 -p -D info/prime.info* %{buildroot}%{_infodir}/prime.info
install -m 0644 -p -D info/mino.info* %{buildroot}%{_infodir}/mino.info


%files
%{_libdir}/libgnudos.so.1
%{_libdir}/libgnudos.so.1.0.9
%{_bindir}/*
%{_mandir}/man1/*
%{_infodir}/*
%{_docdir}/gnudos


%files devel
%{_includedir}/console
%{_libdir}/libgnudos.so


%changelog
* Fri Dec 23 2022 Florian Weimer <fweimer@redhat.com> - 1.11-17
- Build with -D_GNU_SOURCE (#2156071)

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-12
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Feb 27 2020 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.11-10:
- Bugfixes

* Thu Feb 27 2020 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.11-9:
- Bugfixes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.11-5
- Added BuildRequires: gcc

* Sat May 12 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.11-4
- Bugfixes

* Sat May 12 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.11-3
- Added missing copyright notice for ChangeLog file

* Fri May 11 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.11-2
- Added THANKS file and fixed missing copyright notices

* Thu Apr 5 2018 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.11-1
- Bug fixes in mino (almost rewritten from scratch)
- Bug fixes in prime

* Fri Nov 18 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.10-1
- Bug fixes in mino

* Wed Aug 03 2016 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.9-1
- Bug fixes

* Sun Dec 06 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-5
- Added show_about() and show_readme() functions
- Bug fixes

* Fri Oct 16 2015 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-4
- More bug fixes!
- Fixed mino's search and replace functions

* Fri Dec 19 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-3
- More bug fixes!

* Fri Dec 19 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-2
- Debugging and fixing of memory checking

* Sat Dec 13 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.8-1
- Configured prime to copy file mode when copying files/dirs
- Added more key definitions to kbd
- Fixed bugs in prime and mino

* Mon Aug 25 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.7-1
- Modified prime and mino to parse commandline arguments through getopt_long()
- Added the Options menu to prime
- Removed version from the shared library

* Sat Aug 23 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.6-3
- Modified spec file

* Fri Aug 22 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.6-2
- Modified spec file

* Tue Aug 19 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.6-1
- Working on auto indentation in mino
- Included HTML, JavaScript, Basic, Pascal & Fortran syntax highlighting 
  in mino
- Modified mino source files

* Sun Aug 03 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.5-1
- Updated and modified Fog
- Made a separate info file for Fog (was included in gnudos info file)
- Included Texi, Assembly & Python syntax highlighting in mino
- Colorized prime's view

* Tue Jul 29 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.4-1
- Added the keybindings file to the package
- Modified mino & prime source files to include keybindings in help menu
- Updated mino & prime to version 1.1

* Tue Jul 29 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.3-2
- Modified Makefile for info pages

* Sat Jul 12 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.3-1
- Modified Manfiles for manpages and src dirs

* Thu May 29 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.2-2
- Modified info, man, readme, and manual files for gnudos corelib
  and the fog utility

* Tue May 20 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.2-1
- Added ukbd utility for unicode handling
- Added uputchar() to the dialogs utility
- Updated the fog utility program

* Fri May 09 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-4
- Corrected spec file for devel package dependency

* Sat Apr 26 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-3
- Corrected spec file (files & install sections)

* Sat Apr 26 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-2
- Corrected spec file sections: post, postun, and files 

* Fri Apr 18 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.1-1
- Corrected spec file
- Modified source files to point for documentation under doc/gnudos
- Added symlink to devel package

* Fri Apr 11 2014 Mohammed Isam <mohammed_isam1984@yahoo.com> 1.0-1
- First release

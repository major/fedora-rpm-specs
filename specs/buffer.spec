#
# $Id$
#
%define debug_package %{nil}

Summary:        This program speeds up writing tapes on remote tape drives
Summary(fr):    Ce programme accélère l'écriture des bandes sur des périphériques distants

Name:           buffer
Version:        1.19
Release:        31%{?dist}
License:        GPL-1.0-or-later
Url:            http://hello-penguin.com/software/buffer
Source:         http://hello-penguin.com/software/buffer/%{name}-%{version}.tar.gz
 
Patch0:         01-debian-patches.all.gz
Patch1:         02-fedora-patch.all.gz
Patch2:         03-GPL.patch.all.gz


BuildRequires:  gcc
BuildRequires: make
%description
This is a program designed to speed up writing tapes on remote tape drives.
When this program is put "in the pipe", two processes are started.
One process reads from standard-in and the other writes to standard-out.
Both processes communicate via shared memory.

%description -l fr
Le programme buffer est conçu pour accélérer l'écriture des bandes sur des
périphériques bande distants.
Quand ce programme est utilisé dans un tuyau (pipe), deux processus sont 
démarrés.
Un processus lit depuis l'entrée standard et l'autre écrit vers la sortie 
standard.
Les deux processus communiquent au travers de mémoire partagée.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%make_build CFLAGS="%{optflags} -Dultrix"

%install
install -p -m 755 -D buffer --strip %{buildroot}/%{_bindir}/buffer
install -p -m 644 -D buffer.man %{buildroot}/%{_mandir}/man1/buffer.1

%files
%doc README 
%license COPYING
%{_bindir}/buffer
%{_mandir}/man1/buffer.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Miroslav Suchý <msuchy@redhat.com> - 1.19-29
- convert license to SPDX

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Bruno Cornec <bruno@project-builder.org> - 1.19-20
- Use macro make_build as suggested by tstellar

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 02 2015 Bruno Cornec <bruno@project-builder.org> 1.19-8
- Updated to 1.19-8
- Fix spec file for Fedora conformity (Bruno Cornec/Miroslav Suchý)

* Fri Oct 03 2008 Bruno Cornec <bruno@project-builder.org> 1.19-3
- Updated to 1.19-3
- Fix the french summary (Bruno Cornec)

* Thu Oct 02 2008 Bruno Cornec <bruno@project-builder.org> 1.19-2
- Updated to 1.19-2
- Fix build flags for Fedora conformity (Bruno Cornec)

* Sat Sep 20 2008 Bruno Cornec <bruno@project-builder.org> 1.19-1
- Updated to 1.19-1
- Updated to 1.19 (Bruno Cornec)




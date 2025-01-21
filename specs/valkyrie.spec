Name:		valkyrie
Version:	2.0.0
Release:	33%{?dist}
Summary:	Graphical User Interface for Valgrind Suite

%global valkyrie %{name}-%{version}

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://www.valgrind.org/
Source0:	http://www.valgrind.org/downloads/%{valkyrie}.tar.bz2
Source1:	%{name}.desktop
Patch1:		%{name}-docdir.patch
Patch2:		%{name}-usleep.patch
Patch3:		%{name}-getuid.patch
Patch4:		%{name}-getpid.patch

BuildRequires: make
BuildRequires:	desktop-file-utils
BuildRequires:	qt4-devel >= 4.2
Requires:	valgrind >= 3.6.0

%description
Valkyrie is a graphical user interface to the Valgrind suite
of tools for debugging and profiling programs.  It makes use
of the XML output capabilities offered by Valgrind.

%prep
%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%{qmake_qt4} PREFIX=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make INSTALL_ROOT=%{buildroot} install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
install -d %{buildroot}%{_datadir}/pixmaps/
install -m 644 %{_builddir}/%{valkyrie}/icons/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/
cp -p %{_builddir}/%{valkyrie}/COPYING %{buildroot}%{_docdir}/%{valkyrie}
cp -p %{_builddir}/%{valkyrie}/INSTALL %{buildroot}%{_docdir}/%{valkyrie}
cp -p %{_builddir}/%{valkyrie}/README  %{buildroot}%{_docdir}/%{valkyrie}

%files
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_docdir}/%{valkyrie}

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.0-32
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.0.0-13
- use %%qmake_qt4 macro to ensure proper build flags

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.0-11
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar  4 2013 Nathan Scott <nathans@redhat.com> 2.0.0-7
- Remove use of --parent option to %%doc expansion, no longer works.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct  8 2012 Nathan Scott <nathans@redhat.com> 2.0.0-5
- Resolve remaining fedora-review issues (bz 862160)
- Use doc instead of install-sh of {README,LICENSE,INSTALL}
- Rework expansion of docs in general to fit in with this
- Use global instead of define

* Sat Oct  6 2012 Nathan Scott <nathans@redhat.com> 2.0.0-4
- Add getpid patch to resolve build issue reported by Sebastian Dyroff (bz 862160)

* Fri Oct  5 2012 Nathan Scott <nathans@redhat.com> 2.0.0-3
- Add getuid patch to resolve build issue reported by Sebastian Dyroff (bz 862160)

* Thu Oct  4 2012 Nathan Scott <nathans@redhat.com> 2.0.0-2
- Add usleep patch to resolve build issue reported by Sebastian Dyroff (bz 862160)

* Tue Oct  2 2012 Nathan Scott <nathans@redhat.com> 2.0.0-1
- Initial build

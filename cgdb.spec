Name:			cgdb
Version:		0.8.0
Release:		8%{?dist}
Summary:		CGDB is a curses-based interface to the GNU Debugger (GDB)

License:		GPLv2
URL:			https://cgdb.github.io/
Source0:		https://cgdb.me/files/%{name}-%{version}.tar.gz
Source1:		https://cgdb.github.io/images/screenshot_debugging.png
Patch0: cgdb-configure-c99.patch

BuildRequires:  gcc-c++
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	texinfo
BuildRequires:	flex
BuildRequires: make
Requires:		gdb


%description
CGDB is a curses-based interface to the GNU Debugger (GDB).
The goal of CGDB is to be lightweight and responsive; not encumbered with
unnecessary features.
The interface is designed to deliver the familiar GDB text interface,
with a split screen showing the source as it executes.
The UI is modeled on the classic Unix text editor, vi.
Those familiar with vi should feel right at home using CGDB.


%prep
%autosetup -p1
# Avoid re-running configure.
touch -r aclocal.m4 config/*.m4 configure

%build
autoconf
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p"
rm -rf $RPM_BUILD_ROOT/%{_infodir}/dir



%files
%doc AUTHORS COPYING NEWS ChangeLog
%{_bindir}/cgdb
%{_datadir}/cgdb
%{_infodir}/cgdb.info.*

%changelog
* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 08 2023 Florian Weimer <fweimer@redhat.com> - 0.8.0-5
- Port configure script to C99

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 19 2022 Eric Curtin <ecurtin@redhat.com> - 0.8.0-1
- Update to 0.8.0

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 4 2019 Gilboa Davara <gilboad@gmail.com> - 0.6.8-13
- Automatically disable gdb's shell style.

* Wed Apr 24 2019 Björn Esser <besser82@fedoraproject.org> - 0.6.8-12
- Remove hardcoded gzip suffix from GNU info pages

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.6.8-11
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 0.6.8-4
- Rebuild for readline 7.x

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Nov 15 2014 Gilboa Davara <gilboad [AT] gmail.com> - 0.6.8-1
- New upstream release: 0.6.8.
- New BR: help2man, flex, texinfo.

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 02 2013 Gilboa Davara <gilboad [AT] gmail.com> - 0.6.7-3
- Add missing autoconf BR.

* Sun Jun 02 2013 Gilboa Davara <gilboad [AT] gmail.com> - 0.6.7-2
- Fix #925144 by calling autoconf. (Temporary solution, pending upsteam fix).

* Sun Jun 02 2013 Gilboa Davara <gilboad [AT] gmail.com> - 0.6.7-1
- Version upgrade to 0.6.7 (Bug fix release).

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 13 2011 Gilboa Davara <gilboad [AT] gmail.com> - 0.6.6-1
- Version upgrade to 0.6.6 (Bug fix release).

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 11 2010 Gilboa Davara <gilboad [AT] gmail.com> - 0.6.5-1
- Bump to 0.6.5.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.6.4-3
- Autorebuild for GCC 4.3

* Sun Aug 26 2007 <gilboad[AT]gmail.com> - 0.6.4-2
- Fixed license tag.

* Wed May 16 2007 <gilboad[AT]gmail.com> - 0.6.4-1
- 0.6.4
- Fix broken info installation.
- Enable SMP build.
- Preserve the source time-stamp.
- Replace install with %%{__install}.

* Wed Jan 17 2007 <gilboad[AT]gmail.com> - 0.6.3-10
- Fix Source0 URL.
- Replace cp with install.

* Mon Jan 15 2007 <gilboad[AT]gmail.com> - 0.6.3-9
- Do -not- delete cgdb.txt - needed by binary.
- Use the original htdocs instead of htmldocs.
- Preserve timestamps.
- Fix missing URL in imported cgdb.png.

* Mon Jan 15 2007 <gilboad[AT]gmail.com> - 0.6.3-8
- Remove INSTALL
- Move cgdb.txt to %%docs. (Where index.html can see it.)
- Move htdocs to %%docs.
- Fix broken cgdb.png file.

* Sat Jan 13 2007 <gilboad[AT]gmail.com> - 0.6.3-7
- Fix wrong license. (Was LGPL, should be GPL.)

* Sat Jan 13 2007 <gilboad[AT]gmail.com> - 0.6.3-6
- Move HTML docs into %%docs

* Fri Jan 12 2007 <gilboad[AT]gmail.com> - 0.6.3-5
- Keep timestamps on install
- Remove unnecessary comments.
- Add missing HTML docs.

* Mon Jan 08 2007 <gilboad[AT]gmail.com> - 0.6.3-4
- Remove redundant dependencies.
- Add missing ownership.
- Fix texinfo pre/post.
- Fix %%doc in changelog.

* Mon Jan 08 2007 <gilboad[AT]gmail.com> - 0.6.3-3
- Fix %%doc.
- Do not strip debug info; let rpm do it.

* Mon Jan 08 2007 <gilboad[AT]gmail.com> - 0.6.3-2
- Cosmetic clean-up.

* Mon Jan 08 2007 <gilboad[AT]gmail.com> - 0.6.3-1
- Initial release.


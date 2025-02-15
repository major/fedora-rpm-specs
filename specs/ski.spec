Name:           ski
Version:        1.5.0
Release:        1%{?dist}
Summary:        IA-64 user and system mode simulator

License:        GPL-2.0-only and GPL-2.0-or-later
URL:            https://github.com/trofi/ski
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
# some syscalls are missing
ExcludeArch:    aarch64

BuildRequires:  make
BuildRequires:  elfutils-libelf-devel
BuildRequires:  ncurses-devel
BuildRequires:  automake autoconf libtool
BuildRequires:  autoconf-archive
BuildRequires:  gperf
BuildRequires:  bison flex
BuildRequires:  libtool-ltdl-devel
BuildRequires:  gcc
Obsoletes: %{name}-libs < 1.4.0
Obsoletes: %{name}-devel < 1.4.0


%description
The Ski IA-64 user and system simulator originally developed by HP.


%prep
%autosetup -p1


%build
./autogen.sh

%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc AUTHORS NEWS README TODO ChangeLog
%doc doc/ski-notes.html doc/manual/*.pdf
%{_bindir}/ski
%{_bindir}/bski
%{_bindir}/bskinc
%{_bindir}/ski-fake-xterm
%{_mandir}/man1/ski.1*
%{_mandir}/man1/bski.1*
%{_mandir}/man1/bskinc.1*


%changelog
* Thu Feb 13 2025 Dan Horák <dan[at]danny.cz> - 1.5.0-1
- updated to 1.5.0
- fixes GCC 15 FTBFS (rhbz#2341356)

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Florian Weimer <fweimer@redhat.com> - 1.4.0-3
- Backport upstream patches to fix C type errors

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 17 2023 Dan Horák <dan[at]danny.cz> - 1.4.0-1
- updated to 1.4.0

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Florian Weimer <fweimer@redhat.com> - 1.3.2-37
- Apply patches from github.com/trofi/ski to fix C99 compatibility issues
- Fix sporadic build failure due to missing makefile dependency

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Dan Horák <dan[at]danny.cz> - 1.3.2-31
- fix build with gcc 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep  7 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.3.2-22
- Exclude aarch64

* Tue Feb 16 2016 Dan Horák <dan[at]danny.cz> - 1.3.2-21
- fix FTBFS (#1308134)
- spec cleanup

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Jon Ciesla <limburgher@gmail.com> - 1.3.2-19
- Move from lesstif to motif.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.3.2-11
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan  1 2011 Dan Horák <dan[at]danny.cz> 1.3.2-9
- updated the nohayes patch to completely remove TIOC[GS]HAYESESP

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov  1 2008 Dan Horak <dan[at]danny.cz> 1.3.2-6
- rename the ppc patch to nohayes and add other arches without TIOC[GS]HAYESESP

* Wed Apr 30 2008 Dan Horak <dan[at]danny.cz> 1.3.2-5
- fix attributes for files in subpackages

* Thu Apr 10 2008 Dan Horak <dan[at]danny.cz> 1.3.2-4
- fix build on ppc

* Wed Apr  9 2008 Dan Horak <dan[at]danny.cz> 1.3.2-3
- fix linking issues
- use -libs for the subpackage

* Sat Apr  5 2008 Dan Horak <dan[at]danny.cz> 1.3.2-2
- fix compile in rawhide (kernel >= 2.6.25-rc5)

* Tue Feb 19 2008 Dan Horak <dan[at]danny.cz> 1.3.2-1
- update to version 1.3.2
- remove patches integrated into upstream codebase
- create a lib subpackage to be multi-lib aware

* Sat Nov 10 2007 Dan Horak <dan[at]danny.cz> 1.2.6-2
- merge libski and libskiui

* Sat Oct  6 2007 Dan Horak <dan[at]danny.cz> 1.2.6-1
- initial Fedora version

%global udevdir %(pkg-config --variable=udevdir udev)

Name:       fbterm
Version:    1.7
Release:    32%{?dist}
License:    GPL-2.0-or-later
URL:        http://code.google.com/p/fbterm/
Source0:    https://github.com/fujiwarat/fbterm/releases/download/v%{version}/%{name}-%{version}.tar.gz

#Patch0:    %%{name}-1.2-kernel-header.patch
#Patch1:    %%{name}-1.3-setcap.patch
#Patch2:    %%{name}-1.4-iminput.patch
#Patch3:    %%{name}-1.6-rpmpack.patch
#Patch4:    %%{name}-1.6-el5.patch
Patch5:     %{name}-1.7-u16-build.patch

Summary:    A frame-buffer terminal emulator
Summary(zh_CN): 运行在帧缓冲的快速终端仿真器
Summary(zh_TW): 運行在frame-buffer的快速終端模擬機


BuildRequires: autoconf, automake
BuildRequires: fontconfig-devel gpm-devel
BuildRequires: gcc-c++
BuildRequires: pkgconfig(udev)
BuildRequires: make
Requires: fontconfig
# ncurses-term has /usr/share/terminfo/f/fbterm
Requires: ncurses-term
Obsoletes: fbterm-udevrules < %{version}-%{release}

%description
FbTerm is a fast terminal emulator for Linux with frame-buffer device. 
Features include: 
- mostly as fast as terminal of Linux kernel while accelerated scrolling
  is enabled on frame-buffer device 
- select font with fontconfig and draw text with freetype2, same as 
  Qt/Gtk+ based GUI apps 
- dynamically create/destroy up to 10 windows initially running default
  shell 
- record scroll back history for every window 
- auto-detect text encoding with current locale, support double width 
  scripts like  Chinese, Japanese etc 
- switch between configurable additional text encodings with hot keys
  on the fly 
- copy/past selected text between windows with mouse when gpm server 
  is running


%if 0%{?fedora} >= 9
%package udevrules
Summary:    udev rules that grant regular user access
Requires:   udev

%description udevrules
Regular users might use some applications that require access to frame-buffer device.
For example, ibus-fbterm requires access to /dev/fb0.
This sub-package enables regular user for such access.
%endif

%prep

%setup -q
#%%patch0 -p0 -b .kernel-header
#%%patch1 -p0 -b .setcap
#%%patch2 -p0 -b .iminput
#%%patch3 -p0 -b .rpmpack
#%%if 0%{?fedora} >= 9
#%%else
#%%patch4 -p0 -b .el5
#%%endif
%patch -P5 -p1 -b .u16

%build
autoreconf -iv
%configure --disable-static --disable-rpath
make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make DESTDIR=%{buildroot} install
%__chmod 755 %{buildroot}/%{_bindir}/%{name}

%if 0%{?fedora} >= 9
%post
setcap 'cap_sys_tty_config+ep' %{_bindir}/%{name}
%endif

%files 
%doc AUTHORS ChangeLog COPYING README
%if 0%{?fedora} >= 9
%{_bindir}/%{name}
%else
%attr(4755,root,root) %{_bindir}/%{name}
%endif
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 16 2022 Takao Fujiwara <tfujiwar@redhat.com> - 1.7-26
- Migrate license tag to SPDX

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Takao Fujiwara <tfujiwar@redhat.com> - 1.7-20
- Reverted the previous change and requires ncurses-term

* Sun Jun 21 2020 Nick Black <nickblack@linux.com> - 1.7-19
- Install terminfo description, fix source URI

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Nov 11 2016 Takao Fujiwara <tfujiwar@redhat.com> - 1.7-10
- Bug 1226680 - Drop fbterm-udevrules

* Mon Feb 29 2016 Takao Fujiwara <tfujiwar@redhat.com> - 1.7-9
- Bug 1311848 - udev rules from fbterm-udevrules
- Added 1.7-u16-build.patch to fix u16 build failures.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Luis Bazan <lbazan@fedoraproject.org> - 1.7-1
- New Upstream Version
  1. added redirecting /dev/tty0 output to FbTerm's sub-window
  2. added option "ambiguous-wide" to treat ambiguous CJK characters as wide width
  3. added option "font-height" to force font height
  4. added shortcut CTRL_ALT_K to kill the frozen IM server
  5. fixed a bug where curses line drawing characters give inverted questions marks
  6. fixed a text auto selection bug
  7. fixed a logical error in terminal insert mode
  8. fixed a few other bugs 

- From version 1.7, FbTerm redirects /dev/tty0 output to the pseudo terminal of current sub-window. In linux before version 2.6.10, anybody can do this as long as the output was not redirected yet; since version 2.6.10, only root or a process with the CAP_SYS_ADMIN capability may do this.
- In a number of CJK encodings there are ambiguous width characters which have a width of either narrow or wide depending on the context of their use. By default, FbTerm treats them as narrow width characters, the new added option "ambiguous-wide" may be used to change the behavior. 

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 24 2010 Ding-Yi Chen <dchen at redhat dot com> - 1.6-3
- Resolves: #565710
  Add udevrules sub package for installing udev rules for granting regular user access.

* Mon Nov 30 2009 Ding-Yi Chen <dchen at redhat dot com> - 1.6-1
- Fixed [Bug 539186] FTBFS fbterm-1.5-2.fc12
- Upstream fixed [Bug 542284] terminfo file for fbterm not included with fbterm package in fedora.
- Patch for EL-5
- Upstream update:
  1. added VESA video card support 
  2. added rendering messages for IM server development 
  3. fixed a bug where Ctrl+Space is a shortcut even user run FbTerm without "input-method" option 
  4. fixed a bug where user compile FbTerm without gpm mouse support but run it in a gpm server enabled environment 
  5. fixed a IM program dead loop bug triggered by FbTerm's crash 
  6. fixed several spelling errors in FbTerm's help message and man-page

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 15 2009 Ding-Yi Chen <dchen at redhat dot com> - 1.5-1
- Upstream update:  
  1. added support for text rendering with backround image 
  2. added command-line arguments to customize command executed in sub-window 
  3. added Alt-Fn and all FbTerm's shortcuts support when input method is actived 
  4. added option "-v/--verbose" to show some useful information 
  5. fixed some text color issues with version 1.4 
  6. fixed encoding selection error when locale is C/POSIX 
  7. fixed a bug where screen is cleared on startup even in inactive tty 
  8. fixed a bug where variable HOME is not defined
- rpmpack.patch is to allow rpm buildable for non-root account.
- Add BuildRequires automake, autoconf to "refresh" src/Makefile,
  otherwise, the above patch is not effective for a weird reason.

* Mon Mar 23 2009 Ding-Yi Chen <dchen at redhat dot com> - 1.4-1
- Upstream update:
  1. improved text rendering performence 
  2. added private escape sequences for 256 color mode support 
  3. added a option "font-width" to adjust character cell width 
  4. added support for older 2.2/2.4 kernel 
  5. fixed a crash bug with bitmap fonts 
  6. fixed a configure failure in cross-compiling environment
- Note: iminput.patch is applied.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
  
* Tue Jan 06 2009 Ding-Yi Chen <dchen at redhat dot com> - 1.3-1
- SUID fbterm for el5, as it does not have libcap.

* Mon Jan 05 2009 Ding-Yi Chen <dchen at redhat dot com> - 1.3-0
- Upstream update:
  1. added command line arguments to change option values 
  2. added client-server based input method framework 
  3. added screen rotation support 
  4. added support for visual type DIRECTCOLOR used by ATI cards 
     (thanks for Witek's patch) 
  5. fixed a bug that user can't input some unicode characters 
  6. fixed a bug of maybe not restore original console state after 
     FbTerm exited 
  7. fixed several trivial bugs 
  8. added using filesystem capability attributes offered by kernel 
     2.6.27, instead of setting set-user-ID bit on FbTerm 
  9. decreased memory usage of every shell instance by changing size 
      of the struct saving every charater's attribute from 4 to 2 bytes

* Thu Dec 11 2008 Ding-Yi Chen <dchen at redhat dot com> - 1.2-2
- Summary simplified.

* Fri Nov 21 2008 Ding-Yi Chen <dchen at redhat dot com> - 1.2-2
- Upstream update, see 
 http://code.google.com/p/fbterm/
 for details.

* Fri Oct 17 2008 Ding-Yi Chen <dchen at redhat dot com> - 1.1-3
- Add gpm support.

* Thu Oct 16 2008 Ding-Yi Chen <dchen at redhat dot com> - 1.1-2
- Fix the kernel-header build problem in F-10.

* Thu Aug 07 2008 Ding-Yi Chen <dchen at redhat dot com> - 1.1-1
- Unset the SUID flag, as it does not need it.

* Thu Aug 07 2008 Ding-Yi Chen <dchen at redhat dot com> - 1.1-0
- The first version.

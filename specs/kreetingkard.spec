%define		mainver		0.7.1
%define		baserelease	16
%define		repoid		18105



Name:		kreetingkard
Version:	%{mainver}
Release:	%{baserelease}%{?dist}
Summary:	Japanese greeting card writing software for KDE

# SPDX confirmed
License:	GPL-2.0-or-later
URL:		http://linux-life.net/program/cc/kde/app/kreetingkard/
Source0:	http://downloads.sourceforge.jp/%{name}/%{repoid}/%{name}-%{mainver}.tar.gz
# From Mandriva
Patch0:		kreetingkard-0.7.1-fix-build-gcc411.patch
# Patch to detect strlcpy on Fedora 39 glibc, by avoiding
# -pedantic error with std::exit
Patch1:		kreetingkard-0.7.1-configure-no-std-exit-for-strlcpy-detection.patch

BuildRequires:	make
BuildRequires:	gcc-c++
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	kdelibs3-devel
BuildRequires:	libjpeg-devel


%description
KreetingKard is a tool for making Japanese greeting cards. It allows you to 
make greeting cards easily by choosing a template and changing the words.


%prep
%setup -q
%patch -P0 -p1 -b .gcc41
%patch -P1 -p1 -b .strlcpy

cp -p configure configure.orig
sed -i configure \
	-e 's|grep klineedit|grep -i klineedit|' \
	-e '\@x_direct_test_function@,\@main@s@int@#include <X11/Intrinsic.h>\nint@' \
	-e 's|\(${x_direct_test_function}\)()|\1(0)|' \
	%{nil}
sed -i configure \
	-e 's|hardcode_libdir_flag_spec=|hardcode_libdir_flag_spec_goodby=|'

%build
# modify qt.sh
# add aarch64 entry to be sure
cp -a %_sysconfdir/profile.d/qt.sh .
sed -i qt.sh -e 's@ppc64le@ppc64le | aarch64 @'
unset QTDIR
# explicitly source
source ./qt.sh

# Don't call autoheader
touch -r configure \
	config.h.in config.h

%configure

# Remove rpath
for f in `find . -name Makefile` ; do
	%{__sed} -i.rpath -e 's|^\([A-Z][A-Z]*_RPATH = \).*|\1|' $f
done

%make_build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%make_install

# Fixing up
# 1. Desktop file treatment
%{__sed} -i -e '/^Pattern/d' \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Office/%{name}.desktop
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
	--add-category Office \
	--delete-original \
	$RPM_BUILD_ROOT%{_datadir}/applnk/Office/%{name}.desktop
%{__rm} -rf $RPM_BUILD_ROOT%{_datadir}/applnk/

# 2 KDE common symlink to relative
unlink $RPM_BUILD_ROOT%{_defaultdocdir}/HTML/en/%{name}/common
%{__ln_s} -f '../common' $RPM_BUILD_ROOT%{_defaultdocdir}/HTML/en/%{name}/common

# 3 Install icons
for s in 16 32 ; do
	%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/
	%{__install} -cp -m 644 src/cr${s}-app-%{name}.png \
		$RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done

# 4. gettext .mo file
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc	AUTHORS
%license	COPYING
%doc	README

%{_bindir}/%{name}

%{_datadir}/apps/%{name}/
%{_datadir}/icons/crystalsvg/??x??/*/*.png
%{_datadir}/mimelnk/application/x-%{name}.desktop

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/icons/hicolor/??x??/apps/%{name}.png

%{_defaultdocdir}/HTML/en/%{name}/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-12
- SPDX migration

* Mon Oct  2 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-11
- Fix X function dection in configure with -Werror=implicit-function-declaration

* Thu Jul 20 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-10
- Fix strlcpy detection (with glibc 2.38), by fixing -pedantic-error
  with std::exit usage

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-9
- Explicitly source qt3 qt.sh for local build reproducibility
- Disable rpath by nullifying hardcode_libdir_flag_spec

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-8
- Fix for UIC plugin detection behavior change

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7.1-7.1
- Remove obsolete scriptlets

* Wed Aug  9 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-7
- Add BR: libjpeg-devel explicitly

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.7.1-6.4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.1-6
- F-19: kill vendorization of desktop file (fpc#247)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.7.1-5
- F-17: rebuild against gcc47

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-4
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-3
- GTK icon cache updating script update

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Mon Oct 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-2
- Fix typo.

* Thu Oct 18 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.7.1-1
- Initial spec file

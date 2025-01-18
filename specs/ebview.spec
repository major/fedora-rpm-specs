Name:		ebview
Version:	0.3.6.2
Release:	40%{?dist}
Summary:	EPWING CD-ROM dictionary viewer

# data/about.en.in	GPL-2.0-or-later
# intl/		LGPL-2.1-or-later unused
# SPDX confirmed
License:	GPL-2.0-or-later
%if 0
URL:		http://ebview.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
%else
URL:		http://packages.qa.debian.org/e/ebview.html
Source0:	http://ftp.de.debian.org/debian/pool/main/e/ebview/ebview_%{version}.orig.tar.gz
%endif
# Support -Werror=format-security
Patch0:	ebview-0.3.6.2-format-security.patch
# Fix wrong inline
Patch1:	ebview-0.3.6.2-wrong-inline.patch
Source1:	%{name}.desktop
# Use pango instead of pangox-compat
Patch101:	https://sources.debian.org/data/main/e/ebview/0.3.6.2-2/debian/patches/dont-use-pangox.patch
# And link to libX11
Patch102:	https://sources.debian.org/data/main/e/ebview/0.3.6.2-2/debian/patches/link-ebview.diff
# Port to c99, -Werror=implicit-int -Werror=implicit-function-declaration
Patch103:	ebview-0.3.6.2-c99.patch
# Port to c23
Patch104:	ebview-0.3.6.2-c23.patch

BuildRequires:	gcc
BuildRequires:	eb-devel
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(pango)

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	make

#Requires:	VLGothic-fonts

%description
EBView is a EPWING dictionary browser.

%prep
%setup -q
%patch -P0 -p1 -b .format
%patch -P1 -p1 -b .inline
%patch -P101 -p1 -b .pango
%patch -P102 -p1 -b .link
%patch -P103 -p1 -b .c99
%patch -P104 -p1 -b .c23

rm -f m4/glib-gettext.m4
autoreconf -i

# Fix up permission
find . -type f -exec %{__chmod} 0644 {} ';'
%{__chmod} 0755 \
	configure \
	install-sh \
	mkinstalldirs

# Defaults
%{__sed} -i.defaults \
	-e 's|gnome-moz-remote|xdg-open|' \
	-e 's|Kochi |Sazanami |' \
	src/preference.c

# encodings
iconv -f EUCJP -t UTF-8 README > README.tmp && \
	( touch -r README README.tmp ; %{__mv} -f README.tmp README )

%{__sed} -i -e 's|\r||' \
	doc/ja/menu.html \
	doc/ja/body.html

for f in doc/ja/*.html ; do
	iconv -f EUC-JP -t UTF-8 $f | \
		%{__sed} -e 's|EUC-JP|UTF-8|' > $f.tmp && \
		%{__mv} -f $f.tmp $f || \
		%{__rm} -f $f.tmp
done
iconv -f ISO-8859-1 -t UTF-8 doc/en/index.html > doc/en/index.html.tmp && \
	%{__mv} -f doc/en/index.html.tmp doc/en/index.html || \
	%{__rm} -f doc/en/index.html.tmp

# Clearly mark this as unused
rm -f intl/*.{c,h}

%build
%configure \
	--with-eb-conf=%{_libdir}/eb.conf
%make_build -k


%install
%{__rm} -rf $RPM_BUILD_ROOT

# Actually %%makeinstall...
%{__make} install \
	INSTALL="%{__install} -c -p" \
	bindir=$RPM_BUILD_ROOT%{_bindir}  \
	datadir=$RPM_BUILD_ROOT%{_datadir} \
	gnulocaledir=$RPM_BUILD_ROOT%{_datadir}/locale

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/pixmaps
%{__install} -cpm 644 pixmaps/%{name}.xpm \
	$RPM_BUILD_ROOT%{_datadir}/pixmaps/

%{find_lang} %{name}

%files -f %{name}.lang
%doc AUTHORS
%license COPYING
%doc ChangeLog
%doc NEWS
%doc README

%{_bindir}/%{name}
%{_datadir}/%{name}/

%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 16 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-39
- Port to C23

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jan 28 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-37
- SPDX migration

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-32
- Port for strict c99, -Werror=implicit-int -Werror=implicit-function-declaration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-26
- Use pango instead of pangox-compat
  - pangox-compat no longer compatible with pango 1.44 (bug 1836495)
  - pango patch from debian (debian bug 701840)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-16
- Fix wrong inline

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Dec  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-12
- Support -Werror=format-security

* Tue Sep  3 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-11
- Rebuild against new eb

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-9
- F-19: kill vendorization of desktop file (fpc#247)

* Sat Jan 12 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.6.2-8
- Remove explicit font requires

* Sun Oct 14 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.3.6.2-7
- Add BR: pangox-compat-devel on F-18+

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.3.6.2-5
- F-17: rebuild against gcc47

* Wed Nov  9 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.3.6.2-4
- Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 30 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6.2-2
- F-12: Rebuild against new eb

* Tue Aug 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6.2-1
- Use Debian 0.3.6.2 (Masayuki Hatta <mhatta@debian.org>)
- Drop 64 bits patches, remove some unneeded hacks

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6-7
- F-12: Mass rebuild

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6-6
- F-11: Mass rebuild

* Mon Jul 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6-5
- Change Japanese fonts Requires (F-10+)

* Sat Feb  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- Rebuild against gcc43

* Fri Jan 11 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6-4
- Patch extracted from opensuse 0.3.6-105 for 64bits issue,
  which will hopefully fix bug 428195

* Thu Nov 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6-3
- Require fonts-japanese (bug 382551)

* Wed Nov 14 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.3.6-1
- Initial packaging, borrowing desktop file from
  Akihiro Matsushima <amatsus@gsc.riken.jp>


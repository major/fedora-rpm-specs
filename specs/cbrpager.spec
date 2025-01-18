Name:		cbrpager
Version:	0.9.22
Release:	33%{?dist}
Summary:	Simple comic book pager for Linux

# Source itself:	GPL-2.0-or-later
# metainfo:	CC0-1.0
# SPDX confirmed
License:	GPL-2.0-or-later AND CC0-1.0
URL:		http://www.jcoppens.com/soft/cbrpager/index.en.php
Source0:	http://downloads.sourceforge.net/cbrpager/%{name}-%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/cbrpager/%{name}-%{version}.md5
Patch0:	cbrpager-c99.patch

BuildRequires:  gcc
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	make
Requires:	gnome-icon-theme

%description
A no-nonsense, simple to use, small viewer for cbr and cbz
(comic book archive) files. As it is written in C, 
the executable is small and fast. It views jpg (or jpeg), 
gif and png images, and you can zoom in and out.

%prep
%autosetup -p1

for f in \
	ChangeLog \
	CONTRIBUTORS
	do
	iconv -f ISO-8859-1 -t UTF-8 $f > $f.tmp && \
		( touch -r $f $f.tmp ; %{__mv} -f $f.tmp $f )
	rm -f $f.tmp
done

cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=cbrPager
Comment=A simple comic book pager for Linux
Exec=%{name} %%f
Icon=applications-graphics
Terminal=false
Type=Application
Categories=Graphics;Viewer;
EOF

%build
%configure
%make_build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%make_install

desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/cbrpager/support-requests/4/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">cbrpager.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Read comics</summary>
  <description>
    <p>
      cbrPager is a simple comic book reader application with the ability to change pages and zoom.
      It features the ability to open and read cbr, cb7 and cbz comic book archives that contain
      PNG and JPEG images.
    </p>
  </description>
  <url type="homepage">http://www.jcoppens.com/soft/cbrpager/index.en.php</url>
  <screenshots>
    <screenshot type="default">http://www.jcoppens.com/soft/cbrpager/img/snap.jpeg</screenshot>
  </screenshots>
</application>
EOF

%find_lang %{name}

%files	-f %{name}.lang
%defattr(-,root,root,-)
%doc	AUTHORS
%doc	CONTRIBUTORS
%license	COPYING
%doc	ChangeLog
%doc	NEWS
%doc	README
%doc	TODO

%{_bindir}/%{name}
%{_metainfodir}/*%{name}.appdata.xml
%{_datadir}/applications/*%{name}.desktop


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.22-30
- SPDX migration

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Florian Weimer <fweimer@redhat.com> - 0.9.22-28
- C compatibility fix

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.22-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.22-10
- Add an AppData file for the software center

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb  9 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.9.22-6
- F-19: kill vendorization of desktop file (fpc#247)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.22-4
- F-17: rebuild against gcc47

* Tue Nov 08 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.22-3
- Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 21 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.22-1
- 0.9.22

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.20-2
- F-12: Mass rebuild

* Sat May 30 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.20-1
- 0.9.20

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.19-2
- F-11: Mass rebuild

* Mon Aug  4 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.19-1
- 0.9.19

* Sat May 31 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.18-1
- 0.9.18
- 1 patch dropped, upstream applied

* Mon May 26 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.17-2
- Escape filename in zip file properly

* Sat May 24 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.17-1
- 0.9.17
- 2 patches dropped, upstream applied

* Fri May 23 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.16-2
- 0.9.16
- Properly handle file name (shell escaping issue)

* Fri Mar 21 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.9.15-1
- Initial packaging



%{!?_fontbasedir: %global _fontbasedir %{_datadir}/fonts}

%define		archivename		monafont

%define		projectname		mona
%define		fontname		%{projectname}
%define		family_ttf_s		sazanami
%if 0%{?fedora} >= 38
%define		family_ttf_s_dir	%{_fontbasedir}/%{family_ttf_s}-gothic-fonts
%else
%define		family_ttf_s_dir	%{_fontbasedir}/%{family_ttf_s}
%endif
%define		family_ttf_v		vlgothic
%if 0%{?fedora} >= 37
%define		family_ttf_vp		vl-pgothic
%define		family_ttf_vp_dir	%{_fontbasedir}/%{family_ttf_vp}-fonts
%else
%define		family_ttf_vp		vlgothic-p
%define		family_ttf_vp_dir	%{_fontbasedir}/vlgothic
%endif
%define		real_family_ttf_s	sazanami
%define		real_family_ttf_v	VLGothic

%define		rpmname_suffix	fonts

%define		fontdir_bitmap	%{projectname}-bitmap
%define		fontdir_ttf_s		%{projectname}-%{family_ttf_s}
%define		fontdir_ttf_v		%{projectname}-%{family_ttf_v}

%define		name_bitmap		%{fontdir_bitmap}-%{rpmname_suffix}
%define		name_ttf_s		%{fontdir_ttf_s}-%{rpmname_suffix}
%define		name_ttf_v		%{fontdir_ttf_v}-%{rpmname_suffix}

%define		old_name_bitmap	mona-fonts-bitmap
%define		old_name_ttf_s	mona-fonts-sazanami
%define		old_name_ttf_v	mona-fonts-VLGothic

%define		fontdir_bitmap_full	%{_fontbasedir}/%{fontdir_bitmap}
%define		fontdir_ttf_s_full	%{_fontbasedir}/%{fontdir_ttf_s}
%define		fontdir_ttf_v_full	%{_fontbasedir}/%{fontdir_ttf_v}

%define		obsoletes_EVR		2.90-5.999
%define		sazanami_ver		20040629
%define		vlgothic_ver		20220612

%define		catalog_dir		%{_sysconfdir}/X11/fontpath.d

# misc
%define		show_progress		0

%define	common_description	\
Mona Font is a Japanese proportional font which allows you to view \
Japanese text arts correctly.

Name:		%{archivename}
Version:	2.90
Release:	41%{?dist}
Summary:	Japanese font for text arts

# monafont itself is under public domain
# Automatically converted from old format: Public Domain - review is highly recommended.
License:	LicenseRef-Callaway-Public-Domain
URL:		http://monafont.sourceforge.net/
Source0:	http://downloads.sourceforge.net/monafont/%{archivename}-%{version}.tar.bz2

# Appstream metainfo files
# https://bugzilla.redhat.com/show_bug.cgi?id=1165507
Source1:        %{fontname}.metainfo.xml
Source2:        %{fontname}-sazanami.metainfo.xml
Source3:        %{fontname}-vlgothic.metainfo.xml


# Need investigating, however
# it seems that the behavior of "split" changed between 5.10 -> 5.12
Patch0:	monafont-2.90-perl512-split.patch

BuildArch:	noarch
BuildRequires:	make
BuildRequires:	fontpackages-devel
BuildRequires:	%{_bindir}/perl
BuildRequires:	glibc-all-langpacks

%description
%{common_description}

%package -n	%{name_bitmap}
Summary:	Bitmap Japanese font for text arts
# Automatically converted from old format: Public Domain - review is highly recommended.
License:	LicenseRef-Callaway-Public-Domain
# Write BuildRequires a bit verbosely
BuildRequires:	perl-interpreter
BuildRequires:	%{_bindir}/bdftopcf
BuildRequires:	%{_bindir}/mkfontdir
Obsoletes:	%{old_name_bitmap} <= %{obsoletes_EVR}
Provides:	%{old_name_bitmap} = %{version}-%{release}

%description -n	%{name_bitmap}
%{common_description}

%package -n	%{name_ttf_s}
Summary:	True Type Japanese font for text arts based on Sazanami
# monafont itself is Public Domain and this package borrows
# sazanami
# And the outline otf uses Kochi-substitute (later renamed to sazanami),
# which is under BSD
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
BuildRequires:	%{family_ttf_s}-gothic-fonts = 0.%{sazanami_ver}
Requires:	fontpackages-filesystem
Obsoletes:	%{old_name_ttf_s} <= %{obsoletes_EVR}
Provides:	%{old_name_ttf_s} = %{version}-%{release}

%description -n	%{name_ttf_s}
%{common_description}

This package contains True Type fonts generated generated from
%{name} source package which are based on Sazanami fonts.

%package -n	%{name_ttf_v}
Summary:	True Type Japanese font for text arts based on VLGothic
# monafont itself is Public Domain and this package borrows
# VLGothic (mplus and BSD)
# And the outline otf uses Kochi-substitute (later renamed to sazanami),
# which is under BSD
# Automatically converted from old format: mplus and BSD - review is highly recommended.
License:	mplus AND LicenseRef-Callaway-BSD
BuildRequires:	%{family_ttf_vp}-fonts = %{vlgothic_ver}
Requires:	fontpackages-filesystem
Obsoletes:	%{old_name_ttf_v} <= %{obsoletes_EVR}
Provides:	%{old_name_ttf_v} = %{version}-%{release}

%description -n	%{name_ttf_v}
%{common_description}

This package contains True Type fonts generated generated from
%{name} source package which are based on VLGothic fonts.

%prep
%setup -q
%patch -P0 -p1 -b .perl512

iconv -f EUC-JP -t UTF-8 README.euc > README
touch -r README.euc README
iconv -f SHIFT-JIS -t UTF-8 ttfsrc/README-ttf.txt > ttfsrc/README-ttf.txt.tmp
touch -r ttfsrc/README-ttf.txt ttfsrc/README-ttf.txt.tmp
mv -f ttfsrc/README-ttf.txt.tmp ttfsrc/README-ttf.txt

%if ! %{show_progress}
# In the build on koji, showing progress bar is rather dirty
grep -rl '\\rprogress' . | xargs sed -i.bar -e '/\\rprogress/s|print|# print|'
%endif


%build
## Not using parallel make

# 1. bitmap fonts
make bdf

# 2. ttf
cd ttfsrc
cp -p name.src name.src.orig

## 2.1 ttf based on sazanami
sed -e 's|^Mona$|Mona-%{real_family_ttf_s}|' name.src.orig > name.src
make clean
make \
	BASE_OUTLINE_TTF=$(find %{family_ttf_s_dir} -name sazanami-gothic.ttf) \
	BASE_OUTLINE_VERSION=%{real_family_ttf_s}-%{sazanami_ver}
mv mona.ttf mona-%{real_family_ttf_s}.ttf

## 2.2 ttf based on VLGothic
sed -e 's|^Mona$|Mona-%{real_family_ttf_v}|' name.src.orig > name.src
make clean
make \
	BASE_OUTLINE_TTF=$(find %{family_ttf_vp_dir} -name VL-PGothic-Regular.ttf) \
	BASE_OUTLINE_VERSION=%{real_family_ttf_v}-%{vlgothic_ver}
mv mona.ttf mona-%{real_family_ttf_v}.ttf

cd ..

%install
rm -rf $RPM_BUILD_ROOT

# 1. bitmap fonts
mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_bitmap_full}
make install \
	X11BINDIR=%{_bindir} \
	MKDIRHIER="mkdir -p" \
	X11FONTDIR=$RPM_BUILD_ROOT%{fontdir_bitmap_full} \
	GZIP_CMD="gzip -9" \
	install
install -cpm 644 fonts.alias.mona \
	$RPM_BUILD_ROOT%{fontdir_bitmap_full}/fonts.alias

## catalog symlink
mkdir -p $RPM_BUILD_ROOT%{catalog_dir}
pushd $RPM_BUILD_ROOT%{catalog_dir}

UPWARDDIR="../../.."
ln -sf ${UPWARDDIR}%{fontdir_bitmap_full} %{fontdir_bitmap}
if [ ! -f $UPWARDDIR%{fontdir_bitmap_full}/fonts.dir ] ; then
	echo "Perhaps symlink target is wrong"
	exit 1
fi
popd


# 2. ttf
cd ttfsrc

mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_ttf_s_full}
install -cpm 0644 mona-%{real_family_ttf_s}.ttf $RPM_BUILD_ROOT%{fontdir_ttf_s_full}/

mkdir -p -m 0755 $RPM_BUILD_ROOT%{fontdir_ttf_v_full}
install -cpm 0644 mona-%{real_family_ttf_v}.ttf $RPM_BUILD_ROOT%{fontdir_ttf_v_full}/

cd ..

# Add AppStream metadata
# https://bugzilla.redhat.com/show_bug.cgi?id=1165507
install -Dm 0644 -p %{SOURCE1} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-sazanami.metainfo.xml
install -Dm 0644 -p %{SOURCE3} \
        %{buildroot}%{_datadir}/appdata/%{fontname}-vlgothic.metainfo.xml


%post -n	%{name_bitmap}
if [ -x %{_bindir}/fc-cache ] ; then
	%{_bindir}/fc-cache %{fontdir_bitmap_full} || :
fi

%postun -n	%{name_bitmap}
if [ $1 -eq 0 -a -x %{_bindir}/fc-cache ] ; then
	%{_bindir}/fc-cache %{fontdir_bitmap_full} || :
fi

%files -n	%{name_bitmap}
%doc	README
%doc	README.ascii

%{catalog_dir}/%{fontdir_bitmap}
%dir				%{fontdir_bitmap_full}
%verify(not md5 size mtime)	%{fontdir_bitmap_full}/fonts.alias
%verify(not md5 size mtime)	%{fontdir_bitmap_full}/fonts.dir
%{fontdir_bitmap_full}/*.pcf.gz

%define	_font_pkg_name	%{name_ttf_s}
%define	_fontdir	%{fontdir_ttf_s_full}
%_font_pkg mona-%{real_family_ttf_s}.ttf
%doc	ttfsrc/README-ttf.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml
%{_datadir}/appdata/%{fontname}-sazanami.metainfo.xml

%define	_font_pkg_name	%{name_ttf_v}
%define	_fontdir	%{fontdir_ttf_v_full}
%_font_pkg mona-%{real_family_ttf_v}.ttf
%doc	ttfsrc/README-ttf.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml
%{_datadir}/appdata/%{fontname}-vlgothic.metainfo.xml

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.90-40
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri May 31 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-38
- Rebuild for %%patch macro usage update

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 19 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-34
- Reflect sazanami-gothic-fonts packaging change

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.90-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 14 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-32
- Reflect vl-pgothic-fonts packaging change
- Update vl-pgothic version

* Wed Jul 27 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 06 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 25 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-29
- Rebuild for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-28
- BR: glibc-all-langpacks for iconv for Japanese

* Mon Mar  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-27
- Use binary name directly for xorg utility deaggregation

* Sat Jan 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 07 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-25
- F-33: mass rebuild

* Sun Feb 02 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-24
- F-32: mass rebuild

* Mon Jul 16 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-23
- F-29: mass rebuild

* Fri Feb 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-22
- F-26: mass rebuild

* Sat Feb  6 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-21
- F-24: mass rebuild

* Fri Dec 19 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-20
- Rebuild against newer vlgothic
- Add metainfo file for gnome-software
  (bug 1165507, Parag Nemade <pnemade@redhat.com>)

* Thu Jun 12 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-19
- F-21: mass rebuild

* Wed Aug  7 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-18
- F-20: mass rebuild

* Wed Feb 13 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.90-17
- Rebuild against newer vlgothic

* Fri Aug  3 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.90-16
- Rebuild against newer VLGothic

* Fri Nov 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.90-15
- Rebuild against newer VLGothic

* Mon Jul 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.90-14
- Rebuild against newer VLGothic

* Sat Jun 25 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 2.90-13
- Rebuild against newer VLGothic

* Thu Feb 10 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-12
- Rebuild against newer VLGothic

* Thu Sep  9 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-11
- Rebuild for newest VLGothic
- Patch for the behavior change of "split" on perl 5.12

* Thu Jan 14 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-10
- Rebuild for newest VLGothic

* Fri Jul 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-9
- Adjust for fontpackages 1.22

* Fri Mar 27 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-8
- F-11: Again rebuild for new virtual font Provides (bug 491969)

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-7
- F-11: Mass rebuild

* Thu Feb 19 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90.6
- F-11: font naming scheme change
  Now mona-{bitmap,vlgothic,sazanami}-fonts binary rpms are
  created

* Fri Dec  5 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rebuild for new VLGothic

* Wed Dec  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp>
- rebuild for new VLGothic

* Tue Sep  9 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-5
- F-10: Rebuild for new VLGothic

* Tue Aug  5 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-4
- Bump

* Mon Jul 28 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-3
- Rewrite

* Sun Jul  6 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-2
- Gerenal packaing fix according to Fedora fonts packaing
  conventions

* Sat Jul  5 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.90-1
- Initial packaging

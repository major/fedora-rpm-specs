Name:           deco-archive
Version:        1.7
Release:        20%{?dist}
Summary:        Extraction scripts for various archive formats for use of deco
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/peha/deco-archive/
Source0:        https://github.com/peha/deco-archive/archive/%{version}.tar.gz
# Use ffmpeg instead of wine+Monkey's Audio for converting ape to wav.
# Patch sent to upstream via email
Patch0:         deco-archive-ape.diff
# Use ffmpeg instead of non-free shorten decoder, which is not available
# in Fedora
Patch1:         deco-archive-shn.diff
# Use unzoo instead of zoo to extract zoo archives. The latter is not available
# in Fedora
Patch2:         deco-archive-zoo.diff
BuildArch:      noarch

BuildRequires:  make
Requires:       bzip2,coreutils,cpio,gzip,rpm,tar
Requires:       deco >= 1.5.6

%description
deco-archive provides support for popular archive 
formats to the deco file extraction framework.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
echo "Nothing to build."

%install
rm -rf %{buildroot} %{name}-ghosts.list %{name}-links.list

make install DESTDIR=%{buildroot} SHARE=%{_datadir}/%{name}

# %%{_var}/lib/deco is owned by deco.
# This is where deco will look for extraction scripts.
install -dm 755 %{buildroot}/%{_var}/lib/deco

# Install the default archivers and add the others to the ghost files list
pushd x
for i in *; do
   if [[ -d $i || -h $i ]] ; then
      ln -s ../../..%{_datadir}/%{name}/"$i" %{buildroot}/%{_var}/lib/deco
      case $i in
         bz2|cpio|"cpio\.bz2"|"cpio\.gz"|gem|gz|rpm|z|tar|"tar\.bz2"|"tar\.gz"|"tar\.z"|taz|tbz|tbz2|tgz)
            echo "%{_var}/lib/deco/$i" >> ../%{name}-links.list ;;
         *)
            echo "%ghost %{_var}/lib/deco/$i" >> ../%{name}-ghosts.list ;;
      esac
   fi
done
popd
# The following stopped working on F24 mass rebuild
#sed -e 's@[[\\]@?@g' %%{name}-ghosts.list %%{name}-links.list > %%{name}.files
cat %{name}-ghosts.list %{name}-links.list > %{name}.files


%define do_triggerin() for i in %1; do (if [ ! -e %{_var}/lib/deco/$i ]; then ln -s ../../..%{_datadir}/%{name}/"$i" %{_var}/lib/deco/ || : ; fi); done;
%define do_triggerun() ( [ $2 -gt 0 ] && [ $1 -gt 0 ] ) || (for i in %1; do ( rm -f %{_var}/lib/deco/$i || : ); done;)


%triggerin -- binutils
%do_triggerin {a,ar}
%triggerun -- binutils
%do_triggerun {a,ar}

%triggerin -- p7zip
%do_triggerin {7z,"7z\.[0-9]{2,}",t7z,"t7z\.[0-9]{2,}","tar\.7z","tar\.7z\.[0-9]{2,}"}
%triggerun -- p7zip
%do_triggerun {7z,"7z\.[0-9]{2,}",t7z,"t7z\.[0-9]{2,}","tar\.7z","tar\.7z\.[0-9]{2,}"}

%triggerin -- unace
%do_triggerin "ace|[c0-9][0-9]{2}"
%triggerun -- unace
%do_triggerun "ace|[c0-9][0-9]{2}"

%triggerin -- ffmpeg
%do_triggerin {ape,shn}
%triggerun -- ffmpeg
%do_triggerun {ape,shn}

%triggerin -- arc
%do_triggerin {arc,ark,sue}
%triggerun -- arc
%do_triggerun {arc,ark,sue}

%triggerin -- arj
%do_triggerin arj
%triggerun -- arj
%do_triggerun arj

%triggerin -- cabextract
%do_triggerin cab
%triggerun -- cabextract
%do_triggerun cab

%triggerin -- dpkg
%do_triggerin {deb,udeb}
%triggerun -- dpkg
%do_triggerun {deb,udeb}

%triggerin -- unrar
%do_triggerin {cbr,"rar|[rst][0-9]{2}","part[0-9]+\.rar"}
%triggerun -- unrar
%do_triggerun {cbr,"rar|[rst][0-9]{2}","part[0-9]+\.rar"}

%triggerin -- unzip
%do_triggerin {cbz,ear,ipsw,jar,od{c,f,g,i,m,p,s,t},ot{c,f,g,h,i,p,s,t},oxt,pk{3,4},wsz,xpi,zip}
%triggerun -- unzip
%do_triggerun {cbz,ear,ipsw,jar,od{c,f,g,i,m,p,s,t},ot{c,f,g,h,i,p,s,t},oxt,pk{3,4},wsz,xpi,zip}

%triggerin -- flac
%do_triggerin flac
%triggerun -- flac
%do_triggerun flac

%triggerin -- lha
%do_triggerin {lha,lzh}
%triggerun -- lha
%do_triggerun {lha,lzh}

%triggerin -- lrzip
%do_triggerin {lrz,"tar\.lrz"}
%triggerun -- lrzip
%do_triggerun {lrz,"tar\.lrz"}

%triggerin -- lzip
%do_triggerin {lz,"cpio\.lz","tar\.lz"}
%triggerun -- lzip
%do_triggerun {lz,"cpio\.lz","tar\.lz"}

%triggerin -- xz-lzma-compat
%do_triggerin {lzma,"tar\.lzma",tlz}
%triggerun -- xz-lzma-compat
%do_triggerun {lzma,"tar\.lzma",tlz}

%triggerin -- lzop
%do_triggerin {lzo,"cpio\.lzo"}
%triggerun -- lzop
%do_triggerun {lzo,"cpio\.lzo"}

%triggerin -- xz
%do_triggerin {"cpio\.xz","tar\.xz",txz,xz}
%triggerun -- xz
%do_triggerun {"cpio\.xz","tar\.xz",txz,xz}

%triggerin -- rzip
%do_triggerin {rz,"tar\.rz"}
%triggerun -- rzip
%do_triggerun {rz,"tar\.rz"}

%triggerin -- unalz
%do_triggerin alz
%triggerun -- unalz
%do_triggerun alz

%triggerin -- unzoo
%do_triggerin zoo
%triggerun -- unzoo
%do_triggerun zoo

%files -f %{name}.files
%doc LICENSE NEWS README.md
%{_datadir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 1.7-19
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 11 2016 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.7-1
- Version update.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 24 2013 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.6-1
- Version update.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Feb 05 2010 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5.1-1
- Version update.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.5-1
- Version update. New extensions: deb, udeb, tar.xz, txz, xz
- Handle .lzma via xz-lzma-compat from now on

* Sat Apr 04 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.4-3
- Handle .zoo format with unzoo (if installed)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Jan 19 2009 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.4-1
- Version update. New extensions: gem and tbz2
- Handle .shn format (shorten) with ffmpeg (if installed)
- Handle .alz format with unalz (if installed)

* Fri Dec 12 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.3.1-1
- Version update
- Use ffmpeg instead of wine+Monkey's Audio for converting ape to wav

* Mon Dec 01 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-6
- Code cleanup

* Sun Nov 30 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-5
- Workaround for the "broken ghosts".

* Sun Nov 30 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-4
- Fixed a typo in the %%do_trigger* of tar\.lzma
- Added rpm to the default list
- Attempted to mark the non-default archivers as ghosts

* Thu Nov 20 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-3
- License is GPLv3.
- Install the scripts in %%{_datadir}/%%{name} and the symlinks in %%{var}/lib/deco.

* Wed Nov 19 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-2
- Added conditionals to the trigger functions to suppress warnings on updates.

* Wed Oct 29 2008 Orcan Ogetbil <oget [DOT] fedora [AT] gmail [DOT] com> 1.2-1
- Initial build.
